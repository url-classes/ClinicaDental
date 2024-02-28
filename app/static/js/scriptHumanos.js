// Obtener datos de trabajadores almacenados en el local storage
const trabajadores = JSON.parse(localStorage.getItem('trabajadores')) || [];

// Función para cargar los trabajadores guardados en el local storage
function cargarTrabajadores() {
  const wrapper = document.getElementById('carousel-wrapper');
  wrapper.innerHTML = '';
  
  trabajadores.forEach((trabajador, index) => {
    const card = crearCard(trabajador, index);
    wrapper.appendChild(card);
  });
}

// Función para agregar un nuevo trabajador
function agregarTrabajador() {
  const nuevoTrabajador = {
    nombre: '',
    telefono: '',
    especialidad: '',
    descripcion: '',
    foto: ''
  };
  trabajadores.push(nuevoTrabajador);
  localStorage.setItem('trabajadores', JSON.stringify(trabajadores));
  cargarTrabajadores();
}

// Función para eliminar el último trabajador
function eliminarTrabajador() {
  trabajadores.pop();
  localStorage.setItem('trabajadores', JSON.stringify(trabajadores));
  cargarTrabajadores();
}

// Función para crear una tarjeta de trabajador
function crearCard(trabajador, index) {
  const card = document.createElement('div');
  card.classList.add('card');
  card.innerHTML = `
    <img src="${trabajador.foto || 'https://via.placeholder.com/300x200.png'}" alt="Empleado ${index + 1}">
    <div class="card-content">
      <label for="file-input-${index}" class="file-label">Agregar Foto</label>
      <input type="file" id="file-input-${index}" class="file-input" accept="image/*" onchange="actualizarFoto(${index}, this)">
      <div class="form-group">
        <label for="nombre${index}">Nombre completo:</label>
        <input type="text" id="nombre${index}" value="${trabajador.nombre || ''}" onchange="actualizarTrabajador(${index}, 'nombre', this.value)">
      </div>
      <div class="form-group">
        <label for="telefono${index}">Teléfono:</label>
        <input type="text" id="telefono${index}" value="${trabajador.telefono || ''}" onchange="actualizarTrabajador(${index}, 'telefono', this.value)">
      </div>
      <div class="form-group">
        <label for="especialidad${index}">Especialidad:</label>
        <input type="text" id="especialidad${index}" value="${trabajador.especialidad || ''}" onchange="actualizarTrabajador(${index}, 'especialidad', this.value)">
      </div>
      <div class="form-group">
        <label for="descripcion${index}">Descripción:</label>
        <textarea id="descripcion${index}" onchange="actualizarTrabajador(${index}, 'descripcion', this.value)">${trabajador.descripcion || ''}</textarea>
      </div>
    </div>
  `;
  return card;
}

// Función para actualizar los datos de un trabajador
function actualizarTrabajador(index, campo, valor) {
  trabajadores[index][campo] = valor;
  localStorage.setItem('trabajadores', JSON.stringify(trabajadores));
}

// Función para actualizar la foto de un trabajador
function actualizarFoto(index, input) {
  const file = input.files[0];
  const reader = new FileReader();
  
  reader.onload = function(e) {
    const img = document.querySelector(`#carousel-wrapper .card:nth-child(${index + 1}) img`);
    img.src = e.target.result;
    trabajadores[index].foto = e.target.result;
    localStorage.setItem('trabajadores', JSON.stringify(trabajadores));
  }
  
  reader.readAsDataURL(file);
}

// Cargar trabajadores al cargar la página
cargarTrabajadores();