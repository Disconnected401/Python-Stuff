from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging

port = 80

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
file_handler = logging.FileHandler('server.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logging.getLogger().addHandler(file_handler)

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='web', **kwargs)

    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s" %
                     (self.client_address[0],
                      self.log_date_time_string(),
                      format % args))

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serwer http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
