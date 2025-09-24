import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "./"  # Directory where your HTML files are located

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Check if the requested path corresponds to an HTML file without the extension
        if not os.path.splitext(self.path)[1]:  # If no extension is present
            potential_file = os.path.join(DIRECTORY, self.path.lstrip('/')) + ".html"
            if os.path.exists(potential_file):
                self.path = self.path + ".html"  # Add .html extension internally
        
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://0.0.0.0:{PORT}")
    httpd.serve_forever()
