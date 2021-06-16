def serialize_producto_especifico(productoE):
    return {
        'id': productoE.id,
        'nombre': productoE.nombre,
        'precio': float(productoE.precio),
        'descripcion': productoE.descripcion,
        'id_categoria': productoE.id_categoria.nombre,
        'id_marca': productoE.id_marca.nombre
    }
