"""Minimal demo web app for DevSecOps course."""
import http.server
import os

PORT = int(os.environ.get("PORT", "8080"))

# Hardcoded credential (semgrep should flag this)
DB_PASSWORD = "SuperSecret123!"


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"DevSecOps Demo App\n")


if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Listening on port {PORT}")
    server.serve_forever()
