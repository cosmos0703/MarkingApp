using System;
using System.Collections.Generic;
using System.Text;

namespace MarkingApp.Core.Services.Definitions
{
    public interface IAppSettingsService
    {
        string this[string index] { get; }
    }
}
