from time import sleep
from time import time
import json
from sys import exit
import pygame
from pyautogui import size
pygame.init()

def check_exit(line_number):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if progress_change:
                        with open('progress.json', 'r') as progress:
                            data = json.load(progress)
                        data[text_name] = line_number
                        
                        with open('progress.json', 'w') as progress:
                            json.dump(data, progress)
                    pygame.quit
                    exit()
            else:
                if progress_change:
                    with open('progress.json', 'r') as progress:
                        data = json.load(progress)
                    data[text_name] = line_number
                    
                    with open('progress.json', 'w') as progress:
                        json.dump(data, progress)
                pygame.quit()
                exit()

def actual_wpm():
    print(f"Actual WPM: {60/delay}")



text_name = input("What text would you like to read? (Input name of file, including extension)\n")
text = open(text_name, 'r')

run_type = input("Continue from previous progress? {y/n}").lower()

if run_type != 'n':
    progress_change = True
    with open('progress.json', 'r') as progress_var:
        data = json.load(progress_var)
    try:
        progress = int(data[text_name])
    except KeyError:
        data[text_name] = 0
        progress = 0
else:
    progress_change_input = input("Would you like this session to change your stored progress? {y/n}").lower()
    if progress_change_input != 'n':
        progress_change = True
    else:
        progress_change = False
    progress = 0



wpm = int(input('WPM?\n'))
black = (0, 0, 0)
white = (255, 255, 255)
X, Y = size() # Screen Resolution
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Speed Read')
font_path = "static/SourceSans3-SemiBold.ttf"
font_size = 128 # Pixels
font = pygame.font.Font(font_path, font_size)
delay = 60/wpm



for line_number, line in enumerate(text):
    if line_number >= progress:
        for word in line.split():
            sleep(delay)
            text = font.render(word, True, black)
            textRect = text.get_rect()
            textRect.center = (X // 2, Y // 2)
            start = time()
            check_exit(line_number)
            while True:
                display_surface.fill(white)
                display_surface.blit(text, textRect)
                pygame.display.update()
                check_exit(line_number)
                end = time()
                if end-start >= delay:
                    # actual_wpm()
                    break
