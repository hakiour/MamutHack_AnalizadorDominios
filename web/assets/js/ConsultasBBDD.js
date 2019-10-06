function getAjax() {
    $.ajax({
        url: "../ObtenerListadoDominios.py",
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



