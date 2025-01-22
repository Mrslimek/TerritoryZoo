///////////////////
// ПЕРВЫЙ ВАРИАНТ ДОБАВЛЕНИЯ ТОВАРОВ В КОРЗИНУ ЧЕРЕЗ LOCALSTORAGE
///////////////////

// document.addEventListener('DOMContentLoaded', () => {
//     const baskets = document.querySelectorAll('.products___item-basket');
    
//     let basketList = [];

//     baskets.forEach(basket => {
//         basket.addEventListener('click', (event) => {
//             const article = basket.closest('article');
//             if (article) {
//                 const productId = article.getAttribute('productId');
//                 const productTitle = article.getAttribute('productTitle');
//                 let productWeight;
//                 if (article.getAttribute('productWeight').includes(',')) {
//                     productWeight = article.getAttribute('productWeight').split(',');
//                 } else {
//                     productWeight = article.getAttribute('productWeight');
//                 }
//                 const productImage = article.getAttribute('productImage');
//                 const productUnit = article.getAttribute('productUnit');
//                 const productObj = {
//                     'productId': productId,
//                     'productTitle': productTitle,
//                     'productWeight': productWeight,
//                     'productImage': productImage,
//                     'productUnit': productUnit,
//                 }
//                 basketList.push(productObj)
//                 console.log(basketList);
//                 localStorage.setItem('basketList', JSON.stringify(basketList));
//             }
//         });
//     });
// });
