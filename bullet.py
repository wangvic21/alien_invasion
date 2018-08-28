import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, ai_settings, screen, ship):
		super(Bullet, self).__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		self.ship = ship
		
		# 在(0, 0)处创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0, 0, self.ai_settings.bullet_width, self.ai_settings.bullet_height)
		self.rect.centerx = self.ship.rect.centerx
		self.rect.top = self.ship.rect.top

		# 存储用小数表示的子弹位置
		self.y = float(self.rect.y)

		self.color = self.ai_settings.bullet_color
		self.speed_factor = self.ai_settings.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)