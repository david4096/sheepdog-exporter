# sheepdog-exporter
<img src="https://travis-ci.org/david4096/sheepdog-exporter.svg?branch=master" /> <img src="https://img.shields.io/pypi/v/sheepdog-exporter.svg" />

Export metadata from the DCP.

```
# Download the credentials.json from the DCP web UI and put in the current directory
pip install sheepdog-exporter
sheepdog-exporter program project

sheepdog-exporter program project --dcp-url my-url --credentials path/to/credentials --output-path /path/to/write/output
```

This will write a `.json` file with the corresponding metadata
with a filename corresponding to the program and project. `program-project.json`.

The resulting JSON has the form:

```
{
  "manifest": [{DataObject},...],
  "metadata": {
        metadata_type: [{metadata_value}], ...
  }
}
```

Metadata types that are expected to have files associated with them will
have an `id` that matches an `id` in the manifest.

## Development

<img src="diagrams/sheepdog_exporter.svg" width="250" />

* A simple test demonstrates usage of the Exporter class in `test`.

### Using the Python API

The exporter is available for reuse from your Python code, instantiate it
with the location of the credentials.json and the location of the DCP instance
you would like to export from:

```
from sheepdog_exporter import Exporter
exporter = Exporter('path/to/credentials', 'https://dcp.bionimbus.org')
my_export = exporter.export('topmed', 'public')
```

Other convenience methods are available for listing programs and projects: 
`.get_projects()` and `.get_programs()`.

See [sheepdog_exporter.py](sheepdog_exporter.py) for more.

## Issues

* Provenance to the original JSON schemas are lost.
  * It has not been tested if JSON dumps can be used as sheepdog input.
* Some functions in the exporter are unused.
* Print messages cannot be easily suppressed.
* Errors in converting data from DCP are not always relayed properly to the CLI.
