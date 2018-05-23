from apistar_configurator import make_configurator


async def hello_world() -> dict:
    return {"hello": "async"}


def includeme(config):
    config.add_route("/", method="GET", handler=hello_world)


if __name__ == '__main__':
    config = make_configurator()
    config.include(includeme)
    app = config.make_async_app()
    app.serve('127.0.0.1', 5000, debug=True)
