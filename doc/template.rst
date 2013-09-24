Templates
=========

Example
-------

src/templates/test.html:

.. code:: html

        <html>
                <body>
                You are: {{ name }}.
                </body>
        </html>

bin/ipython

.. code:: python

    from gap.template import get_template
    template = get_template('homepage.html').render(
                {"name": "Jan Amos Komensky <jan.amos@example.com>"}
        )
    print template

.. code:: html

        <html>
                <body>
                Your name is: Jan Amos Komensky &lt;jan.amos@example.com&gt;.
                </body>
        </html>

Note that ``<`` and ``>`` are properly escaped.

Description
-----------

Gap templates are only preconfigured `Jinja2 templates <http://jinja.pocoo.org/docs/>`__ (packed with Google Appengine). Read respective `documentation <http://jinja.pocoo.org/docs>`__ for detailed information on how to use Jinja.

Gap's ``get_template`` setups Jinja2 environment with

- auto escape option set to on,
- sets template loader to look in folders defined in `config.py:TEMPLATES_PATH <../gap/templates/src/config.py>`__. The default lookup folder is ``src/templates``.
