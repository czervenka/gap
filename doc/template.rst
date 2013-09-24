Templates
=========

Short version
-------------


src/templates/test.html:

.. code: html

        <html><body>Your name is: {{ name }}.</body></html>

bin/ipython

.. code: python

    In [1]: from gap.template import get_template
    In [2]: template = get_template('homepage.html').render(
    ...         {"name": "Jan Amos Komensky"}
    ...     )
    Out [2]: '<html><body>Jan Amos Komensky</body></html>'

