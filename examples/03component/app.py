from apistar_configurator import make_configurator
from apistar import http


def echo(
    request: http.Request,
    user_agent: http.Header,
    query_params: http.QueryParams,
) -> dict:
    return {
        'params': dict(query_params),
        'user-agent': user_agent,
        'request': {
            'method': request.method,
            'url': request.url,
            'headers': dict(request.headers),
            'body': request.body.decode('utf-8'),
        }
    }


def includeme(config):
    config.add_route("/", method="GET", handler=echo)


if __name__ == '__main__':
    config = make_configurator()
    config.include(includeme)
    app = config.make_app()
    app.serve('127.0.0.1', 5000, debug=True)
