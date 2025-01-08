// <auto-generated/>

#nullable disable

using System;
using System.ClientModel;
using System.ClientModel.Primitives;
using System.Threading;
using System.Threading.Tasks;

namespace Versioning.ReturnTypeChangedFrom.V1
{
    public partial class ReturnTypeChangedFromClient
    {
        protected ReturnTypeChangedFromClient() => throw null;

        public ReturnTypeChangedFromClient(Uri endpoint) : this(endpoint, new ReturnTypeChangedFromClientOptions()) => throw null;

        public ReturnTypeChangedFromClient(Uri endpoint, ReturnTypeChangedFromClientOptions options) => throw null;

        public ClientPipeline Pipeline => throw null;

        public virtual ClientResult Test(BinaryContent content, RequestOptions options = null) => throw null;

        public virtual Task<ClientResult> TestAsync(BinaryContent content, RequestOptions options = null) => throw null;

        public virtual ClientResult<int> Test(string body, CancellationToken cancellationToken = default) => throw null;

        public virtual Task<ClientResult<int>> TestAsync(string body, CancellationToken cancellationToken = default) => throw null;
    }
}
