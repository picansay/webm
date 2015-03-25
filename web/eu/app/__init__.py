
import os
from flask import Flask,url_for
from config import config


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	print app.config
	print config_name
	print config
	#db.init_app(app)
	
	from .test import test as test_blueprint
	app.register_blueprint(test_blueprint, url_prefix='/test')

	from .api_1_0 import api_1_0_bp
	app.register_blueprint(api_1_0_bp, url_prefix='/api_1_0')

        #default
	#app.register_blueprint(api_1_0_bp, url_prefix='/')
	return app
