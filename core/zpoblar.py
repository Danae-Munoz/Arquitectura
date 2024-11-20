import sqlite3
from django.contrib.auth.models import User, Permission
from django.db import connection
from datetime import date, timedelta
from random import randint
from core.models import Categoria, Producto, Carrito, Perfil, Boleta, DetalleBoleta, Bodega

def eliminar_tabla(nombre_tabla):
    conexion = sqlite3.connect('db.sqlite3')
    cursor = conexion.cursor()
    cursor.execute(f"DELETE FROM {nombre_tabla}")
    conexion.commit()
    conexion.close()

def exec_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

def crear_usuario(username, tipo, nombre, apellido, correo, es_superusuario, 
    es_staff, rut, direccion, subscrito, imagen):

    try:
        print(f'Verificar si existe usuario {username}.')

        if User.objects.filter(username=username).exists():
            print(f'   Eliminar {username}')
            User.objects.get(username=username).delete()
            print(f'   Eliminado {username}')
        
        print(f'Iniciando creación de usuario {username}.')

        usuario = None
        if tipo == 'Superusuario':
            print('    Crear Superuser')
            usuario = User.objects.create_superuser(username=username, password='123')
        else:
            print('    Crear User')
            usuario = User.objects.create_user(username=username, password='123')

        if tipo == 'Administrador':
            print('    Es administrador')
            usuario.is_staff = es_staff
            
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo
        usuario.save()

        if tipo == 'Administrador':
            print(f'    Dar permisos a core y apirest')
            permisos = Permission.objects.filter(content_type__app_label__in=['core', 'apirest'])
            usuario.user_permissions.set(permisos)
            usuario.save()
 
        print(f'    Crear perfil: RUT {rut}, Subscrito {subscrito}, Imagen {imagen}')
        Perfil.objects.create(
            usuario=usuario, 
            tipo_usuario=tipo,
            rut=rut,
            direccion=direccion,
            subscrito=subscrito,
            imagen=imagen)
        print("    Creado correctamente")
    except Exception as err:
        print(f"    Error: {err}")

def eliminar_tablas():
    eliminar_tabla('auth_user_groups')
    eliminar_tabla('auth_user_user_permissions')
    eliminar_tabla('auth_group_permissions')
    eliminar_tabla('auth_group')
    eliminar_tabla('auth_permission')
    eliminar_tabla('django_admin_log')
    eliminar_tabla('django_content_type')
    #eliminar_tabla('django_migrations')
    eliminar_tabla('django_session')
    eliminar_tabla('Bodega')
    eliminar_tabla('DetalleBoleta')
    eliminar_tabla('Boleta')
    eliminar_tabla('Perfil')
    eliminar_tabla('Carrito')
    eliminar_tabla('Producto')
    eliminar_tabla('Categoria')
    #eliminar_tabla('authtoken_token')
    eliminar_tabla('auth_user')

