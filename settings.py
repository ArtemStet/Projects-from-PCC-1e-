class Settings():
	"""A class to store all settings for Alien Invasion by Artem."""
	
	def __init__(self):
		"""Initialize the game's seetings."""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 900
		self.bg_color = (63, 232, 245)
		
		#Ship settings
		self.ship_speed_factor = 1.5
		
		#Bullet settings
		self.bullet_speed_factor = 2
		self.bullet_width = 400
		self.bullet_height = 16
		self.bullet_color = 180, 20, 20
		self.bullets_allowed = 10
		
		#Alien settings
		self.alien_speed_factor = 0.5
		self.fleet_drop_speed = 10
		#fleet_direction of 1 represent right, -1 represents left
		self.fleet_direction = 0.5
