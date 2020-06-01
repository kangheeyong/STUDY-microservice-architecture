import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from sanic import Blueprint
from sanic.response import json
from sanic_openapi import doc

from lib_custom import authorized

test = Blueprint('sample_test', url_prefix='/test')


class Test_status:
    status = doc.String()


@test.route('/')
@doc.tag('test')
@doc.summary('test koken')
@doc.description('This is a test route with detail description.')
@doc.consumes(doc.String(name='token'), location='header', required=True)
@doc.response(200, Test_status, description='한글도 되나?')
@doc.response(403, Test_status, description='123aaa')
@authorized(token='12')
async def route(request):
    return json({'status': 'success'})
