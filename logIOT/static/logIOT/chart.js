var ctx = document.getElementById("channelChart");

var data = {
    labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    datasets: [
        {
            label: "Channel Data",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        },
    ]
};

var options = {
    scales: {
        xAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Time'
            }
        }],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Temperature (degC)'
            }
        }]
    }
}

var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options,
});
