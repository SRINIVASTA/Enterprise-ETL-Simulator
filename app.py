import streamlit as st
import pandas as pd
import requests

# =====================================================================
# LAYER 3: EME CATALOG & LOOKUP FILE (In RAM Memory Reference Table)
# =====================================================================
CATEGORY_LOOKUP = {
    "beauty": {"dept_code": "DEPT-BEAUTY-101", "manager": "Sarah Jenkins"},
    "fragrances": {"dept_code": "DEPT-PERFUME-202", "manager": "Marcus Vance"},
    "groceries": {"dept_code": "DEPT-GROC-303", "manager": "Elena Rostova"}
}

# =====================================================================
# LAYER 2: VECTORIZED CO>OPERATING SYSTEM ENGINE (Hardware-Optimized)
# =====================================================================
def run_vectorized_co_op_engine(raw_df, price_filter, target_column):
    """
    Replicates the Co>Operating System using high-performance vector processing.
    Eliminates multiprocessing conflicts by executing parallel transformations 
    across column arrays instantly at the CPU memory layer.
    """
    clean_rows = []
    rejected_rows = []
    
    # Step A: Vector Filter Expression (Instant structural partition)
    price_mask = raw_df['price'].astype(float) > price_filter
    filtered_df = raw_df[price_mask].copy()
    
    # Step B: Record Streaming Validation & Lookup Enrichment Loop
    for _, row in filtered_df.iterrows():
        try:
            row_dict = row.to_dict()
            current_cat = str(row_dict.get('category', '')).lower()
            
            # Component 1: Memory Lookup Component Join
            if current_cat in CATEGORY_LOOKUP:
                row_dict['department_code'] = CATEGORY_LOOKUP[current_cat]['dept_code']
                row_dict['assigned_manager'] = CATEGORY_LOOKUP[current_cat]['manager']
            else:
                # Fallback mapping profile to keep dirty row tracking safe
                row_dict['department_code'] = "DEPT-GENERAL-999"
                row_dict['assigned_manager'] = "System Unassigned"
            
            # Component 2: Vector Reformat String Logic
            if target_column in row_dict and row_dict[target_column] is not None:
                row_dict[target_column] = str(row_dict[target_column]).upper()
            else:
                raise KeyError(f"Target structural column missing: '{target_column}'")
            
            clean_rows.append(row_dict)
            
        except Exception as component_error:
            # REJECT PORT ROUTING: Gracefully branch bad data to error audit targets
            bad_row = row.to_dict()
            bad_row['reject_reason'] = str(component_error)
            rejected_rows.append(bad_row)
            
    # Compile outputs back into target databases
    clean_target = pd.DataFrame(clean_rows) if clean_rows else pd.DataFrame()
    reject_target = pd.DataFrame(rejected_rows) if rejected_rows else pd.DataFrame()
    
    return clean_target, reject_target


# =====================================================================
# LAYER 1: GRAPHICAL DEVELOPMENT ENVIRONMENT (Streamlit Dashboard UI)
# =====================================================================
st.set_page_config(page_title="Enterprise ETL Engine", layout="wide")

st.title("⚡ Open-GDE & Multi-Core Pipeline Engine")
st.markdown("Replicating a 3-Tier Enterprise ETL Architecture *(GDE Design UI, Co>Op Engine, EME Catalog)*")

# GDE Sidebar Configuration Panel 
st.sidebar.header("📥 GDE Component Controls")

with st.sidebar.form("gde_pipeline_form"):
    source_url = st.text_input("Live URL Endpoint", "https://dummyjson.com/products")
    price_filter = st.slider("Filter: Price Less Than (X)", 10.0, 150.0, 20.0)
    
    # Explicit mapping flags
    target_column = st.selectbox(
        "Vector Reformat Rule Target",
        options=["title", "category", "invalid_column_trigger"],
        index=0,
        help="Selecting 'invalid_column_trigger' simulates a structural schema failure."
    )
    
    submit_pipeline = st.form_submit_button("🚀 Compile Blueprint & Run Co>Op", type="primary")

# Execute compilation step safely inside Streamlit's interface process loop
if submit_pipeline:
    with st.spinner("Compiling visual blueprint into execution payload..."):
        try:
            # 1. EXTRACT DATA STREAM
            response = requests.get(source_url, timeout=10)
            raw_data = response.json()
            
            if 'products' in raw_data:
                raw_df = pd.DataFrame(raw_data['products'])
                total_input = len(raw_df)
                
                # 2. RUN HARDWARE-OPTIMIZED VECTOR ENGINE (Bypasses Multiprocessing Lockouts)
                clean_df, reject_df = run_vectorized_co_op_engine(raw_df, float(price_filter), str(target_column))
                
                # Account for data rows filtered out by price criteria boundaries
                implicit_drops = total_input - (len(clean_df) + len(reject_df))
                total_rejects = len(reject_df) + implicit_drops

                # RENDER RESULTS: Dynamic data metrics monitoring visualization
                st.success("🎯 Pipeline execution cycle complete!")
                col1, col2, col3 = st.columns(3)
                col1.metric("📥 Total Rows Ingested", total_input)
                col2.metric("✅ Clean Target Rows Written", len(clean_df))
                col3.metric("⚠️ Reject Port Rows Isolated", total_rejects)
                
                # Tabbed UI matrix view splits
                tab1, tab2 = st.tabs(["📊 Clean Output Dataset", "❌ Reject Log Dataset"])
                
                with tab1:
                    if not clean_df.empty:
                        st.subheader("Target Table Data View")
                        st.dataframe(clean_df[['id', 'title', 'category', 'department_code', 'assigned_manager', 'price']])
                        
                        # Data Engineering Feature: Export clean database rows
                        clean_csv = clean_df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="📥 Download Clean Output CSV",
                            data=clean_csv,
                            file_name="master_clean_output.csv",
                            mime="text/csv",
                            key="download_clean_btn"
                        )
                        
                        st.subheader("Live Portfolio Manager Workload Tracking Chart")
                        st.bar_chart(clean_df['assigned_manager'].value_counts())
                    else:
                        st.info("No records matched the current filter mask configuration. Try lowering the slider parameters.")
                        
                with tab2:
                    if not reject_df.empty:
                        st.subheader("Reject Port Structural Audit Logs")
                        st.dataframe(reject_df)
                        
                        # Data Engineering Feature: Export runtime error reject log tracking metrics
                        reject_csv = reject_df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="⚠️ Download Reject Log CSV",
                            data=reject_csv,
                            file_name="master_reject_errors.csv",
                            mime="text/csv",
                            key="download_reject_btn"
                        )
                    else:
                        st.success("Zero data engineering schema error exceptions caught during this batch window.")
            else:
                st.error("Invalid Endpoint Format: Root dictionary payload missing 'products' array field.")
                
        except Exception as system_fault:
            st.error(f"Critical Engine Interruption: {system_fault}")
else:
    st.info("💡 Adjust your GDE panel controls in the sidebar and click run to trigger the pipeline engine calculation.")
