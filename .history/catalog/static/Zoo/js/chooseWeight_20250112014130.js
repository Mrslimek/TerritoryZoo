
const chooseWeightButton = document.querySelectorAll('.slider__item-weight-list-item');
      chooseWeightButton.forEach(weightButton => {
        weightButton.addEventListener('click', makeActive);
      });


function makeActive(event) {
    if event.current
    event.currentTarget.classList.add('slider__item-weight-list-item-active');
}