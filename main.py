from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import contextlib
import mimetypes
import os.path
config = open("config.txt", "r")
configlist = config.read().split("__")

hostName = str(open("configs/ip.txt", "r").read())
serverPort = "8080"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            mapg = open("files/index.html")
            mp = mapg.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(mp, "utf-8"))
        elif os.path.exists("files" + self.path):
            pgop = open("files" + self.path, "r") 
            pg = pgop.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(pg, "utf-8"))
        else:
            self.send_error(404)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, int(serverPort)), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
