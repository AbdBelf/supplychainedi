from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define the EDI message to be served
edi_message = """
ISA*00* *00* *ZZ*SENDERID *ZZ*RECEIVERID *030101*1253*U*00401*000000001*0*P*:~
GS*PO*SENDERID*RECEIVERID*20030101*1253*1*X*004010~
ST*850*0001~
BEG*00*SA*08234940294**20051117~
TD5*****UPS3~
N1*ST*BigSupplier*9*0923847102938421~
PO1*1*5*EA*9.92*TE*CB*0012345~
CTT*1~
SE*8*0001~
GE*1*1~
IEA*1*000000001~
"""

# HTTP request handler
class MyServer(SimpleHTTPRequestHandler):
    # GET method handler
    def do_GET(self):
        # Set response status code
        self.send_response(200)

        # Set response headers
        if self.path.endswith(".html"):
            self.send_header('Content-type', 'text/html')
        else:
            self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Serve EDI message if requested
        if self.path == "/edi":
            self.wfile.write(bytes(edi_message, "utf-8"))
        else:
            # Serve static files (HTML, CSS, JS)
            super().do_GET()

# Function to run the HTTP server
def run():
    print('Starting server...')
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print('Server running on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
