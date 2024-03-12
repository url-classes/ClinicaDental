// JavaScript para el manejo de datos de dentistas y asistentes
let dentistas = [];
let asistentes = [];

// Funciones para renderizar la información de dentistas y asistentes
function renderizarDentistas() {
    const container = document.getElementById('dentistas-container');
    container.innerHTML = '';

    dentistas.forEach((dentista, indice) => {
        const card = document.createElement('div');
        card.classList.add('dentista-card');
        card.innerHTML = `
            <img src="${dentista.foto}" alt="${dentista.nombre}">
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

function renderizarAsistentes() {
    const container = document.getElementById('asistentes-container');
    container.innerHTML = '';

    asistentes.forEach((asistente, indice) => {
        const card = document.createElement('div');
        card.classList.add('asistente-card');
        card.innerHTML = `
            <div class="imagen-asistente">
                <img src="${asistente.foto}" alt="${asistente.nombre}">
            </div>
            <p><b>Nombre:</b> ${asistente.nombre}</p>
            <p><b>Apellido:</b> ${asistente.apellido}</p>
            <p><b>Escolaridad:</b> ${asistente.escolaridad}</p>
            <p><b>Salario:</b> ${asistente.salario}</p>
            <button onclick="eliminarAsistente(${indice})">Eliminar</button>
            <button onclick="editarAsistente(${indice})">Editar</button>
        `;
        container.appendChild(card);
    });
}

// Funciones para mostrar y ocultar el formulario de agregar dentistas y asistentes
function mostrarFormulario(tipo) {
    document.getElementById(`formulario-${tipo}`).classList.remove('hidden');
}

function cancelar(tipo) {
    document.getElementById(`formulario-${tipo}`).classList.add('hidden');
}

// Funciones para agregar, eliminar y editar dentistas
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

function agregarAsistente() {
    const foto = document.getElementById('foto-asistente').value;
    const nombre = document.getElementById('nombre-asistente').value;
    const apellido = document.getElementById('apellido-asistente').value;
    const escolaridad = document.getElementById('escolaridad-asistente').value;
    const salario = document.getElementById('salario-asistente').value;

    asistentes.push({
        foto,
        nombre,
        apellido,
        escolaridad,
        salario
    });

    guardarDatos('asistentes');
    renderizarAsistentes();
    cancelar('asistente');
}

function eliminarDentista(indice) {
    dentistas.splice(indice, 1);

    guardarDatos('dentistas');
    renderizarDentistas();
}

function eliminarAsistente(indice) {
    asistentes.splice(indice, 1);

    guardarDatos('asistentes');
    renderizarAsistentes();
}

function editarDentista(indice) {
    mostrarFormulario('dentista');
    document.getElementById('foto-dentista').value = dentistas[indice].foto;
    document.getElementById('nombre-dentista').value = dentistas[indice].nombre;
    document.getElementById('apellido-dentista').value = dentistas[indice].apellido;
    document.getElementById('telefono-dentista').value = dentistas[indice].telefono;
    document.getElementById('email-dentista').value = dentistas[indice].email;
    document.getElementById('colegiado-dentista').value = dentistas[indice].colegiado;
    document.getElementById('especialidad-dentista').value = dentistas[indice].especialidad
}

function editarAsistente(indice) {
    mostrarFormulario('asistente');
    document.getElementById('foto-asistente').value = asistentes[indice].foto;
    document.getElementById('nombre-asistente').value = asistentes[indice].nombre;
    document.getElementById('apellido-asistente').value = asistentes[indice].apellido;
    document.getElementById('escolaridad-asistente').value = asistentes[indice].escolaridad;
    document.getElementById('salario-asistente').value = asistentes[indice].salario;
}

// Función para guardar datos en el almacenamiento local
function guardarDatos(tipo) {
    if (tipo === 'dentistas') {
        localStorage.setItem('dentistas', JSON.stringify(dentistas));
    } else if (tipo === 'asistentes') {
        localStorage.setItem('asistentes', JSON.stringify(asistentes));
    }
}

// Función para cargar datos desde el almacenamiento local al cargar la página
function cargarDatos() {
    const datosDentistas = localStorage.getItem('dentistas');
    if (datosDentistas) {
        dentistas = JSON.parse(datosDentistas);
        renderizarDentistas();
    }

    const datosAsistentes = localStorage.getItem('asistentes');
    if (datosAsistentes) {
        asistentes = JSON.parse(datosAsistentes);
        renderizarAsistentes();
    }
}

// Llamar a la función cargarDatos al cargar la página
cargarDatos();
