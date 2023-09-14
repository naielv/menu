import requests
from pdf2image import convert_from_path

def pdf_to_png(url, filename):
    res = requests.request("GET", url).content
    with open("tmp.pdf", "wb") as f:
        f.write(res)
    images = convert_from_path('tmp.pdf')
    images[0].save(filename, 'JPEG')

pdf_to_png("https://menuak.ausolan.com/documentos/AUZOLAGUN/CAS-AUZO-IS-priv.pdf", "menu-ausolan-generico.jpg")
