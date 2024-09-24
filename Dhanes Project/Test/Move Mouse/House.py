import ctypes
import time
import keyboard

# Function to move the mouse using ctypes
def move_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

# Set up the screen dimensions
screen_width = 100
screen_height = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# House parameters
house_width = 15
house_height = 10
roof_height = 5

# Get initial mouse position
start_pos = (screen_width // 2, screen_height // 2)
end_pos = start_pos
move_mouse(*start_pos)

# Main loop
running = True
drawing = False
while running:
    try:
        # Get the current mouse position
        current_pos = ctypes.windll.user32.GetCursorPos()

        # Check if mouse position changed
        if current_pos != end_pos:
            end_pos = current_pos

            # Clear the screen
            print("\033[H\033[J")  # Clear console (Unix/Linux)
            print("\x1b[2J\x1b[H")  # Clear console (Windows)
            print("\n" * 100)  # Clear console (Alternative method for Windows)
            
            # Draw the house
            house_top_left_x = max(0, end_pos[0] - house_width // 2)
            house_top_left_y = max(0, end_pos[1] - house_height)
            house_bottom_right_x = min(screen_width, house_top_left_x + house_width)
            house_bottom_right_y = min(screen_height, house_top_left_y + house_height)
            print(" " * house_top_left_x + "+" + "-" * (house_width - 2) + "+")
            for y in range(house_top_left_y + 1, house_bottom_right_y):
                print(" " * house_top_left_x + "|" + " " * (house_width - 2) + "|")
            print(" " * house_top_left_x + "+" + "-" * (house_width - 2) + "+")
            print(" " * (end_pos[0] - 1) + "|")
            print(" " * (end_pos[0] - 2) + "/\\")

        # Check if 'q' key is pressed to exit
        if keyboard.is_pressed('q'):
            running = False
            break

    except Exception as e:
        print("An error occurred:", e)
        break

    # Wait for a short interval
    time.sleep(0.1)

# Clear the screen before exiting
print("\033[H\033[J")
print("\x1b[2J\x1b[H")
print("\n" * 100)
print("Exited.")
