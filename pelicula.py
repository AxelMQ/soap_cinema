from spyne import ComplexModel, Unicode, Integer

class Pelicula(ComplexModel):
    pelicula = Unicode
    genero = Unicode
    duration = Integer
    