def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def includeme(config):
    config.add_route("/", method="GET", handler=welcome)
