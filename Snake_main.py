import turtle # Import the turtle module
import time 
import random
import winsound # for play sounds on windows

# Create the game screen
screen= turtle.Screen()
screen.title("Snake Game with Power-ups") # Game title

screen.bgcolor("black") #set background color to black
screen.setup(width=600, height=600) # screen size (600x600 pixels)

screen.tracer(0) # turn off automatic updates for smooth animation

# create the snake
snake_segments = [] # list to store the snake parts
starting_position= [(0, 0),(-20, 0),(-40, 0)] # initial positions

for position in starting_position:
    segment = turtle.Turtle("square") # create a square segment
    segment.color("white") # set color to white
    segment.penup() # disable drawing
    segment.goto(position) # move to the starting position
    snake_segments.append(segment) # add to the list

# set initial movment direction
direction = "stop"

# create food
food = turtle.Turtle()
food.shape("circle") # food shape (circle)
food.color("red") # food color
food.penup() # no drawing
food.shapesize(stretch_wid=0.5, stretch_len=0.5) # make food smaller
food.goto(random.randint(-280, 280), random.randint(-280, 280)) # random position

# create special power-ups food (bound food)
bonus_food = turtle.Turtle()
bonus_food.shape("triangle")
bonus_food.color("gold")
bonus_food.penup()
bonus_food.shapesize(stretch_wid=0.7, stretch_len=0.7)
bonus_food.goto(1000, 1000) # Initially hidden

# score variables
score = 0
high_score = 0
speed = 0.1 # Initial speed
reverse_mode = False

# create score display
score_display= turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 270)
score_display.write(f"Score: {score} High_score: {high_score}", align="center", font=("Arial", 20, "bold"))

# Function to update the score
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score} High_score: {high_score}", align="center", font=("Arial", 20, "bold"))

# function to play sound
def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)


# Function to add a new segment to the sanke
def add_segment():
    new_segment = turtle.Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    last_segment=snake_segments[-1] # Get the last segment
    last_segment.goto(last_segment.xcor(), last_segment.ycor()) # place it at the last segment's position
    snake_segments.append(new_segment) # add it to the snake list

# function to spawn bonus food randomly
def spawn_bonus_food():
    x,y = random.randint(-280, 280), random.randint(-280, 280)
    bonus_food.goto(x, y)
    screen.ontimer(remove_bonus_food, 5000) # bonus food disappear in 5 sec

# function to remove bonus food
def remove_bonus_food():
    bonus_food.goto(1000, 1000) # move out of view

# Function to reset the game
def reset_game():
    global score, high_score, speed, reverse_mode
    time.sleep(1)

    # play game over sound
    play_sound("game_over.wav")

    # Reset the snake position and remove extra segments
    for segment in snake_segments:
        segment.goto(1000, 1000)
    snake_segments.clear()

    # recreate the initial snake
    for position in starting_position:
        segment= turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        snake_segments.append(segment)


    # reset score, speed and reverse mode
    if score > high_score:
        high_score= score #update high score
    score = 0
    speed = 0.1 # reset speed to default
    reverse_mode = False
    update_score()



# movment function
def go_up():
    global direction
    if not reverse_mode and direction != "down": # prevenet moving directly in the opposite direction
        direction = "up"
    elif reverse_mode and direction != "up":
        direction = "down"

def go_down():
    global direction
    if not reverse_mode and direction != "up":
        direction = "down"  
    elif reverse_mode and direction != "down":
        direction = "up" 

def go_left():
    global direction
    if not reverse_mode and direction != "right":
        direction = "left"
    elif reverse_mode and direction != "left":
        direction = "right"

def go_right():
    global direction
    if not reverse_mode and direction != "left":
        direction = "right"
    elif reverse_mode and direction != "right":
        direction = "left"

# function to enable reverse mode
def enable_reverse_mode():
    global reverse_mode
    reverse_mode = True
    screen.ontimer(disble_reverse_mode, 5000) # revert after 5 sec

# function to disable reverse mode
def disble_reverse_mode():
    global reverse_mode
    reverse_mode = False 


# Function to move the snake based on the direction
def move():
    global direction, score, speed

    if direction == "up":
        snake_segments[0].seth(90)
    elif direction == "down":
        snake_segments[0].seth(270)
    elif direction == "left":
        snake_segments[0].seth(180)
    elif direction == "right":
        snake_segments[0].seth(0)

    # move each segment to the position of the previous one(starting from last)
    for i in range(len(snake_segments)-1, 0, -1):
        x = snake_segments[i - 1].xcor() # for x-coordinate
        y = snake_segments[i - 1].ycor() # for y-coordinate
        snake_segments[i].goto(x, y)
    
    # move the head forward by 20 pixels
    snake_segments[0].forward(20)


    # detect collision with food
    if snake_segments[0].distance(food) < 15: # if snake head close to food
        food.goto(random.randint(-280, 280), random.randint(-280, 280)) # move food to a new location
        add_segment() # grow the snake
        score+= 10 # Increase score
        update_score()

        # play eating sound
        play_sound("bite.wav")

        # Increase speed slightly
        if speed > 0.05:
            speed -= 0.005 # Reduces the sleep time, making the game faster after every food eaten.

        
        # 10% chance to spawn bonus food
        if random.random() < 0.1:
            spawn_bonus_food()
    

    # detect collision with bonus food
    if snake_segments[0].distance(bonus_food) < 15:
        bonus_food.goto(1000, 1000) # Hide bonus food
        add_segment()
        add_segment() # bonus adds extra length
        score += 30 # bonus points
        update_score()
        play_sound("powerup.wav")

        # 20% chance to activete reverse mode
        if random.random() < 0.2:
            enable_reverse_mode()
    
    # detect wall collision
    x,y = snake_segments[0].xcor(), snake_segments[0].ycor()
    if x > 290 or x < -290 or y > 290 or y < -290:
        reset_game()
    
    # detect self collision
    for segment in snake_segments[1:]:
        if snake_segments[0].distance(segment) < 10:
            reset_game()

# keyboard controls
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")


def game_loop():
    screen.update()
    move()
    screen.ontimer(game_loop, int(speed * 1000))  # Runs again after `speed` milliseconds

game_loop()  # Start the game loop
screen.mainloop()  # Keeps the window running