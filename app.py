from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# --- CONFIGURACIÓN DE SEGURIDAD ---
app.secret_key = 'indumar_seguridad_2026'

# --- CONFIGURACIÓN DEL CORREO (EL BOT) ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True

# TUS CREDENCIALES
app.config['MAIL_USERNAME'] = 'contactoindumar@gmail.com'
app.config['MAIL_PASSWORD'] = 'ihvb xfug ixlw goeu'

mail = Mail(app)

# DATOS DE LA EMPRESA
INFO_EMPRESA = {
    'nombre': 'INDUMAR',
    'telefono': '11 3700-6960',
    'email': 'admarin74@gmail.com',
    'direccion': 'Buenos Aires, Argentina',
    'whatsapp_link': 'https://wa.me/5491137006960'
}

# --- DATOS PARA LA PÁGINA ---
# (Borramos SERVICIOS e INDUSTRIAS porque ahora los cuadros están fijos en el HTML)

STATS = [
    {'numero': 'GMP', 'texto': 'Normativas'},
    {'numero': 'ISO', 'texto': 'Certificación'},
    {'numero': 'RINA', 'texto': 'Estándares'}
]

# --- RUTAS ---

@app.route('/')
def home():
    return render_template('index.html', 
                           empresa=INFO_EMPRESA, 
                           stats=STATS)

@app.route('/proyectos')
def proyectos():
    # Genera la lista de fotos automáticamente: obra1.jpg hasta obra18.jpg
    lista_fotos = [f"obra{i}.jpg" for i in range(1, 19)]
    
    return render_template('proyectos.html', 
                           empresa=INFO_EMPRESA,
                           fotos=lista_fotos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email_cliente = request.form.get('email')
        telefono = request.form.get('telefono')
        empresa_cliente = request.form.get('empresa')
        mensaje = request.form.get('mensaje')

        msg = Message(subject=f"NUEVO CLIENTE WEB: {nombre}",
                      sender='contactoindumar@gmail.com',
                      recipients=['admarin74@gmail.com'])

        msg.body = f"""
        ------------------------------------------------------
        NUEVA CONSULTA DESDE LA WEB INDUMAR
        ------------------------------------------------------
        
        CLIENTE: {nombre}
        EMPRESA: {empresa_cliente}
        TELÉFONO: {telefono}
        EMAIL:   {email_cliente}
        
        MENSAJE:
        {mensaje}
        
        ------------------------------------------------------
        """

        try:
            mail.send(msg)
            flash('¡Mensaje enviado con éxito! Nos pondremos en contacto pronto.', 'success')
        except Exception as e:
            flash('Error al enviar. Por favor intente por WhatsApp.', 'danger')
            print(f"Error detallado: {e}")

        return redirect(url_for('contacto'))

    return render_template('contacto.html', empresa=INFO_EMPRESA)

if __name__ == '__main__':
    app.run(debug=True)