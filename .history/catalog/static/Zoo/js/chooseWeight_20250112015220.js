
const chooseWeightButton = document.querySelectorAll('.slider__item-weight-list-item');
      chooseWeightButton.forEach(weightButton => {
        weightButton.addEventListener('click', makeActive);
      });

// const chosenWeightButton = document.querySelectorAll('.slider__item-weight-list-item-active');
//       chosenWeightButton.forEach(weightButton => {
//         weightButton.addEventListener('click', makeActive);
//       });

function makeActive(event) {
    if (event.currentTarget.classList.contains('slider__item-weight-list-item-active')) {
        event.currentTarget.classList.remove('slider__item-weight-list-item-active');
    } else {
        chooseWeightButton.forEach(weightButton => {
            weightButton.classList.remove('slider__item-weight-list-item-active');
        });
    };
};