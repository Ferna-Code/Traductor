
from translate import Translator

translator = Translator(from_lang='spanish', to_lang='english')

texto = input('¿ Que quieres traducir ? : ')

while texto.strip() == '': # strip() elimina espacios en blanco
   texto = input('Debe ingresar un texto para traducir : ')

respuesta = translator.translate(texto)
print(respuesta)

