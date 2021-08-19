#------------------------------------------------------
#Editar una Veterinaria en la Base de Datos
@app.route('/editar_veterinaria/<id>')
def get_contenido(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM veterinarias WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    return render_template('editar_info_veterinarias.html', contenido = data[0])


@app.route('/editar_info_veterinarias')
def editar_info_veterinarias():
    return render_template('editar_info_veterinarias.html')

    
@app.route('/update/<id>', methods = ['POST'])
def update_contenido(id):
    if request.method == 'POST': 
        departamento = request.form['departamento']
        ciudad = request.form['ciudad']        
        nombre = request.form['nombre']
        horario = request.form['horario']
        direccion = request.form['direccion']       
        telefono = request.form['telefono']
        email = request.form['email']      

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE veterinarias
        SET departamento = %s,
            ciudad = %s,         
            nombre = %s,
            horario = %s,
            direccion = %s,
            telefono = %s,
            email = %s           
        WHERE id = %s
    """, (departamento, ciudad, nombre, horario, direccion, telefono, email, [id]))
    mysql.connection.commit()
    cur.close()    
    return redirect(url_for('enl_veterinarias'))


#######################################################
#------------------------------------------------------
#Editar una Tienda en la Base de Datos
@app.route('/editar_tienda/<id>')
def get_item(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tiendas WHERE id = %s', [id])
    data = cur.fetchall()
    cur.close()
    return render_template('editar_info_tiendas.html', item = data[0])


@app.route('/editar_info_tiendas')
def editar_info_tiendas():
    return render_template('editar_info_tiendas.html')

    
@app.route('/update/<id>', methods = ['POST'])
def update_item(id):
    if request.method == 'POST': 
        departamento = request.form['departamento']
        ciudad = request.form['ciudad']        
        nombre = request.form['nombre']
        horario = request.form['horario']
        direccion = request.form['direccion']       
        telefono = request.form['telefono']
        email = request.form['email']      

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE tiendas
        SET departamento = %s,
            ciudad = %s,         
            nombre = %s,
            horario = %s,
            direccion = %s,
            telefono = %s,
            email = %s           
        WHERE id = %s
    """, (departamento, ciudad, nombre, horario, direccion, telefono, email, [id]))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('enl_tiendas'))  