// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

link = "/api/prediksi/";



async function getDataLinearPred(url) 
{
  const response = await fetch(url);

  const data = await response.json();

  // console.log(data[0]['Linear'][0])

  console.log(data)


  console.log(data)

  showLinePred(data.index, data.y_test, data.prediksi, "prediksi")
  

  showLinePred(data)
}



// console.log(data)


// Area Chart Example
function showLinePred(dataX, dataY1, dataY2, element) {
  var ctx = document.getElementById(element);
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dataX,
      datasets: [{
        label: "data test",
        lineTension: 0.2,
        backgroundColor: "rgba(2,117,216,0.2)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(188,138,228,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 5,
        pointBorderWidth: 1,
        data: dataY1
      },
      {
        label: "data prediksi",
        lineTension: 0.2,
        backgroundColor: "rgba(2,17,16,0.2)",
        borderColor: "rgba(2,17,16,1)",
        pointRadius: 3,
        pointBackgroundColor: "rgba(2,17,16,1)",
        pointBorderColor: "rgba(188,18,28,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,17,16,1)",
        pointHitRadius: 5,
        pointBorderWidth: 1,
        data: dataY2
      },
    ],

    },
    options: {
      scales: {
        xAxes: [{
          gridLines: {
            display: false
          },
          ticks: {
            maxTicksLimit: 7
          },
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: 1,
            maxTicksLimit: 1
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          }
        }],
      },
      legend: {
        display: true
      }
    }
  });
}

getDataLinearPred(link);