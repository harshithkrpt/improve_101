from urllib import request, parse

url = "https://httpbin.org/get"
response = request.urlopen(url)
print(response.read().decode())

# Parsing URLs
parsed = parse.urlparse("https://example.com:8080/path?name=John#section1")
print(parsed.scheme, parsed.netloc, parsed.path)


# from http.server import SimpleHTTPRequestHandler, HTTPServer

# server = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
# print("Serving on http://localhost:8000")
# server.serve_forever()


# from http.client import HTTPConnection

# conn = HTTPConnection("example.com")
# conn.request("GET", "/")
# response = conn.getresponse()
# print(response.status, response.reason)
# print(response.read().decode())
