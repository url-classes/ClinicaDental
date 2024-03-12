let dentistas = [];

function renderizarDentistas() {
    const container = document.getElementById('dentistas-container');
    container.innerHTML = '';

    dentistas.forEach((dentista, indice) => {
        const card = document.createElement('div');
        card.classList.add('dentista-card');
        card.innerHTML = `
            <div class="imagen-asistente">
                <img src="${dentista.foto}" alt="${dentista.nombre}">
            </div>
            <p><b>Nombre:</b> ${dentista.nombre}</p>
            <p><b>Apellido:</b> ${dentista.apellido}</p>
            <p><b>Teléfono:</b> ${dentista.telefono}</p>
            <p><b>Correo electrónico:</b> ${dentista.email}</p>
            <p><b>Número de colegiado:</b> ${dentista.colegiado}</p>
            <p><b>Especialidad:</b> ${dentista.especialidad}</p>
            <button onclick="eliminarDentista(${indice})">Eliminar</button>
            <button onclick="editarDentista(${indice})">Editar</button>
        `;
        container.appendChild(card);
    });
}

function mostrarFormulario(tipo) {
    document.getElementById(`formulario-${tipo}`).classList.remove('hidden');
}

function cancelar(tipo) {
    document.getElementById(`formulario-${tipo}`).classList.add('hidden');
}

function agregarDentista() {
    const foto = document.getElementById('foto-dentista').value;
    const nombre = document.getElementById('nombre-dentista').value;
    const apellido = document.getElementById('apellido-dentista').value;
    const telefono = document.getElementById('telefono-dentista').value;
    const email = document.getElementById('email-dentista').value;
    const colegiado = document.getElementById('colegiado-dentista').value;
    const especialidad = document.getElementById('especialidad-dentista').value;

    dentistas.push({
        foto,
        nombre,
        apellido,
        telefono,
        email,
        colegiado,
        especialidad
    });

    guardarDatos('dentistas');
    renderizarDentistas();
    cancelar('dentista');
}

function eliminarDentista(indice) {
    dentistas.splice(indice, 1);

    guardarDatos('dentistas');
    renderizarDentistas();
}

function editarDentista(indice) {
    mostrarFormulario('dentista');
    document.getElementById('foto-dentista').value = dentistas[indice].foto;
    document.getElementById('nombre-dentista').value = dentistas[indice].nombre;
    document.getElementById('apellido-dentista').value = dentistas[indice].apellido;
    document.getElementById('telefono-dentista').value = dentistas[indice].telefono;
    document.getElementById('email-dentista').value = dentistas[indice].email;
    document.getElementById('colegiado-dentista').value = dentistas[indice].colegiado;
    document.getElementById('especialidad-dentista').value = dentistas[indice].especialidad;
}

function guardarDatos(tipo) {
    if (tipo === 'dentistas') {
        localStorage.setItem('dentistas', JSON.stringify(dentistas));
    }
}

function cargarDatos() {
    const datosDentistas = localStorage.getItem('dentistas');
    if (datosDentistas) {
        dentistas = JSON.parse(datosDentistas);
        renderizarDentistas();
    }
}

cargarDatos();
