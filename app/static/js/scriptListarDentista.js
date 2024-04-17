function guardarImagen() {
    const archivo = document.getElementById('imagen').files[0];
    const lector = new FileReader();

    lector.onload = function(evento) {
        const imagen = new Image();
        imagen.src = evento.target.result;

        imagen.onload = function() {
            const anchoMaximo = 300; // Tamaño máximo para adaptar la imagen
            const proporcion = anchoMaximo / imagen.width;
            const alto = imagen.height * proporcion;
            const canvas = document.createElement('canvas');
            canvas.width = anchoMaximo;
            canvas.height = alto;
            const contexto = canvas.getContext('2d');
            contexto.drawImage(imagen, 0, 0, anchoMaximo, alto);

            const datosImagen = {
                nombre: archivo.name,
                tipo: archivo.type,
                tamaño: archivo.size,
                datos: canvas.toDataURL('image/jpeg') // Convertir la imagen a base64
            };

            // Guardar datosImagen en el almacenamiento local o en un servidor
            localStorage.setItem('imagen', JSON.stringify(datosImagen));
            console.log('Imagen guardada localmente:', datosImagen);
        };
    };

    lector.readAsDataURL(archivo);
}

// Cargar la imagen desde el almacenamiento local
const datosGuardados = localStorage.getItem('imagen');
if (datosGuardados) {
    const datosImagen = JSON.parse(datosGuardados);
    const imagenCargada = new Image();
    imagenCargada.src = datosImagen.datos;
    document.body.appendChild(imagenCargada);
}
