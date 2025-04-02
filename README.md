# Snake_Game
This is my first Game Project in Python programming language using "Turtle library"

🐍 Snake Game  

1. Introduction  
The Snake Game is a classic arcade game where the player controls a snake that grows in length as it consumes food. The goal is to collect as many points as possible without colliding with the walls or itself. This project replicates the Nokia Snake game using the Turtle library in Python.  

---

2. Features
✅ Realistic Snake Movement– The snake moves smoothly in four directions (Up, Down, Left, Right) using the arrow keys.  
✅ Food Mechanics – Randomly placed food increases the snake’s length and score.  
✅ Boundary Collision – The snake dies if it touches the wall.  
✅ Self-Collision Detection – The game ends if the snake collides with itself.  
✅ Score System– A live scoreboard updates the player’s points.  
✅ Pause/Resume Feature– The game can be paused and resumed with the spacebar.  
✅ Game Over & Reset– The game restarts when the player loses.  
✅ Smooth Animation & Speed Control – The snake's speed increases gradually as the score increases.  

---

3. Technologies Used  
🔹 Python– The main programming language.  
🔹 Turtle Library – Used for game graphics and animations.  
🔹 Random Library – Generates random positions for food.  
🔹 Time Module – Controls game speed and pause functionality.  
🔹 Winsound Module (Windows) – Adds sound effects for eating food and game over.  

---

4. Working of the Game
1⃣ Game Starts – The snake appears at the center of the screen.  
2⃣ Player Controls – The snake moves using **arrow keys**.  
3⃣ Eating Food – When the snake reaches food, it grows, and the score increases.  
4⃣ Boundary & Self-Collision – If the snake touches the wall or itself, the game ends.  
5⃣ Game Over & Restart – The player can restart the game after losing.  

---

5. Challenges Faced & Solutions
🔹 Smooth Movement Implemented  separate functions for controlling the snake's direction.  
🔹 Collision Detection:  Used  coordinate checking for walls and self-collision.   
🔹 Game Over Handling: Created a reset function that restarts the game when a collision occurs.  
 
---

7. Conclusion  
The Snake Game in Python is a fun and engaging project that enhances understanding of game logic, animation, and event handling. It provides a solid foundation for building more advanced games using Python and Turtle graphics.
