from sanic import Blueprint

from .test import test

sample = Blueprint.group(test, url_prefix='/sample')
