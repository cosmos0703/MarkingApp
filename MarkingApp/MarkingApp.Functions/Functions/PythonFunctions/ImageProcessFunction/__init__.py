#pylint: disable=relative-beyond-top-level
import logging, tempfile
import azure.functions as func
from ..Shared.Services import AzureStorageService
from io import BytesIO

def main(req: func.HttpRequest) -> func.HttpResponse:
    storage = AzureStorageService()
    id = req.params.get("id")
    with tempfile.NamedTemporaryFile('wb') as tmp:
        data = storage.get_blob_file("uploads", id, tmp)
        return func.HttpResponse("{0}".format(data))