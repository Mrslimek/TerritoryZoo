let fetchUrl = 'http://127.0.0.1:8000/api/filtered_products/'
let title = localStorage.getItem('title')
let isSearch = 1

const params = {
    fetchUrl: fetchUrl,
    title: title,
    isSearch: isSearch
}

filterProducts(params)




