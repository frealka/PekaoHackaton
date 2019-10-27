var ctx = document.getElementById("myAreaChart1_mounth");

var myPredictionChart_1 = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["201804", "201806", "201807", "201808", "201809", "201810", "201811", "201812", "201901"],
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
      data: ["4", "1", "50", "18846", "14546", "14546", , ,],
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
      data: [, , , , , 13722, 13310, 12898],
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
            return number_format(value) + " zł";
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
          return datasetLabel + ": " + number_format(tooltipItem.yLabel) + " zł";
        }
      }
    }
  }
});