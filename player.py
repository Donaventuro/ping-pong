import pygame
from pygame.sprite import Sprite

class Player(Sprite):

	def __init__ (self, settings, screen):

		super().__init__()
		self.screen = screen
		self.settings = settings

		self.rect = pygame.Rect(0,0, 10, 100)
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.left + 30
		self.rect.centery = self.screen_rect.centery

		self.center = float(self.rect.centery)

		self.color = settings.player_color
		self.speed_factor = settings.player_speed

		self.moving_top = False
		self.moving_bot = False

	def update(self):

		if self.moving_top and self.rect.top > 0:
			self.center -= self.settings.player_speed

		if self.moving_bot and self.rect.bottom <= self.screen_rect.bottom:
			self.center += self.settings.player_speed

		self.rect.centery = self.center

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
