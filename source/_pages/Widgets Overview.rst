Widgets Overview
================

Button
------

A clickable widget for triggering actions. The Button widget is a core
interactive element in Clera. It allows users to trigger specific
actions when clicked.

.. code:: python

   Button(value='Submit', func=my_function)

**Key Attributes:**

-  **value** (str): The label displayed on the button.

-  **func** (function): A function to be executed upon clicking the
   button.

-  **icon** (str): Optional path to an icon displayed on the button.

-  **tooltip** (str): Text that appears when hovering over the button.

-  **sizepolicy** (tuple): Defines how the button resizes within its
   layout.

-  **checkable** (bool): Allows the button to maintain an on/off state
   when clicked.

-  **checked** (bool): Initial state if ``checkable`` is True.

**Example:**

.. code:: python

   def on_button_click():
       print("Button was clicked!")

   Button(
       value='Click Me',
       func=on_button_click,
       tooltip='Click this button to trigger an action',
       checkable=True
   )

**Advanced Usage:**

Integrating a hover effect:

.. code:: python

   Button(
       value='Hover Me',
       hover=call(print, "Hovered!"),
       tooltip='Hover over this button'
   )


Text
----

The Text widget is used to display static or dynamic text content.

.. code:: python

   Text(value='Hello, Clera!')

.. _key-attributes-1:

**Key Attributes:**

-  **value** (str): The displayed text.

-  **alignment** (str): Align the text (``left``, ``center``,
   ``right``).

-  **wordwrap** (bool): Enables wrapping for long text.

-  **id** (str): Assigns an identifier for updating the text
   dynamically.

.. _example-1:

**Example:**

.. code:: python

   Text(
       value='Hello, World!',
       alignment='center',
       id='-greeting-'
   )

**Dynamic Text Update:**

.. code:: python

   window.update('-greeting-', Text(value='Updated Text'))


Input
-----

The Input widget captures single-line text from the user. It can be
customized for passwords or standard text fields.

.. code:: python

   Input(placeholder='Enter your username', type='password')

.. _key-attributes-2:

**Key Attributes:**

-  **placeholder** (str): Hint text displayed when the input field is
   empty.

-  **type** (str): Defines the input type (``standard``, ``password``,
   ``no_echo``).

-  **maxlength** (int): Maximum number of characters allowed.

-  **readonly** (bool): If True, the field cannot be edited.

-  **value** (str): Initial value of the input field.

-  **text_changed** (function): A function triggered when the text
   changes.

**Example:**

.. code:: python

   def on_text_change():
       print("Text has changed")

   Input(
       placeholder='Enter your username',
       maxlength=20,
       text_changed=on_text_change
   )

**Password Field:**

.. code:: python

   Input(
       placeholder='Enter your password',
       type='password'
   )


Checkbox
--------

A Checkbox is used for toggling options on or off. Represents a binary
state.

.. code:: python

   CheckBox(label='Accept Terms', checked=False)

.. _key-attributes-3:

**Key Attributes:**

-  **label** (str): Text displayed beside the checkbox.

-  **checked** (bool): Initial state.

-  **state_changed** (function): Triggered when the state changes.

**Example:**

.. code:: python

   def on_check_change():
       print("Checkbox state changed")

   CheckBox(
       label='Accept Terms',
       checked=False,
       state_changed=on_check_change
   )


RadioButton
-----------

Used for exclusive selection within a group.

.. code:: python

   RadioButton(label='Option A', checked=True)

.. _key-attributes-4:

**Key Attributes:**

-  ``label`` (str): Text displayed beside the button.

-  ``checked`` (bool): Initial state.


ProgressBar
-----------

Visual representation of progress. The ProgressBar widget visually
indicates progress for tasks.

.. code:: python

   ProgressBar(min=0, max=100, value=75)

.. _key-attributes-5:

**Key Attributes:**

-  **min** (int): Minimum value of the progress bar.

-  **max** (int): Maximum value.

-  **value** (int): Current progress.

-  **orientation** (str): Either ``horizontal`` or ``vertical``.

-  **text_visible** (bool): Displays progress as text if True.

.. _example-2:

**Example:**

.. code:: python

   ProgressBar(
       min=0,
       max=100,
       value=50,
       orientation='horizontal'
   )


Textarea
--------

Multi-line text input for larger text content. The Textarea widget
allows multi-line input for larger text content, making it ideal for
comments or detailed user inputs.

.. code:: python

   Textarea(placeholder='Enter detailed notes', readonly=False)

.. _key-attributes-6:

**Key Attributes:**

-  **placeholder** (str): Hint text displayed when the Textarea is
   empty.

-  **value** (str): Initial text content of the Textarea.

-  **readonly** (bool): Prevents editing when set to True.

