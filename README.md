# ⚡ Open-GDE & Multi-Core Pipeline Engine

A high-fidelity Python simulation of a 3-Tier Enterprise ETL Architecture utilizing **Streamlit** for the orchestration interface, **Pandas** for memory-layer data transformation, and structured **Error Isolation (Reject Ports)**. 

This project demonstrates how enterprise data integration suites (such as Ab Initio) separate visual orchestration, data transit rules, and metadata catalogs.

---

## 🏗️ 3-Tier Architecture Mapping

The codebase is divided into three distinct operational layers:

┌────────────────────────────────────────────────────────┐
│      Layer 1: Graphical Development Environment        │
│      (Streamlit Sidebar UI, Metrics, & Data Tabs)      │
└───────────────────────────┬────────────────────────────┘
                            │ Compiles Parameters
                            ▼
┌────────────────────────────────────────────────────────┐
│    Layer 2: Vectorized Co>Operating System Engine     │
│       (Pandas Vectorized Masks + Streaming Loop)       │
└───────────────────────────┬────────────────────────────┘
                            │ Joins / Enriches
                            ▼
┌────────────────────────────────────────────────────────┐
│            Layer 3: EME Catalog & Lookup               │
│        (In-Memory Static Category Dictionary)          │
└────────────────────────────────────────────────────────┘


### 🔹 Layer 1: Open-GDE (Graphical Development Environment)
* Implemented via **Streamlit**.
* Serves as the developer console to inject custom extraction endpoints, price filtering thresholds, and structural reformat targets.
* Offers real-time data governance metrics monitoring, operational tracking charts, and physical CSV export layers for automated compliance logs.

### 🔹 Layer 2: Vectorized Co>Operating System Engine
* Houses the core pipeline transformation mechanics.
* Evaluates input records instantly against structural filters using memory-optimized operations.
* Contains a dedicated **Reject Port Routing** architecture. If data fails schema transformation validation, the system isolates the row, logs the technical exception tracking reason, and dynamically branches it away from the clean production warehouse data targets.

### 🔹 Layer 3: EME Catalog (Enterprise Metadata Exchange)
* A high-speed memory catalog lookup matrix table.
* Replicates centralized corporate metadata rules by automatically mapping raw categories to standardized global data definitions (`department_code`) and data owners (`assigned_manager`).

---

## 🚀 Getting Started

### 📋 Prerequisites
Ensure you have Python 3.8+ installed along with the required dependencies:
```bash
pip install streamlit pandas requests
```

### 🏃 Running the Application
Launch the pipeline dashboard interface using your local terminal:
```bash
streamlit run your_script_name.py
```

---

## 🕹️ Operational Run Scenarios

You can validate the resilience of the pipeline architecture using two predefined testing configurations inside the sidebar dashboard control panel:

### Scenario A: The Clean Production Path
1. Keep the default API target endpoint (`https://dummyjson.com`).
2. Set the **Vector Reformat Rule Target** to `title`.
3. Click **Compile Blueprint & Run Co>Op**.
4. **Expected Result:** Data streams successfully. Clean records are enriched using the EME reference catalog, and an active database portfolio manager workload tracking chart is populated dynamically under the clean tab.

### Scenario B: Simulated Component Schema Failure (Reject Port Audit)
1. Navigate to the sidebar control menu.
2. Toggle the **Vector Reformat Rule Target** dropdown to `invalid_column_trigger`.
3. Click **Compile Blueprint & Run Co>Op**.
4. **Expected Result:** The pipeline encounters a missing structural target key. Instead of a critical app crash, the system catches the internal software engine exceptions, safely keeps dirty rows tracked, and logs them in the **Reject Port Structural Audit Logs** tab with precise error descriptions.

---

## 🛠️ Technology Stack
* **UI/Orchestration:** Streamlit
* **Data Processing:** Pandas DataFrames
* **Ingestion Layer:** Requests (REST API Integration)
