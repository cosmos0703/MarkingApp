#pylint: disable=relative-beyond-top-level
import logging, tempfile, os
import azure.functions as func
from ..Shared.Services import (
        AzureStorageService,
        OpenCVImageProcessor)
from io import BytesIO

def main(req: func.HttpRequest) -> func.HttpResponse:
    storage = AzureStorageService()
    id = req.params.get("id")
    filepath = storage.get_blob_file("uploads", id)
    processor = OpenCVImageProcessor()
    processor.threshold_and_invert(filepath)
    return func.HttpResponse("{0}".format(filepath))