from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_socketio import SocketIO, send
from flask_mysqldb import MySQL, MySQLdb

import stripe 
import bcrypt


app = Flask(__name__)


#Conexión del Chat con Flask-socketio
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)


#######################################################
#------------------------------------------------------
#Registro Mascotas Base de Datos

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'peluditosdb'
mysql = MySQL(app)


#------------------------------------------------------
#Settings - Sesión mensaje Flash
app.secret_key = 'mysecretkey'


#######################################################
#------------------------------------------------------
#Sección Entrada - Login - Registro - 
@app.route('/')
def entrar():
    return render_template('secc_entrar.html')

#------------------------------------------------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        contraseña = request.form['contraseña'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT *FROM usuarios WHERE email = %s',(email,))
        user = cur.fetchone()
        cur.close()

        if len(user) > 0:
            if bcrypt.hashpw(contraseña, user['contraseña'].encode('utf-8')) == user['contraseña'].encode('utf-8'):
                session['nombre'] = user['nombre']
                session['email'] = user['email']
                return render_template('secc_principal.html')
            else:
                return "Error contraseña o usuario no registrado"  


#------------------------------------------------------
@app.route('/registro')
def registro():
    return render_template('registro.html')


@app.route('/reg_usuario', methods=['GET','POST'])
def reg_usuario():
    if request.method == 'GET':
        return render_template("registro.html")
    else:    
        nombre = request.form['nombre']     
        email = request.form['email']
        contraseña = request.form['contraseña'].encode('utf-8')
        hash_password = bcrypt.hashpw(contraseña, bcrypt.gensalt())
                         
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (nombre, email, contraseña) VALUES (%s, %s, %s)', (nombre, email, hash_password))
        mysql.connection.commit()
        cur.close()

        session['nombre'] = nombre
        session['email'] = email

        flash('Registro de Mascota Agregado con Éxito')
        return render_template('login.html')


#------------------------------------------------------      
@app.route('/recuperar')
def recuperarpass():
    return render_template('recuperarpass.html')


#######################################################
#------------------------------------------------------
#Secciones
@app.route('/principal')
def principal():   
    return render_template('secc_principal.html')  


#******************************************************
#------------------------------------------------------
##Sección Veterinarias - Registro - Edición 
@app.route('/enl_veterinarias')
def enl_veterinarias():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM veterinarias')
    data = cur.fetchall()
    cur.close()
    return render_template('enl_veterinarias.html', contenidos = data)


#------------------------------------------------------
##Insertar una Veterinaria en la Base de Datos
@app.route('/agre_veterinaria', methods=['GET','POST'])
def agre_veterinaria():
    if request.method == 'GET':     
        return render_template('agre_veterinaria.html')   
    else:  
        departamento = request.form['departamento']
        ciudad = request.form['ciudad']        
        nombre = request.form['nombre']
        horario = request.form['horario']
        direccion = request.form['direccion']       
        telefono = request.form['telefono']
        email = request.form['email']
                         
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO veterinarias (departamento, ciudad, nombre, horario, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s, %s, %s)', (departamento, ciudad, nombre, horario, direccion, telefono, email))
        mysql.connection.commit() 
        cur.close()
        return redirect(url_for('enl_veterinarias'))


#******************************************************
#------------------------------------------------------
#Enlaces Sección Principal - Tiendas
@app.route('/enl_tiendas')
def enl_tiendas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tiendas')
    data = cur.fetchall()
    cur.close()
    return render_template('enl_tiendas.html', items = data)
   

@app.route('/agre_tienda', methods=['GET','POST'])
def agre_tienda():
    if request.method == 'GET':     
        return render_template('agre_tienda.html')   
    else:  
        departamento = request.form['departamento']
        ciudad = request.form['ciudad']        
        nombre = request.form['nombre']
        horario = request.form['horario']
        direccion = request.form['direccion']       
        telefono = request.form['telefono']
        email = request.form['email']
                         
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tiendas (departamento, ciudad, nombre, horario, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s, %s, %s)', (departamento, ciudad, nombre, horario, direccion, telefono, email))
        mysql.connection.commit() 
        cur.close()
        return redirect(url_for('enl_tiendas')) 
    

