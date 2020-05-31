from sanic import Sanic
from sanic.response import text
from sanic.views import HTTPMethodView

from sanic_openapi import doc, swagger_blueprint

app = Sanic(__name__)
app.config["API_TITLE"] = "Sanci-OpenAPI"
app.config["API_VERSION"] = "0.1.0"
app.config["API_DESCRIPTION"] = "An example Swagger from Sanic-OpenAPI"
app.config["API_CONTACT_EMAIL"] = "cagojeiger@naver.com"
app.config["API_TERMS_OF_SERVICE"] = "https://github.com/huge-success/sanic-openapi/blob/master/README.md"
app.config["API_LICENSE_NAME"] = "MIT"
app.config["API_LICENSE_URL"] = "https://github.com/huge-success/sanic-openapi/blob/master/LICENSE"
app.blueprint(swagger_blueprint)


@app.route("/")
@doc.tag("test")
@doc.summary("test route")
@doc.description('This is a test route with detail description.')
async def test(request):
    return text("hello world")





class SimpleView(HTTPMethodView):

    ex1 = {'11': int,
           '123': str}

    @doc.tag("test")
    @doc.consumes(doc.String(name="X-API-VERSION"), location="header", required=True)
    @doc.consumes(doc.String(name="name"), location="query")
    @doc.response(200, ex1, description='123aaa')
    def get(self, request):
        return text("I am get method")

    @doc.consumes(
        doc.JsonBody(
            {
                "useranme": doc.String("The name of your user account."),
                "password": doc.String("The password of your user account."),
            }
        ),
        content_type="Application/json",
        location="body"
    )
    def post(self, request):
        return text("I am post method")

    def put(self, request):
        return text("I am put method")

    def patch(self, request):
        return text("I am patch method")

    def delete(self, request):
        return text("I am delete method")

app.add_route(SimpleView.as_view(), "/test")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070)


