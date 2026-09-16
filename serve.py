import http.server, threading, webbrowser

PORT = 8000
threading.Timer(1, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
http.server.HTTPServer(("localhost", PORT), http.server.SimpleHTTPRequestHandler).serve_forever()