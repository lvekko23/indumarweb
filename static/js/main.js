// 1. EL ARRAY DE DATOS (Con las rutas corregidas)
const servicios = [
  {
    titulo: "Instalaciones Industriales",
    descripcion: "Montaje de cañerías de servicios (vapor, aire, agua), soportería y estructuras metálicas en planta.",
    img: "/static/img/instalaciones-industriales.jpg",
    link: "#"
  },
  {
    titulo: "Circuitos CIP",
    descripcion: "Fabricación y montaje de Skids de limpieza CIP. Soldadura orbital y cañerías de acero inoxidable.",
    img: "/static/img/circuitos-cip.jpg",
    link: "#"
  },
  {
    titulo: "Tratamiento de Agua",
    descripcion: "Montaje electromecánico de plantas de tratamiento. Interconexión de tanques y bombas.",
    img: "/static/img/tratamiento-agua.jpg",
    link: "#"
  },
  {
    titulo: "Plantas de Ósmosis",
    descripcion: "Ingeniería, montaje y puesta en marcha de sistemas de ósmosis inversa.",
    img: "/static/img/plantas-osmosis.jpg",
    link: "#"
  },
  {
    titulo: "Montaje de Plantas Nuevas",
    descripcion: "Ejecución integral de proyectos de montaje para nuevas líneas de producción.",
    img: "/static/img/montaje-plantas-nuevas.jpg",
    link: "#"
  }
];

// 2. LA FUNCIÓN QUE DIBUJA LAS TARJETAS EN EL HTML
const contenedor = document.getElementById('contenedor-servicios');

if (contenedor) {
    let htmlContent = '';

    servicios.forEach(servicio => {
        htmlContent += `
            <div class="card">
                <div class="card-img-container">
                    <img src="${servicio.img}" alt="${servicio.titulo}">
                </div>
                <div class="card-body">
                    <h3>${servicio.titulo}</h3>
                    <p>${servicio.descripcion}</p>
                    <a href="${servicio.link}" class="btn-detalles">MÁS DETALLES</a>
                </div>
            </div>
        `;
    });

    contenedor.innerHTML = htmlContent;
} else {
    console.error('No se encontró el elemento con id "contenedor-servicios"');
}