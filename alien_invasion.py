# coding:utf8

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
import game_functions as gf

def run_game():
	# initialize
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
  
	# 创建一艘飞船
	ship = Ship(screen, ai_settings)

	stats = GameStats(ai_settings)

	msg = "Play"
	play_button = Button(ai_settings, screen, msg)
	score_board = ScoreBoard(ai_settings, screen, stats)

	# alien = Alien(ai_settings, screen)
	aliens = Group()
	gf.create_fleet(ai_settings, screen, aliens, ship)

	# 创建一个用于存储子弹的编组
	bullets = Group()

	# 设置背景色
	bg_color = ai_settings.bg_color

	# main program
	while True:
		gf.check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens)
		if stats.game_active:
			ship.update()	
			gf.update_bullet(bullets, aliens, ai_settings, screen, ship, stats)
			gf.update_aliens(aliens, ai_settings, ship, stats, bullets, screen, score_board)
			# 每次循环时都重绘屏幕
		gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, score_board)
			# print(str(stats.game_active))

run_game()