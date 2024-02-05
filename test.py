import pygame
import random
import psutil
import datetime  # Add this import for datetime

# ... (previous code)

# Function to get RAM and CPU information



# Initialize pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 1080, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RAM Tester - Balls")  # Set window title
WHITE = (255, 255, 255)
BALL_RADIUS = 15
BALL_DIAMETER = 2 * BALL_RADIUS
GRAVITY = 0.5
BALLSCOUNT = 9999

# Initialize clock for controlling the frame rate
clock = pygame.time.Clock()

# Function to get RAM and CPU information
def get_system_info():
    # RAM information
    ram = psutil.virtual_memory()
    ram_percentage = ram.percent

    # CPU usage
    cpu_percentage = psutil.cpu_percent()

    return ram_percentage, cpu_percentage

# Function to log data to a file

def get_system_info():
    # RAM information
    ram = psutil.virtual_memory()
    ram_percentage = ram.percent

    # CPU usage
    cpu_percentage = psutil.cpu_percent()

    return ram_percentage, cpu_percentage

# Function to log data to a file with timestamp# Function to log data to a file with timestamp
def log_to_file(ram_usage, fps, cpu_usage):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log.txt", "a") as file:
        file.write(f"{timestamp} - RAM = {ram_usage}%, FPS = {fps:.2f}, CPU = {cpu_usage}%\n")


# ... (remaining code)

class Ball:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y > HEIGHT - BALL_RADIUS:
            self.y = HEIGHT - BALL_RADIUS
            self.velocity = -self.velocity * 0.9  # Invert and reduce the velocity for bouncing

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), BALL_RADIUS)


# Create 50 initial balls
balls = [Ball(random.randint(0, WIDTH), random.randint(0, HEIGHT), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) for _ in range(BALLSCOUNT)]

ball_counter = len(balls)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw balls
    for ball in balls:
        ball.update()

    for ball in balls:
        ball.draw(SCREEN)

    # Duplicate ball when it hits the bottom
    new_balls = [Ball(random.randint(0, WIDTH), 0, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) for ball in balls if ball.y == HEIGHT - BALL_RADIUS]
    balls.extend(new_balls)
    ball_counter += len(new_balls)

    # Draw counter and information
    font = pygame.font.Font(None, 36)
    text = font.render(f"Ball count: {ball_counter}", True, WHITE)
    SCREEN.blit(text, (WIDTH - 200, HEIGHT - 100))

    # Get and display RAM and CPU usage percentage
    ram_percentage, cpu_percentage = get_system_info()
    ram_text = font.render(f"RAM Usage: {ram_percentage}%", True, WHITE)
    SCREEN.blit(ram_text, (10, 50))

    cpu_text = font.render(f"CPU Usage: {cpu_percentage}%", True, WHITE)
    SCREEN.blit(cpu_text, (10, 90))

    # Get and display FPS
    fps = int(clock.get_fps())
    fps_text = font.render(f"FPS: {fps}", True, WHITE)
    SCREEN.blit(fps_text, (10, 10))

    # Log data to a file
    log_to_file(ram_percentage, fps, cpu_percentage)

    # Update display
    pygame.display.flip()

    # No frame rate cap
    clock.tick()

pygame.quit()
