import logging
import azure.functions as func
from marking_app_python.services import AzureStorageService

def main(req: func.HttpRequest) -> func.HttpResponse:
    storage = AzureStorageService()
    id = req.params.get("id")
    a = storage.get_file("uploads", id)
    return func.HttpResponse("{0}".format(a))