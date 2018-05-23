import base64
from apistar_configurator import make_configurator
from apistar import exceptions, http, Component


class User:
    def __init__(self, username: str):
        self.username = username


class UserComponent(Component):
    def resolve(self, authorization: http.Header) -> User:
        """
        Determine the user associated with a request, using HTTP Basic Authentication.
        """
        if authorization is None:
            return None

        scheme, token = authorization.split()
        if scheme.lower() != 'basic':
            return None

        username, password = base64.b64decode(token).decode('utf-8').split(':')
        if not self.check_authentication(username, password):
            raise exceptions.Forbidden('Incorrect username or password.')

        return User(username)

    def check_authentication(self, username: str, password: str) -> bool:
        # Just an example here. You'd normally want to make a database lookup,
        # and check against a hash of the password.
        return password == 'secret'


class MustBeAuthenticated():
    def on_request(self, user: User = None) -> None:
        if user is None:
            raise NotAuthenticated()


class NotAuthenticated(exceptions.HTTPException):
    default_status_code = 401
    default_detail = "Not authenticated"

    def get_headers(self):
        d = super().get_headers()
        d['WWW-Authenticate'] = 'Basic realm="SECRET AREA"'
        return d


def hello_user(user: User) -> dict:
    return {'hello': user.username}


def includeme(config):
    config.add_route('/', method='GET', handler=hello_user)
    config.add_component(UserComponent())
    config.add_event_hook(MustBeAuthenticated())


if __name__ == "__main__":
    config = make_configurator()
    config.include(includeme)
    app = config.make_app()
    app.serve('127.0.0.1', 5000, debug=True)
