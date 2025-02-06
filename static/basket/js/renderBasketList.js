//////////////////////
// ЗДЕСЬ ПРОИСХОДИТ РЕНДЕР ТОВАРОВ В КОРЗИНЕ, ПОЛУЧЕННЫХ ИЗ LOCALSTORAGE
/////////////////////

// const basketProductsList = JSON.parse(localStorage.getItem('basketList')) || [];

// if (Array.isArray(basketProductsList) && basketProductsList.length < 1) {
//       const basketList = document.querySelector('.basket__list');
//       const basketListEmpty = document.createElement('p');
//             basketListEmpty.textContent = 'Корзина пуста';
//             basketListEmpty.setAttribute('style', 'color: black;')
//             basketList.appendChild(basketListEmpty);
// } else {
//       const basketList = document.querySelector('.basket__list');
//       basketProductsList.forEach(product => {

//         const basketListItem = document.createElement('li');
//               basketListItem.classList.add('basket__list-item')

//         const basketListItemImg = document.createElement('div');
//               basketListItemImg.classList.add('basket__list-item-img');
//         const basketListItemImgImage = document.createElement('img');
//               basketListItemImgImage.setAttribute('src', `${product.productImage}`);
//               basketListItemImgImage.setAttribute('alt', '');
//               basketListItemImg.appendChild(basketListItemImgImage);
//               basketListItem.appendChild(basketListItemImg);

//         const basketListItemWrap = document.createElement('div');
//               basketListItemWrap.classList.add('basket__list-item-wrap')
//         const basketListItemTitle = document.createElement('div');
//               basketListItemTitle.classList.add('basket__list-item-title');
//               basketListItemTitle.textContent = `${product.productTitle}`;
//               basketListItemWrap.appendChild(basketListItemTitle);
//         const basketListItemWeightList = document.createElement('ul');
//               basketListItemWeightList.classList.add('basket__list-item-weight-list');
//         const basketListItemWeightListItem = document.createElement('li');
//               basketListItemWeightListItem.classList.add('basket__list-item-weight-list-item');

//               console.log(Array.isArray(product.productWeight));

//               if (Array.isArray(product.productWeight)) {
//                   product.productWeight.forEach((weight) => {
//                       basketListItemWeightListItem.innerHTML = `${weight} <span>${product.productUnit}</span>`;
//                   });
//               } else {
//                   basketListItemWeightListItem.innerHTML = `${product.productWeight} <span>${product.productUnit}</span>`;
//               }

//               basketListItemWeightList.appendChild(basketListItemWeightListItem);
//               basketListItemWrap.appendChild(basketListItemWeightList);
//         const basketListItemWeightWrap = document.createElement('div');
//               basketListItemWeightWrap.classList.add('basket__list-item-weight-wrap');
//         const basketListItemWeightText = document.createElement('p');
//               basketListItemWeightText.classList.add('basket__list-item-weight-text');
//               basketListItemWeightText.textContent = 'Указать свой вес';
//               basketListItemWeightWrap.appendChild(basketListItemWeightText);
//         const basketListItemWeight = document.createElement('div');
//               basketListItemWeight.classList.add('basket__list-item-weight');
//         const weightInput = document.createElement('input');
//               weightInput.setAttribute('type', 'text');
//               weightInput.setAttribute('name', '');
//               weightInput.setAttribute('id', '');
//               weightInput.setAttribute('placeholder', 'Укажите вес');
//               basketListItemWeight.appendChild(weightInput);
//         const weightApplyButton = document.createElement('button');
//               weightApplyButton.setAttribute('type', 'button');
//               basketListItemWeight.appendChild(weightApplyButton);
//               basketListItemWeightWrap.appendChild(basketListItemWeight);
//               basketListItemWrap.appendChild(basketListItemWeightWrap);
//               basketListItem.appendChild(basketListItemWrap);     
        
