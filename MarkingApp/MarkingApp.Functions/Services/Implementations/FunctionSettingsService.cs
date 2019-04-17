using System;
using System.Collections.Generic;
using System.Text;
using MarkingApp.Core.Services.Definitions;
using System.Configuration;
using Microsoft.Extensions.Configuration;

namespace MarkingApp.Functions.Services.Implementations
{
    public class FunctionSettingsService : IAppSettingsService
    {
        private readonly IConfigurationRoot _config;

        public FunctionSettingsService()
        {
            _config = new ConfigurationBuilder()
                .SetBasePath(Environment.CurrentDirectory)
                .AddJsonFile("local.settings.json", optional: true, reloadOnChange: true)
                .AddEnvironmentVariables()
                .Build();
        }

        public string this[string index] => _config[index];
    }
}
