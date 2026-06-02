import streamlit as st
import pandas as pd
import requests
import numpy as np
from multiprocessing import Pool

# --- LAYER 3: EME CATALOG & LOOKUP FILE (In RAM Memory) ---
CATEGORY_LOOKUP = {
    "beauty": {"dept_code": "DEPT-BEAUTY-101", "manager": "Sarah Jenkins"},
    "fragrances": {"dept_code": "DEPT-PERFUME-202", "manager": "Marcus Vance"},
    "groceries": {"dept_code": "DEPT-GROC-303", "manager": "Elena Rostova"}
}

# --- LAYER 2: CO>OPERATING SYSTEM ENGINE WORKER (CPU Threads) ---
def co_op_core_worker(args):
    data_chunk, price_filter, target_column = args
    clean_rows, rejected_rows = [], []
    try:
        price_mask = data_chunk['price'].astype(float) > price_filter
        filtered_chunk = data_chunk[price_mask].copy()
        for _, row in filtered_chunk.iterrows():
            try:
                row_dict = row.to_dict()
                current_cat = str(row_dict.get('category', '')).lower()
                if current_cat in CATEGORY_LOOKUP:
                    row_dict['department_code'] = CATEGORY_LOOKUP[current_cat]['dept_code']
                    row_dict['assigned_manager'] = CATEGORY_LOOKUP[current_cat]['manager']
                else:
                    raise ValueError(f"Unmapped category: '{current_cat}'")
                if target_column in row_dict and row_dict[target_column] is not None:
                    row_dict[target_column] = str(row_dict[target_column]).upper()
                else:
                    raise KeyError(f"Column missing: '{target_column}'")
                clean_rows.append(row_dict)
            except Exception as e:
                bad_row = row.to_dict()
                bad_row['reject_reason'] = str(e)
                rejected_rows.append(bad_row)
    except Exception as hardware_fault:
        pass
    return {"clean": clean_rows, "reject": rejected_rows}

# --- LAYER 1: STREAMLIT VISUAL GDE INTERFACE ---
st.set_page_config(page_title="Enterprise ETL Simulator", layout="wide")

st.title("⚡ Open-GDE & Multi-Core Pipeline Engine")
st.markdown("Replicating a 3-Tier Enterprise ETL Architecture (GDE Design, Co>Op Engine, EME Catalog)")

# GDE Controls: Sidebar Configuration Panel
st.sidebar.header("📥 GDE Component Controls")
source_url = st.sidebar.text_input("Live URL Endpoint", "https://dummyjson.com")
price_filter = st.sidebar.slider("Filter: Price Greater Than (X)", 10.0, 150.0, 50.0)
target_column = st.sidebar.selectbox("Vector Reformat Rule", ["title", "bad_column_trigger"])

if st.sidebar.button("🚀 Compile Blueprint & Run Co>Op", type="primary"):
    with st.spinner("Executing pipeline across multi-core processors..."):
        try:
            # 1. EXTRACT
            response = requests.get(source_url, timeout=10)
            raw_df = pd.DataFrame(response.json()['products'])
            total_input = len(raw_df)
            
            # 2. MULTI-FILE PARTITION (2-Way split)
            df_splits = np.array_split(raw_df, 2)
            worker_tasks = [(split, price_filter, target_column) for split in df_splits]
            
            # 3. PARALLEL COMPUTE ENGINE
            with Pool(processes=2) as pool:
                worker_outputs = pool.map(co_op_core_worker, worker_tasks)
                
            # 4. GATHER STREAMS
            combined_clean, combined_reject = [], []
            for out in worker_outputs:
                combined_clean.extend(out["clean"])
                combined_reject.extend(out["reject"])
                
            clean_df = pd.DataFrame(combined_clean) if combined_clean else pd.DataFrame()
            reject_df = pd.DataFrame(combined_reject) if combined_reject else pd.DataFrame()
            
            implicit_drops = total_input - (len(clean_df) + len(reject_df))
            total_rejects = len(reject_df) + implicit_drops

            # UI Display: Real-time Metric Cards
            col1, col2, col3 = st.columns(3)
            col1.metric("📥 Total Rows Ingested", total_input)
            col2.metric("✅ Clean Target Rows Written", len(clean_df))
            col3.metric("⚠️ Reject Port Rows Isolated", total_rejects)
            
            # Data Preview Tabs
            tab1, tab2 = st.tabs(["📊 Clean Output Dataset", "❌ Reject Log Dataset"])
            with tab1:
                if not clean_df.empty:
                    st.dataframe(clean_df[['id', 'title', 'category', 'department_code', 'assigned_manager', 'price']])
                    # Live Visual Workload Chart
                    st.subheader("Live Portfolio Manager Workload Chart")
                    st.bar_chart(clean_df['assigned_manager'].value_counts())
                else:
                    st.info("No records passed the clean execution mask.")
            with tab2:
                if not reject_df.empty:
                    st.dataframe(reject_df)
                else:
                    st.success("Zero data validation errors caught during this run cycle.")
                    
        except Exception as system_fault:
            st.error(f"Critical Pipeline Interruption: {system_fault}")
