import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/":
            filename = "form-e2.html"
            contents = read_html_file(filename).render(context={})
        elif path == "/echo":
            filename = "echo2.html"
            if "msg" in arguments and "chk" not in arguments:
                msg = arguments["msg"][0]
                contents = read_html_file(filename).render(context={"todisplay": msg})
            elif "chk" and "msg" in arguments:
                msg = arguments["msg"][0].upper()
                contents = read_html_file(filename).render(context={"todisplay": msg})  #Hago mayusculas todo si pongo upper aqui

            else:
                contents = read_html_file(filename).render(context={"todisplay": ""})
        else:
            filename = "error.html"
            contents = read_html_file(filename).render(context={})

        print(arguments)

        self.send_response(200)
        self.send_header('Content-Type', 'html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()


