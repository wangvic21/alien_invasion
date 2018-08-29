# coding:utf8

class Settings():
	"""docstring for Settings"""
	def __init__(self):
		"""初始化游戏的静态设置"""
		# 屏幕设置
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# 飞船数量
		self.ship_limit = 2

		# 子弹设置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 250, 60, 60

		# 外星人设置
		self.fleet_drop_speed = 10

		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1
		self.speedup_bullet_limit = 1.2
		self.score_scale = 1.2
		self.initialize_dynamic_settings()

		# 在任何情况下都不应重置最高分

	def initialize_dynamic_settings(self):
		"""初始化随游戏进度而变化的设置"""
		self.ship_speed_factor = 5
		self.bullet_speed_factor = 2
		self.alien_speed_factor = 2
		# fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1
		self.bullet_allowed = 6
		self.alien_points = 20

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.bullet_allowed = int(self.bullet_allowed * self.speedup_bullet_limit)
		self.alien_points = int(self.alien_points * self.score_scale)