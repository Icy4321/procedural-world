# Testable 2D Procedural World Engine

A modular, cross-platform 2D world generation engine built in Python, showcasing a decoupled framework specifically engineered for automated testing and CI/CD validation. 

# Project Structure

```
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
```

# Getting Started

Prerequisites:
* Python 3.8 or higher

1. Installation:
Clone this repository

git clone https://github.com/Icy4321/procedural-world.git
cd procedural-world

Install the required test engine packages:
pip install -r requirements.txt

2. Running the Automated Test Suite:
To launch the automated test inspectors from the root path with detailed logging data:
python -m pytest -v

3. Launching the Simulator:
To play the interactive console application across Windows, macOS, or Linux systems:
python src/main.py