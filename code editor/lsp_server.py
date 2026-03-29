import ssl
from pygls.lsp.server import LanguageServer

# Initialize the Server
server = LanguageServer("web-editor-lsp", "v1.0")

# Setup SSL for Production (WSS)
# ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

@server.feature("textDocument/didOpen")
def did_open(ls, params):
    ls.show_message("LSP connected to Web Editor")

if __name__ == "__main__":
    print("Starting LSP on ws://localhost:1234")
    server.start_ws("127.0.0.1", 1234)
