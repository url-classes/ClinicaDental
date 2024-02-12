let imagenes = [
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
        "nombre": "Recursos Humano",
        "descripcion": "Implementado para mejorar y replantear Recursos humanos"

    },
    {
        "url": baseUrlStatic + "img/financiero.webp",
        "nombre": "Financiero",
        "descripcion": "Módulo implementado para manejar las finanzas e impuestos."

    },
]


let atras = document.getElementById('atras');
let adelante = document.getElementById('adelante');
let imagen = document.getElementById('img');
let puntos = document.getElementById('puntos');
let texto = document.getElementById('texto')
let actual = 0
posicionCarrusel()

atras.addEventListener('click', function(){
    actual -=1

    if (actual == -1){
        actual = imagenes.length - 1
    }

    imagen.innerHTML = ` <img class="img" src="${imagenes[actual].url}" alt="logo pagina" loading="lazy"></img>`
    texto.innerHTML = `
    <h3>${imagenes[actual].nombre}</h3>
    <p>${imagenes[actual].descripcion}</p>
    `
    posicionCarrusel()
})  
adelante.addEventListener('click', function(){
    actual +=1

    if (actual == imagenes.length){
        actual = 0
    }

    imagen.innerHTML = ` <img class="img" src="${imagenes[actual].url}" alt="logo pagina" loading="lazy"></img>`
    texto.innerHTML = `
    <h3>${imagenes[actual].nombre}</h3>
    <p>${imagenes[actual].descripcion}</p>
    `
    posicionCarrusel()
})  

function posicionCarrusel() {
    puntos.innerHTML = ""
    for (var i = 0; i <imagenes.length; i++){
        if(i == actual){
            puntos.innerHTML += '<p class="bold">.<p>'
        }
        else{
            puntos.innerHTML += '<p>.<p>'
        }
    } 
}