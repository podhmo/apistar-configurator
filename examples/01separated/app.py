from apistar_configurator import make_configurator

if __name__ == '__main__':
    config = make_configurator()
    config.include("welcome")
    app = config.make_app()
    app.serve('127.0.0.1', 5000, debug=True)
