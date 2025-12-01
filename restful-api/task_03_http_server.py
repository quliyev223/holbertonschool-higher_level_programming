#!/usr/bin/env python3
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""

        # --- Root endpoint "/" ---
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # --- /data endpoint ---
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
            return

        # --- /status endpoint ---
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # --- /info endpoint ---
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_data = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
            return

        # --- Any undefined endpoint ---
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = f"Endpoint '{self.path}' not found"
            self.wfile.write(message.encode("utf-8"))


def run(server_class=http.server.HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ("", 8000)  # Listen on port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

