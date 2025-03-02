.. toctree::
   :maxdepth: 2
   :caption: Table of contents:
   :hidden:

   _pages/Introduction.rst
   _pages/Installation Guide.rst
   _pages/Getting Started.rst
   _pages/Widgets Overview.rst
   _pages/Layouts Overview.rst
   _pages/Core Elements.rst
   _pages/Functionality.rst
   _pages/Tutorials and Examples.rst
   _pages/Troubleshooting.rst
   _pages/FAQs.rst
   _pages/Documentation.rst


Getting Started with Clera: A Beginner's Guide
===================================================

Welcome to Clera! This guide is designed to help beginners quickly get started with Clera for creating GUI applications using Python. Whether you're a novice programmer or new to GUI development, Clera makes building applications simple and intuitive.

What is Clera?
--------------

Clera is a Python-based GUI framework built on PySide6. It simplifies the creation of visually appealing and functional applications with minimal effort. Here are some reasons why Clera is beginner-friendly:

- Intuitive and clean syntax.
- Ready-to-use widgets like buttons, text inputs, and dropdowns.
- Built-in layouts to organize your user interface.
- Cross-platform compatibility (Windows, macOS, Linux).

Prerequisites
-------------

Before starting, ensure you have the following:

- **Python Installed**: Version 3.7 or newer.
- **pip**: Python’s package manager.

To verify Python installation, run:

.. code-block:: bash

    python --version

To verify pip installation, run:

.. code-block:: bash

    pip --version

If either is missing, download and install Python from `python.org <https://www.python.org>`_.

Installing Clera
----------------

Clera can be installed with a single pip command:

.. code-block:: bash

    pip install clera

Verifying Installation
----------------------

To confirm Clera is installed correctly, run the following in Python:

.. code-block:: python

    import clera
    print('Clera is installed!')

If no errors occur, you're ready to start using Clera!

Your First Clera Application
----------------------------

Let’s create a simple window with Clera.

Step 1: Initialize the Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open a text editor (e.g., VS Code, PyCharm, or Notepad++) or an IDE.
2. Save a new Python file (e.g., `app.py`).
3. Write the following code:

.. code-block:: python

    from clera import Window

    # Create the application window
    window = Window()

    # Start the application
    window.run()

4. Run the file using:

.. code-block:: bash

    python app.py

You’ll see an empty window pop up. Congratulations—you’ve created your first Clera application!

Adding Widgets
--------------

Widgets are the building blocks of your application. Let’s enhance the window by adding some widgets.

Step 2: Adding a Text Widget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Text widget is used to display static or dynamic text.

.. code-block:: python

    from clera import Window, Text, Box

    window = Window()

    # Add a Text widget
    Box([[Text(value='Hello, Clera!', alignment='center')]])

    window.run()

This code displays a centered text message.

Step 3: Adding a Button
~~~~~~~~~~~~~~~~~~~~~~~~

Add a clickable Button that performs an action when clicked.

.. code-block:: python

    from clera import Window, Button, Box

    window = Window()

    def on_button_click():
        print("Button clicked!")

    # Add a Button widget
    Box([[Button(value='Click Me', func=on_button_click)]])

    window.run()

Run the script and click the button. You’ll see "Button clicked!" printed in the console.

Organizing Your UI with Layouts
-------------------------------

Layouts control how widgets are arranged in your application. Clera offers multiple layouts, such as Box and Grid.

Step 4: Using Box Layout
~~~~~~~~~~~~~~~~~~~~~~~~~

The Box layout stacks widgets in rows or columns.

.. code-block:: python

    from clera import Window, Box, Text, Button

    window = Window()

    # Arrange widgets in a Box layout
    Box([
        [Text(value='Row 1: Hello, Clera!', alignment='center')],
        [Button(value='Row 2: Click Me')]
    ])

    window.run()

Each inner list in Box represents a row of widgets. You can add as many rows as needed.

Interactive Example: Building a Simple Form
-------------------------------------------

Combine widgets and layouts to create a form with input fields and a submit button.

Step 5: Creating a Login Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from clera import Window, Box, Input, Button, Text, GET

   window = Window()

   def on_login():
      print(f"Username: {GET('uname')}, Password: {GET('pwd')}")

   # Define input fields
   username = Input(id="uname", placeholder='Enter Username')
   password = Input(id="pwd", placeholder='Enter Password', type='password')


   # Arrange inputs and a button in a Box layout
   Box([
      [Text(value='Login Form', alignment='center')],
      [username],
      [password],
      [Button(value='Submit', func=on_login)]
   ])

   window.run()

How It Works
~~~~~~~~~~~~

- **Input Fields**: Input captures user data (e.g., username and password).
- **Submit Button**: The Button triggers the on_login function, which prints the inputs to the console.

Run the code, enter a username and password, and click submit.

Styling Your Application
-------------------------

Clera allows you to style widgets with CSS-like syntax for a polished look.

Step 6: Applying Styles
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    window.run("""
        Button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
         }

        Text {
            font-family: Arial;
            font-size: 16px;
         }
    """)

Run this code to see your button and text styled.

Next Steps
----------

Congratulations on completing the Getting Started guide! From here, you can:

- Explore advanced widgets like ProgressBar, Checkbox, and ListWidget.
- Experiment with dynamic widget updates using `window.update()`.
- Refer to the detailed documentation for more advanced examples and features.
- Visit the official Clera documentation for more resources and tutorials.

Happy coding with Clera!