#******************************************************
#------------------------------------------------------
#Enlaces Sección Principal - Noticias
@app.route('/enl_noticias')
def enl_noticias():
    return render_template('enl_noticias.html')


@app.route('/noticia_uno')
def noticia_uno():
    return render_template('noticia_uno.html')


@app.route('/noticia_dos')
def noticia_dos():
    return render_template('noticia_dos.html')


@app.route('/noticia_tres')
def noticia_tres():
    return render_template('noticia_tres.html')


@app.route('/noticia_cuatro')
def noticia_cuatro():
    return render_template('noticia_cuatro.html')


#******************************************************
#------------------------------------------------------
#Sección Mascotas - Registro - Edición - Adopción
@app.route('/mascotas')
def mascotas():
    return render_template('secc_mascotas.html')


#------------------------------------------------------
#Insertar una Mascota en la Base de Datos
@app.route('/agre_mascota', methods=['GET','POST'])
def agre_mascota():
    if request.method == 'POST':        
        estado = request.form['estado']
        departamento = request.form['departamento']
        ciudad = request.form['ciudad']
        especie = request.form['especie']
        nombre = request.form['nombre']
        tamaño = request.form['tamaño']
        peso = request.form['peso']
        color = request.form['color']
        email = request.form['email']
        telefono = request.form['telefono']
                         
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO mascotas (estado, departamento, ciudad, especie, nombre, tamaño, peso, color, email, telefono) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (estado, departamento, ciudad, especie, nombre, tamaño, peso, color, email, telefono))
        mysql.connection.commit()
        cur.close()        
        return redirect(url_for('mascotas'))

