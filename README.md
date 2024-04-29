# ogc-i3s-community-standard

Public Repo for the development of future versions and releases of the OGC I3S Community Standard.

This repo was initially populated using content from the OGC I3S CS version 1.1 document and the Esri I3S public repo version 1.7

Please see the README.md file in the _format_ subfolder for information on the I3S document structure and publication guidance.

An automatically built draft document is available [here](https://docs.ogc.org/DRAFTS/17-014r11.html).

## Building the document

from this folder, run the following command.

`docker run -v "$(pwd)":/metanorma -v ${HOME}/.fontist/fonts/:/config/fonts metanorma/metanorma metanorma compile --agree-to-terms -t ogc -x xml,html format/17-014r11.adoc`

After building the document using docker, next add the custom license to the generated HTML document by calling the following command from the same folder.

`python3 format/add_license.py`
