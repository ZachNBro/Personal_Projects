"""
    File name: robot.py
    Author: Zachary Brown
    Date created: 05/24/23
    Date last modified: 05/29/23
    Python version: 3.9
    Description: Control a robot using keystrokes or
    speech-to-text modes. This program uses the pygame
    and speech recognition modules as well as threading
    for smoother operation.
"""

import pygame
import math
import speech_recognition as sr
import threading

WIDTH = 800
HEIGHT = 600
CONTROL_WIDTH = 200

class Robot:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.orientation = 0
        self.image = image

    def move_forward(self, distance):
        self.x += distance * math.cos(self.orientation)
        self.y += distance * math.sin(self.orientation)

    def move_backward(self, distance):
        self.x -= distance * math.cos(self.orientation)
        self.y -= distance * math.sin(self.orientation)

    def turn_left(self, angle):
        self.orientation += angle

    def turn_right(self, angle):
        self.orientation -= angle

    def draw(self, surface):
        # Rotate the image based on the current orientation
        rotated_image = pygame.transform.rotate(self.image, math.degrees(self.orientation))
        rect = rotated_image.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated_image, rect)

class RobotController:
    def __init__(self):
        self.robot_image = pygame.image.load("robot.png_small")
        self.robot = Robot(WIDTH // 2, HEIGHT // 2, self.robot_image)
        self.graph = pygame.Surface((WIDTH, HEIGHT))
        self.controls = pygame.Surface((CONTROL_WIDTH, HEIGHT))
        self.font = pygame.font.SysFont(None, 24)
        self.speech_mode = False
        self.command_queue = []

        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def draw_movement(self):
        self.graph.fill((255, 255, 255))  # Clear the graph surface
        self.robot.draw(self.graph)

    def move_robot(self, key):
        if key == pygame.K_w:
            self.robot.move_forward(10)
        elif key == pygame.K_s:
            self.robot.move_backward(10)
        elif key == pygame.K_a:
            self.robot.turn_left(0.1)
        elif key == pygame.K_d:
            self.robot.turn_right(0.1)

    def draw_controls(self):
        self.controls.fill((200, 200, 200))
        text = self.font.render("Controls:", True, (0, 0, 0))
        self.controls.blit(text, (20, 20))
        text = self.font.render("W: Move Forward", True, (0, 0, 0))
        self.controls.blit(text, (20, 60))
        text = self.font.render("S: Move Backward", True, (0, 0, 0))
        self.controls.blit(text, (20, 100))
        text = self.font.render("A: Turn Left", True, (0, 0, 0))
        self.controls.blit(text, (20, 140))
        text = self.font.render("D: Turn Right", True, (0, 0, 0))
        self.controls.blit(text, (20, 180))
        text = self.font.render("Q: Quit", True, (0, 0, 0))
        self.controls.blit(text, (20, 260))  # Add this line for the quit option

        if self.speech_mode:
            text = self.font.render("Speech-to-Text", True, (255, 0, 0))
            self.controls.blit(text, (20, 220))
        else:
            text = self.font.render("Keyboard", True, (0, 0, 255))
            self.controls.blit(text, (20, 220))

    def toggle_mode(self):
        self.speech_mode = not self.speech_mode

        if self.speech_mode:
            self.start_listening_thread()
        else:
            self.stop_listening_thread()

    def start_listening_thread(self):
        self.command_queue.clear()  # Clear any pending commands
        threading.Thread(target=self.listen_for_command).start()

    def stop_listening_thread(self):
        self.command_queue.clear()  # Clear any pending commands

    def listen_for_command(self):
        with self.microphone as source:
            print("Listening for command...")
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio)
            print("Recognized command:", command)
            self.command_queue.append(command)
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError as e:
            print("Error occurred during speech recognition:", str(e))

    def handle_commands(self):
        if len(self.command_queue) > 0:
            command = self.command_queue.pop(0)
            self.process_command(command)

    def process_command(self, command):
        if "move forward" in command:
            self.robot.move_forward(10)
        elif "move backward" in command:
            self.robot.move_backward(10)
        elif "turn left" in command:
            self.robot.turn_left(0.1)
        elif "turn right" in command:
            self.robot.turn_right(0.1)
        elif "quit" in command:
            pygame.event.post(pygame.event.Event(pygame.QUIT))  # Post a QUIT event to exit the program

    def close_window(self):
        pygame.quit()

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window = pygame.display.set_mode((WIDTH + CONTROL_WIDTH, HEIGHT))
pygame.display.set_caption("Robot Control")

# Create an instance of the RobotController class
controller = RobotController()

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                controller.toggle_mode()
            elif event.key == pygame.K_q:
                running = False

    if not controller.speech_mode:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            controller.move_robot(pygame.K_w)
        elif keys[pygame.K_s]:
            controller.move_robot(pygame.K_s)
        elif keys[pygame.K_a]:
            controller.move_robot(pygame.K_a)
        elif keys[pygame.K_d]:
            controller.move_robot(pygame.K_d)
    else:
        controller.handle_commands()

    # Clear the window
    window.fill((255, 255, 255))

    # Draw the robot's movement
    controller.draw_movement()

    # Draw the controls
    controller.draw_controls()

    # Blit the graph and controls onto the window
    window.blit(controller.graph, (0, 0))
    window.blit(controller.controls, (WIDTH, 0))

    # Update the display
    pygame.display.flip()

    clock.tick(60)

# Close the window and quit the program
controller.close_window()
