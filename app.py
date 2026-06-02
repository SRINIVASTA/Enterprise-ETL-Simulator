import streamlit as st
import pandas as pd
import requests
import numpy as np
from multiprocessing import Pool

# =====================================================================
# LAYER 3: EME CATALOG & LOOKUP FILE (In RAM Memory Reference Table)
# =====================================================================
CATEGORY_LOOKUP = {
    "beauty": {"dept_code": "DEPT-BEAUTY-101", "manager": "Sarah Jenkins"},
    "fragrances": {"dept_code": "DEPT-PERFUME-202", "manager": "Marcus Vance"},
    "groceries": {"dept_code": "DEPT-GROC-303", "manager": "Elena Rostova"}
}

# =====================================================================
# LAYER 2: CO>OPERATING SYSTEM ENGINE WORKER (CPU Threads Pipeline)
# =====================================================================
def co_op_core_worker(args):
    """
    Isolated parallel worker executing vector math on assigned chunk splits.
    Routes data records to the Reject Port if schema validations break.
    """
    data_chunk, price_filter, target_column = args
    clean_rows = []
    rejected_rows = []
    
    try:
        # Step A: Vector Filter Expression (Hardware-level matrix partition)
        price_mask = data_chunk['price'].astype(float) > price_filter
        filtered_chunk = data_chunk[price_mask].copy()
        
        # Step B: Record Streaming Validation Loop
        for _, row in filtered_chunk.iterrows():
            try:
                row_dict = row.to_dict()
                current_cat = str(row_dict.get('category', '')).lower()
                
                # Component 1: Memory Lookup Component Join
                if current_cat in CATEGORY_LOOKUP:
                    row_dict['department_code'] = CATEGORY_LOOKUP[current_cat]['dept_code']
                    row_dict['assigned_manager'] = CATEGORY_LOOKUP[current_cat]['manager']
                else:
                    raise ValueError(f"Unmapped lookup category code: '{current_cat}'")
                
                # Component 2: Vector Reformat String Logic
                if target_column in row_dict and row_dict[target_column] is not None:
                    row_dict[target_column] = str(row_dict[target_column]).upper()
                else:
                    raise KeyError(f"Target structural column missing: '{target_column}'")
                
                clean_rows.append(row_dict)
                
            except Exception as component_error:
                # REJECT PORT TRIGGER: Gracefully branch bad data without system crashes
                bad_row = row.to_dict()
                bad_row['reject_reason'] = str(component_error)
                rejected_rows.append(bad_row)
                
    except Exception as hardware_fault:
        pass
        
    return {"clean": clean_rows, "reject": rejected_rows}


# =====================================================================
# LAYER 1: GRAPHICAL DEVELOPMENT ENVIRONMENT (Streamlit Dashboard UI)
# =====================================================================
st.set_page_config(page_title="Enterprise ETL Engine", layout="wide")

st.title("⚡ Open-GDE & Multi-Core Pipeline Engine")
st.markdown("Replicating a 3-Tier Enterprise ETL Architecture *(GDE Design UI, Co>Op Engine, EME Catalog)*")

# GDE Side Control Panel inside an explicit Form component to eliminate cache hangs
st.sidebar.header("📥 GDE Component Controls")

with st.sidebar.form("gde_pipeline_form"):
    source_url = st.text_input("Live URL Endpoint", "https://dummyjson.com/products")
    price_filter = st.slider("Filter: Price Greater Than (X)", 10.0, 150.0, 30.0)
    
    # Static selector options matching explicit payload schemas
    target_column = st.selectbox(
        "Vector Reformat Rule Target",
        options=["title", "category", "invalid_column_trigger"],
        index=0,
        help="Selecting 'invalid_column_trigger' simulates an operational schema failure."
    )
    
    # Submit handler to force an execution refresh wave
    submit_pipeline = st.form_submit_button("🚀 Compile Blueprint & Run Co>Op", type="primary")

# Execute engine sequence only upon explicit button submission click
if submit_pipeline:
    with st.spinner("Dispatching parallel multi-core cluster data streams..."):
        try:
            # 1. EXTRACT DATA STREAM
            response = requests.get(source_url, timeout=10)
            raw_data = response.json()
            
            if 'products' in raw_data:
                raw_df = pd.DataFrame(raw_data['products'])
                total_input = len(raw_df)
                
                # 2. MULTI-FILE PARTITION: Split the data array across CPU core allocations
                df_splits = np.array_split(raw_df, 2)
                worker_tasks = [(split, float(price_filter), str(target_column)) for split in df_splits]
                
                # 3. PARALLEL DISTRIBUTED COMPUTE
                with Pool(processes=2) as pool:
                    worker_outputs = pool.map(co_op_core_worker, worker_tasks)
                    
                # 4. GATHER STREAMS: Re-stitch distributed arrays back together
                combined_clean, combined_reject = [], []
                for out in worker_outputs:
                    combined_clean.extend(out["clean"])
                    combined_reject.extend(out["reject"])
                    
                clean_df = pd.DataFrame(combined_clean) if combined_clean else pd.DataFrame()
                reject_df = pd.DataFrame(combined_reject) if combined_reject else pd.DataFrame()
                
                # Account for data dropped silently by the initial filter condition threshold
                implicit_drops = total_input - (len(clean_df) + len(reject_df))
                total_rejects = len(reject_df) + implicit_drops

                # RENDER DATA: Output metrics cards safely to the layout panel
                st.success("🎯 Pipeline execution cycle complete!")
                col1, col2, col3 = st.columns(3)
                col1.metric("📥 Total Rows Ingested", total_input)
                col2.metric("✅ Clean Target Rows Written", len(clean_df))
                col3.metric("⚠️ Reject Port Rows Isolated", total_rejects)
                
                # Tab interface matrix splits
                tab1, tab2 = st.tabs(["📊 Clean Output Dataset", "❌ Reject Log Dataset"])
                
                with tab1:
                    if not clean_df.empty:
                        st.subheader("Target Table Data View")
                        st.dataframe(clean_df[['id', 'title', 'category', 'department_code', 'assigned_manager', 'price']])
                        
                        st.subheader("Live Portfolio Manager Workload Tracking Chart")
                        st.bar_chart(clean_df['assigned_manager'].value_counts())
                    else:
                        st.info("No records matched the current filter mask configuration. Try lowering the slider parameters.")
                        
                with tab2:
                    if not reject_df.empty:
                        st.subheader("Reject Port Structural Audit Logs")
                        st.dataframe(reject_df)
                    else:
                        st.success("Zero data engineering schema error exceptions caught during this batch window.")
            else:
                st.error("Invalid Endpoint Format: Root dictionary payload missing the expected 'products' array field.")
                
        except Exception as system_fault:
            st.error(f"Critical Engine Interruption: {system_fault}")
else:
    st.info("💡 Adjust your GDE panel controls in the sidebar and click run to trigger the pipeline engine calculation.")
