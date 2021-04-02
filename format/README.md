# Overview
This is the publication template for the I3S Community Standard.

Note that the files index.adoc, 0-preface.adoc, asciidoctor.css, and all files in folder _resources_ should not be modified. Please begin with file er.adoc. The file er.adoc has instructions in the form of comment. These don't need to be removed. Other files have helper texts that provide instructions.

It is very important that the names of the file er.adoc will not be changed, as the scripts to mass-convert all ERs fail! Ideally, you only name

* OGC Indexed 3d Scene Layer Format Specification.adoc (Root)
  * clause_0_front_material.adoc
  * clause_1_scope.adoc
  * clause_2_conformance.adoc
  * clause_3-references.adoc
  * clause_4_terms_and_definitions.adoc
  * clause_6_informative_text.adoc
  * clause_7_normative_text.adoc
  * clause_8_media_types.adoc

  * annex-a.adoc
  * annex-b.adoc    
  * annex-c.adoc

  * annex-history.adoc
  * annex-bibliography.adoc

# How to compile your raw files
Command for PDF output:
asciidoctor-pdf -a pdf-stylesdir=resources -a pdf-style=ogc -a pdf-fontsdir=resources/fonts -r asciidoctor-bibtex er.adoc

Command for HTML output:
asciidoctor -a stylesheet=rocket-panda.css -a stylesdir=./resources/stylesheets -r asciidoctor-bibtex er.adoc
