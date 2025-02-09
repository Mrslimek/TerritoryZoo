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
    
    localStorage.clear(); //TODO: Сделать так, чтобы при обновлении страницы стандартным способ сбрасывались и кнопки

    const radioButtons = document.querySelectorAll("input[type='radio']");
    const checkboxes = document.querySelectorAll("input[class='brand__type-list-item-hdie']");

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
            typeId: localStorage.getItem("type-id"),
            brandIds: JSON.parse(localStorage.getItem("brand-ids")) || [],
            productCategoryId: document.getElementById("filter_item_active").getAttribute("data_id"),
            promotion: JSON.parse(localStorage.getItem("promotion")),
            orderByData: localStorage.getItem("orderByData"),
            pageNumber: localStorage.getItem("pageNumber"),
        };
    }

    // Добавляет выбранное значение в localStorage и вызывает getLocalStorageData, вызывает функцию для fetch запроса
    // Не вызывает UpdateLocalStorage, потому что я посчитал, что сбрасывать этот фильтр не нужно
    selectListItem.forEach((item) => {
        item.addEventListener("click", () => {
            // Выбраный пункт становится активным
            catalogSelectActive.innerText = item.innerText;
            let orderByData = item.getAttribute("orderByData");
            localStorage.setItem("orderByData", orderByData);
            let localStorageData = getLocalStorageData();
            filterProducts(
                fetchUrl,
                this.value,
                localStorageData.typeId,
                localStorageData.brandIds.map((id) => parseInt(id, 10)),
                localStorageData.productCategoryId,
                localStorageData.promotion,
                localStorageData.orderByData,
                localStorage.pageNumber
            );
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

            filterProducts(
                fetchUrl,
                this.value,
                localStorageData.typeId,
                localStorageData.brandIds.map((id) => parseInt(id, 10)),
                localStorageData.productCategoryId, //TODO: Разбораться с функцией в map
                localStorageData.promotion,
                localStorageData.orderByData,
                localStorage.pageNumber
            );
        });
    });

    const promotionCheckbox = document.querySelector("input[class='promotional__item-input-hide']");
    promotionCheckbox.addEventListener("change", function() {
      const promotion = this.getAttribute("promotion");
      updateLocalStorage("promotion", promotion, promotionCheckbox.checked);

      const localStorageData = getLocalStorageData();

      filterProducts(
        fetchUrl,
        this.value,
        localStorageData.typeId,
        localStorageData.brandIds.map((id) => parseInt(id, 10)),
        localStorageData.productCategoryId,
        localStorageData.promotion,
        localStorageData.orderByData,
        localStorage.pageNumber
      );
    });

    // Для каждого чекбокса (чекбоксы это brandIds и promotion) вызывает функцию, вызывает UpdateLocalStorage,
    // вызывает функцию для fetch запроса
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener("change", function () {

            const brandId = this.getAttribute("brand-id");

            updateLocalStorage("brand-ids", brandId, checkbox.checked);

            const localStorageData = getLocalStorageData();

            filterProducts(
                fetchUrl,
                this.value,
                localStorageData.typeId,
                localStorageData.brandIds.map((id) => parseInt(id, 10)),
                localStorageData.productCategoryId,
                localStorageData.promotion,
                localStorageData.orderByData,
                localStorage.pageNumber
            );
        });
    });
});

// Функция для fetch запроса
function filterProducts(
    value,
    typeId,
    brandIds,
    productCategoryId,
    promotion,
    orderByData,
    pageNumber
) {
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

    // Функция для создания json-а на основе полученых из localStorage данных
    function getBodyDataForFilters(
        typeId,
        brandIds,
        productCategoryId,
        promotion,
        orderByData,
        pageNumber
    ) {
        let bodyData = {};

        let rawObject = {
            product_type: typeId,
            brand: brandIds,
            product_category: productCategoryId,
            promotion: promotion,
            order_by: orderByData,
            page_number: pageNumber,
        };

        for (let key in rawObject) {
            if (rawObject[key]) {
                bodyData[key] = rawObject[key];
            }
        }

        return JSON.stringify(bodyData);
    }

    //Получение json-a для fetch запроса
    const bodyData = getBodyDataForFilters(
        typeId,
        brandIds,
        productCategoryId,
        promotion,
        orderByData,
        pageNumber
    );

    console.log(bodyData);

    fetch(fetchUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: bodyData,
    })
        .then((response) => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error(
                    `Запрос не получился - статус ${response.status}`
                );
            }
        })
        .then((data) => {
            console.log(data);
            renderProducts(data);
        })
        .catch((error) => {
            console.error("Ошибка:", error);
        });
}

