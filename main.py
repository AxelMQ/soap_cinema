from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from service import CinemaService

# Crear la aplicación SOAP
app = Application(
    [CinemaService],
    tns='cinema.soap.service',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

# Crear el servidor WSGI para manejar las solicitudes SOAP
wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP server listening on port 8000...")
    server.serve_forever()
