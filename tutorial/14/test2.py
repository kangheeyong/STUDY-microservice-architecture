import pytest

import sample


@pytest.yield_fixture
def app():
    app = sample.app
    yield app


@pytest.fixture
def test_cli(loop, app, sanic_client):
        return loop.run_until_complete(sanic_client(app))


async def test_get(test_cli):
    resp = await test_cli.get("/test_get")
    resp_json = await resp.json()
    assert resp_json == {'GET': True}


async def test_post(test_cli):
    resp = await test_cli.post("/test_get")
    resp_json = await resp.json()
    assert resp_json == {'POST': True}
