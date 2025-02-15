
let fetchUrl = 'http://127.0.0.1:8000/api/search/'
let payload = localStorage.getItem('query')

// Функция для получения куки файла, но испольется только для получения csrf-токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}

// Получение csrf-а
const csrftoken = getCookie("csrftoken");

fetch(fetchUrl, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(data => {
    renderProductsSearch(fetchUrl, data)
})