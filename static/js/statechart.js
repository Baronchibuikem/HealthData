$.ajax({
    url: $("#status").attr("data-url"),
    dataType: 'json',
    success: function (data) {
        Highcharts.chart("container", data);
    })