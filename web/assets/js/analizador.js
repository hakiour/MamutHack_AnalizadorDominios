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

    iniciarProceso(dominio.value, tematica.value)
}

function mostrarAlerta(mensaje){
    $('#alerta-mensaje').text(mensaje);
    $('#alerta').modal();
}

function mostrarLoader(){
    $('#loader').modal();
}

function iniciarProceso(dominio, tematica) {
    $.ajax({
        url: "../FiltroPalabrasv2.0.py",
        type: "POST",
        timeout: 60000,
        async: true,
        data: {"url": dominio, "tema": tematica},
        success: function (response) {
            alert(response)
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
            alert(thrownError);
          }
    });

}