# Testable 2D Procedural World Engine

A modular, cross-platform 2D world generation engine built in Python, showcasing a decoupled framework specifically engineered for automated testing and CI/CD validation. 

# Architecture and QA Methodology

In traditional script design, simulation logic is heavily coupled with user-interface inputs and platform-specific terminal console functions. This layout refactors that pattern into a clean, testable design:

* Decoupled Engine Core: The mathematical simulation (game_engine.py) runs fully headlessly. It handles the 2D Perlin noise generation matrices and coordinate structures independently of any rendering window.
* Automated Regression Suite: Features an automated validation layer (test_game.py) running tests under 0.1 seconds to protect foundational rules against code regressions.
* Deterministic Verification: Validates map generation deterministically across identical random seeds to ensure world stability.
* Boundary Validation and Edge Handling: Sweeps limits for out-of-bounds array coordinates, tests negative space vectors, checks obstacle collision boundaries, and asserts fuzzy-tested safe spawning logic across 100 iterations.

- Project Structure

qa-procedural-world/
|
|-- src/                      # Production source logic
|   |-- __init__.py
|   |-- game_engine.py        # Core generation math and state mechanics
|   |-- main.py               # Cross-platform runtime application loop
|
|-- tests/                    # Automation suite
|   |-- __init__.py
|   |-- test_game.py          # Functional regression test checkpoints
|
|-- pyproject.toml            # Path mapping for test environment root
|-- requirements.txt          # Framework dependencies
|-- README.md                 # Project documentation

- Getting Started

Prerequisites:
* Python 3.8 or higher installed on your system.

1. Installation:
Clone this repository to your local system and navigate to the project directory:
git clone https://github.com/Icy4321/procedural-world.git
cd qa-procedural-world

Install the required test engine packages:
pip install -r requirements.txt

2. Running the Automated Test Suite:
To launch the automated test inspectors from the root path with detailed logging data:
python -m pytest -v

3. Launching the Simulator Game:
To play the interactive console application across Windows, macOS, or Linux systems:
python src/main.py