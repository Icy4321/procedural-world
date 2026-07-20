import math
import random

CONFIG = {
    "width": 40,
    "height": 40,
    "view_w": 14,
    "view_h": 14,
    "vision_radius": 5
}

TERRAIN_TYPES = {
    "~": "deep water",
    "=": "shallow water",
    ",": "sand",
    ".": "grass",
    "t": "forest",
    "*": "wildflower meadow",
    "^": "hills",
    "#": "mountains"
}

def fade(t):
    return t ** 3 * (t * (t * 6 - 15) + 10)

def lerp(t, a, b):
    return a + t * (b - a)

def grad(hash_val, x, y):
    h = hash_val & 7
    if h == 0: return x + y
    elif h == 1: return -x + y
    elif h == 2: return x - y
    elif h == 3: return -x - y
    elif h == 4: return x
    elif h == 5: return -x
    elif h == 6: return y
    else: return -y

def perlin_noise_2d(x, y, p_table):
    X = int(math.floor(x)) & 255
    Y = int(math.floor(y)) & 255
    xf = x - math.floor(x)
    yf = y - math.floor(y)
    u = fade(xf)
    v = fade(yf)

    aa = p_table[p_table[X] + Y]
    ab = p_table[p_table[X] + Y + 1]
    ba = p_table[p_table[X + 1] + Y]
    bb = p_table[p_table[X + 1] + Y + 1]

    x1 = lerp(u, grad(aa, xf, yf), grad(ba, xf - 1, yf))
    x2 = lerp(u, grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1))
    return lerp(v, x1, x2)

def generate_map(w, h, seed):
    if w <= 0 or h <= 0:
        raise ValueError("Map dimensions must be greater than zero.")
        
    rng = random.Random(seed)
    permutation = list(range(256))
    rng.shuffle(permutation)
    p_table = permutation * 2

    tiles = []
    for y in range(h):
        row = []
        for x in range(w):
            nx = x / 25.0
            ny = y / 15.0
            val = perlin_noise_2d(nx, ny, p_table) + (perlin_noise_2d(nx * 2, ny * 2, p_table) * 0.5)
            val = max(0.0, min(1.0, (val + 1.2) / 2.4))

            if val < 0.22: tile = "~"
            elif val < 0.32: tile = "="
            elif val < 0.40: tile = ","
            elif val < 0.65: tile = "."
            elif val < 0.78: tile = "t"
            elif val < 0.88: tile = "^"
            else: tile = "#"

            if rng.random() < 0.03 and tile in [".", "t", ","]:
                tile = "*"
            row.append(tile)
        tiles.append(row)
    return tiles

class GameSession:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else random.randint(1, 100000)
        self.tiles = generate_map(CONFIG["width"], CONFIG["height"], self.seed)
        self.px = CONFIG["width"] // 2
        self.py = CONFIG["height"] // 2
        self.steps = 0
        self.message = "Welcome to the world center."
        
        # Enforce valid spawn point boundary condition
        if self.tiles[self.py][self.px] in ["~", "#", "="]:
            self.tiles[self.py][self.px] = "."

    def try_move(self, dx, dy):
        nx, ny = self.px + dx, self.py + dy
        if 0 <= nx < CONFIG["width"] and 0 <= ny < CONFIG["height"]:
            target_tile = self.tiles[ny][nx]
            if target_tile not in ["~", "#", "="]:
                self.px, self.py = nx, ny
                self.steps += 1
                self.message = f"Moved to {TERRAIN_TYPES.get(target_tile, 'unknown')}."
                return True
        self.message = "That terrain is too rough to cross."
        return False

    def get_view_buffer(self):
        """Constructs a matrix representation of what the camera sees."""
        half_w, half_h = CONFIG["view_w"] // 2, CONFIG["view_h"] // 2
        radius = CONFIG["vision_radius"]
        view = []
        
        for y in range(self.py - half_h, self.py + half_h + 1):
            row = []
            for x in range(self.px - half_w, self.px + half_w + 1):
                if not (0 <= x < CONFIG["width"] and 0 <= y < CONFIG["height"]):
                    row.append(" ")
                elif x == self.px and y == self.py:
                    row.append("@")
                else:
                    if math.sqrt((x - self.px)**2 + (y - self.py)**2) <= radius:
                        row.append(self.tiles[y][x])
                    else:
                        row.append("?")
            view.append(row)
        return view