from __future__ import annotations
import json
import pygame
from typing import Optional

from account_manager import Accounts, User
from helper import Helper
from settings import Settings

# Initializing objects / variables
accounts = Accounts('account_data.json')
user = accounts.handle_login()
run = True
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))

# main loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
