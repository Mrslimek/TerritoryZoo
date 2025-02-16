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
        title: localStorage.getItem('title'),
        typeId: localStorage.getItem('type-id')
    };
}

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

// Функция для fetch запроса
function filterProducts(params) {
    const { fetchUrl, value, typeId, brandIds, promotion, orderByData, pageNumber, title, isSearch, productCategoryId} = params

    // Функция для создания json-а на основе полученых из localStorage данных
    function getBodyDataForFilters(obj) {
        let bodyData = {};

        for (let key in obj) {
            if (obj[key]) {
                bodyData[key] = obj[key];
            }
        }

        return JSON.stringify(bodyData);
    }

    let rawObject = {
        brand_id__in: brandIds,
        promotion: promotion,
        order_by: orderByData,
        page_number: pageNumber,
        title__icontains: title,
        is_search: isSearch,
        product_type_id: typeId,
        product_category: productCategoryId
    };

    //Получение json-a для fetch запроса
    const filters = getBodyDataForFilters(rawObject);
    // Получение csrf-а
    const csrftoken = getCookie("csrftoken");

    fetch(fetchUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: filters,
    })
    .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
            renderProducts(fetchUrl, data);
      })
      .catch((error) => {
        console.error("Ошибка:", error);
      });
}
