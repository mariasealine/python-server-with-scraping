#!/usr/bin/env python
from scraping import (getSearchResultFromUrl)
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        searchresult = getSearchResultFromUrl(self.path)
        respondWith = searchresult
       
        self.send_response(200)
        
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
 
        self.wfile.write(bytes(respondWith, "utf8"))
        
        return

def run():
  print('starting server...')

  server_address = ('', port)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()