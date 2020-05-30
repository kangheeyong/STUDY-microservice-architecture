
from sanic import Sanic
from sanic import response


app = Sanic("test_sanic_app")

@app.route("/test_get", methods=['GET'])
async def test_get(request):
    return response.json({"GET": True})

@app.route("/test_get", methods=['POST'])
async def test_post(request):
    return response.json({"POST": True})




