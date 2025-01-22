
const chooseWeightButton = document.querySelectorAll('.slider__item-weight-list-item');
      chooseWeightButton.forEach(weightButton => {
        weightButton.addEventListener('click', makeActive);
      });

      const chooseWeightButton = document.querySelectorAll('.slider__item-weight-list-item');
      chooseWeightButton.forEach(weightButton => {
        weightButton.addEventListener('click', makeActive);
      });

function makeActive(event) {
    if (event.currentTarget.classList === 'slider__item-weight-list-item-active') {
        event.currentTarget.classList.add('slider__item-weight-list-item');
    } else {
        event.currentTarget.classList.add('slider__item-weight-list-item-active');
    };
};