#------------------------------------------------------
#Editar una Mascota en la Base de Datos
@app.route('/editar_mascota/<id>')
def get_registro(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM mascotas WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    return render_template('editar_info_mascotas.html', registro = data[0])


@app.route('/editar_info_mascotas')
def editar_info_mascotas():
    return render_template('editar_info_mascotas.html')


@app.route('/update/<id>', methods = ['POST'])
def update_registro(id):
    if request.method == 'POST':
        estado = request.form['estado']
        departamento = request.form['departamento']
        ciudad = request.form['ciudad']
        especie = request.form['especie']
        nombre = request.form['nombre']
        tamaño = request.form['tamaño']
        peso = request.form['peso']
        color = request.form['color']
        email = request.form['email']
        telefono = request.form['telefono']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE mascotas
        SET estado = %s,
            departamento = %s,
            ciudad = %s,
            especie = %s,
            nombre = %s,
            tamaño = %s,
            peso = %s,
            color = %s,
            email = %s,
            telefono = %s
        WHERE id = %s
    """, (estado, departamento, ciudad, especie, nombre, tamaño, peso, color, email, telefono, [id]))
    mysql.connection.commit()
    cur.close()   
    return redirect(url_for('cane_canelones'))

#------------------------------------------------------ 
@app.route('/notificar_mascota')
def notificar_mascota():
    return'recibido'

#------------------------------------------------------
#Adoptar una mascotas - eliminar en la Base de Datos
@app.route('/adoptar_mascota/<id>')
def get_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM mascotas WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    return render_template('adoptar_mascota.html', registro = data[0])


@app.route('/eliminar_mascota/<id>', methods = ['GET','POST'])
def eliminar_mascota(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM mascotas WHERE id = {0}'.format(id))    
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('cane_canelones'))


#######################################################
#------------------------------------------------------
#Departamentos - Ciudades
@app.route('/departamentos')
def departamentos():
    return render_template('secc_departamentos.html')

#------------------------------------------------------
#Artigas
@app.route('/artigas')
def artigas():
    return render_template('dep_artigas.html')

@app.route('/arti_artigas')
def arti_artigas():
    return render_template('arti_artigas.html')

@app.route('/arti_bellaunion')
def arti_bellaunion():
    return render_template('arti_bellaunion.html')

#------------------------------------------------------
#Canelones
@app.route('/canelones')
def canelones():
    return render_template('dep_canelones.html')

@app.route('/cane_canelones')
def cane_canelones():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM mascotas')
    data = cur.fetchall()
    return render_template('cane_canelones.html', registros = data)
   
    
@app.route('/cane_laspiedras')
def cane_laspiedras():
    return render_template('cane_laspiedras.html')

@app.route('/cane_progreso')
def cane_progreso():
    return render_template('cane_progreso.html')

@app.route('/cane_santalucia')
def cane_santalucia():
    return render_template('cane_santalucia.html')


#------------------------------------------------------
#Cerro Largo
@app.route('/cerro_largo')
def cerro_largo():
    return render_template('dep_cerro_largo.html')


#------------------------------------------------------
#Colonia
@app.route('/colonia')
def colonia():
    return render_template('dep_colonia.html')

#------------------------------------------------------
#Durazno
@app.route('/durazno')
def durazno():
    return render_template('dep_durazno.html')


#------------------------------------------------------
#Flores
@app.route('/flores')
def flores():
    return render_template('dep_flores.html')


#------------------------------------------------------
#Florida
@app.route('/florida')
def florida():
    return render_template('dep_florida.html')


#------------------------------------------------------
#Lavalleja
@app.route('/lavalleja')
def lavalleja():
    return render_template('dep_lavalleja.html')


#------------------------------------------------------
#Maldonado
@app.route('/maldonado')
def maldonado():
    return render_template('dep_maldonado.html')


#------------------------------------------------------
#Montevideo
@app.route('/montevideo')
def montevideo():
    return render_template('dep_montevideo.html')

#Montevideo
@app.route('/monte_montevideo')
def monte_montevideo():
    return render_template('monte_montevideo.html')

#------------------------------------------------------
#Paysandú
@app.route('/paysandu')
def paysandu():
    return render_template('dep_paysandu.html')


#------------------------------------------------------
#Río Negro
@app.route('/rio_negro')
def rio_negro():
    return render_template('dep_rio_negro.html')


#------------------------------------------------------
#Rivera
@app.route('/rivera')
def rivera():
    return render_template('dep_rivera.html')


#------------------------------------------------------
#Rocha
@app.route('/rocha')
def rocha():
    return render_template('dep_rocha.html')


#------------------------------------------------------
#Salto
@app.route('/salto')
def salto():
    return render_template('dep_salto.html')


#------------------------------------------------------
#San José
@app.route('/san_jose')
def san_jose():
    return render_template('dep_san_jose.html')


#------------------------------------------------------
#Soriano
@app.route('/soriano')
def soriano():
    return render_template('dep_soriano.html')


#------------------------------------------------------
#Tacuarembó
@app.route('/tacuarembo')
def tacuarembo():
    return render_template('dep_tacuarembo.html')


#------------------------------------------------------
#Treina y Tres
@app.route('/treinta_tres')
def treinta_tres():
    return render_template('dep_treinta_tres.html')


#######################################################
#------------------------------------------------------
#Sección Donaciones
@app.route('/donaciones')
def donaciones():
    return render_template('secc_donaciones.html')

 
#######################################################
#------------------------------------------------------
#Sección Chat - Configuración módulo SocketIO
@app.route('/chat')
def chat():
    return render_template('secc_chat.html')


@socketio.on('message')
def handleMessage(msg):
    print("Message: " + msg)
    send(msg, broadcast = True)

 
#######################################################
#------------------------------------------------------
#Sección Contacto
@app.route('/contacto')
def contacto():
    return render_template('secc_contacto.html')


#######################################################
#------------------------------------------------------
#Sección Salir
@app.route('/salir')
def salir():
     return render_template('secc_entrar.html')


#######################################################
#------------------------------------------------------
if __name__ == '__main__':
    app.run(port=3000, debug=True)






















