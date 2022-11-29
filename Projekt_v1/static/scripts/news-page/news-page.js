const expandArrow = document.querySelector('#expandArrow');
const dropDown = document.querySelector('.dropDown');
const inputWrapper = document.querySelector('.inputWrapper');
const searchIcon = document.querySelector('.searchIcon')

inputWrapper.addEventListener('mouseover', () => {
    inputWrapper.classList.add('inputWrapperWider');
    expandArrow.classList.add('expandArrowWider');
})
inputWrapper.addEventListener('mouseout', () => {
    inputWrapper.classList.remove('inputWrapperWider');
    expandArrow.classList.remove('expandArrowWider');
})

expandArrow.addEventListener('click', () => {
    inputWrapper.classList.remove('inputWrapperWider');
    expandArrow.classList.remove('expandArrowWider');
    expandArrow.classList.toggle('expandArrowWiderClick');
    inputWrapper.classList.toggle('inputWrapperWiderClick');
    dropDown.classList.toggle('displayFlex');
})