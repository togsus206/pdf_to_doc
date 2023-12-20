from pdf2docx import Converter 
from read_line import input_with_correction



try:
    pdf_file = input_with_correction("Introduzca la ruta de su archivo pdf a covertir: ")

    doc_file = input_with_correction("Introduzca el nombre de salida de su archivo: ")
    doc_file = doc_file + ".docx"
    #doc_file = "output.docx"

    cv = Converter(pdf_file)
    cv.convert(doc_file)
    cv.close()
    
except Exception as e:
            print("Hubo un problema con el archivo: \n", str(e))
            print("Asegurese de estar usando un archivo pdf")
        