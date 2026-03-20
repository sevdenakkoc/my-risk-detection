"""
features.py — Feature Engineering

Builds behavioral features from raw transaction data:
- Rolling window aggregations (7d, 30d, 90d)
- Near-threshold transaction counts
- Velocity ratios and drift metrics
- Dormancy-to-activity transitions
- Monthly client-level snapshots with forward-looking labels
"""