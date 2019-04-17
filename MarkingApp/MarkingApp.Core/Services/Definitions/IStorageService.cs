using System.IO;
using System.Threading.Tasks;

namespace MarkingApp.Services.Definitions.Storage
{
    public interface IStorageService
    {
        Task<string> SaveFileAsync(string storageKey, string path, string mimeType = null);
    }
}
