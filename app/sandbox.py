class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.handle_home()
        elif self.path == "/about":
            self.handle_about()
        else:
            self.handle_404()

    def do_POST(self):
        if self.path == "/submit":
            self.handle_submit()
        else:
            self.handle_404()

    def handle_home(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Welcome to Home Page</h1>")

    def handle_about(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>About Page</h1>")

    def handle_submit(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode()
        print("Form submitted:", body)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Form received!")

    def handle_404(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"404 Not Found")
