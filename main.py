import os
from flask_.app import create_app
from gevent.pywsgi import WSGIServer
import config


app = create_app(config.ProdConfig) 

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    if app.config['DEBUG']:
        app.run(port=port)
    else:    
        http_server = WSGIServer(('0.0.0.0', port), app)
        http_server.serve_forever()