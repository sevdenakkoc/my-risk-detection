"""
features.py — Feature Engineering

Builds behavioral features from raw transaction data:
- Rolling window aggregations (7d, 30d, 90d)
- Fan-in signals: unique senders, received volume concentration
- Cycle signals: sender-receiver overlap, circular flow indicators
- Velocity ratios and drift metrics
- Dormancy-to-activity transitions
- Monthly client-level snapshots with forward-looking labels
"""