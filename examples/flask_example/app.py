from flask import Flask, Response
from scalar_py import Options, Spec, api_reference_html, CustomOptions, get_base_path_from_spec

app = Flask(__name__)

@app.route('/api-docs')
def api_docs():
    spec_url = "https://petstore.swagger.io/v2/swagger.json"
    base_path = get_base_path_from_spec(spec_url)

    opts = Options(
        spec=Spec(url=spec_url),
        custom_options=CustomOptions(page_title="My API Docs"),
        servers=[
            {"url": "https://api.example.com", "description": "Production server"},
            {"url": "https://api-staging.example.com", "description": "Staging server"},
            {"url": "http://localhost:8000", "description": "Local development server"},
        ],
        pathRouting={"basePath": base_path} if base_path else None
    )

    html = api_reference_html(opts)
    return Response(html, mimetype="text/html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
