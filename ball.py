import pygame
from pygame.sprite import Sprite

class Ball(Sprite):

	def __init__(self, settings, screen):

		super().__init__()
		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load('images/ball.gif')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

	def check_ball_bot(self):
		if self.rect.bottom >= self.screen_rect.bottom:
			return True

	def check_ball_right(self):
		if self.rect.right >= self.screen_rect.right:
			return True

	def check_ball_top(self):
		if self.rect.top < 0:
			return True

	def check_ball_left(self):
		if self.rect.left < 0:
			return True

	def update(self):
		self.centerx +=	(self.settings.ball_speed
			* self.settings.ball_direction_x)
		self.centery +=	(self.settings.ball_speed
			* self.settings.ball_direction_y)

		self.rect.centerx = self.centerx
		self.rect.centery = self.centery


	def blitme(self):

		self.screen.blit(self.image, self.rect)

