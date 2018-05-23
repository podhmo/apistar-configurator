from apistar_configurator import make_configurator
from apistar import exceptions, App

USERS = {1: 'hazel', 2: 'james', 3: 'ana'}


def list_users(app: App) -> list:
    return [
        {
            'username': username,
            'url': app.reverse_url('get_user', user_id=user_id)
        } for user_id, username in USERS.items()
    ]


def get_user(app: App, user_id: int) -> dict:
    if user_id not in USERS:
        raise exceptions.NotFound()
    return {'username': USERS[user_id], 'url': app.reverse_url('get_user', user_id=user_id)}


def includeme(config):
    config.add_route('/users/', method='GET', handler=list_users),
    config.add_route('/users/{user_id}/', method='GET', handler=get_user)


if __name__ == '__main__':
    config = make_configurator()
    config.include(includeme)
    app = config.make_app()
    app.serve('127.0.0.1', 5000, debug=True)
