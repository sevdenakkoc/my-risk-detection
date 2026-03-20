"""
train.py — Model Training

Trains and compares AML risk scoring models:
- Rule-based baseline (traditional threshold detection)
- Logistic Regression (interpretable baseline)
- LightGBM (gradient-boosted ensemble)

Handles class imbalance, time-based train/test splits,
and hyperparameter tuning.
"""