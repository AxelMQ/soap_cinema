from spyne import ServiceBase, rpc, Array, Unicode, Integer
from pelicula import Pelicula

# Inicializar la cartelera 
cartelera = [
    Pelicula(pelicula="Harry potter", genero="fantasia", duration=160),
    Pelicula(pelicula="Parasito", genero="drama", duration=130),
    Pelicula(pelicula="DeadPool", genero="super heroe", duration=70),
    Pelicula(pelicula="Coraline", genero="fantasia", duration=100)
]

class CinemaService(ServiceBase):
    @rpc(_returns=Array(Pelicula))
    def getCartelera(ctx):
        return cartelera
    
    @rpc(Unicode, _returns=Pelicula)
    def getPelicula(ctx, pelicula_name):
        for pelicula in cartelera:
            if pelicula.pelicula == pelicula_name:
                return pelicula
        return None

    @rpc(Pelicula, _returns=Unicode)
    def addPelicula(ctx, new_pelicula):
        cartelera.append(new_pelicula)
        return f"{new_pelicula.pelicula} added successfully."

    @rpc(Unicode, Unicode, Integer, _returns=Unicode)
    def updatePelicula(ctx, pelicula_name, genero, duration):
        for pelicula in cartelera:
            if pelicula.pelicula == pelicula_name:
                pelicula.genero = genero
                pelicula.duration = duration
                return f"{pelicula_name} updated successfully."
        return f"{pelicula_name} not found."

    @rpc(Unicode, _returns=Unicode)
    def deletePelicula(ctx, pelicula_name):
        global cartelera
        cartelera = [pelicula for pelicula in cartelera if pelicula.pelicula != pelicula_name]
        return f"{pelicula_name} deleted successfully."
