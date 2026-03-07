# Intelligent Agent Credit Card Fraud Detection System

> A real-time, AI-powered fraud detection platform built on a **Multi-Agent System (MAS)** architecture. Three specialized agents collaborate autonomously to ingest transaction data, classify fraud using machine learning, and dispatch actionable alerts, all observable through a live interactive dashboard.

---

## Table of Contents

- [Project Overview](#-project-overview)
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
- [Technologies Used](#-technologies-used)
- [How It Works](#-how-it-works)
- [Dashboard & Visualization](#-dashboard--visualization)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Performance Metrics](#-performance-metrics)

---

##  Project Overview

This project demonstrates how **Multi-Agent Systems (MAS)** and **Machine Learning** can be combined to tackle one of the most critical challenges in financial security: **real-time credit card fraud detection**.

Rather than using a monolithic detection pipeline, the system decomposes the problem into three autonomous, communicating agents, each responsible for a distinct stage of the detection workflow. This design mirrors real-world financial fraud systems and showcases the power of agent-based modeling for complex, event-driven tasks.

**Who is this for?**
-  Financial institutions needing a prototype fraud detection pipeline
-  Researchers and students studying multi-agent systems or applied ML
-  Developers exploring the Mesa agent-based modeling framework
-  Data scientists looking for an end-to-end fraud detection showcase

---

##  System Architecture

The system is composed of three specialized agents that communicate through an internal message-passing protocol:

```
┌─────────────────┐     data_ready      ┌──────────────────┐     fraud_detection     ┌──────────────────────┐
│  DataFetcher    │ ──────────────────► │  FraudDetector   │ ──────────────────────► │  NotificationSender  │
│     Agent       │                     │      Agent       │                          │        Agent         │
│                 │                     │                  │                          │                      │
│ • Load CSV      │                     │ • Preprocess     │                          │ • Generate alerts    │
│ • Validate data │                     │ • Train XGBoost  │                          │ • Risk scoring       │
│ • Compute stats │                     │ • Predict fraud  │                          │ • Send notifications │
└─────────────────┘                     └──────────────────┘                          └──────────────────────┘
```

All agents are coordinated by the `FraudDetectionModel`, which manages the shared message bus, scheduling, and live metrics collection via Mesa's `DataCollector`.

---

##  Key Features

- **Multi-Agent Coordination** — Agents communicate asynchronously via typed messages (`data_ready`, `fraud_detection`, `notification_complete`), enabling a decoupled, fault-tolerant design.
- **XGBoost Classification** — The `FraudDetectorAgent` trains a gradient-boosted classifier with automatic feature preprocessing (scaling of `Amount` and `Time`) and computes per-feature importance scores.
- **Real-Time Alert System** — The `NotificationSenderAgent` generates structured fraud alerts with confidence scores, top risk indicators, and recommended actions for each flagged transaction.
- **Live Interactive Dashboard** — A Mesa-powered web dashboard with step-by-step simulation control, agent status cards, animated communication logs, and performance charts — suitable for both technical and non-technical audiences.
- **System Metrics Tracking** — Continuous collection of transactions processed, fraud detection rate, processing speed (tx/sec), and system uptime, all updated at each simulation step.
- **Risk Severity Classification** — Detected frauds are tiered into Critical, High, and Medium risk levels based on transaction amount and model confidence, with tailored response recommendations.

---

##  Technologies Used

| Category | Technology |
|---|---|
| **Agent Framework** | [Mesa](https://mesa.readthedocs.io/) — Python agent-based modeling |
| **Machine Learning** | [XGBoost](https://xgboost.readthedocs.io/) — Gradient Boosting Classifier |
| **Data Processing** | [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) |
| **Preprocessing** | [Scikit-learn](https://scikit-learn.org/) — `StandardScaler`, `train_test_split` |
| **Visualization** | Mesa `ModularServer`, custom HTML/CSS/SVG dashboard elements |
| **Language** | Python 3.x |

---

##  How It Works

The system runs as a stepped simulation. Each call to `model.step()` advances all agents simultaneously. The full pipeline completes in approximately **3–5 steps**:

### Step 1 — Data Ingestion (`DataFetcherAgent`)
- Reads `creditcard.csv` into a Pandas DataFrame
- Computes dataset statistics: total transactions, fraud ratio, amount distribution
- Posts a `data_ready` message to the shared message bus with the raw data and statistics

### Step 2 — Fraud Detection (`FraudDetectorAgent`)
- Receives the `data_ready` message and extracts the transaction data
- Scales `Amount` and `Time` features; selects 30 feature columns (`V1`–`V28` + scaled fields)
- Performs an 80/20 train-test split and fits an `XGBClassifier`
- Predicts fraud on the test set; computes accuracy and feature importances
- Posts a `fraud_detection` message with predictions, flagged transactions, and model metadata

### Step 3 — Alert Dispatch (`NotificationSenderAgent`)
- Receives the `fraud_detection` message
- Iterates over each flagged transaction, generating a structured notification with:
  - Alert ID, transaction amount, timestamp
  - Top 3 XGBoost feature importance indicators
  - AI confidence score (75–95%)
- Appends all alerts to the model's notification registry and posts a `notification_complete` confirmation

---

## Dashboard & Visualization

Launch the interactive web dashboard via `visualization.py`. It runs on **[http://127.0.0.1:8521](http://127.0.0.1:8521)** and provides:

| Panel | Description |
|---|---|
|  **About Section** | Plain-language project purpose and technical highlights |
|  **System Overview** | Live counters for transactions analyzed, fraud detected, and detection rate |
|  **Agent Workflow** | Color-coded agent status cards (`idle` / `processing` / `completed` / `error`) with live metrics |
|  **Communication Log** | Animated inter-agent message timeline with both simple and technical descriptions |
|  **Performance Charts** | SVG bar and line charts for fraud alert progress and transaction throughput |
|  **Transaction Monitor** | Real-time feed of flagged high-risk transactions with risk scores |
|  **Alert Center** | Full fraud alert detail view with risk tier, amount, confidence, top indicators, and recommended actions |

---

##  Getting Started

### Prerequisites

```bash
pip install mesa pandas numpy xgboost scikit-learn
```

### Dataset

Download the [Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from Kaggle and place `creditcard.csv` in the project root directory.

### Run the Core System (CLI)

```bash
python fraud_detection_system.py
```

This runs 8 simulation steps and prints a full summary report to the terminal.

### Launch the Interactive Dashboard

```bash
python visualization.py
```

Then open **[http://127.0.0.1:8521](http://127.0.0.1:8521)** in your browser.

Use the **Step** button to advance the simulation one agent cycle at a time and observe the agents communicate in real time.

---

##  Project Structure

```
├── fraud_detection_system.py   # Core agents, model, and message-passing logic
├── visualization.py            # Mesa dashboard server and all UI elements
├── creditcard.csv              # Dataset (not included — download from Kaggle)
└── README.md
```

---

##  Dataset

This system uses the publicly available **[ULB Credit Card Fraud Detection dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)**:

- **284,807** transactions made by European cardholders (September 2013)
- **492 fraud cases** (~0.172% of all transactions)
- 28 PCA-transformed features (`V1`–`V28`) + `Time`, `Amount`, and `Class` label
- Highly imbalanced — making it a realistic and challenging benchmark

---

##  Performance Metrics

At the end of a full simulation run, the system reports:

| Metric | Description |
|---|---|
| **Transactions Analyzed** | Number of test-set transactions evaluated by XGBoost |
| **Fraud Cases Detected** | Count of transactions classified as fraudulent |
| **Detection Rate** | `frauds_detected / transactions_processed` |
| **Processing Speed** | Transactions per second from start to completion |
| **Model Accuracy** | Fraction of correct predictions on the test split |

---

## Future Work
Several improvements are planned for future versions. On the ML side, handling class imbalance with SMOTE and adding SHAP-based explanations would make the model more accurate and its alerts easier to interpret. 

Architecturally, replacing the CSV loader with a live Kafka stream would enable true real-time processing, and adding a feedback agent would allow analyst verdicts to improve detection over time. The dashboard could be rebuilt in Streamlit for a cleaner, more modern interface. 

Finally, packaging the system with Docker and exposing a FastAPI endpoint would make it straightforward to deploy in a real financial environment.

---

##  Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request for:
- Alternative classifiers (e.g., LightGBM, Random Forest, Isolation Forest)
- SMOTE or other class-imbalance handling strategies
- Persistent notification storage (database or file export)
- REST API endpoint for real-time transaction scoring

---

##  License

> This project is released for educational and research purposes.
-----
## Note from me :)
> This project was developed as part of an applied research effort in intelligent systems and financial security, combining multi-agent architecture with machine learning to address real-world fraud detection challenges.
Contributions, suggestions, and feedback are welcome, feel free to explore !!
----
