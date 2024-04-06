const imagenes = [
    {
        "url": baseUrlStatic + "img/inventario.webp",
        "nombre": "Inventario",
        "descripcion": "Creado para controlar el manejo de material e instrumentos en la clínica"
    },
    {
        "url": baseUrlStatic + "img/Ventas.webp",
        "nombre": "Ventas",
        "descripcion": "Optimizar los procesos que conlleva el brindar un servicio."
    },
    {
        "url": baseUrlStatic + "img/rh.webp",
        "nombre": "Recursos Humanos",
        "descripcion": "Implementado para mejorar y replantear Recursos humanos"
    },
    {
        "url": baseUrlStatic + "img/financiero.webp",
        "nombre": "Financiero",
        "descripcion": "Módulo implementado para manejar las finanzas e impuestos."
    }
];

const atrasBtn = document.getElementById('atras');
const adelanteBtn = document.getElementById('adelante');
const imagenElement = document.getElementById('img');
const puntosElement = document.getElementById('puntos');
const textoElement = document.getElementById('texto');
let actualIndex = 0;

atrasBtn.addEventListener('click', function() {
    cambiarImagen(-1);
});

adelanteBtn.addEventListener('click', function() {
    cambiarImagen(1);
});

function cambiarImagen(delta) {
    actualIndex = (actualIndex + delta + imagenes.length) % imagenes.length;
    const imagen = imagenes[actualIndex];
    
    imagenElement.src = imagen.url;
    textoElement.innerHTML = `<h3>${imagen.nombre}</h3><p>${imagen.descripcion}</p>`;
    actualizarPuntos();
}

function actualizarPuntos() {
    puntosElement.innerHTML = imagenes.map((_, index) => {
        return `<p${index === actualIndex ? ' class="bold"' : ''}>.</p>`;
    }).join('');
}

// Mostrar la primera imagen al cargar la página
cambiarImagen(0);
