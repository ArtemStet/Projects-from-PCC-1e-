class Settings():
	"""A class to store all settings for Alien Invasion by Artem."""
	
	def __init__(self):
		"""Initialize the game's seetings."""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (63, 232, 245)
		
		#Ship settings
		self.ship_speed_factor = 1.5
		
		#Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 4
		self.bullet_height = 16
		self.bullet_color = 180, 20, 20
