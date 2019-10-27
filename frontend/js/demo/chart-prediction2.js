var ctx = document.getElementById("myAreaChart2");

var myPredictionChart_2 = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['7:00 - 7:59', '8:00 - 8:59', '9:00 - 9:59', '10:00 - 10:59', '11:00 - 11:59', '12:00 - 12:59', '13:00 - 13:59', '14:00 - 14:59', '15:00 - 15:59', '16:00 - 16:59', '17:00 - 17:59', '18:00 - 18:59', '19:00 - 19:59', '20:00 - 20:59'],
    datasets: [{
      label: "Dane archiwalne",
      lineTension: 0.3,
      backgroundColor: "rgba(78, 115, 223, 0.05)",
      borderColor: "#8B0000",
      pointRadius: 3,
      pointBackgroundColor: "#8B0000",
      pointBorderColor: "#8B0000",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "#8B0000",
      pointHoverBorderColor: "#8B0000",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      data: [30, 60, 70, 55, 90, 105, 110, 90],
    },
    {
      label: "Predykcja",
      lineTension: 0.3,
      backgroundColor: "rgba(0, 102, 104, 0.05)",
      borderColor: "#058B00",
      pointRadius: 3,
      pointBackgroundColor: "#058B00",
      pointBorderColor: "#058B00",
      pointHoverRadius: 3,
      pointHoverBackgroundColor: "#058B00",
      pointHoverBorderColor: "#058B00",
      pointHitRadius: 10,
      pointBorderWidth: 2,
      borderDash: [10,5],
      data: [ , , , , , , , 90, 50, 30, 20,10,5,0],
    }],

  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function(value, index, values) {
            return number_format(value);
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      intersect: false,
      mode: 'index',
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ": " + number_format(tooltipItem.yLabel);
        }
      }
    }
  }
});
