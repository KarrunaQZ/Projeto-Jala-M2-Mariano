import pygame
import os

# Global
ASSETS_PATH = os.path.join(os.path.dirname(__file__), '..', "assets")
TITLE = "The Adventurer's Journey"
ICON = pygame.image.load(os.path.join(ASSETS_PATH, 'icon.png'))
SCREEN_WIDTH = 927
SCREEN_HEIGHT = 435
BACKGROUND = pygame.image.load(os.path.join(ASSETS_PATH, 'background.jpg'))
BACKGROUND_MENU = pygame.image.load(os.path.join(ASSETS_PATH, 'background-menu.jpg'))
FPS = 30
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Adventurer's Journey (alpha edition)")




#Adventurer
ADVENTURER_SIZE = 100
ADVENTURER_X = 130
ADVENTURER_Y = 275
JUMP_VEL = 8.5
SLIDE_VEL = 8.5
ATTACK_VEL = 8.5
AIR_ATTACK_VEL = 8.5

ADVENTURER_IDLE = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/idle/adventurer-idle-2-00.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/idle/adventurer-idle-2-01.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/idle/adventurer-idle-2-02.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/idle/adventurer-idle-2-03.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE))
]

ADVENTURER_RUN = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/run/adventurer-run-00.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/run/adventurer-run-01.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/run/adventurer-run-02.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/run/adventurer-run-03.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/run/adventurer-run-04.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/run/adventurer-run-05.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE))
]

ADVENTURER_JUMP = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/jump/adventurer-jump-00.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/jump/adventurer-jump-01.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/jump/adventurer-jump-02.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    #pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/jump/adventurer-jump-03.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE))
]

ADVENTURER_FALL = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/fall/adventurer-fall-00.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/fall/adventurer-fall-01.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE))
]

ADVENTURER_SLIDE = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/slide/adventurer-slide-00.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/slide/adventurer-slide-01.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE))

]

ADVENTURER_ATTACK = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/attack/adventurer-attack3-00.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/attack/adventurer-attack3-01.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/attack/adventurer-attack3-02.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/attack/adventurer-attack3-03.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/attack/adventurer-attack3-04.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/attack/adventurer-attack3-05.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE))
]

ADVENTURER_AIR_ATTACK = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/air_attack/adventurer-air-attack1-00.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/air_attack/adventurer-air-attack1-01.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/air_attack/adventurer-air-attack1-02.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'adventurer/air_attack/adventurer-air-attack1-03.png')), (ADVENTURER_SIZE, ADVENTURER_SIZE))

]

# Bird
BIRD_SIZE = 64

BIRD = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'bird/bird (1).png')), (BIRD_SIZE, BIRD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'bird/bird (2).png')), (BIRD_SIZE, BIRD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'bird/bird (3).png')), (BIRD_SIZE, BIRD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'bird/bird (4).png')), (BIRD_SIZE, BIRD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'bird/bird (5).png')), (BIRD_SIZE, BIRD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'bird/bird (6).png')), (BIRD_SIZE, BIRD_SIZE))
]

# Wood
WOOD_SIZE = 50

SLIME = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'slime/slime-idle-0.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'slime/slime-idle-1.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'slime/slime-idle-2.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'slime/slime-idle-3.png')), (WOOD_SIZE, WOOD_SIZE))
]


# Metal
METAL_SIZE = 50

SMALL_METAL = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'metal/small_metal/small_metal_spike_01.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'metal/small_metal/small_metal_spike_02.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'metal/small_metal/small_metal_spike_03.png')), (WOOD_SIZE, WOOD_SIZE))
]

LONG_METAL = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'metal/long_metal/long_metal_spike_01.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'metal/long_metal/long_metal_spike_02.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'metal/long_metal/long_metal_spike_03.png')), (WOOD_SIZE, WOOD_SIZE)),
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'metal/long_metal/long_metal_spike_04.png')), (WOOD_SIZE, WOOD_SIZE))
]

METAL = [
    SMALL_METAL,
    LONG_METAL
]

# Sword
SWORD_SIZE = 80

SWORD = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'sword/sword.png')), (SWORD_SIZE, SWORD_SIZE))
]

SHIELD_SIZE = 40

SHIELD = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'shield/shield.png')), (SHIELD_SIZE, SHIELD_SIZE))
]

APPLE_SIZE = 40

APPLE = [
    pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'rotten apple/rotten apple.png')), (APPLE_SIZE, APPLE_SIZE))
]

