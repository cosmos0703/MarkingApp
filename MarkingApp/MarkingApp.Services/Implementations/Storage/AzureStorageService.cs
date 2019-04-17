using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using MarkingApp.Core.Services.Definitions;
using MarkingApp.Services.Definitions.Storage;
using Microsoft.Azure.Storage;
using Microsoft.Azure.Storage.Auth;
using Microsoft.Azure.Storage.Blob;

namespace MarkingApp.Services.Implementations.Storage
{
    public class AzureStorageService : IStorageService
    {
        private readonly CloudBlobClient _blobClient;
        private readonly Dictionary<string, string> _mimeDict = new Dictionary<string, string>()
        {
            {"image/jpeg", ".jpg"},
            {"image/jpg", ".jpg"},
            {"image/png", ".png"}
        };

        public AzureStorageService(IAppSettingsService settingsService)
        {
            var credentials = new StorageCredentials(settingsService["AzureStorageName"],
                settingsService["AzureStorageKey"]);

            var account = new CloudStorageAccount(credentials, true);
            _blobClient = account.CreateCloudBlobClient();
        }

        public async Task<string> SaveFileAsync(string storageKey, string path, string mimeType)
        {
            using (var stream = new FileStream(path, FileMode.OpenOrCreate))
            {
                return await SaveFileAsync(storageKey, stream, path, mimeType);
            }
        }

        private async Task<string> SaveFileAsync(string blobName, Stream stream, string path, string mimeType)
        {
            var blobContainer = PrepareBlob(blobName);
            var blob = blobContainer.GetBlockBlobReference($"{Guid.NewGuid().ToString()}{_mimeDict[mimeType]}");
            blob.Properties.ContentType = mimeType;
            await blob.UploadFromStreamAsync(stream);
            return blob.Uri.AbsoluteUri;
        }

        private CloudBlobContainer PrepareBlob(string blobName)
        {
            var blobContainer = _blobClient.GetContainerReference(blobName);

            if (blobContainer.CreateIfNotExists())
            {
                var permissions = blobContainer.GetPermissions();
                permissions.PublicAccess = BlobContainerPublicAccessType.Blob;
                blobContainer.SetPermissions(permissions);
            }

            return blobContainer;
        }
    }
}
