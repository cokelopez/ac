$(function () {

    $(".js-add-driver").click(function () {
        $.ajax({
            url: 'drivers/add/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                console.log('modal succeeded');
                // $("#modal-driver").modal("show");
            },
            success: function (data) {
                console.log('modal succeeded');
                // $("#modal-driver .modal-content").html(data);
            }
        });
    });

});