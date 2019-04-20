using System.IO;
using System.Threading.Tasks;

namespace MarkingApp.Services.Definitions.Storage
{
    public interface IStorageService
    {
        Task<string> SaveFileAsync(string container, string path, string mimeType = null);

        Task<Stream> GetFileAsync(string container, string id);
    }
}
