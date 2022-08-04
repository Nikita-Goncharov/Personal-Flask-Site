# from flask_script import Manager, Server
from flask_ import create_app
import config
from gevent.pywsgi import WSGIServer
app = create_app(config.DevConfig)


# manager = Manager(app)

# manager.add_command('runserver', Server(host=app.config['HOST'], port=app.config['PORT']))

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
    # app.run(port=44445, host='0.0.0.0')