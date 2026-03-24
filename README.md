# Temporal Client Risk Scoring for AML Pattern Detection

## Objective

Develop a client-level risk scoring model that predicts whether a client will exhibit **suspicious AML behavior** (fan-in or cycle patterns) within the next 30 days, using only data available at prediction time.

This project demonstrates how supervised machine learning can enhance AML (Anti-Money Laundering) detection by modeling **behavioral evolution over time**, rather than relying on static rule-based alerts.

### AML Patterns Detected
- **Fan-in:** Multiple sources funneling money to a single receiver - a common money laundering technique
- **Cycle:** Circular flows between accounts designed to obscure the origin of funds

## Approach

Instead of classifying individual transactions, we construct a **temporal behavioral dataset** where each row represents a client at a monthly snapshot, with aggregated features from historical activity. This mirrors how production AML risk engines refresh risk scores periodically.

**Models Compared:**
| Model | Purpose |
|-------|---------|
| Rule-based baseline | Replicates traditional AML monitoring logic |
| Logistic Regression | Interpretable risk scores aligned with regulatory expectations |
| LightGBM | Captures non-linear behavioral patterns and interaction effects |

**Evaluation focuses on operational AML metrics:**
- Precision@TopK (investigation capacity)
- Recall within alert budget
- False positive reduction vs. rule-based approach
- Model interpretability via SHAP

## Dataset

Synthetic transaction data generated using [IBM AMLSim](https://github.com/IBM/AMLSim), containing fan-in and cycle money laundering patterns. See [`data/README.md`](data/README.md) for download instructions.

## Project Structure
```
my-risk-detection/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md              # How to get the data
│   ├── raw/                   # Original CSVs
│   ├── processed/             # Final modeling datasets
│   └── interim/               # Intermediate transformations
├── docs/
│   └── 01_problem_understanding.md
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb  # (upcoming)
│   ├── 03_modeling.ipynb      # (upcoming)
│   └── 04_evaluation.ipynb    # (upcoming)
└── src/
    ├── __init__.py
    ├── data.py                # Data loading & preprocessing
    ├── features.py            # Feature engineering functions
    ├── train.py               # Model training
    └── evaluate.py            # Evaluation metrics
```

## Getting Started
```bash
# Clone the repo
git clone https://github.com/sevdenakkoc/my-risk-detection.git
cd my-risk-detection

# Install dependencies
pip install -r requirements.txt

# Download the data (see data/README.md for details)
# Then run the notebooks in order: 01_eda → 02_features → 03_modeling → 04_evaluation
```

## Status

🔄 **In Progress** — EDA complete, feature engineering next.

## Author

Sevde Nur Akkoc