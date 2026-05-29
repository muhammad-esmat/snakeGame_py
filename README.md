# 🐍 Terminal Snake Game

A classic Snake game implemented in Python using the `curses` library and object-oriented design. Play directly in your terminal with smooth controls, dynamic food spawning, and real-time score tracking.

## 🚀 Features

- **Terminal-Based**: Runs natively in any standard terminal (Linux, macOS, WSL)
- **OOP Architecture**: Clean separation of logic with a dedicated `snake` class
- **Dynamic Gameplay**: Food respawns randomly; difficulty adjusts via `curses` timeout
- **ASCII Visuals**: Uses special characters (diamond `◆` for snake, sterling `£` for food)
- **Score Tracking**: Calculates and displays the final score upon game over

## 🛠️ Requirements

- **Python**: Version 3.x or higher
- **Library**: `curses` (pre-installed on Linux/macOS; requires `windows-curses` on Windows)

## How to Run

1. **Clone or download** the repository:
   ```bash
   git clone https://github.com/muhammad-esmat/snakeGame_py.git
   cd snakeGame_py
   ```

2. **Install dependencies** (Windows only):
   ```bash
   pip install windows-curses
   ```

3. **Run the game**:
   ```bash
   python snake_game.py
   ```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `↑` `↓` `←` `→` | Change direction |
| Any key | Exit after game over |

> The snake moves automatically. Press a direction key to turn.

## 📁 Project Structure

```
snakeGame_py/
├── snake.py    # Snake class definition (movement, collision, scoring)
├── snake_game.py   # Main game loop, terminal setup, and rendering
└── README.md       # Project documentation
```

## 🧠 Architecture Overview

- **`snake` Class**: Encapsulates the snake's body coordinates, direction logic, head/tail management, and collision detection
- **Main Loop**: Utilizes `curses` for non-blocking input handling and efficient screen refreshing
- **Collision Logic**: Detects wall hits and self-intersection to trigger the game over state
- **Food Logic**: Generates random coordinates ensuring food never spawns on the snake's body

## ⚠️ Platform Compatibility

This project relies on the `curses` library, which is **native to Unix-based systems** (Linux/macOS).

**Windows Users**: You must install the compatibility layer:
```bash
pip install windows-curses
```

## 📜 License

This project is open source and available for educational purposes. Feel free to study, modify, and share!

---
