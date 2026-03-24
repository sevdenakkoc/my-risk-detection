# Problem Understanding

## Objective
The model will prioritize which customers investigators should review given limited time capacity.

## AML Patterns Targeted
- **Fan-in:** Multiple accounts sending funds to a single receiver - indicative of layering or collection points
- **Cycle:** Circular transaction flows between accounts - designed to obscure the origin of funds

## Why These Patterns?
The AMLSim dataset contains ground-truth labels for fan-in and cycle patterns. These are real, operationally significant AML typologies that Dutch banks (ING, ABN AMRO, Rabobank) actively monitor for.

## Approach
Rather than classifying individual transactions, we build a temporal behavioral dataset where each row represents a client at a monthly snapshot. Features are aggregated from historical transaction behavior. This mirrors production AML risk engines.