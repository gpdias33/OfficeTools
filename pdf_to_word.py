from pdf2docx import Converter

arquivo_pdf = 'Minha_Apresentacao.pdf'
arquivo_docx = 'Minha_Apresentacao.docx'

converter = Converter(arquivo_pdf)
converter.convert(arquivo_docx)
converter.close

print('done!')