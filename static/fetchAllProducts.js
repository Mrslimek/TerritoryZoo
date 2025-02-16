
let fetchUrl = 'http://127.0.0.1:8000/api/filtered_products/'

try {
    const productCategoryId = document.getElementById('filter_item_active').getAttribute('data_id')
    filters = {
        product_category: productCategoryId
    }
    const csrfToken = getCookie('csrftoken')
    fetch(fetchUrl, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(filters)
    })
    .then(response => response.json())
    .then(data => {
            renderProducts(fetchUrl, data, filters)
    })
} catch {
    fetch(fetchUrl)
    .then(response => response.json())
    .then(data => {
            renderProducts(fetchUrl, data)
        }
    )   
}