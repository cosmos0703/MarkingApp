using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;

namespace MarkingApp.Core.Services.Definitions
{
    public interface IImageService
    {
        Task<string> UploadImageAsync(HttpRequest request);
    }
}
