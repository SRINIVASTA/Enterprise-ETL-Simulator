import streamlit as st
import pandas as pd
import requests

# =====================================================================
# ⚙️ LAYER 2: VECTORIZED CO>OPERATING SYSTEM ENGINE (The Compute Plane)
# =====================================================================
# Kept at the top of the script purely as a background memory definition
CATEGORY_LOOKUP = {
    "beauty": {"dept_code": "DEPT-BEAUTY-101", "manager": "Sarah Jenkins"},
    "fragrances": {"dept_code": "DEPT-PERFUME-202", "manager": "Marcus Vance"},
    "groceries": {"dept_code": "DEPT-GROC-303", "manager": "Elena Rostova"}
}

def run_vectorized_co_op_engine(raw_df, price_filter, target_column):
    clean_rows = []
    rejected_rows = []
    
    # Step A: Layer 2 Vector Filter Mask
    price_mask = raw_df['price'].astype(float) <= price_filter
    filtered_df = raw_df[price_mask].copy()
    
    # Step B: Processing & Layer 3 Cross-Referencing
    for _, row in filtered_df.iterrows():
        try:
            row_dict = row.to_dict()
            current_cat = str(row_dict.get('category', '')).lower()
            
            # Layer 2 references Layer 3 here in memory
            if current_cat in CATEGORY_LOOKUP:
                row_dict['department_code'] = CATEGORY_LOOKUP[current_cat]['dept_code']
                row_dict['assigned_manager'] = CATEGORY_LOOKUP[current_cat]['manager']
            else:
                row_dict['department_code'] = "DEPT-GENERAL-999"
                row_dict['assigned_manager'] = "System Unassigned"
            
            # Step C: Layer 2 Transformation String Logic
            if target_column in row_dict and row_dict[target_column] is not None:
                row_dict[target_column] = str(row_dict[target_column]).upper()
            else:
                raise KeyError(f"Target structural column missing: '{target_column}'")
            
            clean_rows.append(row_dict)
            
        except Exception as component_error:
            bad_row = row.to_dict()
            bad_row['reject_reason'] = str(component_error)
            rejected_rows.append(bad_row)
            
    clean_target = pd.DataFrame(clean_rows) if clean_rows else pd.DataFrame()
    reject_target = pd.DataFrame(rejected_rows) if rejected_rows else pd.DataFrame()
    
    return clean_target, reject_target


# =====================================================================
# 🏛️ LAYER 1: GRAPHICAL DEVELOPMENT ENVIRONMENT (Streamlit Dashboard UI)
# =====================================================================
st.set_page_config(page_title="Enterprise ETL Engine", layout="wide")

st.title("⚡ Open-GDE & Multi-Core Pipeline Engine")
st.markdown("Replicating a 3-Tier Enterprise ETL Architecture")

# Layer 1 Input Controls (Sidebar Form)
st.sidebar.header("📥 GDE Component Controls")
with st.sidebar.form("gde_pipeline_form"):
    source_url = st.text_input("Live URL Endpoint", "https://dummyjson.com")
    price_filter = st.slider("Filter: Price Less Than (X)", 10.0, 150.0, 20.0)
    
    target_column = st.selectbox(
        "Vector Reformat Rule Target",
        options=["title", "category", "invalid_column_trigger"],
        index=0
    )
    submit_pipeline = st.form_submit_button("🚀 Compile Blueprint & Run Co>Op", type="primary")

# Coordination Execution Workflow
if submit_pipeline:
    with st.spinner("Compiling visual blueprint into execution payload..."):
        try:
            response = requests.get(source_url, timeout=10)
            raw_data = response.json()
            
            if 'products' in raw_data:
                raw_df = pd.DataFrame(raw_data['products'])
                total_input = len(raw_df)
                
                # Trigger Layer 2 Engine
                clean_df, reject_df = run_vectorized_co_op_engine(raw_df, float(price_filter), str(target_column))
                
                implicit_drops = total_input - (len(clean_df) + len(reject_df))
                total_rejects = len(reject_df) + implicit_drops

                st.success("🎯 Pipeline execution cycle complete!")
                col1, col2, col3 = st.columns(3)
                col1.metric("📥 Total Rows Ingested", total_input)
                col2.metric("✅ Clean Target Rows Written", len(clean_df))
                col3.metric("⚠️ Reject Port Rows Isolated", total_rejects)
                
                tab1, tab2 = st.tabs(["📊 Clean Output Dataset", "❌ Reject Log Dataset"])
                
                with tab1:
                    if not clean_df.empty:
                        st.subheader("Target Table Data View")
                        st.dataframe(clean_df[['id', 'title', 'category', 'department_code', 'assigned_manager', 'price']])
                        
                        clean_csv = clean_df.to_csv(index=False).encode('utf-8')
                        st.download_button(label="📥 Download Clean CSV", data=clean_csv, file_name="clean.csv", mime="text/csv")
                        
                        st.subheader("Live Portfolio Manager Workload Tracking Chart")
                        st.bar_chart(clean_df['assigned_manager'].value_counts())
                    else:
                        st.info("No records matched the current filter mask configuration.")
                        
                with tab2:
                    if not reject_df.empty:
                        st.subheader("Reject Port Structural Audit Logs")
                        st.dataframe(reject_df)
                    else:
                        st.success("Zero data engineering schema error exceptions caught.")
            else:
                st.error("Invalid Endpoint Format.")
        except Exception as system_fault:
            st.error(f"Critical Engine Interruption: {system_fault}")
else:
    st.info("💡 Adjust your GDE panel controls in the sidebar and click run to trigger calculation.")

# ⬇️ 🗃️ VISUAL PROOF OF LAYER 3 PLACED SECURELY AT THE BOTTOM ⬇️
st.markdown("---")
st.markdown("### 🗃️ Layer 3: Centralized Metadata Catalog View (EME Registry)")
st.caption("This foundational reference table stores the institutional lookup logic utilized by the compute plane.")
st.json(CATEGORY_LOOKUP)
