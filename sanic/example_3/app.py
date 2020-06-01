from sanic import Sanic
from sanic_openapi import swagger_blueprint

from sample import sample

app = Sanic(__name__)

app.config["API_TITLE"] = "My-DataHub-OpenAPI"
app.config["API_VERSION"] = "0.1.0"
app.config["API_DESCRIPTION"] = "An example Swagger from Sanic-OpenAPI"
app.config["API_CONTACT_EMAIL"] = "cagojeiger@naver.com"
app.config["API_TERMS_OF_SERVICE"] = "https://github.com/kangheeyong/PROJECT-datahub-api-server.git"
app.config["API_LICENSE_NAME"] = "MIT LICENSE"
app.blueprint(swagger_blueprint)
app.blueprint(sample)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8070)



