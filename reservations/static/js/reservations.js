// Example JavaScript code for restaurant booking system

// Validate reservation form
function validateReservationForm() {
    var table = document.getElementById('table').value;
    var date = document.getElementById('date').value;
    var time = document.getElementById('time').value;

    if (table === '' || date === '' || time === '') {
        alert('Please fill in all fields.');
        return false;
    }
    // Additional validation logic can be added here if needed
    return true;
}

// Perform AJAX request to cancel reservation
function cancelReservation(reservationId) {
    if (confirm('Are you sure you want to cancel this reservation?')) {
        // Make AJAX request to cancel reservation
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/cancel/' + reservationId + '/', true);
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        xhr.onload = function () {
            if (xhr.status === 200) {
                alert('Reservation canceled successfully.');
                window.location.reload(); // Refresh page after cancellation
            } else {
                alert('Failed to cancel reservation. Please try again.');
            }
        };
        xhr.send();
    }
}

// Helper function to get CSRF token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}