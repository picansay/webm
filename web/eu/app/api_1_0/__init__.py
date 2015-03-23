
from flask import Blueprint

from flask.ext.restplus import Api, Resource, fields,apidoc
api_1_0_bp= Blueprint("api_1_0", __name__)
#api = Api(api_1_0_bp,ui=False)
api = Api(api_1_0_bp, version='1.0', title='webMonitor EU API',
		description='WEB Monitor API doc',
		)

@api_1_0_bp.route('/doc/', endpoint='doc')
def swagger_ui():
	    return apidoc.ui_for(api)

from . import views
from . import core
