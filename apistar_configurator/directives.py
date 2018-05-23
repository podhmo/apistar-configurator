import logging
logger = logging.getLogger(__name__)


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


def add_component(config, factory_or_component, *args, **kwargs):
    # todo: confilict detection?
    def register():
        if callable(factory_or_component):
            component = factory_or_component(*args, **kwargs)
        else:
            component = factory_or_component
        logger.debug("add component %s", component)
        config.components.append(component)

    return config.action(register)


def add_event_hook(config, factory_or_hook, *args, **kwargs):
    # todo: confilict detection?
    def register():
        if callable(factory_or_hook):
            hook = factory_or_hook(*args, **kwargs)
        else:
            hook = factory_or_hook
        logger.debug("add event_hook %s", hook)
        config.event_hooks.append(hook)

    return config.action(register)


def includeme(config):
    config.add_directive("add_route", add_route)
    config.add_directive("add_component", add_component)
    config.add_directive("add_event_hook", add_event_hook)
