// Ensuring global access to currentMonth and currentYear
var currentMonth = new Date().getMonth();
var currentYear = new Date().getFullYear();
var citas = []; // Ensure this is filled with your data as needed

function createCalendar() {
    const calendarElement = document.getElementById('calendar');
    const currentMonthYear = document.getElementById('currentMonthYear');
    const date = new Date(currentYear, currentMonth, 1);
    const firstDayIndex = date.getDay();
    const lastDay = new Date(currentYear, currentMonth + 1, 0).getDate();

    const monthNames = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"];
    
    currentMonthYear.textContent = `${monthNames[currentMonth]} ${currentYear}`;

    let calendarHtml = '<table><tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr><tr>';

    for (let i = 0; i < firstDayIndex; i++) {
        calendarHtml += '<td></td>';
    }

    for (let day = 1; day <= lastDay; day++) {
        calendarHtml += `<td>${day}</td>`;
        if ((day + firstDayIndex - 1) % 7 === 6) {
            calendarHtml += '</tr><tr>';
        }
    }

    if ((lastDay + firstDayIndex) % 7 !== 0) {
        for (let i = (lastDay + firstDayIndex) % 7; i < 7; i++) {
            calendarHtml += '<td></td>';
        }
    }

    calendarHtml += '</tr></table>';
    calendarElement.innerHTML = calendarHtml;
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

document.addEventListener('DOMContentLoaded', function() {
    createCalendar(); // Call this to setup the calendar initially
});
