var TIEMPO_ESPERA_ENTRE_BUSQUEDAS = 10000;

function elegirDominio(idDominio, nombreDominio) {
      $.ajax({
          url: "py/obtenerDatosEstadisticas.py",
          type: "POST",
          data: {"dominio": idDominio},
          success: function (response) {
              var jsonObject = JSON.parse(response);
              var resultado = jsonObject.respuestaLinks
  
              document.getElementById("tituloDominioBuscado").innerText = nombreDominio
  
              crearGraficaDominio(resultado)
          },
          error: function (xhr, ajaxOptions, thrownError) {
              alert(xhr.status);
              alert(thrownError);
          }
      })
  
      $.ajax({
          url: "py/obtenerDatosPalabras.py",
          type: "POST",
          data: {"dominio": idDominio},
          success: function (response) {
              var jsonObject = JSON.parse(response);
              var resultado = jsonObject.respuestaPalabras
  
              crearGraficaPalabras(resultado)
          },
          error: function (xhr, ajaxOptions, thrownError) {
              alert(xhr.status);
              alert(thrownError);
          }
      })
  }
  
  var coloresGrafica = ["#633d94", "#e1b9b4", "#d9909e", "#e77344", "#433191", "#78b726", "#b93fa6", "#5f8740", "#414e95", "#ad832c"]
  
  function crearGraficaDominio(arrayDatos) {
      var ctx = document.getElementById('graficaLinksBuscado').getContext('2d');
  
      var valores = []
      var labelsValores = []
  
      for (let index = 0; index < arrayDatos.length; index++) {
          labelsValores.push(arrayDatos[index][0])
          valores.push(arrayDatos[index][1])
      }   
  
      data = {
          datasets: [{
              data: valores,
              backgroundColor: coloresGrafica 
          }],
          labels: labelsValores
      };
      
  
      new Chart(ctx, {
          data: data,
          type: 'polarArea',
      });
  }
  
  function crearGraficaPalabras(arrayDatos) {
      var ctx = document.getElementById('graficaPalabrasBuscado').getContext('2d');
  
      var valores = []
      var labelsValores = []
  
      for (let index = 0; index < arrayDatos.length; index++) {
          labelsValores.push(arrayDatos[index][0])
          valores.push(arrayDatos[index][1])
      }   
  
      labelsValores.push("")
      valores.push("0")
  
      data = {
          datasets: [{
              data: valores,
              backgroundColor: coloresGrafica
          }],
          labels: labelsValores
      };
      
  
      new Chart(ctx, {
          data: data,
          type: 'bar'
      });
  }
  

  
function obtenerUltimosDominiosAnalizados(){
    $.ajax({
        url: "py/obtenerListadoDominios.py",
        context: document.body
      }).done(function(datos) {
            var links = JSON.parse(datos).respuesta;
            var ultimasPaginas = document.getElementById("ultimas_paginas");
            ultimasPaginas.innerHTML = "";
            document.getElementById("tituloDominioBuscado").innerText = links[0][0]
            elegirDominio(links[0][1], links[0][0]);
            for(var i = 0;i < links.length;i++){
                var link = links[i][0]; //Obtenemos la frase
                var id = links[i][1]; //Obtenemos el id
                var node = document.createElement("LI");
                var textnode = document.createTextNode(link);
                node.appendChild(textnode);
                node.className = "list-inline-item pointer white";
                node.setAttribute("onclick","elegirDominio("+id+", '"+link+"')")
                ultimasPaginas.appendChild(node);
            }
          
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