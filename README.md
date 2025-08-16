# Flappy Bird Game (Python + Pygame)

This is a clone of the classic **Flappy Bird** game, built using **Python** and the **Pygame** library. The game includes sprites, background, pipes, and sound effects to create a smooth gaming experience.

---

## 🎮 Features
- Classic **Flappy Bird gameplay** with score tracking.  
- **Collision detection** with pipes and ground.  
- **Sound effects** (wing flap, point, hit, die, swoosh).  
- **Custom sprites** for player, background, pipes, and base.  
- Automatically generated pipes for continuous gameplay.  

---

## 📂 Project Structure
```
FlappyBird/
│
├── flappybird.py          # Main game file
├── gallery/
│   ├── sprites/
│   │   ├── player.png
│   │   ├── background.png
│   │   ├── pipe.png
│   │   ├── base.png
│   │   ├── message.png
│   │   ├── 0.png ... 9.png   # Number sprites
│   └── audio/
│       ├── die.wav
│       ├── hit.wav
│       ├── point.wav
│       ├── swoosh.wav
│       └── wing.wav
```

---

## ⚙️ Requirements
- Python 3.10+ (your code uses Python 3.13 path, so ensure compatibility)  
- [Pygame](https://www.pygame.org/wiki/GettingStarted) library  

Install pygame with:
```bash
pip install pygame
```

---

## 🚀 How to Run
1. Clone or download the project.  
2. Make sure the `gallery/sprites` and `gallery/audio` folders are placed correctly.  
3. Open a terminal/command prompt in the project folder.  
4. Run the game using:
   ```bash
   python flappybird.py
   ```
   Or (if Python 3.13 is installed at `C:\Python313\python.exe`):
   ```bash
   C:\Python313\python.exe flappybird.py
   ```

---

## 🕹️ Gameplay
- Press **SPACE** or **UP ARROW** to flap the bird.  
- Avoid hitting the pipes or ground.  
- Each time you pass between pipes, your **score increases**.  
- The game ends when the bird collides with a pipe or the ground.  

---

## 🔊 Sounds
- **wing.wav** → Flap sound  
- **point.wav** → Scoring sound  
- **hit.wav** → Collision with pipe  
- **die.wav** → Game over sound  
- **swoosh.wav** → Transition sound  

---

## 📸 Screenshots
*(Add screenshots of your game here if you want)*  

---

## 👨‍💻 Author
This project was built as a **Pygame practice project**. Inspired by CodeWithHarry’s Flappy Bird tutorial.  
