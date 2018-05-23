from miniconfig import ConfiguratorCore, reify
from miniconfig import Context as _Context
import apistar
import logging
logger = logging.getLogger(__name__)


class Context(_Context):
    @reify
    def routes(self):
        return []


class Configurator(ConfiguratorCore):
    context_factory = Context

    app_factory = apistar.App
    async_app_factory = apistar.ASyncApp
    route_factory = apistar.Route

    def _make_app(self, factory, *, kwargs):
        self.commit()
        app = factory(
            routes=self.routes,
            **kwargs,
        )
        return app

    def make_app(self, **kwargs):
        return self._make_app(self.app_factory, kwargs=kwargs)

    def make_async_app(self, **kwargs):
        return self._make_app(self.async_app_factory, kwargs=kwargs)


def add_route(config, url, method, handler, name=None, documented=True, standalone=False):
    # todo: confilict detection?
    def register():
        route = config.route_factory(
            url,
            method,
            handler,
            name=name,
            documented=documented,
            standalone=standalone,
        )
        logger.debug("add route %s %s %s", method, url, route.name)
        config.routes.append(route)

    return config.action(register)


def make_configurator(configurator_factory=Configurator):
    c = configurator_factory()
    c.add_directive("add_route", add_route)
    return c
