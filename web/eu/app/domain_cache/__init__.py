
from flask import Blueprint

#domain_cache = Blueprint("domain_cache", __name__)
from flask.ext.restplus import API, apidoc
domain_cache = Blueprint("domain_cache", __name__)
api = Api(domain_cache, ui=False)

from . import views
