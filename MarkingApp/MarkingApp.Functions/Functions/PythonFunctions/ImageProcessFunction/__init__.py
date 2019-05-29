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
    with tempfile.TemporaryDirectory(prefix="!") as dirpath:
        filepath = storage.get_blob_file("uploads", id, dirpath)
        processor = OpenCVImageProcessor()
        processor.extract_questions(dirpath, filepath)
        return func.HttpResponse("{0}".format(filepath))