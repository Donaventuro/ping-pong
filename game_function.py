import sys
import pygame
from time import sleep


def update_screen(screen, settings, ball, player1, player2, scores):

		screen.fill(settings.bg_color)

		player1.draw()
		player2.draw()

		ball.blitme()

		
		scores.prep_score()
		scores.show_score()

		pygame.display.flip()
		
def check_events(screen, settings, player1, player2):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, player1, player2)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, player1, player2)



def check_keydown_events(event, player1, player2):

	if event.key == pygame.K_ESCAPE:
		pygame.display.quit()
		sys.exit()
	if event.key == pygame.K_w:
		player1.moving_top = True
	if event.key == pygame.K_s:
		player1.moving_bot = True
	if event.key == pygame.K_UP:
		player2.moving_top = True
	if event.key == pygame.K_DOWN:
		player2.moving_bot = True

def check_keyup_events(event, player1, player2):

	if event.key == pygame.K_w:
		player1.moving_top = False
	if event.key == pygame.K_s:
		player1.moving_bot = False
	if event.key == pygame.K_UP:
		player2.moving_top = False
	if event.key == pygame.K_DOWN:
		player2.moving_bot = False    


def check_ball_edges(settings, ball, player1, player2, scores):

	if ball.check_ball_bot() or ball.check_ball_top():
		settings.ball_direction_y *= -1

	if ball.check_ball_right():
		settings.ball_direction_x *= -1
		scores.score_1 += 1
		ball.centerx = ball.screen_rect.centerx
		ball.centery = ball.screen_rect.centery
		sleep(1)
		

	if ball.check_ball_left():
		settings.ball_direction_x *= -1
		scores.score_2 += 1
		ball.centerx = ball.screen_rect.centerx
		ball.centery = ball.screen_rect.centery
		sleep(1)



def update_ball(settings, ball, player1, player2, scores):

	check_ball_edges(settings, ball, player1, player2, scores)

	if (ball.rect.right == player2.rect.centerx and player2.rect.bottom >= ball.rect.bottom and ball.rect.top >= player2.rect.top):
		settings.ball_direction_x *= -1

		

	if (ball.rect.left == player1.rect.centerx and player1.rect.bottom >= ball.rect.bottom and ball.rect.top >= player1.rect.top):
		settings.ball_direction_x *= -1


	
	ball.update()
	

	
