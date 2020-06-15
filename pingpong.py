import pygame

from settings import Setting
import game_function as gf

from ball import Ball
from player import Player
from scoreboard import Scoreboard

def run_game():

	pygame.init()
	settings = Setting()
	screen = pygame.display.set_mode(
		(settings.screen_width, settings.screen_height) )
	pygame.display.set_caption('ping pong')

	player1 = Player(settings, screen)
	player2 = Player(settings, screen)
	player2.rect.centerx = player2.screen_rect.right - 30

	ball = Ball(settings, screen)

	scores = Scoreboard(settings, screen)
	

	while True:

		gf.check_events(screen, settings, player1, player2)

		player1.update()
		player2.update()

		

		gf.update_ball(settings, ball, player1, player2, scores)

		gf.update_screen(screen, settings, ball, player1, player2, scores)


run_game()
