.. image:: https://travis-ci.org/podhmo/apistar-configurator.svg?branch=master
    :target: https://travis-ci.org/podhmo/apistar-configurator

apistar_configurator
========================================

configurator for `apistar <https://github.com/encode/apistar>`_


app.py

.. code-block:: python

  from apistar_configurator import make_configurator

  if __name__ == '__main__':
      config = make_configurator()
      config.include("welcome")
      app = config.make_app()
      app.serve('127.0.0.1', 5000, debug=True)

welcome.py

.. code-block:: python

  def welcome(name=None):
      if name is None:
          return {'message': 'Welcome to API Star!'}
      return {'message': 'Welcome to API Star, %s!' % name}


  def includeme(config):
      config.add_route("/", method="GET", handler=welcome)


more examples are `here <./examples>`_