-  **font** (str): Font family for the text content.

-  **fontsize** (int): Font size for the text content.

-  **text_changed** (function): Function called when the text changes.

-  **wordwrap** (bool): Enables word wrapping within the Textarea.

.. _example-3:

**Example:**

.. code:: python

   def on_text_changed():
       print("Textarea content changed")

   Textarea(
       placeholder='Write your thoughts here...',
       text_changed=on_text_changed,
       wordwrap=True
   )


ListWidget
----------

Displays a list of selectable items. The ListWidget displays selectable
items in a list format.

.. code:: python

   ListWidget(list_items=['Item 1', 'Item 2'], mode='single')

.. _key-attributes-7:

**Key Attributes:**

-  **list_items** (list): A list of items to display.

-  **mode** (str): Selection mode (``single``, ``multi``, etc.).

-  **current_item_changed** (function): Function triggered when the
   selected item changes.

.. _example-4:

**Example:**

.. code:: python

   ListWidget(
       list_items=['Item 1', 'Item 2', 'Item 3'],
       mode='single',
   )


Select
------

The Select widget provides a dropdown menu for users to choose from
multiple options.

.. code:: python

   Select(options=['Option 1', 'Option 2'], placeholder='Choose an option')

.. _key-attributes-8:

**Key Attributes:**

-  **options** (list): List of selectable options.

-  **placeholder** (str): Default text shown before a selection is made.

-  **current_text_changed** (function): Function triggered when the
   selection changes.

.. _example-5:

**Example:**

.. code:: python

   select = Select(
       options=['Option 1', 'Option 2', 'Option 3'],
       placeholder='Choose an option',
   )


Image
-----

The Image widget displays graphical content, including icons and photos.

.. code:: python

   Image(source='path/to/image.png')

.. _key-attributes-9:

**Key Attributes:**

-  **source** (str): Path to the image file.

-  **size** (tuple): Dimensions of the image (height, width).

-  **alignment** (str): Aligns the image (``left``, ``center``,
   ``right``).

-  **hidden** (bool): Hides the widget if set to True.

.. _example-6:

**Example:**

.. code:: python

   Image(
       source='path/to/image.png',
       size=(200, 100),
       alignment='center'
   )


Slider
------

The **Slider** widget is used to select a value within a range by
sliding a handle. It can be displayed horizontally or vertically.

.. code:: python

   Slider(min=0, max=100, value=50, orientation='horizontal')

.. _key-attributes-10:

**Key Attributes:**

-  **min (int):** The minimum value of the slider.

-  **max (int):** The maximum value of the slider.

-  **value (int):** The initial value of the slider.

-  **orientation (str):** Determines the slider’s orientation
   (``horizontal`` or ``vertical``).

-  **value_changed (function):** A callback function triggered when the
   slider value changes.

-  **step (int):** The step size for increments/decrements.

-  **tooltip (str):** Text that appears when hovering over the slider.

.. _example-7:

**Example:**

.. code:: python

   def on_slider_value_change(value):
       print(f"Slider value: {GET('-slider-')}")

   Slider(
       id='-slider-',
       min=0,
       max=100,
       value=25,
       orientation='vertical',
       value_changed=on_slider_value_change,
       tooltip='Adjust the slider to change the value'
   )


Dial
----

The **Dial** widget provides a rotary interface for selecting a value,
commonly used for adjusting settings like volume or brightness.

.. code:: python

   Dial(min=0, max=360, value=90)

.. _key-attributes-11:

**Key Attributes:**

-  **min (int):** The minimum value of the dial.

-  **max (int):** The maximum value of the dial.

-  **value (int):** The initial value of the dial.

-  **notches (bool):** Displays notches around the dial.

-  **value_changed (function):** A callback function triggered when the
   dial value changes.

-  **tooltip (str):** Text that appears when hovering over the dial.

.. _example-8:

**Example:**

.. code:: python

   def on_dial_change(value):
       print(f"Dial value: {GET('-dial-')}")

   Dial(
       id='-dial-',
       min=0,
       max=100,
       value=50,
       notches=True,
       value_changed=on_dial_change,
   )


Table
-----

The **Table** widget displays data in a structured, grid-like format
with rows and columns.

.. code:: python

   Table(row=5, column=5)

.. _key-attributes-12:

**Key Attributes:**

-  **table_data (list):** A list of rows, where each row is a list of
   cell values.

-  **row (int):** The number of rows in the table.

-  **column (int):** The number of columns in the table.

-  **id (str):** Identifier for dynamic updates.

.. _example-9:

**Example:**

.. code:: python

   data = [
        td('Data 1', 0, 0)
   ]

   Box([
        [Table(row=5, column=5, table_data=data)]
   ])
