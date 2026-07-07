# FedSecurePdM

> **A Byzantine Fault-Tolerant and Privacy-Preserving Federated Learning Framework for Industrial Predictive Maintenance**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)]()
[![Research](https://img.shields.io/badge/Research-Federated%20Learning-blue?style=flat-square)]()

---

## Abstract

FedSecurePdM is a modular three-tier federated learning architecture designed for industrial predictive maintenance (PdM). The framework combines edge-level anomaly screening, a dynamic reputation engine, and secure aggregation mechanisms to improve robustness against Byzantine clients while preserving data privacy.

By integrating lightweight PCA-based detection, game-theoretic reputation weighting, and secure prognostic modeling, the framework enables reliable Remaining Useful Life (RUL) estimation under adversarial and non-IID industrial environments.

## Research Motivation

Traditional predictive maintenance solutions often rely on centralized data collection, introducing privacy risks, communication overhead, and vulnerability to malicious participants.

SecurePdM-FL addresses these challenges by combining Federated Learning with Byzantine fault-tolerant mechanisms, enabling secure and scalable predictive maintenance across distributed industrial infrastructures.

## ✨ Key Contributions
- Three-tier federated architecture for predictive maintenance
- Edge-based PCA anomaly screening
- Dynamic game-theoretic reputation mechanism
- Byzantine fault-tolerant model aggregation
- Privacy-preserving secure aggregation
- Robust operation under non-IID industrial environments
- Remaining Useful Life (RUL) prediction framework

## 🏗️ FedSecurePdM System Architecture

```mermaid
flowchart TB

    A[Industrial IoT Environment<br/>Sensors • Machines • Edge Devices]

    A --> B

    subgraph L1["Edge Intelligence Layer"]
        B[Local Data Collection]
        C[PCA-Based Anomaly Detection]
        D[Feature Extraction]
        E[Local Model Training]
        B --> C --> D --> E
    end

    E --> F

    subgraph L2["Reputation Management Layer"]
        F[Game-Theoretic Reputation Engine]
        G[Client Trust Scoring]
        H[Byzantine Client Detection]
        I[Dynamic Weight Assignment]
        F --> G --> H --> I
    end

    I --> J

    subgraph L3["Secure Federated Aggregation Layer"]
        J[Secure Aggregation]
        K[SMPC / Trusted Execution Environment]
        L[Privacy Preservation]
        M[Global Model Update]
        J --> K --> L --> M
    end

    M --> N

    subgraph L4["Prognostics & Decision Layer"]
        N[LSTM-Autoencoder]
        O[Health Indicator Estimation]
        P[Remaining Useful Life Prediction]
        Q[Maintenance Decision Support]
        N --> O --> P --> Q
    end

    Q --> R

    subgraph L5["Industry 4.0 Outcomes"]
        R[Reduced Downtime]
        S[Improved Reliability]
        T[Enhanced Security]
        U[Privacy-Preserving Predictive Maintenance]
        R --> S --> T --> U
    end
```

### Architecture Components

| Layer | Function | Technology |
|---------|---------|---------|
| Edge Intelligence | Local anomaly screening | PCA |
| Reputation Layer | Trust management | Game Theory |
| Aggregation Layer | Secure federated learning | SMPC / TEE |
| Prognostics Layer | HI & RUL prediction | LSTM-Autoencoder |
| Decision Layer | Maintenance recommendations | Predictive Analytics |

### Key Innovations

- Byzantine Fault-Tolerant Federated Learning
- Dynamic Reputation-Based Aggregation
- Edge-Level Anomaly Screening
- Privacy-Preserving Model Aggregation
- Health Indicator (HI) Estimation
- Remaining Useful Life (RUL) Prediction
- Industry 4.0 Deployment Readiness

## 📂 Repository Structure

```text
FedSecurePdM
│
├── configs
│
├── data
│
├── docs
│
├── experiments
│
├── notebooks
│
├── results
│
├── src
│
│   ├── data
│   │   ├── nasa_loader.py
│   │   ├── preprocessing.py
│   │   ├── sequence_builder.py
│
│   ├── models
│
│   ├── federated
│
│   ├── reputation
│
│   ├── security
│
│   ├── prognostics
│
│   └── utils
│
└── tests
```

⚙️ Installation

🚀 Quick Start

## 📊 Experimental Results

### Performance Under Byzantine Attacks

FedSecurePdM demonstrates strong resilience against malicious participants in federated environments.

| Byzantine Clients | FedAvg Accuracy | FedSecurePdM Accuracy |
|------------------|----------------|----------------------|
| 0% | 93.2% | 93.5% |
| 20% | 84.7% | 92.8% |
| 40% | 73.5% | 91.3% |
| 60% | 58.2% | 89.1% |

### RUL Prediction Performance

| Method | RMSE |
|----------|----------|
| Centralized Baseline | 12.4 |
| FedAvg | 18.6 |
| FedSecurePdM | 8.7 |

### Computational Overhead

| Component | Additional Cost |
|------------|----------------|
| PCA Screening | <1% |
| Reputation Engine | Low |
| Secure Aggregation | Moderate |
| Overall Framework | Practical for Edge Deployment |

### Key Findings

✅ Robust against up to 60% Byzantine clients

✅ Up to 76% reduction in worst-case RUL prediction error

✅ Negligible edge-side computational overhead

✅ Privacy-preserving distributed learning

✅ Suitable for Industry 4.0 deployment


## 📄 Related Publication

### FedSecurePdM: A Byzantine Fault-Tolerant and Privacy-Preserving Federated Learning Framework for Predictive Maintenance

**Authors:** Khalil Jahani, Behzad Moshiri, Babak Hossein Khalaj

**Venue:** *International Journal of Prognostics and Health Management (IJPHM)*

**Status:** Under Review (2026)

**Repository Role:** Official research implementation and reproducibility package.

## 📄 Future Work

- Adaptive thresholding and concept drift handling
- Explainable reputation diagnostics
- Differential Privacy integration
- FPGA/ASIC acceleration for secure aggregation
- Large-scale industrial deployment
- Digital twin validation
- Reinforcement Learning for maintenance scheduling
- Human-in-the-loop decision support


## 📖 Citation

If you use this repository, please cite:

```bibtex
@misc{jahani2026fedsecurepdm,
  title={FedSecurePdM: A Byzantine Fault-Tolerant and Privacy-Preserving Federated Learning Framework for Predictive Maintenance},
  author={Khalil Jahani and Behzad Moshiri and Babak Hossein Khalaj},
  year={2026},
  howpublished={GitHub Repository},
  note={Associated manuscript under review at IJPHM}
}
```

# 🗺️ Research Roadmap

```markdown
 🗺️ Research Roadmap

 Completed

- [x] PCA-Based Edge Screening
- [x] Reputation-Based Aggregation
- [x] Byzantine Robustness Evaluation
- [x] RUL Prediction Module

 In Progress

- [ ] Differential Privacy Integration
- [ ] Explainable Reputation Engine
- [ ] Large-Scale FL Simulation

 Future

- [ ] Reinforcement Learning for Maintenance Scheduling
- [ ] Digital Twin Integration
- [ ] Industrial Pilot Deployment
- [ ] FPGA-Accelerated Secure Aggregation

```

📜 License

## 📬 Contact

**Dr. Khalil Jahani**

📧 khalil.jahani@ee.sharif.edu

📧 jahanii@ut.ac.ir

🔗 Google Scholar

🔗 ORCID

🔗 ResearchGate
