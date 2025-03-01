from fastapi import FastAPI, Response
from scalar_py import Options, api_reference_html, CustomOptions, Spec

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

@app.get("/api-docs")
def api_docs():
    opts = Options(
        spec=Spec(
            url="https://petstore.swagger.io/v2/swagger.json",
            ),
        custom_options=CustomOptions(page_title="My API Docs")
    )
    html = api_reference_html(opts)
    return Response(content=html, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
