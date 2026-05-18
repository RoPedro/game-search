from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
       
    # Silent logs
    def log_message(self, format: str, *args: Any) -> None:
        return
    
def run_health_server(): 
    HTTPServer(("0.0.0.0", 8080), HealthHandler).serve_forever()