def poblar_bd(test_user_email=''):
    eliminar_tablas()
    
    crear_usuario(
        username='nzamora',
        tipo='Cliente', 
        nombre='Nicolas', 
        apellido='Zamora', 
        correo=test_user_email if test_user_email else 'nic.zamora@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='20612698-1',	
        direccion='5121 Esopo, Pedro Aguirre Cerda, \nSantiago 82000 \nChile', 
        subscrito=True, 
        imagen='perfiles/niczam.jpg'
    )

    crear_usuario(
        username='d.munoz',
        tipo='Cliente', 
        nombre='Danae', 
        apellido='Munoz', 
        correo=test_user_email if test_user_email else 'd.munozo@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='234779295',	
        direccion='233 La Victoria, Villa Sur, \nSantiago 2431 \nChile', 
        subscrito=True, 
        imagen='perfiles/dmunozo.png'
    )

    crear_usuario(
        username='tleithon',
        tipo='Cliente', 
        nombre='Tom', 
        apellido='Leithon', 
        correo=test_user_email if test_user_email else 't.leithon@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='22319199-k',	
        direccion='102 Renca, Colina, \nSantiago 232 101 \nChile', 
        subscrito=True, 
        imagen='perfiles/tleithon.jpg'
    )

    crear_usuario(
        username='czamora',
        tipo='Cliente', 
        nombre='Claudia', 
        apellido='Zamora', 
        correo=test_user_email if test_user_email else 'c.zamora@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='24870967-7',	
        direccion='202 Pudahuel, Laguna Sur, \nSantiago 40202 \nChile', 
        subscrito=True, 
        imagen='perfiles/czamora.jpg'
    )

    crear_usuario(
        username='mnavarro',
        tipo='Cliente', 
        nombre='Michael.', 
        apellido='Navarro', 
        correo=test_user_email if test_user_email else 'mnavarro@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='20723447-8',	
        direccion='303 Villa  Sur, Pedro Aguirre Cerda, \nSantiago 90001 \nChile', 
        subscrito=True, 
        imagen='perfiles/mnavarro.jpg'
    )

    crear_usuario(
        username='amunoz',
        tipo='Cliente', 
        nombre='Ana', 
        apellido='Munoz', 
        correo=test_user_email if test_user_email else 'a.munoz@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='18240323-7',	
        direccion='503 Maipu, El monte, \nSantiago 61000 \nChile', 
        subscrito=True, 
        imagen='perfiles/amunoz.jpg'
    )
    #----------

    crear_usuario(
        username='eperez',
        tipo='Cliente', 
        nombre='Evaristo', 
        apellido='Perez', 
        correo=test_user_email if test_user_email else 'eperez@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='25.747.200-0',	
        direccion='223 Las Condes, Providencia, \nSantiago 61000 \nChile', 
        subscrito=True, 
        imagen='perfiles/eperez.jpg')

    crear_usuario(
        username='mferrada',
        tipo='Cliente', 
        nombre='Matias', 
        apellido='Ferrada', 
        correo=test_user_email if test_user_email else 'm.ferrada@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='20.202.357-5', 
        direccion='Las Lilas, PAC, \nSantiago 10001 \nChile', 
        subscrito=True, 
        imagen='perfiles/mferrada.jpg')

    crear_usuario(
        username='ccontreras',
        tipo='Cliente', 
        nombre='Camilo', 
        apellido='Contreras', 
        correo=test_user_email if test_user_email else 'ccontreras@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='11.991.600-3', 
        direccion='San Jose de la Estrella, Puente Alto, \nSantiago, 95014 \nChile', 
        subscrito=False, 
        imagen='perfiles/ccontreras.jpg')

    crear_usuario(
        username='amontalva',
        tipo='Cliente', 
        nombre='Antonia', 
        apellido='Montalva', 
        correo=test_user_email if test_user_email else 'amontalva@duocuc.cl', 
        es_superusuario=False, 
        es_staff=False, 
        rut='16.469.725-8', 
        direccion='San Miguel 5th Avenida, \nSantiago, 10118 \nChile', 
        subscrito=False, 
        imagen='perfiles/amontalva.jpg')

    crear_usuario(
        username='rgonzalez',
        tipo='Administrador', 
        nombre='Rodrigro', 
        apellido='Gonzalez', 
        correo=test_user_email if test_user_email else 'rgonzalez@duocuc.cl', 
        es_superusuario=False, 
        es_staff=True, 
        rut='19.441.980-5', 
        direccion='San Felipe 5323, \nValparaiso 33101 \nChile', 
        subscrito=False, 
        imagen='perfiles/rgonzalez.jpg')
    
    crear_usuario(
        username='cmartinez',
        tipo='Administrador', 
        nombre='Cesar', 
        apellido='Martinez', 
        correo=test_user_email if test_user_email else 'cmartinez@duocuc.cl', 
        es_superusuario=False, 
        es_staff=True, 
        rut='21.708.052-3', 
        direccion='Peñaflor 5422, \nSantiago \nChile', 
        subscrito=False, 
        imagen='perfiles/cmartinez.jpg')

    crear_usuario(
        username='super',
        tipo='Superusuario',
        nombre='Sol',
        apellido='Martinez',
        correo=test_user_email if test_user_email else 'smartinez@duocuc.cl',
        es_superusuario=True,
        es_staff=True,
        rut='13.029.317-4',
        direccion='Peñaflor 5422, \nSantiago \nChile',
        subscrito=False,
        imagen='perfiles/smartinez.jpg')
    
    categorias_data = [
        {'id': 1, 'nombre': 'Consulta General'},
        {'id': 2, 'nombre': 'Consulta Cardiológica'},
        {'id': 3, 'nombre': 'Exámenes de Laboratorio'},
        {'id': 4, 'nombre': 'Consulta Pediátrica'}
    ]

    print('Crear categorías')
    for categoria in categorias_data:
        Categoria.objects.create(**categoria)
    print('Categorías creadas correctamente')

    productos_data = [
    # Categoría "Consultas Médicas" (5 productos)
    {
        'id': 1,
        'categoria': Categoria.objects.get(id=1),  # Consulta Pediatría
        'nombre': 'Consulta Pediátrica',
        'descripcion': 'Consulta médica especializada para niños, donde se evalúa el desarrollo físico y emocional, se realizan exámenes básicos y se brindan recomendaciones de salud.',
        'precio': 39990,
        'descuento_subscriptor': 10,
        'descuento_oferta': 15,
        'imagen': 'productos/consulta_pediatria.jpg'
    },
    {
        'id': 2,
        'categoria': Categoria.objects.get(id=1),  # Consulta Ginecológica
        'nombre': 'Consulta Ginecológica',
        'descripcion': 'Examen ginecológico completo, incluyendo revisión de salud reproductiva y diagnóstico preventivo de enfermedades ginecológicas.',
        'precio': 49990,
        'descuento_subscriptor': 10,
        'descuento_oferta': 20,
        'imagen': 'productos/consulta_ginecologica.jpg'
    },
    {
        'id': 3,
        'categoria': Categoria.objects.get(id=1),  # Consulta Cardiología
        'nombre': 'Consulta Cardiológica',
        'descripcion': 'Evaluación del sistema cardiovascular, incluye chequeo del corazón y recomendaciones para mantener una vida saludable.',
        'precio': 69990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 10,
        'imagen': 'productos/consulta_cardiologia.jpg'
    },
    {
        'id': 4,
        'categoria': Categoria.objects.get(id=1),  # Consulta Oftalmológica
        'nombre': 'Consulta Oftalmológica',
        'descripcion': 'Revisión completa de la vista, detección de problemas oculares y prescripción de lentes si es necesario.',
        'precio': 49990,
        'descuento_subscriptor': 10,
        'descuento_oferta': 15,
        'imagen': 'productos/consulta_oftalmologica.jpg'
    },
    {
        'id': 5,
        'categoria': Categoria.objects.get(id=1),  # Consulta Medicina General
        'nombre': 'Consulta Medicina General',
        'descripcion': 'Examen físico general, diagnóstico de enfermedades comunes y consejos de prevención de salud.',
        'precio': 29990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 10,
        'imagen': 'productos/consulta_medico_general.jpg'
    },
    # Categoría "Servicios de Salud" (5 productos)
    {
        'id': 6,
        'categoria': Categoria.objects.get(id=2),  # Examen de Laboratorio
        'nombre': 'Examen de Laboratorio',
        'descripcion': 'Exámenes médicos de laboratorio para análisis de sangre, orina y otros parámetros para detectar posibles enfermedades.',
        'precio': 19990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 10,
        'imagen': 'productos/examen_laboratorio.jpg'
    },
    {
        'id': 7,
        'categoria': Categoria.objects.get(id=2),  # Radiografía
        'nombre': 'Radiografía',
        'descripcion': 'Estudio radiológico para diagnóstico de fracturas, enfermedades óseas o problemas pulmonares.',
        'precio': 24990,
        'descuento_subscriptor': 10,
        'descuento_oferta': 15,
        'imagen': 'productos/radiografia.jpg'
    },
    {
        'id': 8,
        'categoria': Categoria.objects.get(id=2),  # Ecografía
        'nombre': 'Ecografía',
        'descripcion': 'Examen no invasivo que utiliza ondas sonoras para examinar órganos internos, como el abdomen, los riñones, y el embarazo.',
        'precio': 39990,
        'descuento_subscriptor': 10,
        'descuento_oferta': 20,
        'imagen': 'productos/ecografia.jpg'
    },
    {
        'id': 9,
        'categoria': Categoria.objects.get(id=2),  # Electrocardiograma
        'nombre': 'Electrocardiograma (ECG)',
        'descripcion': 'Prueba diagnóstica para medir la actividad eléctrica del corazón, ayudando a detectar arritmias y otros problemas cardíacos.',
        'precio': 29990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 10,
        'imagen': 'productos/electrocardiograma.jpg'
    },
    {
        'id': 10,
        'categoria': Categoria.objects.get(id=2),  # Terapia Física
        'nombre': 'Sesión de Terapia Física',
        'descripcion': 'Tratamientos de rehabilitación para aliviar dolor muscular, mejorar la movilidad y restaurar la funcionalidad física.',
        'precio': 39990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 10,
        'imagen': 'productos/terapia_fisica.jpg'
    },
    # Categoría "Bienestar y Cuidado Personal" (5 productos)
    {
        'id': 11,
        'categoria': Categoria.objects.get(id=3),  # Suplemento Vitaminico
        'nombre': 'Suplemento Multivitamínico',
        'descripcion': 'Suplemento nutricional que proporciona vitaminas y minerales esenciales para fortalecer el sistema inmune y mejorar la salud general.',
        'precio': 15990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 10,
        'imagen': 'productos/suplemento_multivitaminico.jpg'
    },
    {
        'id': 12,
        'categoria': Categoria.objects.get(id=3),  # Aceite Esencial
        'nombre': 'Aceite Esencial de Lavanda',
        'descripcion': 'Aceite esencial utilizado para reducir el estrés, mejorar el sueño y aliviar dolores musculares mediante aromaterapia.',
        'precio': 29990,
        'descuento_subscriptor': 10,
        'descuento_oferta': 15,
        'imagen': 'productos/aceite_esencial_lavanda.jpg'
    },
    {
        'id': 13,
        'categoria': Categoria.objects.get(id=3),  # Masaje Terapéutico
        'nombre': 'Sesión de Masaje Terapéutico',
        'descripcion': 'Masaje especializado para aliviar tensiones musculares, mejorar la circulación y reducir el estrés.',
        'precio': 49990,
        'descuento_subscriptor': 10,
        'descuento_oferta': 20,
        'imagen': 'productos/masaje_terapeutico.jpg'
    },
    {
        'id': 14,
        'categoria': Categoria.objects.get(id=3),  # Tratamiento Facial
        'nombre': 'Tratamiento Facial Antiedad',
        'descripcion': 'Tratamiento estético facial para prevenir el envejecimiento, hidratar la piel y mejorar la apariencia del rostro.',
        'precio': 69990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 15,
        'imagen': 'productos/tratamiento_facial.jpg'
    },
    {
        'id': 15,
        'categoria': Categoria.objects.get(id=3),  # Terapia Psicológica
        'nombre': 'Sesión de Terapia Psicológica',
        'descripcion': 'Consulta psicológica con un profesional para tratar temas de ansiedad, depresión, estrés y otros trastornos emocionales.',
        'precio': 79990,
        'descuento_subscriptor': 5,
        'descuento_oferta': 10,
        'imagen': 'productos/terapia_psicologica.jpg'
    },
]

    print('Crear productos')
    for producto in productos_data:
        Producto.objects.create(**producto)
    print('Productos creados correctamente')

    print('Crear carritos')
    for rut in ['25.747.200-0', '11.991.600-3']:
        cliente = Perfil.objects.get(rut=rut)
        for cantidad_productos in range(1, 11):
            producto = Producto.objects.get(pk=randint(1, 10))
            if cliente.subscrito:
                descuento_subscriptor = producto.descuento_subscriptor
            else:
                descuento_subscriptor = 0
            descuento_oferta = producto.descuento_oferta
            descuento_total = descuento_subscriptor + descuento_oferta
            descuentos = int(round(producto.precio * descuento_total / 100))
            precio_a_pagar = producto.precio - descuentos
            Carrito.objects.create(
                cliente=cliente,
                producto=producto,
                precio=producto.precio,
                descuento_subscriptor=descuento_subscriptor,
                descuento_oferta=descuento_oferta,
                descuento_total=descuento_total,
                descuentos=descuentos,
                precio_a_pagar=precio_a_pagar
            )
    print('Carritos creados correctamente')

    print('Crear boletas')
    nro_boleta = 0
    perfiles_cliente = Perfil.objects.filter(tipo_usuario='Cliente')
    for cliente in perfiles_cliente:
        estado_index = -1
        for cant_boletas in range(1, randint(6, 21)):
            nro_boleta += 1
            estado_index += 1
            if estado_index > 3:
                estado_index = 0
            estado = Boleta.ESTADO_CHOICES[estado_index][1]
            fecha_venta = date(2023, randint(1, 5), randint(1, 28))
            fecha_despacho = fecha_venta + timedelta(days=randint(0, 3))
            fecha_entrega = fecha_despacho + timedelta(days=randint(0, 3))
            if estado == 'Anulado':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'En espera':
                fecha_despacho = None
                fecha_entrega = None
            elif estado == 'Atendido':
                fecha_entrega = None
            boleta = Boleta.objects.create(
                nro_boleta=nro_boleta, 
                cliente=cliente,
                monto_sin_iva=0,
                iva=0,
                total_a_pagar=0,
                fecha_venta=fecha_venta,
                fecha_despacho=fecha_despacho,
                fecha_entrega=fecha_entrega,
                estado=estado)
            detalle_boleta = []
            total_a_pagar = 0
            for cant_productos in range(1, randint(4, 6)):
                producto_id = randint(1, 10)
                producto = Producto.objects.get(id=producto_id)
                precio = producto.precio
                descuento_subscriptor = 0
                if cliente.subscrito:
                    descuento_subscriptor = producto.descuento_subscriptor
                descuento_oferta = producto.descuento_oferta
                descuento_total = descuento_subscriptor + descuento_oferta
                descuentos = int(round(precio * descuento_total / 100))
                precio_a_pagar = precio - descuentos
                bodega = Bodega.objects.create(producto=producto)
                DetalleBoleta.objects.create(
                    boleta=boleta,
                    bodega=bodega,
                    precio=precio,
                    descuento_subscriptor=descuento_subscriptor,
                    descuento_oferta=descuento_oferta,
                    descuento_total=descuento_total,
                    descuentos=descuentos,
                    precio_a_pagar=precio_a_pagar)
                total_a_pagar += precio_a_pagar
            monto_sin_iva = int(round(total_a_pagar / 1.19))
            iva = total_a_pagar - monto_sin_iva
            boleta.monto_sin_iva = monto_sin_iva
            boleta.iva = iva
            boleta.total_a_pagar = total_a_pagar
            boleta.fecha_venta = fecha_venta
            boleta.fecha_despacho = fecha_despacho
            boleta.fecha_entrega = fecha_entrega
            boleta.estado = estado
            boleta.save()
            print(f'    Creada boleta Nro={nro_boleta} Cliente={cliente.usuario.first_name} {cliente.usuario.last_name}')
    print('Boletas creadas correctamente')

    print('Agregar productos a bodega')
    for producto_id in range(1, 11):
        producto = Producto.objects.get(id=producto_id)
        cantidad = 0
        for cantidad in range(1, randint(2, 31)):
            Bodega.objects.create(producto=producto)
        print(f'    Agregados {cantidad} "{producto.nombre}" a la bodega')
    print('Productos agregados a bodega')

    

