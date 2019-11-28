var ctx = document.getElementById("channelChart");

// Format data into pairs for chart.js
var plot_data = [];
var n_data = x_data.length;
for (var i = 0; i < n_data; i++) {
    plot_data.push({x: x_data[i], y: y_data[i]})
}

var data = {
    datasets: [
        {
            label: channel_name,
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: plot_data,
        },
    ]
};

var options = {
    scales: {
        xAxes: [{
            type: 'time',
            scaleLabel: {
                display: true,
                labelString: 'Time'
            },
        }],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: y_label
            }
        }]
    }
}

var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: options,
});
