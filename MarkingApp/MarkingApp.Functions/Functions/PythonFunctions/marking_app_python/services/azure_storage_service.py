from marking_app_python.core import BaseStorageService
from azure.storage.blob import BlockBlobService
from io import BytesIO
import os, sys

class AzureStorageService(BaseStorageService):

    def __init__(self, *args, **kwargs):
        storage_name = os.environ["AzureStorageName"]
        storage_key = os.environ["AzureStorageKey"]
        self.block_blob_service = BlockBlobService(account_name=storage_name, account_key=storage_key)
        return super().__init__(*args, **kwargs)

    def get_file(self, container: str, id: str):
        self.block_blob_service.create_container(container)
        self.prepare_blob(container)
        with BytesIO() as stream:
            blob = self.block_blob_service.get_blob_to_stream(container, id, stream)
            return sys.getsizeof(stream)
        return None

    def prepare_blob(self, name):
        if self.block_blob_service.exists(container_name=name):
            self.block_blob_service.create_container(name, public_access="blob")
        
        
