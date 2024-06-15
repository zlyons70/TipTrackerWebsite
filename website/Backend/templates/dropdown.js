$(document).ready(function(){
    $('.dropdown-item').click(function(event){
        event.preventDefault();
        var range = $(this).data('range');
        
        if (range === 'year') {
            $('#yearForm').show();
        } else {
            $('#yearForm').hide();
            fetchData(range);
        }
    });

    $('#submitYear').click(function(){
        var year = $('#yearInput').val();
        if (year) {
            fetchData('year', year);
        }
    });

    function fetchData(range, year = null) {
        $.ajax({
            url: '/fetch-data',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({range: range, year: year}),
            success: function(response) {
                $('#dataDisplay').html(response);
            }
        });
    }
});
