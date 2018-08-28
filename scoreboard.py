import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard():
	"""docstring for ScoreBoard"""
	def __init__(self, ai_settings, screen, stats):
		"""初始化显示得分涉及的属性"""
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.stats = stats

		# 显示得分信息时使用的字体设置
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 30)
		self.level_font = pygame.font.SysFont(None, 25)
		# 准备初始得分图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""将score渲染为图像"""
		# self.score_str = str(self.stats.score)
		round_score = int(round(self.stats.score, -1))
		self.score_str = "{:,}".format(round_score)
		self.score_image = self.font.render(self.score_str, True, self.text_color, self.ai_settings.bg_color) # 文本转图像
		# 将得分放在屏幕右上角
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.right = self.screen_rect.right - 20
		self.score_image_rect.top = 20

	def prep_high_score(self):
		round_high_score = int(round(self.stats.high_score, -1))
		self.high_score_str = "{:,}".format(round_high_score)
		self.high_score_image = self.font.render(self.high_score_str, True, self.text_color, self.ai_settings.bg_color) # 文本转图像
		# 将得分放在屏幕右上角
		self.high_score_image_rect = self.high_score_image.get_rect()
		self.high_score_image_rect.center = self.screen_rect.center
		self.high_score_image_rect.top = 20		

	def prep_level(self):
		self.level_str = "LV: " + str(self.stats.level)
		self.level_image = self.level_font.render(self.level_str, True, self.text_color, self.ai_settings.bg_color) # 文本转图像
		# 将得分放在屏幕右上角
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.right = self.score_image_rect.right
		self.level_image_rect.top = self.score_image_rect.bottom + 5

	def prep_ships(self):
		"""显示还余下多少艘飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.screen, self.ai_settings)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		# 绘制绘制文本
		self.prep_score()
		self.prep_level()
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.high_score_image, self.high_score_image_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.ships.draw(self.screen)
