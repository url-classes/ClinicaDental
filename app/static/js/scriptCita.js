// Ensuring global access to currentMonth and currentYear
var currentMonth = new Date().getMonth();
var currentYear = new Date().getFullYear();
var citas = []; // Ensure this is filled with your data as needed

function createCalendar(citas) {
    const calendarElement = document.getElementById('calendar');
    const currentMonthYear = document.getElementById('currentMonthYear');
    const date = new Date(currentYear, currentMonth, 1);
    const firstDayIndex = date.getDay();
    const lastDay = new Date(currentYear, currentMonth + 1, 0).getDate();
    const monthNames = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"];

    // Update the current month and year display
    currentMonthYear.textContent = `${monthNames[currentMonth]} ${currentYear}`;

    // Start building the calendar HTML
    let calendarHtml = '<table><tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr><tr>';

    // Fill in the blank days until the first day of the month
    for (let i = 0; i < firstDayIndex; i++) {
        calendarHtml += '<td></td>';
    }

    // Fill each day into the calendar
    for (let day = 1; day <= lastDay; day++) {
        const currentDateString = new Date(currentYear, currentMonth, day).toISOString().split('T')[0];
        const citasForDay = citas.filter(cita => cita.fields.fecha_propuesta.startsWith(currentDateString));

        calendarHtml += `<td><div>${day}</div>`;
        citasForDay.forEach(cita => {
            calendarHtml += `<div>${cita.fields.paciente_idpaciente.nombre} ${cita.fields.paciente_idpaciente.apellido}</div>`;
        });
        calendarHtml += '</td>';

        if ((day + firstDayIndex - 1) % 7 === 6) {
            calendarHtml += '</tr><tr>';
        }
    }

    // Fill in the blank days after the last day of the month
    if ((lastDay + firstDayIndex) % 7 !== 0) {
        for (let i = (lastDay + firstDayIndex) % 7; i < 7; i++) {
            calendarHtml += '<td></td>';
        }
    }

    calendarHtml += '</tr></table>';
    calendarElement.innerHTML = calendarHtml;  // Set the inner HTML of the calendar element
}


function changeMonth(step) {
    currentMonth += step;
    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
    } else if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }
    createCalendar(); // No need to pass citas if it's handled globally or not needed directly
}

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}