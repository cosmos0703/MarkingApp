using System;
using System.Collections.Generic;
using System.Text;
using Autofac;
using AzureFunctions.Autofac.Configuration;
using MarkingApp.Core.Services.Definitions;
using MarkingApp.Core.Services.Implementations;
using MarkingApp.Functions.Services.Implementations;
using MarkingApp.Services.Definitions.Storage;
using MarkingApp.Services.Implementations.Storage;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Hosting;
using Microsoft.Extensions.DependencyInjection;

namespace MarkingApp.Functions
{
    public class InjectionConfiguration
    {
        public InjectionConfiguration(string functionName)
        {
            DependencyInjection.Initialize(builder =>
                {
                    builder.RegisterType<AzureStorageService>().As<IStorageService>().SingleInstance();
                    builder.RegisterType<FunctionSettingsService>().As<IAppSettingsService>().SingleInstance();

                    builder.RegisterType<ImageService>().As<IImageService>().SingleInstance();

                }, functionName);
        }
    }
}
