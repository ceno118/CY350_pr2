import http.server 

# The following creates a subclass of the http.server.BaseHTTPRequestHandler
class SimpleServer(http.server.BaseHTTPRequestHandler):
    # TODO: Complete your server logic within this class - you can write methods and create variables as needed
    # Reference: https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
    # The variables and methods of BaseHTTPRequestHandler are the minimum of what you will need to build a successful server

# As you write your server code, you need to test it:
# TODO: add code down here that binds your server to an address ('host', port), just like how you set addresses in project 1 
# TODO: create your server using the http.server.HTTPServer(address, SimpleServer) command
# TODO: Ensure you start running your server