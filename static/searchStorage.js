
const searchButton = document.querySelector('.header__bottom-search-img')
      searchButton.addEventListener('click', addQueryDataToLocalStorage)

function addQueryDataToLocalStorage() {

    const searchData = document.getElementById('id_query').value
    localStorage.setItem('title', searchData)

}