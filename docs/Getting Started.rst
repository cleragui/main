Quick Start / Getting Started
=============================

Creating Your First Clera Application
-------------------------------------

In GUI applications, a window is the primary viewing area where
interface elements like widgets, buttons, and layouts are displayed.
Clera’s ``Window()`` class serves as the canvas for all components.
Without a ``Window`` instance, no interface can be created.

Steps to Create a Window:

1. **Import the** ``**Window**`` **Class**: Begin by importing the
   ``Window`` class from Clera.

2. **Initialize the Window**: Create an instance of the ``Window``
   class.

3. **Run the Window**: Use the ``run()`` method to display it.

Here’s a minimal example to create and display a window:

.. code:: python

   from clera import Window

   # Initialize and run the window
   window = Window()
   window.run()

In this script:

-  The ``Window`` class is imported and instantiated.

-  The ``run()`` method displays the GUI.

-  This setup forms the foundation for building more complex interfaces.

Adding Content to the Window
----------------------------

An empty window is not useful, so let’s explore how to add interactive
elements. In Clera, these elements are called “widgets.” To organize
widgets within a window, Clera uses layouts. Think of a layout as a
bookshelf and widgets as books placed on its shelves.

.. figure:: /_static/shelf.jpg
   :width: 600px
   :align: center

Widgets are organized using nested lists. The main list represents the
bookshelf, sublists represent rows, and items within sublists are the
widgets themselves. Clera supports two main layouts:

.. figure:: /_static/box-grid.jpg
   :width: 400px
   :align: center

1. **Box Layout**: Arranges widgets in rows (or columns) and stretches
   them to fill available space. All rows are adjusted to maintain a
   consistent appearance.

2. **Grid Layout** (Under Development): Automatically arranges widgets
   in a grid, with specific cells defined by row and column indices.

Quick Start Example:

.. code:: python

   from clera import Window, Box, Text

   # Initialize the window
   window = Window()

   # Add a text widget with layout
   Box([
       [Text('Welcome to Clera!', alignment='center')]
   ])

   # Run the window
   window.run()

**Explanation:**

-  The ``Box`` class organizes widgets into a layout.

-  A ``Text`` widget displays the message “Hello Clera!” centered in the
   window.

-  The ``run()`` method launches the application.

Adding Interactivity with Buttons
---------------------------------

Clera supports interactive widgets, such as buttons, which respond to
user actions. Let’s enhance the previous example by adding a button that
updates the window to display “Hello Clera!” when clicked.

An interactive application with a button:

.. code:: python

   from clera import Window, Box, Button, Text, GET

   # Initialize the window
   window = Window()

   # Define a function to handle button clicks
   def show_message():
       text_widget = Text('Hello Clera!', alignment='center')
       GET('-button-').update(text_widget)

   # Add a button widget
   Box([
       [Button('Click me', show_message, id='-button-')]
   ])

   # Run the window
   window.run()

Observe the GUI window and experiment with widgets.

**Explanation:**

1. **Defining a Function**: The ``show_message()`` function creates a
   ``Text`` widget with the message “Hello Clera!” and centers it.

2. **Referencing Widgets**: The ``GET`` function, using the button’s ID
   (``'-button-'``), retrieves the button widget and updates it.

3. **Adding a Button**: The ``Button`` widget is labeled “Click me,”
   triggers ``show_message()`` on click, and is assigned an ID for
   reference.

4. **Running the Application**: The ``run()`` method launches the window
   with the button.

This example demonstrates how to add interactivity, making your GUI
application responsive to user actions.
