from apistar_configurator import make_configurator


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def includeme(config):
    config.add_route("/", method="GET", handler=welcome)


def includeme2(config):
    config.add_route("/", method="GET", handler=lambda name=None: {"message": name})


if __name__ == '__main__':
    config = make_configurator()

    config.include(includeme)
    config.include(includeme)  # ok
    config.include(includeme2)  # ng

    app = config.make_app()
    app.serve('127.0.0.1', 5000, debug=True)
