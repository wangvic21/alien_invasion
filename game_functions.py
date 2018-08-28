# coding:utf8

import json
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ship, ai_settings, screen, bullets, stats, aliens):
	"""相应按键"""
	if event.key == pygame.K_RIGHT:
		"""向右移动飞船"""
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		"""向右移动飞船"""
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(bullets, ai_settings, screen, ship)
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p and not stats.game_active:
		start_game(stats, aliens, bullets, ai_settings, screen, ship)
		

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		"""向右移动飞船"""
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		"""向右移动飞船"""
		ship.moving_left = False

def check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens):
	# listen keyboard and mouse
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship, ai_settings, screen, bullets, stats, aliens)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(play_button, stats, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, score_board):
	# 每次循环时都重绘屏幕
	screen.fill(ai_settings.bg_color)
	# 在飞船和外星人后面绘制所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	# alien.blitme()
	aliens.draw(screen)
	score_board.show_score()

	# 如果游戏处于非活动状态，就绘制button按钮
	if not stats.game_active:
		play_button.draw_button()

	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullet(bullets, aliens, ai_settings, screen, ship, stats):
	"""更新并删除已消失的子弹"""
	bullets.update()

	# 删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# print(len(bullets))
	check_bullet_alien_coliision(ai_settings, screen, aliens, ship, bullets, stats)
	

def check_bullet_alien_coliision(ai_settings, screen, aliens, ship, bullets, stats):
	# 检查是否有子弹击中了外星人，如果有，删除相应的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
	if len(aliens) == 0:
		ai_settings.increase_speed()
		# 删除现有的子弹并新建一群外星人
		bullets.empty()
		create_fleet(ai_settings, screen, aliens, ship)
		stats.level += 1

def fire_bullet(bullets, ai_settings, screen, ship):
	"""如果还没有达到限制，就发射一颗子弹"""
	# 创建一颗子弹，并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens, ship):
	"""创建外星人群"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien_height = alien.rect.height
	ship_height = ship.rect.height
	number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
	number_aliens_y = get_number_rows(ai_settings, alien_height, ship_height)
	# 创建第一行外星人
	for alien_number in range(number_aliens_x):
		for row_number in range(number_aliens_y):
			# 创建第一个外星人并加入当前行
			create_alien(aliens, ai_settings, screen, alien_width, alien_height, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (alien_width * 2))
	return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
	"""计算屏幕可容纳多少行外星人"""
	available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
	number_aliens_y = int(available_space_y / (2 * alien_height))
	return number_aliens_y

def create_alien(aliens, ai_settings, screen, alien_width, alien_height, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien.x = alien_width + 2 * alien_number * alien_width
	alien.rect.x = alien.x
	alien.y = alien_height + 2 * row_number * alien_height
	alien.rect.y = alien.y
	aliens.add(alien)

def update_aliens(aliens, ai_settings, ship, stats, bullets, screen, score_board):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# 检测外星人和飞船及底端之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		#print("Ship hit!!!")
		ship_hit(stats, aliens, bullets, ai_settings, screen, ship, score_board)

	check_aliens_bottom(stats, aliens, bullets, ai_settings, screen, ship, score_board)

def check_fleet_edges(ai_settings, aliens):
	"""有外星人达到边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(stats, aliens, bullets, ai_settings, screen, ship, score_board):
	"""响应被外星人撞到的飞船"""
	aliens.empty()
	bullets.empty()
	# 创建一群新的外星人。并将飞船放到屏幕底端中央
	create_fleet(ai_settings, screen, aliens, ship)
	ship.center_ship()
	if 	stats.ship_left > 0:
		stats.ship_left -= 1
		# 暂停
		sleep(0.5)
		score_board.prep_ships()
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)
		check_high_score(stats, score_board)

def check_aliens_bottom(stats, aliens, bullets, ai_settings, screen, ship, score_board):
	"""有外星人到达底部时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.rect.bottom >= ai_settings.screen_height:
			ship_hit(stats, aliens, bullets, ai_settings, screen, ship, score_board)
			break

def check_play_button(play_button, stats, mouse_x, mouse_y, aliens, bullets, ai_settings, screen, ship):
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		start_game(stats, aliens, bullets, ai_settings, screen, ship)

def start_game(stats, aliens, bullets, ai_settings, screen, ship):
	# 隐藏光标
	pygame.mouse.set_visible(False)
	stats.reset_stats()
	stats.game_active = True
	aliens.empty()
	bullets.empty()
	create_fleet(ai_settings, screen, aliens, ship)
	ship.center_ship()
	ai_settings.initialize_dynamic_settings()

def check_high_score(stats, score_board):
	"""检查是否诞生了新的最高分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		score_board.prep_high_score()
		# 如果以前存储了最高分，就加载，否则，创建新的文件
		filename = 'high_score.json'
		with open(filename, 'w') as hs_obj:
			json.dump(stats.high_score, hs_obj)











