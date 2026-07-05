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

## 🏗️ System Architecture

Industrial Sensors
        │
        ▼
 ┌─────────────────┐
 │ Edge Layer      │
 │ PCA Screening   │
 └─────────────────┘
        │
        ▼
 ┌─────────────────┐
 │ Reputation Tier │
 │ Trust Scoring   │
 └─────────────────┘
        │
        ▼
 ┌─────────────────┐
 │ Secure FL Server│
 │ SMPC / TEE      │
 └─────────────────┘
        │
        ▼
 ┌─────────────────┐
 │ LSTM-AE Model   │
 │ HI / RUL Output │
 └─────────────────┘

📂 Repository Structure

⚙️ Installation

🚀 Quick Start

## 📊 Experimental Results

Key findings from the paper:

- >89% classification accuracy maintained under up to 60% malicious clients.
- Up to 76% reduction in worst-case RUL RMSE compared to unprotected federated baselines.
- Less than 1% computational overhead introduced by edge PCA screening.
- Only marginal convergence delay under adversarial conditions.

## 📄 Future Work

- Adaptive thresholding and concept drift handling
- Explainable reputation diagnostics
- Differential Privacy integration
- FPGA/ASIC acceleration for secure aggregation
- Large-scale industrial deployment
- Digital twin validation
- Reinforcement Learning for maintenance scheduling
- Human-in-the-loop decision support

📖 Citation

🗺️ Roadmap

📜 License

📬 Contact
