from wsgi.flask_app import init_app
from wsgi.config import DevConfig

app = init_app(DevConfig)

if __name__ == '__main__':
    app.run()
