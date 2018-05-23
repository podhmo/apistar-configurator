import os.path
from apistar import App
from apistar_configurator import make_configurator


def welcome(app: App, name=None):
    return app.render_template('index.html', name=name)


def includeme(config):
    config.add_route("/{name}", method="GET", handler=welcome)


if __name__ == '__main__':
    config = make_configurator()
    config.include(includeme)
    basedir = os.path.dirname(__file__)
    app = config.make_app(
        template_dir=os.path.join(basedir, "templates"),
        static_dir=os.path.join(basedir, "static"),
    )
    app.serve('127.0.0.1', 5000, debug=True)
