// Validación del formulario
function validateForm() {
    let name = document.forms["carForm"]["name"].value;
    let price = document.forms["carForm"]["price"].value;
    if (name == "" || price == "") {
        alert("Todos los campos deben ser completados");
        return false;
    }
}

function addToCart(carId) {
    fetch(`/add_to_cart/${carId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    }).then(response => {
        if (response.ok) {
            alert('Auto añadido al carrito');
        } else {
            alert('Error al añadir el auto al carrito');
        }
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
