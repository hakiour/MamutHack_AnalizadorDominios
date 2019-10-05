document.getElementById("analizar").addEventListener("click", ejecutarAnalisis); 

function ejecutarAnalisis(){
    var tematica = document.getElementById("tematica");
    var dominio = document.getElementById("dominio");
    if(tematica.value.trim() == ""){
        mostrarAlerta("Tienes que seleccionar una temática.");
        return;
    }else if(dominio.value.trim() == ""){
        mostrarAlerta("Tienes que introducir un dominio válido.");
        return;
    }

    mostrarLoader();
}

function mostrarAlerta(mensaje){
    $('#alerta-mensaje').text(mensaje);
    $('#alerta').modal();
}

function mostrarLoader(){
    $('#loader').modal();
}