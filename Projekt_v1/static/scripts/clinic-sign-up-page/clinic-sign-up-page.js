const form = document.querySelector('form')
const password = document.querySelector('#password');
const confPassword = document.querySelector('#confPassword')

const specialChar = document.querySelector('#passwordHelp p:nth-of-type(2)');
const number = document.querySelector('#passwordHelp p:nth-of-type(3)');
const capitalChar = document.querySelector('#passwordHelp p:nth-of-type(4)');
const smallChar = document.querySelector('#passwordHelp p:nth-of-type(5)');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if(password.value.search(/[a-z]/)<0){
        password.classList.add('form-control-wrong');
        smallChar.classList.add('passwordHelpActive')
    } else if (password.value.search(/[a-z]/)>0){
        smallChar.classList.remove('passwordHelpActive')
    }
    if(password.value.search(/[A-Z]/)<0){
        password.classList.add('form-control-wrong');
        capitalChar.classList.add('passwordHelpActive')
    } else if(password.value.search(/[A-Z]/)>0){
        capitalChar.classList.remove('passwordHelpActive')
    }
    if(password.value.search(/[@#$%^&]/)<0){
        password.classList.add('form-control-wrong');
        specialChar.classList.add('passwordHelpActive')
    } else if(password.value.search(/[@#$%^&]/)>0){
        specialChar.classList.remove('passwordHelpActive')
    }
    if(password.value.search(/[0-9]/)<0){
        password.classList.add('form-control-wrong');
        number.classList.add('passwordHelpActive')
    } else if(password.value.search(/[0-9]/)>0){
        number.classList.remove('passwordHelpActive')
    }
    const regularExpression = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]/;
    if(regularExpression.test(password.value)){
        password.classList.remove('form-control-wrong');
        if(!(password.value === confPassword.value)){
            confPassword.classList.add('form-control-wrong')
        }
    }
})


