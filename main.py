from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def __get_html_content(self):
        # Чтение HTML-файла и возвращение его содержимого
        html_file = os.path.join(os.path.dirname(__file__), "/Users/miya/PycharmProjects/django/homework.html")
        with open(html_file, "r") as html_file:
            return html_file.read()

    def do_GET(self):
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
