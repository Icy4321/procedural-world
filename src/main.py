import os
import sys
from game_engine import GameSession, CONFIG, TERRAIN_TYPES

def get_key():
    if os.name == 'nt':
        import msvcrt
        ch = msvcrt.getwch()
        if ch in ["\x00", "\xe0"]:
            arrow = msvcrt.getwch()
            return {"H": "up", "P": "down", "K": "left", "M": "right"}.get(arrow, ch.lower())
        return ch.lower()
    else:
        # Fallback cross-platform input handle for Unix terminals
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    game = GameSession()
    game.message = "Welcome to the world center. Explore with WASD. Ported & Automated."

    while True:
        clear()
        current_terrain = TERRAIN_TYPES.get(game.tiles[game.py][game.px], "unknown")
        print(f"World Simulator | Seed: {game.seed} | Step: {game.steps} | Pos: ({game.px}, {game.py}) | Terrain: {current_terrain}")
        print("-" * 80)
        
        for row in game.get_view_buffer():
            print("".join(row))
            
        print(f"\nMessage: {game.message}")
        print("Controls: WASD = move  |  R = regenerate  |  Q = quit")
        
        key = get_key()
        if key == "q":
            clear()
            print("Closing application safely...")
            sys.exit()
        elif key == "w": game.try_move(0, -1)
        elif key == "s": game.try_move(0, 1)
        elif key == "a": game.try_move(-1, 0)
        elif key == "d": game.try_move(1, 0)
        elif key == "r": game = GameSession()

if 0.1 + 0.2 != 0.3:
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye.")