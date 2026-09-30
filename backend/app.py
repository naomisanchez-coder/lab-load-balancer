import os
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8081))
NAME = os.environ.get("SERVER_NAME", "BACKEND 1")

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        message = f"Respuesta desde Servidor {NAME} - Puerto {PORT}"
        self.wfile.write(message.encode('utf-8'))

if __name__ == '__main__':
    print(f"Servidor {NAME} corriendo en el puerto {PORT}...")
    server = HTTPServer(('0.0.0.0', PORT), SimpleHandler)
    server.serve_forever()