from ..Core import BaseStorageService
from azure.storage.blob import BlockBlobService
from io import BytesIO
import os, tempfile

class AzureStorageService(BaseStorageService):

    def __init__(self, *args, **kwargs):
        storage_name = os.environ["AzureStorageName"]
        storage_key = os.environ["AzureStorageKey"]
        self.block_blob_service = BlockBlobService(account_name=storage_name, account_key=storage_key)
        super().__init__(*args, **kwargs)

    def get_blob_stream(self, container: str, id: str, stream: BytesIO):
        self.block_blob_service.create_container(container)
        self.prepare_blob(container)
        self.block_blob_service.get_blob_to_stream(container, id, stream)
        return stream
    
    def get_blob_file(self, container: str, id: str, dir: str):
        file_extension = os.path.splitext(id)[1]
        with tempfile.NamedTemporaryFile('wb', dir= dir, suffix=file_extension, delete=False) as tmp:
            with BytesIO() as stream:
                self.get_blob_stream(container, id, stream)
                stream.seek(0)
                tmp.write(stream.getbuffer())
                tmp.flush()
                return tmp.name

    def prepare_blob(self, name):
        if self.block_blob_service.exists(container_name=name):
            self.block_blob_service.create_container(name, public_access="blob")
        
        
