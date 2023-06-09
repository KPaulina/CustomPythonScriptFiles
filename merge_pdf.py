from PyPDF2 import PdfMerger
from natsort import os_sorted
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

merger = PdfMerger()
pdfs = os_sorted(os.listdir(DATA_DIR))

print(pdfs)

for file in pdfs:
    merger.append(DATA_DIR + "\\" + file)

merger.write("data.pdf")
merger.close()
