import apistar
from miniconfig import ConfiguratorCore, reify
from miniconfig import Context as _Context


class Context(_Context):
    collection_factory = list

    @reify
    def routes(self):
        return self.collection_factory()

    @reify
    def components(self):
        return self.collection_factory()

    @reify
    def event_hooks(self):
        return self.collection_factory()


class Configurator(ConfiguratorCore):
    context_factory = Context

    app_factory = apistar.App
    async_app_factory = apistar.ASyncApp
    route_factory = apistar.Route

    def _make_app(self, factory, *, kwargs):
        self.commit()
        if "routes" in kwargs:
            self.routes.extend(kwargs.pop("routes"))
        if "components" in kwargs:
            self.components.extend(kwargs.pop("components"))
        if "event_hooks" in kwargs:
            self.event_hooks.extend(kwargs.pop("event_hooks"))

        app = factory(
            routes=self.routes,
            components=self.components,
            event_hooks=self.event_hooks,
            **kwargs,
        )
        return app

    def make_app(self, **kwargs):
        return self._make_app(self.app_factory, kwargs=kwargs)

    def make_async_app(self, **kwargs):
        return self._make_app(self.async_app_factory, kwargs=kwargs)


def make_configurator(configurator_factory=Configurator):
    c = configurator_factory()
    c.include(".directives")
    return c
