import pygame.font

class Scoreboard():

	def __init__(self, settings, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.score_1 = 0
		self.score_2 = 0

		self.text_color = (30, 30, 30)
		self.font = pygame.font.Font('Hardpixel.ttf', 30)

	def prep_score(self):

		score_str = str(self.score_1) + ' : ' + str(self.score_2)

		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

		self.score_rect = self.score_image.get_rect()
		self.score_rect.centerx = self.screen_rect.centerx
		self.score_rect.centery = self.screen_rect.top + 20

	def show_score(self):
		'''Выводит счет на экран'''
		self.screen.blit(self.score_image, self.score_rect)
	
