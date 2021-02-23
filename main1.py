import cherrypy
import random
import string
# Basic application (minimal app)


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'

    @cherrypy.expose
    def generate(self, length=10):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == "__main__":
    cherrypy.quickstart(HelloWorld())
