import os
import pygame
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASSETS_DIR = os.path.join(BASE_DIR, 'rs')

BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')

IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')

IMG_GAME_START = os.path.join(ASSETS_DIR, 'images/start.png')

BG_MUSIC = os.path.join(ASSETS_DIR, 'sounds/game_bg_music.mp3')

TEXT_SOCRE_COLOR = pygame.Color(0, 0, 0)

SCORE_SHOOT_SMALL = 1

PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, 'store/rect.txt')

UOR_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/main1.png'),
    os.path.join(ASSETS_DIR, 'images/main2.png')
]

BULLET_TMG = os.path.join(ASSETS_DIR, 'images/virus.png')

BULLET_SHOOT_TMG = os.path.join(ASSETS_DIR, 'sounds/bullet.wav')

SMALL_ENEMY_PLANE_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/mask.png')
]

BLACK_COFFIN = os.path.join(ASSETS_DIR, 'images/black.png')