import random
import string
import cherrypy
import json


class Generator(object):
    @cherrypy.expose
    def index(self):
        return"""
    <html>
    <head> </head>
    <body>
      <form method="get" action="generate">
      <input type="text" value="10" name="length" />
      <button type="submit">Let it rain!</button>
      </form>
    </body>
    </html>"""

    @cherrypy.expose
    def generate(self, length=10):
        return ''.join(random.sample(string.hexdigits, int(length)))

    @cherrypy.expose
    def json(self):
        res = "Pong"
        return json.dumps({"Ping": res})


if __name__ == "__main__":
    cherrypy.quickstart(Generator())
