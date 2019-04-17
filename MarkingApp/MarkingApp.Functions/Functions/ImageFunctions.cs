using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using AzureFunctions.Autofac;
using MarkingApp.Core.Services.Definitions;
using MarkingApp.Services.Definitions.Storage;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace MarkingApp.Functions
{
    [DependencyInjectionConfig(typeof(InjectionConfiguration))]
    public static class ImageFunctions
    {
        [FunctionName(nameof(ImageUploadFunction))]
        public static async Task<IActionResult> ImageUploadFunction(
            [HttpTrigger(AuthorizationLevel.Function, "post", Route = "v1/image/upload")] HttpRequest req,
            [Inject]IImageService imageService,
            ILogger log)
        {
            var url = await imageService.UploadImageAsync(req);
            return new OkObjectResult(url);
        }
    }
}
