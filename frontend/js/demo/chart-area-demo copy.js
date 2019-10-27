// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['0:00 - 0:59', '1:00 - 1:59', '2:00 - 2:59', '3:00 - 3:59', '4:00 - 4:59', '5:00 - 5:59', '6:00 - 6:59', '7:00 - 7:59', '8:00 - 8:59', '9:00 - 9:59', '10:00 - 10:59', '11:00 - 11:59', '12:00 - 12:59', '13:00 - 13:59', '14:00 - 14:59', '15:00 - 15:59', '16:00 - 16:59', '17:00 - 17:59', '18:00 - 18:59', '19:00 - 19:59', '20:00 - 20:59', '21:00 - 21:59', '22:00 - 22:59', '23:00 - 23:59'],
    datasets: [{
      label: "Średnia z godziny",
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
      data: [39.427, 36.825, 37.614, 42.80, 52.634, 51.9813, 26.8412, 30.6320, 19.447, 19.872, 23.8942, 23.755, 23.9617, 29.647, 36.841, 40.827, 41.888, 41.990, 42.25, 44.6886, 46.6218, 53.4827, 58.886, 52.010],
    },
    {
      label: "Zbliżeniowe",
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
      //data: [32.55, 30.02, 30.14, 31.01, 39.63, 33.59, 21.79, 23.77, 15.66, 16.8, 20.78, 21.59, 22.43, 27.25, 33.44, 37.16, 38.52, 38.6, 38.63, 39.4, 39.65, 42.02, 42.46, 39.32],
    },
    {
      label: "Kartowe",
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
      //data: [100.88, 100.57, 103.6, 126.4, 128.59, 165.09, 61.08, 93.45, 68.04, 55.45, 55.56, 45.78, 39.47, 50.45, 62.73, 67.62, 66.44, 66.71, 68.09, 80.63, 91.74, 120.58, 153.5, 138.7],
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


