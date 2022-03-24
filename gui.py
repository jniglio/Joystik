from guizero import App, Text, Picture, PushButton
import pygame
import time
import random

#functions and games
def snake_game():
    print("code for snake game")

def asteroid_game():
    print("code for asteroid game")

def collision_game():
    print("code for collision game")

#initial GUI
app = App(title = "Joystik")
welcome_message = Text(app, text="Welcome to Joystik!", size = 20, color = "lightgreen")
python_choice = PushButton(app, command = snake_game, text="SNAKE GAME")
python_choice = PushButton(app, command = asteroid_game, text="ASTEROID GAME")
python_choice = PushButton(app, command = collision_game, text="COLLISION GAME")
#my_logo = Picture(app, image="logo.PNG")

#display everything
app.display()