//         const basketListActionWrap = document.createElement('div');
//               basketListActionWrap.classList.add('basket__list-action-wrap');
//         const basketListAction = document.createElement('div');
//               basketListAction.classList.add('basket__list-action');
//         const basketListActionMius = document.createElement('button');
//               basketListActionMius.classList.add('basket__list-action-mius');
//               basketListActionMius.setAttribute('type', 'button');
//               basketListActionMius.textContent = '-';
//         const basketListActionCount = document.createElement('div');
//               basketListActionCount.textContent = '0'; // Этот 0 возможно потом надо будет сделать динамическим счетчиком
//         const basketListActionPlus = document.createElement('button');
//               basketListActionPlus.classList.add('basket__list-action-plus');
//               basketListActionPlus.setAttribute('type', 'button');
//               basketListActionPlus.textContent = '+';
//               basketListAction.appendChild(basketListActionMius);
//               basketListAction.appendChild(basketListActionCount);
//               basketListAction.appendChild(basketListActionPlus);
//               basketListActionWrap.appendChild(basketListAction);
//         const basketListActionImg = document.createElement('div');
//               basketListActionImg.classList.add('basket__list-action-img');
//         const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
//               svg.setAttribute('width', '24');
//               svg.setAttribute('height', '24');
//               svg.setAttribute('viewBox', '0 0 24 24');
//               svg.setAttribute('fill', 'none');
//               svg.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
//         const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
//         const clipPath = document.createElementNS('http://www.w3.org/2000/svg', 'clipPath');
//               clipPath.setAttribute('id', 'clip946_10662');
//         const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
//               rect.setAttribute('id', 'Delete');
//               rect.setAttribute('width', '24');
//               rect.setAttribute('height', '24');
//               rect.setAttribute('fill', 'white');
//               rect.setAttribute('fill-opacity', '0');
//               clipPath.appendChild(rect);
//               defs.appendChild(clipPath);
//               svg.appendChild(defs);
//         const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
//               g.setAttribute('clip-path', 'url(#clip946_10662)');
//         const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
//               path.setAttribute('id', 'Shape');
//               path.setAttribute('d', 'M12 1.75C13.7329 1.75 15.1494 3.10645 15.2446 4.81555L15.25 5L20.5 5C20.9141 5 21.25 5.33582 21.25 5.75C21.25 6.1297 20.9678 6.44348 20.6016 6.49316L20.5 6.5L19.7041 6.5L18.4238 19.5192C18.291 20.8683 17.1982 21.91 15.8628 21.9944L15.687 22L8.31299 22C6.95752 22 5.81348 21.0145 5.59863 19.6934L5.57617 19.5192L4.29492 6.5L3.5 6.5C3.12012 6.5 2.80664 6.21783 2.75684 5.85175L2.75 5.75C2.75 5.3703 3.03223 5.05652 3.39844 5.00684L3.5 5L8.75 5C8.75 3.20508 10.2051 1.75 12 1.75ZM18.1968 6.5L5.80176 6.5L7.06885 19.3724C7.12744 19.9696 7.6001 20.4343 8.18604 20.4936L8.31299 20.5L15.687 20.5C16.2871 20.5 16.7959 20.0751 16.9121 19.4982L16.9312 19.3724L18.1968 6.5ZM13.75 9.25C14.1299 9.25 14.4434 9.53217 14.4932 9.89825L14.5 10L14.5 17C14.5 17.4142 14.1641 17.75 13.75 17.75C13.3701 17.75 13.0566 17.4678 13.0068 17.1017L13 17L13 10C13 9.58582 13.3359 9.25 13.75 9.25ZM10.25 9.25C10.6299 9.25 10.9434 9.53217 10.9932 9.89825L11 10L11 17C11 17.4142 10.6641 17.75 10.25 17.75C9.87012 17.75 9.55664 17.4678 9.50684 17.1017L9.5 17L9.5 10C9.5 9.58582 9.83594 9.25 10.25 9.25ZM12 3.25C11.082 3.25 10.3286 3.95709 10.2559 4.85645L10.25 5L13.75 5C13.75 4.03351 12.9663 3.25 12 3.25Z');
//               path.setAttribute('fill', '#212121');
//               path.setAttribute('fill-opacity', '1');
//               path.setAttribute('fill-rule', 'nonzero');
//               g.appendChild(path);
//               svg.appendChild(g);
//               basketListActionImg.appendChild(svg);
//               basketListActionWrap.appendChild(basketListActionImg);
//               basketListItem.appendChild(basketListActionWrap);
//               basketList.appendChild(basketListItem);
//       })
// }