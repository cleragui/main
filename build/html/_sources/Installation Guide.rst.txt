Installation Guide
==================

Prerequisites
-------------

To effectively use Clera, you need a basic understanding of Python. If
you’re new to Python, it’s recommended to learn its basics before diving
into GUI development. Since Clera is Python-based, familiarity with
Pythonic principles is key to maximizing its potential.

Ensure the following are installed:

-  **Python 3.7 or newer**

-  **pip**, the Python package manager

**Step-by-Step Installation**

Using pip

To install Clera:

::

   pip install clera

Verifying Installation

After installation, verify it works:

::

   python -c "import clera; print('Clera is installed!')"

Troubleshooting
---------------

-  **Error:** ``ModuleNotFoundError``: Ensure Python is correctly
   installed and accessible via your system path.

-  **Proxy Issues:** Configure pip for proxies using ``--proxy`` option.

-  **Compatibility Errors:** Ensure Python is version 3.7 or later.

-  **Pip Issues:** Use ``pip install --upgrade pip`` for outdated pip
   issues.
