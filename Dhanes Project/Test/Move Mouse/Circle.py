import ctypes
import time
import math

# Constants for mouse input
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_ABSOLUTE = 0x8000
SM_CXSCREEN = 0
SM_CYSCREEN = 1

# Function to get the screen dimensions
def get_screen_size():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(SM_CXSCREEN), user32.GetSystemMetrics(SM_CYSCREEN)

# Function to simulate mouse click and movement to draw a circle
def draw_circle(radius, speed):
    screen_width, screen_height = get_screen_size()

    # Calculate the center of the screen
    center_x = screen_width // 2 + 1
    center_y = screen_height // 2 - 18.5  # Adjusted 2 pixels above the center

    # Calculate the number of points along the circle based on the speed
    num_points = int(360 / (speed * 2)) + 1

    # Calculate the time interval based on the desired speed and number of points
    interval = 1 / (speed * num_points)

    # Wait for 3 seconds
    time.sleep(1)

    # Simulate mouse movement to the starting point of the circle
    start_x = center_x + radius
    start_y = center_y
    start_x_abs = int(start_x / screen_width * 65535)
    start_y_abs = int(start_y / screen_height * 65535)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, start_x_abs, start_y_abs, 0, 0)

    # Perform a left mouse button down (draw)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    # Simulate mouse movement to draw the circle
    for angle in range(0, 361, int(360 / num_points)):  # Increment angle based on the number of points
        # Calculate the position based on the angle
        x = int(center_x + radius * math.cos(math.radians(angle)))
        y = int(center_y + radius * math.sin(math.radians(angle)))

        # Convert coordinates to absolute values
        x_abs = int(x / screen_width * 65535)
        y_abs = int(y / screen_height * 65535)

        # Move the mouse to the new position
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, x_abs, y_abs, 0, 0)

        # Wait for a short interval before the next move
        time.sleep(interval)

    # Perform a left mouse button up (stop drawing)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# Set the radius of the circle
radius = 360    # Adjust as needed

# Set the speed of the mouse movement (1 = slow, 10 = fast)
speed = 1
print("Press F11 in https://neal.fun/perfect-circle/")
# Draw a circle
draw_circle(radius, speed)
