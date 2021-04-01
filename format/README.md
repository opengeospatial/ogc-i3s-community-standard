# Overview
This is the publication template for the I3S Community Standard.

Note that the files index.adoc, 0-preface.adoc, asciidoctor.css, and all files in folder _resources_ should not be modified. Please begin with file er.adoc. The file er.adoc has instructions in the form of comment. These don't need to be removed. Other files have helper texts that provide instructions.

It is very important that the names of the file er.adoc will not be changed, as the scripts to mass-convert all ERs fail! Ideally, you only name

* OGC Indexed 3d Scene Layer Format Specification.adoc (Root)
  * clause_0_front_material.adoc
  * 2-references.adoc
  * 3-terms.adoc
  * 4-overview.adoc
  * 5-example.adoc (some asciidoc syntax help. Use as many copies as you need sections in your document)

  * annex-a.adoc  --|
  * annex-b.adoc    |-- Use as needed
  * annex-c.adoc  --|

  * annex-history.adoc
  * annex-bibliography.adoc

# How to compile your raw files
Command for PDF output:
asciidoctor-pdf -a pdf-stylesdir=resources -a pdf-style=ogc -a pdf-fontsdir=resources/fonts -r asciidoctor-bibtex er.adoc

Command for HTML output:
asciidoctor -a stylesheet=rocket-panda.css -a stylesdir=./resources/stylesheets -r asciidoctor-bibtex er.adoc
