#!/usr/bin/env python

from docx import *
document = opendocx("document.doc")
body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]
body.append(paragraph('Appending this.'))

