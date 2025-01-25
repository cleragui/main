Functionalies
-------------

Shortcut
--------

The **Shortcut** widget enables assigning keyboard shortcuts to specific
actions.

.. code:: python

   Shortcut(key='Ctrl+S', func=function)

**Key Attributes:**

-  **key (str):** The keyboard shortcut (e.g., ``'Ctrl+S'``).
-  **func (function):** The function to be executed when the shortcut is
   triggered.

**Example:**

.. code:: python

   Shortcut(key='Ctrl+Q', func=lambda: print('Quit triggered!'))


Screenshot
----------

The **Screenshot** function captures the current window or screen
content and saves it as an image.

.. code:: python

   screenshot(filename='screenshot.png')

.. _key-attributes-1:

**Key Attributes:**

-  **filename (str):** Path to save the captured screenshot.

.. _example-1:

**Example:**

.. code:: python

   screenshot(filename='capture.png')


Thread
------

The **Thread** widget allows running tasks in a separate thread to avoid
blocking the main application.

.. code:: python

   thread(target=background_task)

.. _key-attributes-2:

**Key Attributes:**

-  **target (function):** The function to run in the thread.
-  **wait (bool):** If ``True``, don’t run the process immediately.

.. _example-2:

**Example:**

.. code:: python

   thread(target=lambda: print('Task in thread'), wait=False)


Encode
------

The **Encode** function is used to encode data into a specified format
such as Base64. Data such as ``images``, ``strings``, ``binary`` or any
``file``.

.. code:: python

   encoded_data = encode(b'Hello, World!')
   print(encoded_data)  # Output: 'SGVsbG8sIFdvcmxkIQ=='


Decode
------

The **Decode** function is used to decode data from a specified encoded
format such as Base64. Data such as ``images``, ``strings``, ``binary`` or any
``file``.

.. code:: python

   decoded_data = decode('SGVsbG8sIFdvcmxkIQ==')
   print(decoded_data)  # Output: 'Hello, World!'


Database
--------

The Database class provides an abstraction for interacting with an SQLite database. It abstracts common database operations such as creating tables, inserting, selecting,
updating, and deleting records. Below is a detailed guide on how to use
this class and its methods effectively.

Initialization
~~~~~~~~~~~~~~

To use the database, first, you need to initialize an instance of the
``Database`` class.

**Syntax:**

.. code:: python

   db = Database(name='example', PATH='/path/to/database')

**Parameters:**

-  **name (str):** The name of the database file. If not provided,
   it defaults to ``'clera.db'``. Ensure the name does not include the
   ``.db`` extension, as it is automatically appended.
-  **PATH (str):** The directory path where the database file is
   stored. If not provided, it defaults to the current working
   directory.

.. _example-3:

**Example:**

.. code:: python

   db = Database(name='my_database', PATH='./databases')


create Method
~~~~~~~~~~~~~

This method creates a new table in the database.

.. _syntax-1:

**Syntax:**

.. code:: python

   db.create(name='table_name', data={'column_name': data_type, ...}, commit=True)

.. _parameters-1:

**Parameters:**

-  **name (str):** The name of the table.
-  **data (dict):** A dictionary where keys are column names and
   values are data types. Supported types include:

   -  ``int`` → ``INTEGER``
   -  ``float`` → ``REAL``
   -  ``str`` → ``TEXT``
   -  ``blob`` → ``BLOB``
   -  ``null``/``None`` → ``NULL``

-  **commit (bool):** Whether to commit the transaction immediately.
   Defaults to ``True``
   
.. _example-4:

**Example:**

.. code:: python

   db.create('users', {'id': int, 'name': str, 'age': int})


insert Method
~~~~~~~~~~~~~

This method inserts data into a table.

.. _syntax-2:

**Syntax:**

.. code:: python

   db.insert(table='table_name', value=data, commit=True)

.. _parameters-2:

**Parameters:**

-  **table (str):** The name of the table.
-  **value (any):** The data to insert. It can be:

   -  **dict:** Key-value pairs of column names and values.
   -  **list/tuple:** A sequence of values corresponding to the
      table’s columns.

-  **commit (bool):** Whether to commit the transaction immediately.
   Defaults to ``True``.

.. _example-5:

**Example:**

.. code:: python

   # Insert using a dictionary
   db.insert('users', {'id': 1, 'name': 'Alice', 'age': 30})

   # Insert using a list or tuple
   db.insert('users', (2, 'Bob', 25))


select Method
~~~~~~~~~~~~~

This method retrieves data from a table.

.. _syntax-3:

**Syntax:**

.. code:: python

   db.select(table='table_name', data='*', condition='')

.. _parameters-3:

**Parameters:**

-  **table (str):** The name of the table.
-  **data (str):** The columns to retrieve. Defaults to ``"*"``,
   which selects all columns.
-  **condition (str):** An optional SQL ``WHERE`` clause to filter
   results.

**Returns:**

-  A list of tuples representing the query result.

.. _example-6:

**Example:**

.. code:: python

   # Select all rows
   rows = db.select('users')
   print(rows)

   # Select specific columns
   rows = db.select('users', data='name, age')

   # Select with a condition
   rows = db.select('users', condition="age &gt; 25")


update Method
~~~~~~~~~~~~~

This method updates data in a table.

.. _syntax-4:

**Syntax:**

.. code:: python

   db.update(table='table_name', value={'column': value, ...}, condition='SQL condition')

.. _parameters-4:

**Parameters:**

-  **table (str):** The name of the table.
-  **value (dict):** A dictionary where keys are column names and
   values are the new data.
-  **condition (str):** A SQL ``WHERE`` clause to specify which rows
   to update.

.. _example-7:

**Example:**

.. code:: python

   db.update('users', {'name': 'Charlie'}, "id = 1")


delete Method
~~~~~~~~~~~~~

This method deletes rows from a table based on a condition.

.. _syntax-5:

**Syntax:**

.. code:: python

   db.delete(table='table_name', condition='SQL condition')

.. _parameters-5:

**Parameters:**

-  **table (str):** The name of the table.
-  **condition (str):** A SQL ``WHERE`` clause to filter which rows
   to delete.

.. _example-8:

**Example:**

.. code:: python

   db.delete('users', "age &lt; 25")


drop Method
~~~~~~~~~~~

This method removes a table from the database.

.. _syntax-6:

**Syntax:**

.. code:: python

   db.drop(table='table_name')

.. _parameters-6:

**Parameters:**

-  **table (str):** The name of the table.

.. _example-9:

**Example:**

.. code:: python

   db.drop('users')


commit and close Methods
~~~~~~~~~~~~~~~~~~~~~~~~

-  **commit()**: Manually commits the current transaction to the
   database.

   .. code:: python

      db.commit()

-  **close()**: Closes the database connection.

   .. code:: python

      db.close()


Example Workflow
~~~~~~~~~~~~~~~~

Here’s how you can use the ``Database`` class to manage data:

.. code:: python

   # Initialize the database
   db = Database(name='my_app')

   # Create a table
   db.create('users', {'id': int, 'name': str, 'age': int})

   # Insert data
   db.insert('users', {'id': 1, 'name': 'Alice', 'age': 30})
   db.insert('users', (2, 'Bob', 25))

   # Retrieve data
   print(db.select('users'))  # [(1, 'Alice', 30), (2, 'Bob', 25)]

   # Update data
   db.update('users', {'name': 'Charlie'}, "id = 1")

   # Delete data
   db.delete('users', "age &lt; 25")

   # Drop table
   db.drop('users')

   # Close the connection
   db.close()
