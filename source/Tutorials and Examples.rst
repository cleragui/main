Tutorials and Examples
======================

Tutorial: Hello World
---------------------

Create your first Clera application:

.. code:: python

   from clera import Window, Text, Box

   window = Window()
   Box([
       [Text('Hello, World!', alignment='center')]
   ])
   window.run()

Advanced Example: Login Form
----------------------------

.. code:: python

   from clera import Window, Box, Input, Button, Text

   window = Window()

   def login():
       print('Login submitted')

   Box([
       [Text('Login Form', alignment='center')],
       [Input(placeholder='Username')],
       [Input(placeholder='Password', type='password')],
       [Button('Submit', func=login)]
   ])

   window.run()

Custom Title Bars
-----------------

Replace the default title bar:

.. code:: python

   from clera import Window, Titlebar

   window = Window(frame=False)
   Titlebar(
       title='Custom Title',
       text_color='white',
       background_color='blue'
   )
   window.run()

Dynamic Updates
---------------

Update widgets dynamically:

.. code:: python

   window.update('widget_id', Button('Updated Button'))

Styling Widgets
---------------

You can use CSS to style widgets. For example:

.. code:: python

   from clera import Window, Box, Input, Button, Text

   window = Window()

   css = '''
   Button {
       border: 1px solid black;
       color: red;
       background: yellow;
   }
   '''

   Box([
       [Button('Click Me!', func=call(print, "Clicked!"))]
   ])

   window.run(css)

Applying External Styles with ``clera``

In ``clera``, you can apply custom styles to your user interface
elements using an external stylesheet with the ``.cx`` extension. This
approach allows for a more organized and flexible way to manage your
UI’s appearance, separating the logic from the design. Here’s how you
can style your elements:

**Example Code**: ``interface.py``

.. code:: python

   from clera import Window, Button, Textarea, Input, Box, link
   link('style.cx')  # Link to the external stylesheet
   window = Window('interface', fixed_size=(218, 166)) 

   layout = [
       [Button('One', id='one_id'), Button('Two', id='two_id')], 
       [Textarea('text_id', 'Textarea Widget')],
       [Input('Input Widget', 'input_id')],
       [Button('Three', id='three_id')]
   ]
   Box(layout)  # Organize the layout within a box
   window.run()  # Run the application

**External Stylesheet:** ``style.cx``

.. code:: css

   @interface.py /* Targeting the interface.py file */

   window {
       background: #171717;
   }

   button {
       color: blue;
       border: 0px solid;
       border-radius: 1px;
   }

   one_id {
       color: yellow;
       background: red;
   }

   text_id {
       border: 1px solid red;
   }

   three_id {
       background: #5C7CFA;
       color: white;
   }

   input_id {
       border: 0px solid;
       background: green;
       color: white;
   }

   two_id {
       background: yellow;
   }

**How It Works:**

1. **Linking the Stylesheet:**

   -  The ``link('style.cx')`` command in your ``interface.py`` script
      connects the Python interface to the external CSS file. This
      allows you to apply styles written in ``style.cx`` to the UI
      components defined in the Python code.

2. **Styling Elements:**

   -  In the ``style.cx`` file, you can specify CSS rules to style the
      different UI elements. Each UI element, such as buttons or
      textarea, can be targeted using either general tags (like
      ``button``) or specific IDs (like ``one_id`` for a button with a
      unique ID).
   -  For example, ``one_id`` styles the button with the ID ``one_id``,
      setting its background color to red and text color to yellow.

3. **CSS Syntax:**

   -  The syntax used in the ``.cx`` file is similar to standard CSS but
      is specifically designed to work with ``clera``. Each style rule
      specifies properties such as ``background``, ``color``,
      ``border``, and ``border-radius`` to customize the appearance of
      UI elements.
   -  Additionally, you can target specific components with their unique
      IDs, ensuring that you can apply precise styles to individual
      widgets.

This approach of using external styling ensures that the appearance of
your application is modular and easily maintainable, while the Python
code remains focused on the functionality.``\`

--------------

.. _troubleshooting-1:
