const expandArrow = document.querySelector('#expandArrow');
const dropDown = document.querySelector('.dropDown');
const inputWrapper = document.querySelector('.inputWrapper');
const searchIcon = document.querySelector('.searchIcon')
expandArrow.addEventListener('click', () => {
    inputWrapper.classList.toggle('inputWrapperWider');
    dropDown.classList.toggle('displayFlex');
})