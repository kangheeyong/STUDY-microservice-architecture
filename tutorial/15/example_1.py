from sanic import  Sanic
from sanic import response

import plotly.express as px
import plotly.io as pio

app = Sanic(__name__)


@app.get('/')
def test(request):
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    html = pio.to_html(fig)
    return response.html(html)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8070)



