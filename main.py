import pygame
import random
import time


def pause():
    paused = True
    while paused:
        for event2 in pygame.event.get():
            if event2.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event2.type == pygame.KEYDOWN:
                paused = False


def print_text(message, y, colors, font_size):
    font_type = pygame.font.Font(None, font_size)
    text = font_type.render(message, True, colors)
    text_rect = text.get_rect(center=(W / 2, y))
    display.blit(text, text_rect)
    pygame.display.update()


def get_sentence():
    sentences = open('file.txt').read().splitlines()
    line = random.choice(sentences)
    return line


def show_results(mistake, start_time, words, length):
    total_time = round(time.time() - start_time, 1)
    wpn = round(words * 60 / total_time, 1)
    text = f'Время:{int(total_time // 60)}:{round(total_time % 60, 2)} {wpn} зн/мин Ошибок:{mistake} ' \
           f'({round(mistake / length, 2)}%)'
    print_text(text, 400, WHITE, 30)
    text2 = 'Нажмите любую клавишу что бы начать заново'
    print_text(text2, 450, WHITE, 35)


W = 1000
H = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
FPS = 30
time_start = 0
mistakes = 0
total_words = 0
color = WHITE
pygame.init()
pygame.display.set_caption('клавиатурный тренажер')
display = pygame.display.set_mode((W, H))
input_text = ''
sentence = get_sentence()
mistake_exist = False
pressed = False
running = True
mistake_number = len(sentence)
while running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    display.fill((0, 0, 0))
    pygame.draw.rect(display, WHITE, (50, 230, 900, 80))
    pygame.draw.rect(display, color, (50, 230, 900, 80), 4)
    print_text(input_text, 270, BLACK, 30)
    print_text(sentence, 100, YELLOW, 30)
    if mistake_exist:
        color = RED
    else:
        color = WHITE
        if len(input_text) == len(sentence):
            show_results(mistakes, time_start, total_words, len(sentence))
            pause()
            sentence = get_sentence()
            mistakes = 0
            total_words = 0
            pressed = False
            input_text = ''
    if not pressed:
        print_text('Нажмите любую клавишу что бы начать', 400, RED, 35)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not pressed:
                time_start = time.time()
                pressed = True
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif len(input_text) < len(sentence):
                total_words += 1
                input_text += event.unicode
            if 0 < len(input_text) <= mistake_number:
                if input_text[-1] != sentence[len(input_text) - 1]:
                    if not mistake_exist:
                        mistakes += 1
                        mistake_exist = True
                        mistake_number = len(input_text)
                elif mistake_exist:
                    mistake_exist = False
                    mistake_number = len(sentence)
