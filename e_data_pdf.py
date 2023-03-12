import pandas as pd
import pdfquery

from pdfquery import PDFQuery

pdf = PDFQuery('people.pdf')
pdf.load()

# CSS-like selectors
text_elements = pdf.pq('LTTextLineHorizontal')

# text extraction from the elements
text = [t.text for t in text_elements]

print(text)

pdf = pdfquery.PDFQuery('users.pdf')
pdf.load()


#PDF to XML convertion
pdf.tree.write('users.xml', pretty_print = True)
pdf

# access the data using coordinates
user_name = pdf.pq('LTTextLineHorizontal:in_bbox("68.0, 231.57, 101.990, 234.893")').text()

print(user_name)

