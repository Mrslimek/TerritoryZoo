const fetchUrl = 'http://127.0.0.1:8000/api/products_paginated'
fetch('http://127.0.0.1:8000/api/products_paginated')
.then(response => response.json())
.then(data => {
        console.log(data)
        renderProducts(data,)
    }
)