import json


class GameStats():
	"""docstring for GameStats"""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats() # 通过reset_stats初始化
		# 游戏刚启动时处于活动状态
		self.game_active = False
		self.high_score = 0
		self.load_high_score()


	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ship_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1

	def load_high_score(self):
		# 如果以前存储了最高分，就加载，否则，创建新的文件
		filename = 'high_score.json'
		try:
			with open(filename) as hs_obj:
				self.high_score = json.load(hs_obj)
		except FileNotFoundError:
			with open(filename, 'w') as hs_obj:
				json.dump(0, hs_obj)

			




