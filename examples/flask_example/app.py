from flask import Flask, Response
from scalar_py import Options, Spec, api_reference_html, CustomOptions

app = Flask(__name__)

@app.route('/api-docs')
def api_docs():
    opts = Options(
        spec=Spec(
            url="https://petstore.swagger.io/v2/swagger.json",
        ),
        custom_options=CustomOptions(page_title="My API Docs")
    )
    html = api_reference_html(opts)
    return Response(html, mimetype="text/html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
