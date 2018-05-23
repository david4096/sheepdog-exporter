sheepdog-exporter
=================

Export metadata from the DCP.

::

    sheepdog-exporter program project

    sheepdog-exporter program project --dcp-url my-url --credentials path/to/credentials --output-path /path/to/write/output

This will write a ``.json`` file with the corresponding metadata with a
filename corresponding to the program and project.
``program-project.json``.

Development
-----------

-  A simple test demonstrate usage of the exporter class in ``test``.

Issues
------

-  JSON data is created by translating from TSV to work around a
   sheepdog issue.
-  Provenance to the original JSON schemas are lost.
-  Some functions in the exporter are unused.
