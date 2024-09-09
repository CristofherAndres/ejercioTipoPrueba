from django.shortcuts import render

# Create your views here.

def miTienda(request):
    return render(request, 'clasesApp/miTienda.html')

def electronica(request):
    data = {
        'seccion': 'Electrónica',
        'productos': [
            {
            'id':1,
            'nombre': 'Smartphone',
            'descripcion': 'Teléfono inteligente con cámara de 48MP',
            'precio': '$800',
            'imagen': 'https://via.placeholder.com/150/ff0000'
            },
            {
            'id':2,
            'nombre': 'Smartwatch',
            'descripcion': 'Reloj inteligente con GPS',
            'precio': '$200',
            'imagen': 'https://via.placeholder.com/150/00ff00'
            },
            {
            'id':3,
            'nombre': 'Tablet',
            'descripcion': 'Tablet con pantalla de 10 pulgadas',
            'precio': '$500',
            'imagen': 'https://via.placeholder.com/150/0000ff'
            }
        ]
    }
    return render(request, 'clasesApp/productos.html', data)


# Aca van todos los productos dado que no tenemos una base de datos
def detalles_producto(request, id_producto):
    productos = [
        {
            'id': 1,
            'nombre': 'Smartphone',
            'descripcion': 'Teléfono inteligente con cámara de 48MP',
            'precio': '$800',
            'imagen': 'https://via.placeholder.com/150/ff0000',
            'comentarios': [
                {'usuario': 'Juan', 'comentario': 'Excelente producto'},
                {'usuario': 'Pedro', 'comentario': 'Muy buen teléfono'},
                {'usuario': 'Ana', 'comentario': 'No me gustó mucho'}
            ]
        },
        {
            'id': 2,
            'nombre': 'Smartwatch',
            'descripcion': 'Reloj inteligente con GPS',
            'precio': '$200',
            'imagen': 'https://via.placeholder.com/150/00ff00'
        },
        {
            'id': 3,
            'nombre': 'Tablet',
            'descripcion': 'Tablet con pantalla de 10 pulgadas',
            'precio': '$500',
            'imagen': 'https://via.placeholder.com/150/0000ff'
        }
    ]

    # Buscar el producto por su ID
    producto = None
    for p in productos:
        if p['id'] == id_producto:
            producto = p
            break

    if producto:
        return render(request, 'clasesApp/detallesProducto.html', {'producto': producto})
    else:
        return render(request, 'clasesApp/404.html', status=404)






