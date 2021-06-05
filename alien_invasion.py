import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
	#Initialize pygame, settings and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion by Artem")
	
	#Make a ship, a group of aliens and bullets
	ship = Ship(ai_settings, screen)
	aliens = Group()
	bullets = Group()
	
	#Make a fleet of alien
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Start the main loop for the game.
	while True:
		#Watch fpr keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, ship, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()
