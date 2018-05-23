from functools import wraps
import logging
logger = logging.getLogger(__name__)


def add_route(config, url, method, handler, name=None, documented=True, standalone=False):
    @wraps(handler)
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

    discriminator = (add_route, url, method)
    return config.action(discriminator, register)


def add_component(config, factory_or_component, *args, **kwargs):
    def register():
        if callable(factory_or_component):
            component = factory_or_component(*args, **kwargs)
        else:
            component = factory_or_component
        logger.debug("add component %s", component)
        config.components.append(component)

    if callable(factory_or_component):
        register = wraps(factory_or_component)(register)
    discriminator = (add_component, _marker(factory_or_component))
    return config.action(discriminator, register)


def add_event_hook(config, factory_or_hook, *args, **kwargs):
    def register():
        if callable(factory_or_hook):
            hook = factory_or_hook(*args, **kwargs)
        else:
            hook = factory_or_hook
        logger.debug("add event_hook %s", hook)
        config.event_hooks.append(hook)

    if callable(factory_or_hook):
        register = wraps(factory_or_hook)(register)
    discriminator = (add_event_hook, _marker(factory_or_hook))
    return config.action(discriminator, register)


def _marker(ob):
    if callable(ob):
        return ob
    if hasattr(ob, "__marker__"):
        return ob
    return _marker(ob.__class__)


def includeme(config):
    config.add_directive("add_route", add_route)
    config.add_directive("add_component", add_component)
    config.add_directive("add_event_hook", add_event_hook)
