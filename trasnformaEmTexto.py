import PyPDF2
import urllib.request
import io

links = ["http://www.editais.ufu.br/sites/editais.ufu.br/files/VAGA%20PARA%20EST%C3%81GIO%20RECEP%C3%87%C3%83O%20-%20COMFORT%20HOTEL_0.pdf", "http://www.editais.ufu.br/sites/editais.ufu.br/files/Programa%20Trainee%20BURGER%20KING%202018.pdf", "http://www.editais.ufu.br/sites/editais.ufu.br/files/Abertura%20de%20vaga%20para%20est%C3%A1gio%20NCE.pdf"]


def transformaEmTexto(entrada):
    i = len(entrada)
    retorno = {}
    for i in range(0, i):
        url = entrada[i]
        remote_file = urllib.request.urlopen(url).read()
        memory_file = io.BytesIO(remote_file)

        read_pdf = PyPDF2.PdfFileReader(memory_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        retorno[i] = page_content.encode('utf-8')
        i-1
    return retorno


transformaEmTexto(links)
