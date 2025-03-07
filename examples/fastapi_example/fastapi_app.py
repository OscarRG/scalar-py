from fastapi import FastAPI, Response
from scalar_py import Options, api_reference_html, CustomOptions, Spec, get_base_path_from_spec

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

@app.get("/api-docs")
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
    return Response(content=html, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
