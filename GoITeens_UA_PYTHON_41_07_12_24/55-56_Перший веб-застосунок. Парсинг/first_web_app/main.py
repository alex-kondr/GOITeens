from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import mimetypes
from pathlib import Path


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == "/":
            self.send_html_file("index.html")
        elif pr_url.path == "/search":
            self.send_html_file("search.html")
        elif Path().joinpath(pr_url.path.split('/')[-1]).exists():
            self.send_static()
        else:
            self.send_error(404, "Ага, а такої сторінки не існує")

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        try:
            with open(filename, "rb") as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "Сторінку не знайдено")

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt[0]:
            self.send_header("Content-type", mt[0])
        self.end_headers()
        try:
            with open(f".{self.path}", "rb") as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, "Сторінку не знайдено")


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ("", 8002)
    http = server_class(server_address, handler_class)
    try:
        print(f"Сервер запущено на <http://localhost:{server_address[-1]}>")
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    run()
