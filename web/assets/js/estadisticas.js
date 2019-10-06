var TIEMPO_ESPERA_ENTRE_BUSQUEDAS = 10000;
function obtenerUltimosDominiosAnalizados(){
    $.ajax({
        url: "py/obtenerListadoDominios.py",
        context: document.body
      }).done(function(datos) {
            var links = JSON.parse(datos).respuesta;
            var ultimasPaginas = document.getElementById("ultimas_paginas");
            ultimasPaginas.innerHTML = "";
            links.forEach(link => {
                  link = link[0]; //Obtenemos la frase
                  var node = document.createElement("LI");
                  var textnode = document.createTextNode(link);
                  node.appendChild(textnode);
                  node.className = "list-inline-item pointer white";
                  ultimasPaginas.appendChild(node);
            });
            setTimeout(obtenerUltimosDominiosAnalizados,TIEMPO_ESPERA_ENTRE_BUSQUEDAS);
      });
}

function obtenerPalabrasMasUsadas(){
      $.ajax({
          url: "py/obtenerPalabrasMasUsadas.py",
          context: document.body
        }).done(function(datos) {
              var palabras = JSON.parse(datos).respuesta;
              var ultimasPaginas = document.getElementById("top_palabras");
              ultimasPaginas.innerHTML = "";
              palabras.forEach(palabra => {
                    palabra = palabra[0]; //Obtenemos la frase
                    var node = document.createElement("LI");
                    var textnode = document.createTextNode(palabra);
                    node.appendChild(textnode);
                    node.className = "list-inline-item pointer white";
                    ultimasPaginas.appendChild(node);
              });
            setTimeout(obtenerPalabrasMasUsadas,TIEMPO_ESPERA_ENTRE_BUSQUEDAS);
        });
  }
obtenerUltimosDominiosAnalizados();
obtenerPalabrasMasUsadas();