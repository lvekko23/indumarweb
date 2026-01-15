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
SERVICIOS = [
    {'titulo': 'Instalaciones Industriales', 'desc': 'Montaje de cañerías de acero inoxidable y carbono para procesos críticos.', 'img': '/static/taller.jpg'},
    {'titulo': 'Circuitos CIP', 'desc': 'Skids de limpieza automatizada para industrias alimenticias y farmacéuticas.', 'img': '/static/cip.jpg'},
    {'titulo': 'Tratamiento de Agua', 'desc': 'Plantas de tratamiento, osmosis inversa y ablandadores industriales.', 'img': '/static/agua.jpg'},
    {'titulo': 'Industrias Farmacéuticas', 'desc': 'Normativas GMP/FDA. Soldaduras sanitarias y documentación técnica.', 'img': '/static/farma.jpg'},
    {'titulo': 'Fabricación y Soldadura', 'desc': 'Soldaduras especiales TIG/MIG en taller propio y montajes en planta.', 'img': '/static/instalaciones.jpg'},
    {'titulo': 'Pre-montajes', 'desc': 'Modularidad y pre-fabricación en taller para reducir tiempos en obra.', 'img': '/static/premontaje.jpg'}
]

STATS = [
    {'numero': 'GMP', 'texto': 'Normativas'},
    {'numero': '24/7', 'texto': 'Soporte'},
    {'numero': '100%', 'texto': 'Calidad'}
]

INDUSTRIAS = [
    {'nombre': 'Alimenticia', 'icono': 'fa-utensils', 'desc': 'Lácteos, bebidas y procesados.'},
    {'nombre': 'Farmacéutica', 'icono': 'fa-pills', 'desc': 'Laboratorios y cosmética.'},
    {'nombre': 'Química', 'icono': 'fa-flask', 'desc': 'Reactores y fluidos peligrosos.'},
    {'nombre': 'Naval', 'icono': 'fa-anchor', 'desc': 'Reparaciones y montajes a bordo.'},
    {'nombre': 'Petróleo', 'icono': 'fa-oil-well', 'desc': 'Redes de incendio y piping.'},
    {'nombre': 'Civil', 'icono': 'fa-building', 'desc': 'Estructuras metálicas y naves.'}
]

# --- RUTAS ---

@app.route('/')
def home():
    return render_template('index.html', 
                           empresa=INFO_EMPRESA, 
                           servicios=SERVICIOS, 
                           stats=STATS, 
                           industrias=INDUSTRIAS)

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
        asunto = request.form.get('asunto')
        mensaje = request.form.get('mensaje')

        msg = Message(subject=f"NUEVO CLIENTE WEB: {asunto}",
                      sender='contactoindumar@gmail.com',
                      recipients=['admarin74@gmail.com'])

        msg.body = f"""
        ------------------------------------------------------
        NUEVA CONSULTA DESDE LA WEB INDUMAR
        ------------------------------------------------------
        
        CLIENTE: {nombre}
        EMAIL:   {email_cliente}
        ASUNTO:  {asunto}
        
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