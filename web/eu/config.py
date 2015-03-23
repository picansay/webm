
import os

class Config:
	pass
	@staticmethod
	def init_app(app):
		pass


class TestConfig(Config):
	pass

class DevelopmentConfig(Config):
	@classmethod
	def init_app(cls,app):
		Config.init_app(app)
		print "-------------"
		pass

config = {
		'development': DevelopmentConfig,
		"default":DevelopmentConfig,
		}
