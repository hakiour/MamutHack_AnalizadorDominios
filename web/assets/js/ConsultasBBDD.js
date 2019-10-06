function getAjax() {
    $.ajax({
        url: "../../obtenerListadoDominios.py",
        type: "GET",
        success: function (response) {
            alert(response);
            var obj = JSON.parse(response);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
            alert(thrownError);
        }
    })
}

function elegirDominio(idDominio, nombreDominio) {
    $.ajax({
        url: "../../obtenerDatosEstadisticas.py",
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
        url: "../../obtenerDatosPalabras.py",
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

    data = {
        datasets: [{
            data: valores,
            backgroundColor: coloresGrafica
        }],
        labels: labelsValores
    };
    

    new Chart(ctx, {
        data: data,
        type: 'bar',
    });
}






getAjax();