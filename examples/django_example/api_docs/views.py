import requests
from django.http import HttpResponse
from scalar_py import Options, api_reference_html, CustomOptions, Spec

def api_docs(request):
    opts = Options(
        spec=Spec(
            url="https://petstore.swagger.io/v2/swagger.json"
        ),
        custom_options=CustomOptions(page_title="My API Docs (Django)")
    )
    html = api_reference_html(opts)
    return HttpResponse(html)
