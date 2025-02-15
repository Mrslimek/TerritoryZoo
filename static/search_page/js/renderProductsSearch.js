function renderProductsSearch(fetchUrl, data) {
    const container = document.querySelector('.products__list')
    container.innerHTML = data.results.results.map(product => {
        const promotion = product.promotion_set && product.promotion_set.length > 0;
        const properties = product.productproperties_set && product.productproperties_set.length > 0;
        const props = properties ? product.productproperties_set : [{ weight: product.amount }];
    
        const weights = props.map(prop => `<li class="slider__item-weight-list-item">${prop.weight} ${product.unit}</li>`).join('');
    
        const price = promotion
            ? `<p class="products___item-price-promotion">${product.price} BYN</p>
                <p class="products___item-price">${product.promotion_set[0].discount} BYN</p>`
            : `<p class="products___item-price">${product.price} BYN</p>`;
    
        const promotionDiv = promotion ? `<div class="products___item-promotion">Акция</div>` : '';
    
        return `
            <li class="products__list-item">
            <article class="products___item">
                <div class="products___item-img">
                <img src="${product.productimage_set[0].image}" alt="item">
                </div>
                ${promotionDiv}
                <a href="/details/${product.id}" class="products___item-title">${product.title}</a>
                <ul class="products___item-weight-list">
                ${weights}
                </ul>
                <div class="products___item-price-basket">
                ${price}
                <div class="products___item-basket" onclick="window.location.href='http://127.0.0.1:8000/add_to_cart/${product.id}'">
                    <div class="slider__item-basket-text">+</div>
                    <div class="slider__item-basket-img">
                    <!-- SVG код корзины -->
                    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M1 1C1 0.447715 1.44932 0 2.00358 0H3.50894C4.34034 0 5.01431 0.671572 5.01431 1.5V2.06055L17.5883 2.96818C18.4651 3.02278 19.1089 3.81081 18.9846 4.67739L18.1194 10.7121C18.0135 11.4511 17.3783 12 16.6292 12H5.01431V14H15.0572C16.72 14 18.068 15.3431 18.068 17C18.068 18.6569 16.72 20 15.0572 20C13.3945 20 12.0465 18.6569 12.0465 17C12.0465 16.6494 12.1069 16.3128 12.2178 16H6.85015C6.9611 16.3128 7.02147 16.6494 7.02147 17C7.02147 18.6569 5.67352 20 4.01073 20C2.34795 20 1 18.6569 1 17C1 15.6938 1.83779 14.5825 3.00716 14.1707V3.00923C3.00711 3.00372 3.00711 2.99821 3.00716 2.99268V2H2.00358C1.44932 2 1 1.55228 1 1ZM5.01431 4.06445V10H16.194L16.9208 4.93051L5.01431 4.06445ZM14.0537 17C14.0537 16.4477 14.503 16 15.0572 16C15.6115 16 16.0608 16.4477 16.0608 17C16.0608 17.5523 15.6115 18 15.0572 18C14.503 18 14.0537 17.5523 14.0537 17ZM3.00716 17C3.00716 16.4477 3.45647 16 4.01073 16C4.56499 16 5.01431 16.4477 5.01431 17C5.01431 17.5523 4.56499 18 4.01073 18C3.45647 18 3.00716 17.5523 3.00716 17Z" fill="#5C5F62"/>
                    </svg>
                    </div>
                </div>
                </div>
                <button type="button" class="products___item-btn">Купить в 1 клик</button>
            </article>
            </li>
        `;
        }).join('');
}


  