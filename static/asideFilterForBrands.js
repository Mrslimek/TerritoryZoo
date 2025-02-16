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
    
    let fetchUrl = 'http://127.0.0.1:8000/api/filtered_products/'

    const brandCheckboxes = document.querySelectorAll("input[class='brand__type-list-item-hdie']");

    // Добавляет выбранное значение в localStorage и вызывает getLocalStorageData, вызывает функцию для fetch запроса
    // Не вызывает UpdateLocalStorage, потому что я посчитал, что сбрасывать этот фильтр не нужно
    selectListItem.forEach((item) => {
        item.addEventListener("click", () => {
            // Выбраный пункт становится активным
            catalogSelectActive.innerText = item.innerText;
            let orderByData = item.getAttribute("orderByData");
            localStorage.setItem("orderByData", orderByData);
            let localStorageData = getLocalStorageData();
            console.log(localStorageData);
            
            const params = {
                fetchUrl: fetchUrl,
                orderByData: localStorageData.orderByData,
                brandIds: localStorageData.brandIds.map((id) => parseInt(id, 10)),
                promotion: localStorageData.promotion,
                title: localStorageData.title
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
                brandIds: localStorageData.brandIds.map((id) => parseInt(id, 10)),
                promotion: localStorageData.promotion,
                title: localStorageData.title
            }

            filterProducts(params);
          });

    // Для каждого чекбокса (чекбоксы это brandIds и promotion) вызывает функцию, вызывает UpdateLocalStorage,
    // вызывает функцию для fetch запроса
    brandCheckboxes.forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {
            const brandId = this.getAttribute("brand-id");
            console.log(brandId)

            updateLocalStorage("brand-ids", brandId, checkbox.checked);

            const localStorageData = getLocalStorageData();
            const params = {
                fetchUrl: fetchUrl,
                promotion: localStorageData.promotion,
                brandIds: localStorageData.brandIds.map((id) => parseInt(id, 10)),
                title: localStorageData.title
            }

            filterProducts(params);
        });
    });
});


/*Обновляет localStorage
    * Если brandIds нет в localStorage, то создает пустой массив и push-ит в него значение и добавляет в localStorage
    * Если ключ НЕ brandIds, то создает в localStorage переданое значение, также удаляет, если checkbox был unchecked
    */
function updateLocalStorage(key, value, add) {
    if (key === "brand-ids") {
        let currentArray = JSON.parse(localStorage.getItem(key)) || [];
        if (!Array.isArray(currentArray)) {
            currentArray = [];
        }
        if (add) {
            if (!currentArray.includes(value) && value !== null) {
                currentArray.push(value);
            }
        } else {
            currentArray = currentArray.filter((item) => item !== value);
        }
        localStorage.setItem(key, JSON.stringify(currentArray));
    } else {
        if (add) {
            localStorage.setItem(key, value);
        } else {
            localStorage.removeItem(key);
        }
    }
}


// Просто получаем данные из localStorage
function getLocalStorageData() {
    return {
        brandIds: JSON.parse(localStorage.getItem("brand-ids")) || [],
        promotion: JSON.parse(localStorage.getItem("promotion")),
        orderByData: localStorage.getItem("orderByData"),
        pageNumber: localStorage.getItem("pageNumber"),
        title: localStorage.getItem('title')
    };
}