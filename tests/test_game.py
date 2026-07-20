import pytest
from src.game_engine import GameSession, generate_map, CONFIG

# 1. Determinism Test: Ensures the Perlin map generation is predictable given a fixed seed
def test_map_generation_is_deterministic():
    seed = 42
    map_a = generate_map(CONFIG["width"], CONFIG["height"], seed)
    map_b = generate_map(CONFIG["width"], CONFIG["height"], seed)
    assert map_a == map_b, "Regression Error: Map generation is non-deterministic for identical seeds!"

# 2. Input/Boundary Validation Test: Tests handling of invalid parameters
def test_invalid_map_dimensions_raise_exception():
    with pytest.raises(ValueError):
        generate_map(-10, 40, 12345)

# 3. Spawn State Integrity Test: Confirms safety conditions for initial player location
def test_spawn_tile_is_always_passable():
    for seed in range(100):  # Fuzzy test across 100 unique seeds
        game = GameSession(seed=seed)
        spawn_tile = game.tiles[game.py][game.px]
        assert spawn_tile not in ["~", "#", "="], f"Initialization Failure: Player spawned on blocked tile '{spawn_tile}' using seed {seed}."

# 4. Movement Boundaries Test: Validates step limits and obstruction parameters
def test_movement_logic():
    game = GameSession(seed=42)
    initial_x, initial_y = game.px, game.py
    
    # Inject an impassable block right above the player to verify obstruction behavior
    game.tiles[initial_y - 1][initial_x] = "#"
    moved = game.try_move(0, -1)
    
    assert moved is False, "Safety Violation: Player successfully walked into an impassable mountain block."
    assert game.px == initial_x and game.py == initial_y, "State Corruption: Player coordinates updated despite failed movement."
    assert game.steps == 0, "Telemetry Error: Step count increments on blocked movements."

# 5. Out-of-Bounds Test: Assures coordinate tracking handles map edges without index exceptions
def test_map_edge_boundaries():
    game = GameSession(seed=11)
    # Artificially teleport the player to the far left boundary column
    game.px = 0
    game.tiles[game.py][0] = "."  # Force passable spot
    
    moved = game.try_move(-1, 0)
    assert moved is False, "Boundary Violation: Player slipped past the zero index column array boundary."
    assert game.px == 0, "State Corruption: Player coordinate dropped into negative indices."