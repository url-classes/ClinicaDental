// Array para almacenar los servicios
let services = ['Limpieza', 'Extracción', 'Blanqueamiento'];

// Función para agregar un nuevo servicio
function addCustomService() {
  const newServiceInput = document.getElementById('new-service-input');
  const serviceName = newServiceInput.value.trim();

  if (serviceName === '') {
    alert('Por favor ingresa un nombre de servicio válido.');
    return;
  }

  services.push(serviceName);
  renderServices();
  newServiceInput.value = ''; // Limpiar el campo de entrada
}

// Función para renderizar los botones de servicios
function renderServices() {
  const servicesContainer = document.getElementById('services-container');
  servicesContainer.innerHTML = '';

  services.forEach(service => {
    const button = document.createElement('button');
    button.classList.add('service-btn');
    button.textContent = service;
    button.onclick = function() {
      addSale(service);
    };
    servicesContainer.appendChild(button);
  });
}

// Función para simular la venta de un servicio
function addSale(serviceName) {
  alert(`Se vendió el servicio: ${serviceName}`);
}

// Renderizar los servicios iniciales
renderServices();
