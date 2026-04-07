import http.server
import functools

Handler = functools.partial(
    http.server.SimpleHTTPRequestHandler,
    directory="/Users/leslydsouza/Desktop/brand-engine"
)
server = http.server.HTTPServer(("", 8731), Handler)
print("Serving on port 8731")
server.serve_forever()
