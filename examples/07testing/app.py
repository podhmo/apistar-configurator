from apistar_configurator import make_configurator


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def includeme(config):
    config.add_route("/", method="GET", handler=welcome)


def make_app():
    config = make_configurator()
    config.include(includeme)
    return config.make_app()


if __name__ == '__main__':
    app = make_app()
    app.serve('127.0.0.1', 5000, debug=True)
