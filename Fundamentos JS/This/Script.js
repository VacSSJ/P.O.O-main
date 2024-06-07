function ejemplo(elemento){
    console.log("elemento clickeado", elemento);
    if(elemento.textContent == 'On'){
        elemento.style.backgroundColor = 'Red'
        elemento.textContent = 'Off'
    }
    else{
        elemento.style.backgroundColor = 'green'
        elemento.textContent = 'On'
    }
}

function TurnOff(elemento){
    elemento.style.backgroundColor = 'red'
    elemento.textContent = 'Off';
}

function hide(elemento){
    elemento.remove();
}