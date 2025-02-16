// Выпадающий список 'Сортировать по'. Изначально был в файле select.js. Для удобства перенесен сюда
const select = document.querySelector(".catalog__sort-select");
const selectList = document.querySelector(".catalog__sort-select-list");
const selectListItem = document.querySelectorAll(
    ".catalog__sort-select-list-item"
);
const catalogSelectActive = document.querySelector(
    ".catalog__sort-select-active"
);

//EventListener для 'выпадания списка' выше
select.addEventListener("click", () => {
    selectList.classList.toggle("catalog__sort-select-list-active");
});

//EventListener для момента, когда полностью загружен DOM
document.addEventListener("DOMContentLoaded", function () {

    const fetchUrl = 'http://127.0.0.1:8000/api/filtered_products/'

    const radioButtons = document.querySelectorAll("input[type='radio']");
    const checkboxes = document.querySelectorAll("input[class='brand__type-list-item-hdie']");
    const productCategoryId = document.getElementById('filter_item_active').getAttribute('data_id')

    // Добавляет выбранное значение в localStorage и вызывает getLocalStorageData, вызывает функцию для fetch запроса
    // Не вызывает UpdateLocalStorage, потому что я посчитал, что сбрасывать этот фильтр не нужно
    selectListItem.forEach((item) => {
        item.addEventListener("click", () => {
            // Выбраный пункт становится активным
            catalogSelectActive.innerText = item.innerText;
            let orderByData = item.getAttribute("orderByData");
            localStorage.setItem("orderByData", orderByData);
            let localStorageData = getLocalStorageData();

            const params = {
                fetchUrl: fetchUrl,
                orderByData: localStorageData.orderByData,
                brandIds: localStorageData.brandIds.map((id) => parseInt(id, 10)),
                promotion: localStorageData.promotion,
                typeId: localStorageData.typeId,
                title: localStorageData.title,
                productCategoryId: productCategoryId
            }
            filterProducts(params);
        });
    });

    // Для каждой радио кнопки вызывает функцию, вызывает updateLocalStorage, вызывает функцию для fetch запроса
    radioButtons.forEach(function (radioButton) {
        radioButton.addEventListener("click", function () {
            const typeId = this.getAttribute("type-id");
            if (typeId) {
                updateLocalStorage("type-id", typeId, true);
            }

            const localStorageData = getLocalStorageData();

            const params = {
                fetchUrl: fetchUrl,
                orderByData: localStorageData.orderByData,
                brandIds: localStorageData.brandIds.map((id) => parseInt(id, 10)),
                promotion: localStorageData.promotion,
                typeId: localStorageData.typeId,
                title: localStorageData.title,
                productCategoryId: productCategoryId
            }

            filterProducts(params);
        });
    });

    const promotionCheckbox = document.querySelector("input[class='promotional__item-input-hide']");
    promotionCheckbox.addEventListener("change", function() {
      const promotion = this.getAttribute("promotion");
      updateLocalStorage("promotion", promotion, promotionCheckbox.checked);

      const localStorageData = getLocalStorageData();

      const params = {
        fetchUrl: fetchUrl,
        orderByData: localStorageData.orderByData,
        brandIds: localStorageData.brandIds.map((id) => parseInt(id, 10)),
        promotion: localStorageData.promotion,
        typeId: localStorageData.typeId,
        title: localStorageData.title,
        productCategoryId: productCategoryId
    }

    filterProducts(params);
    });

    // Для каждого чекбокса (чекбоксы это brandIds и promotion) вызывает функцию, вызывает UpdateLocalStorage,
    // вызывает функцию для fetch запроса
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {

            const brandId = this.getAttribute("brand-id");

            updateLocalStorage("brand-ids", brandId, checkbox.checked);

            const localStorageData = getLocalStorageData();

            const params = {
                fetchUrl: fetchUrl,
                orderByData: localStorageData.orderByData,
                brandIds: localStorageData.brandIds.map((id) => parseInt(id, 10)),
                promotion: localStorageData.promotion,
                typeId: localStorageData.typeId,
                title: localStorageData.title,
                productCategoryId: productCategoryId
            }

            filterProducts(params);
        });
    });
});