import pytest as pytest

from sanic.blueprints import Blueprint
from sanic.constants import HTTP_METHODS
from sanic.exceptions import InvalidUsage
from sanic.request import Request
from sanic.response import HTTPResponse, text
from sanic.views import CompositionView, HTTPMethodView


def test_unexisting_methods(app):
    class DummyView(HTTPMethodView):
        def get(self, request):
            return text("I am get method")

    app.add_route(DummyView.as_view(), "/")
    request, response = app.test_client.get("/")
    assert response.text == "I am get method"
    request, response = app.test_client.post("/")
    assert "Method POST not allowed for URL /" in response.text
