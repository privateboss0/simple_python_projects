import turtle
import time

# Switch to Logo mode - Up = 0 degrees, then go clockwise
turtle.mode("logo")

# Clock Hand Lengths
SECOND_HAND = 105
MINUTE_HAND = 85
HOUR_HAND = 65

# Create a Turtle screen
window = turtle.Screen()
window.bgcolor("red")
window.tracer(0)

# Create a Turtle object
face = turtle.Turtle(visible=False)
face.speed(5)  
hands = turtle.Turtle(visible=False)

# Function to draw a clock face with hands
def draw_clock_face():
    face.clear()
    face.penup()
    face.goto(150, 0) 
    face.setheading(0)
    face.pendown()
    face.circle(150)

    # Draw the clock numbers and balls.. Not what you are thinking! :)
    for i in range(12):
        hour = 12 if i == 0 else i
        face.penup()
        face.goto(0,0)
        face.setheading(i*30) # angle in degrees
        face.forward(125)
        face.pendown()
        face.dot(15, "pink" if hour in [3, 6, 9, 12] else "blue")
        face.setheading(180)
        face.penup()
        face.forward(25)
        face.color("black")
        face.write(str(hour), align="center", font=("Arial", 10, "normal"),)

# Function to draw clock hands
def draw_clock_hands():
    current_time = time.localtime()
    # Clear previous hands
    hands.clear()

    # Calculate angles for the hands
    second_angle = current_time.tm_sec * 6
    minute_angle = current_time.tm_min * 6 - current_time.tm_sec * 0.1
    hour_angle = (current_time.tm_hour % 12) * 30 + current_time.tm_min * 0.5
   
    # Draw the second hand
    hands.penup()
    hands.goto(0, 0)
    hands.pendown()
    hands.color("white")
    hands.setheading(second_angle)
    hands.pensize(1)
    hands.forward(SECOND_HAND)

    # Draw the minute hand
    hands.penup()
    hands.goto(0, 0)
    hands.pendown()
    hands.color("gold")
    hands.setheading(minute_angle)
    hands.pensize(3)
    hands.forward(MINUTE_HAND)

    # Draw the hour hand
    hands.penup()
    hands.goto(0, 0)
    hands.pendown()
    hands.color("green")
    hands.setheading(hour_angle)
    hands.pensize(5)
    hands.forward(HOUR_HAND)

# Function to update the clock continuously
def update_clock():
    draw_clock_face()
    while True:
        draw_clock_hands()  
        window.update()  
        time.sleep(1)  

# Main program
if __name__ == "__main__":
    
    # Call the function to draw the clock face
    update_clock()  # Call the function to draw the clock hands
    screen.exitonclick() # Close the window when clicked
