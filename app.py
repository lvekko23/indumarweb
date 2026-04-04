from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# --- CONFIGURACIÓN DE SEGURIDAD ---
app.secret_key = 'indumar_seguridad_2026'

# --- CONFIGURACIÓN DEL CORREO (EL BOT) ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
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

STATS = [
    {'numero': 'GMP', 'texto': 'Normativas'},
    {'numero': 'ISO', 'texto': 'Certificación'},
    {'numero': 'RINA', 'texto': 'Estándares'}
]

# --- RUTAS ---

@app.route('/')
def home():
    return render_template('index.html', empresa=INFO_EMPRESA, stats=STATS)

# --- LAS 3 RUTAS DE GALERÍAS (CON FORMATO WINDOWS) ---

@app.route('/farmaceuticas')
def farma():
    # Busca 15 fotos: farma (1).jpg hasta farma (15).jpg
    fotos = [f"farma ({i}).jpg" for i in range(1, 16)] 
    return render_template('galeria.html', empresa=INFO_EMPRESA, sector="Farmacéuticas", fotos=fotos)

@app.route('/alimenticias')
def alimen():
    # Busca 15 fotos: alimen (1).jpg hasta alimen (15).jpg
    fotos = [f"alimen ({i}).jpg" for i in range(1, 16)]
    return render_template('galeria.html', empresa=INFO_EMPRESA, sector="Alimenticias", fotos=fotos)

@app.route('/naval')
def naval():
    # Busca 55 fotos: naval (1).jpg hasta naval (55).jpg
    fotos = [f"naval ({i}).jpg" for i in range(1, 56)]
    return render_template('galeria.html', empresa=INFO_EMPRESA, sector="Naval", fotos=fotos)

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