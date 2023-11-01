from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import contextlib
import mimetypes
import os.path

#sets hostname and ports
hostName = str(open("configs/ip.txt", "r").read())
serverPort = "8080"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            #gets "index.html"
            mapg = open("files/index.html")
            mp = mapg.read()
            #sends page to user
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(mp, "utf-8"))
        elif os.path.exists("files" + self.path):
            #gets page html
            pgop = open("files" + self.path, "r") 
            pg = pgop.read()
            #sends page
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
