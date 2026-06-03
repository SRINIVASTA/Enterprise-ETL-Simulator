# ⚡ Open-GDE & Multi-Core Pipeline Engine
**Created by srinivasta**

A high-performance, single-file Streamlit application that emulates a traditional 3-Tier Enterprise ETL Architecture. It models the core mechanics of visual pipeline design, rapid catalog reference lookups, and hardware-optimized vectorized array transformations.

---

## 🏛️ Architecture Overview

The application splits data processing responsibilities across three distinct functional layers:

### 1. Layer 1: Graphical Development Environment (GDE UI)
* **Tech Stack**: Streamlit Dashboard Core
* **Function**: Serves as the orchestration plane. Engineers dynamically configure system inputs, tweak sliding price thresholds, and toggle structural schema validation rules.

### 2. Layer 2: Vectorized Co>Operating System Engine
* **Tech Stack**: Pandas Array Vectorization
* **Function**: Eliminates CPU multi-threading bottlenecks and slow Python processing loops. Uses native memory-layer array methods (`.map()`, `.str`) to filter records, execute structural reformats, and partition schema failures to error tracking targets.

### 3. Layer 3: EME Catalog & Lookup Files
* **Tech Stack**: In-Memory Dictionary Registry
* **Function**: Acts as the centralized reference store for business rules, tracking department mappings and managerial ownership metadata used during the transformation cycle.

---

## ⚙️ Core Pipeline Logic

```mermaid
graph TD
    %% Define Node Styles
    classDef process fill:#1f6feb,stroke:#58a6ff,stroke-width:2px,color:#ffffff;
    classDef data fill:#21262d,stroke:#30363d,stroke-width:2px,color:#c9d1d9;
    classDef reject fill:#da3633,stroke:#f85149,stroke-width:2px,color:#ffffff;

    A([Raw Ingest Stream]):::data --> B[Vector Filter Mask]:::process
    
    B -->|Price Threshold Exceeded| C[Implicit Drops Log]:::data
    B -->|Valid Price| D[Schema Target Check]:::process
    
    D -->|Missing Target Column| E[Reject Port Targets]:::reject
    D -->|Schema Passed| F[Memory Catalog Join]:::process
    
    F --> G[Upper Case Reformat]:::process
    G --> H([Clean Master Target]):::data
```

---

## 🚀 Quick Start

### 📋 Prerequisites
Ensure your local Python runtime matches the requirements:
* Python 3.8+
* `pip` package manager

### 🔧 Installation
1. Clone or download this project folder to your local machine.
2. Install the necessary data-engineering dependencies:
   ```bash
   pip install streamlit pandas requests
   ```

### 🏃 Running the Application
Boot the visual pipeline controller directly from your terminal workspace:
```bash
streamlit run app.py
```

---

## 🔬 Testing Structural Failures

The dashboard features built-in error routing simulations:
1. Open the sidebar navigation menu.
2. Locate the **Vector Reformat Rule Target** drop-down menu.
3. Switch the active target parameter to `invalid_column_trigger`.
4. Run the engine to see the component route 100% of rows to the **Reject Port Structural Audit Logs**.
