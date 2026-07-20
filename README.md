# Testable 2D Procedural World Engine

A modular, cross-platform 2D world generation engine built in Python, featuring a decoupled framework specifically engineered for automated testing and CI/CD validation.

## 🛠️ QA & Automation Highlights
* **Decoupled Architecture:** Separates volatile UI/input loops from pure logic, allowing the entire core engine to be unit tested headlessly.
* **Deterministic Validation:** Tests use fixed seeding vectors to verify Perlin noise terrain arrays consistently.
* **Boundary Guarding:** Automated edge-case sweeps validation for negative indexes, impassable obstacle collisions, and safe spawn tolerances.

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* pytest

### Installation & Running Tests