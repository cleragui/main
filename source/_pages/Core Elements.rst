Core Elements
=============

GET
---

The **GET** function retrieves a widget by its ID for dynamic updates.

.. code:: python

   GET(id='widget-id')

**Example:**

.. code:: python

   widget = GET(id='-my-widget-')
   widget.value(42)
   

Popup
-----

The **Popup** creates a modal or non-modal dialog window for displaying
content or gathering input.

.. code:: python

   Popup(title='Popup Title', widgets=[[widget1], [widget2, widget3]])

**Key Attributes:**

-  **title (str):** Title of the popup window.

-  **widgets (list):** Nested List of widgets to display inside the
   popup.

-  **size (tuple):** Width and height of the popup.

-  **modal (bool):** If ``True``, disables interaction with the parent
   window.

-  **center (bool):** Centers the popup on the screen.

.. _example-1:

**Example:**

.. code:: python

   Popup(
       title='Settings',
       widgets=[
           [Text(value='Adjust your settings')],
           [Button(value='Close', func=lambda: print('Popup closed'))]
       ],
       size=(300, 200),
       modal=True
   )


Folder
------

The **Folder** dialog allows users to select a directory.

.. code:: python

   Folder(caption='Select Folder', directory='/path/to/start')

.. _key-attributes-1:

**Key Attributes:**

-  **caption (str):** Title of the folder selection dialog.

-  **directory (str):** Initial directory to display.

.. _example-2:

**Example:**

.. code:: python

   folder = Folder(caption='Choose a Directory')
   print(f'Selected Folder: {folder}')


File
----

The **File** dialog enables selecting or saving files.

.. code:: python

   File.open(caption='Open File', filter='*.txt')

.. _key-attributes-2:

**Key Attributes:**

-  **caption (str):** Title of the file dialog.

-  **filter (str):** File type filter (e.g., ``*.txt``).

-  **directory (str):** Initial directory to display.

-  **type (str):** ``single`` or ``multi`` for selecting one or multiple
   files.

.. _example-3:

**Example:**

.. code:: python

   file = File()
   selected_file = file.open(caption='Open Text File', filter='Text Files (*.txt)')
   print(f'Selected File: {selected_file}')


Toolbar
-------

The **Toolbar** provides a customizable bar for tool buttons.

.. code:: python

   Toolbar(name='Main Toolbar', tool_items=[button1, button2])

.. _key-attributes-3:

**Key Attributes:**

-  **name (str):** Name of the toolbar.

-  **tool_items (list):** List of buttons or actions.

-  **movable (bool):** Allows the toolbar to be moved.

-  **position (str):** Position on the window (``top``, ``bottom``,
   ``left``, ``right``).

.. _example-4:

**Example:**

.. code:: python

   Toolbar(
       name='Main Toolbar',
       tool_items=[
           Button(value='Save', func=lambda: print('Saved')),
           Button(value='Open', func=lambda: print('Opened'))
       ],
       position='top'
   )


Titlebar
--------

The **Titlebar** allows customization of the window’s title bar. To
display title bar, window’s ``frame`` must be set to ``False``.
``Window(frame=False)``

.. code:: python

   Titlebar(title='My Application')

.. _key-attributes-4:

**Key Attributes:**

-  **title (str):** Text displayed in the title bar.

-  **widgets (list):** Additional widgets to include in the title bar.

-  **background_color (str):** Background color of the title bar.

-  **text_color (str):** Color of the title text.

.. _example-5:

**Example:**

.. code:: python

   Titlebar(
        title='Custom Titlebar',
        widgets=[Button(value='Help', func=lambda: print('Help clicked'))],
        background_color='gray',
        text_color='white',
        alignment=center
   )


Menubar
-------

The **Menubar** provides a menu system for the window.

.. code:: python

   Menubar(menu_items=[menu1, menu2])

.. _key-attributes-5:

**Key Attributes:**

-  **menu_items (list):** A list of menus and their actions.

.. _example-6:

**Example:**

.. code:: python

   Menubar(
       menu_items=[
           ['File', [item(label='Open', func=lambda: print('File Opened'))]],
           ['Edit', [item(label='Copy', func=lambda: print('Copied'))]]
       ]
   )


Statusbar
---------

The **Statusbar** displays messages and widgets at the bottom of the
window.

.. code:: python

   Statusbar()

.. _key-attributes-6:

**Key Attributes:**

-  **message (str):** Temporary status message.

-  **add (widget):** Adds a widget to the status bar.

.. _example-7:

**Example:**

.. code:: python

   status = Statusbar()
   status.message('Ready', time=5)


Highlight
---------

The **Highlight** widget is used for syntax highlighting.

.. code:: python

   Highlight(widget_id='-widget_id-')

.. _key-attributes-7:

**Key Attributes:**

-  **widget_id (str):** Referencing widget to apply the syntax
   highlighting to.

-  **synthax (dict):** A dictionary of syntax patterns to highlight. You
   can use regex using the ``r()`` function.

.. _example-8:

**Example:**

.. code:: python

    synthax = {
        r(['rgb',"rgba"]): {
            'color': 'rgb(155, 102, 197)'
        },
    }

    Highlight(widget_id='-widget_id-', synthax)


TabWidget
---------

The **TabWidget** allows you to organize content into multiple tabs,
enabling efficient navigation between different views or sections.

.. code:: python

   TabWidget(tabs=[tab1, tab2], current=0)

.. _key-attributes-8:

**Key Attributes:**

-  **tabs (list):** A list of tabs, each defined using the ``tab()``
   function.

-  **current (int):** The index of the tab to display initially.

-  **id (str):** Assigns an identifier for dynamic tab updates.

-  **tab_changed (function):** A callback function triggered when the
   current tab is changed.

.. _example-9:

**Example:**

.. code:: python

   TabWidget(
       tabs=[
           tab(layout='Content of Tab 1', name='Tab 1'),
           tab(layout='Content of Tab 2', name='Tab 2')
       ],
       current=0,
       tab_changed=lambda index: print(f"Switched to Tab {index}")
   )


ScrollArea
----------

The **ScrollArea** widget creates a scrollable container, allowing users
to navigate through large or overflowing content.

.. code:: python

   ScrollArea(widgets=layout)

.. _key-attributes-9:

**Key Attributes:**

-  **widgets (list):** A list of widgets to display within the
   scrollable area.

-  **id (str):** Identifier for dynamic updates.

-  **contain (bool):** Enables resizing of child widgets to fit within
   the scrollable area.

.. _example-10:

**Example:**

.. code:: python

   layout = Box([
        [Text(value='This is a long text inside a scrollable area.')],
        [Image(source='example.png')]
   ])

   ScrollArea(
        widgets=layout,
        id='-scrollable-section-',
        contain=True
   )


ColorPicker
-----------

The **ColorPicker** widget provides a popup for selecting colors.

.. code:: python

   ColorPicker(title='Pick a Color', current='#FF5733')

.. _key-attributes-10:

**Key Attributes:**

-  **title (str):** Title of the color picker popup.

-  **current (str):** The initial color in hex format (e.g.,
   ``#FFFFFF``).

-  **color_selected (function):** Callback function executed when a
   color is selected.

-  **modal (bool):** Determines if the popup is modal.

.. _example-11:

**Example:**

.. code:: python

   def on_color_select(color):
       print(f"Selected Color: {color}")

   ColorPicker(
       title='Choose Background Color',
       current='#FFFFFF',
       color_selected=on_color_select
   )