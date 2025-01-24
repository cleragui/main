Layouts Overview
================

Box Layout
----------

The Box layout organizes widgets into rows and columns.

.. code:: python

   Box([
       [Text('Row 1')],
       [Text('Row 2'), Button('Click')]
   ])

.. _key-attributes-10:

**Key Attributes:**

-  **widgets** (list): A nested list defining the structure of rows and
   columns.

-  **orientation** (str): ``horizontal`` or ``vertical`` orientation.

.. _example-7:

**Example:**

.. code:: python

   from clera import Box, Text, Button

   Box([
       [Text('Row 1 Text')],
       [Button(value='Row 2 Button')]
   ])


Grid Layout
-----------

The Grid Layout will arrange widgets in a tabular structure based on
specified rows and columns. Stay tuned for updates on this feature.

.. code:: python

   Grid([
       [Text('Row 1')],
       [Text('Row 2'), Button('Click')]
   ])

.. _key-attributes-11:

*Key Attributes:*

-  **widgets** (list): A nested list defining the structure of rows and
   columns.


Additional Layout Features
--------------------------

**Group Layout**

The Group layout organizes button widgets within a container. It
supports vertical or horizontal orientation and allows nesting other
layouts within.

.. _key-attributes-12:

**Key Attributes:**

-  **widgets** (list): List of child button widgets.

-  **orientation** (str): ``vertical`` or ``horizontal``.

-  **strict** (bool): Enforces strict alignment of child widgets if
   True.

.. _example-8:

**Example:**

.. code:: python

   from clera import Group, Button, Text

   group(
       widgets=[
           Button(value='Action 1'),
           Button(value='Action 2')
       ],
       orientation='vertical'
   )


**Fieldset Layout**

The Fieldset layout groups related widgets together under a labeled
border, making it ideal for forms or sections.

.. _key-attributes-13:

**Key Attributes:**

-  **label** (str): Title of the fieldset.

-  **widgets** (list): List of widgets inside the fieldset.

-  **orientation** (str): ``vertical`` or ``horizontal``.

.. _example-9:

**Example:**

.. code:: python

   from clera import Fieldset, Input, Button

   fieldset(
       label='Login Details',
       widgets=[
           Input(placeholder='Username'),
           Input(placeholder='Password', type='password'),
           Button(value='Login')
       ],
       orientation='vertical'
   )
