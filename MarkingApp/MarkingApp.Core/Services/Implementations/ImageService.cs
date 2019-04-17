using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MarkingApp.Core.Services.Definitions;
using MarkingApp.Services.Definitions.Storage;
using Microsoft.AspNetCore.Http;

namespace MarkingApp.Core.Services.Implementations
{
    public class ImageService : IImageService
    {
        private readonly IStorageService _storageService;

        private static readonly string[] ImageContentTypes = { "image/png", "image/jpeg", "image/jpg" };

        public ImageService(IStorageService storageService)
        {
            _storageService = storageService;
        }

        public async Task<string> UploadImageAsync(HttpRequest request)
        {
            IFormCollection form;

            try
            {
                form = await request.ReadFormAsync();
            }
            catch (Exception)
            {
                throw new BadImageFormatException();
            }

            if (!ImageContentTypes.Contains(form.Files.First().ContentType))
                throw new BadImageFormatException();

            var file = form.Files.First();
            var imagePath = await RetreiveAndSaveImage(file);
            return await _storageService.SaveFileAsync("uploads", imagePath, file.ContentType);
        }

        private static async Task<string> RetreiveAndSaveImage(IFormFile file)
        {
            var filePath = Path.GetTempFileName();
            if (file.Length < 0)
                return null;

            using (var stream = new FileStream(filePath, FileMode.Create))
                await file.CopyToAsync(stream);

            return filePath;
        }
    }
}
