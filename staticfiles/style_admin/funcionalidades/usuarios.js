$(document).ready(function() {

    $("#tablausuario").DataTable({
        "language": {
            "lengthMenu": "Mostrar _MENU_ registros",
            "search": "Buscar:",
            "zeroRecords": '<i class="far fa-sad-tear"></i> Registro no encontrado <i class="far fa-sad-tear"></i>',
            "info": "Mostrando _PAGE_ de _PAGES_",
            "infoEmpty": "No records available",
            "infoFiltered": "(filtered from _MAX_ total records)",
            paginate: {
                previous: "Anterior",
                next: "Siguiente"
            }
        },
        scrolly: 400,
        lengthMenu: [
            [10, 15, 20, -1],
            [10, 15, 20, "All"]
        ]
    })

})