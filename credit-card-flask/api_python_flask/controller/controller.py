
class Controller:

    def __init__(self, a=None):
        app = a

    @app.route('/')
    def start():
        #will start the program once the website is up and running and return some JSON information
        return {'result': "Hello World"}

