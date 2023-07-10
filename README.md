# ogc-i3s-community-standard

Public Repo for the development of future versions and releases of the OGC I3S Community Standard.

This repo was initially populated using content from the OGC I3S CS version 1.1 document and the Esri I3S public repo version 1.7

Please see the README.md file in the _format_ subfolder for information on the I3S document structure and piblication guidance.


## Building the document

from this folder, run the following command.

`docker run -v "$(pwd)":/metanorma -v ${HOME}/.fontist/fonts/:/config/fonts metanorma/metanorma metanorma compile --agree-to-terms -t ogc -x xml,html format/m17-014r9.adoc`