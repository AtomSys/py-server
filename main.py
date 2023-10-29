from http.server import BaseHTTPRequestHandler, HTTPServer
import time
config = open("config.txt", "r")
configlist = config.read().split("__")

hostName = "0.0.0.0"
serverPort = "8080"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            mapg = open("srvf/index.html")
            mp = mapg.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(mp))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, int(serverPort)), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
