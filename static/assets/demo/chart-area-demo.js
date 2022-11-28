// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

link = "/api/SVM/";



async function getDataLinear(url) 
{
  const response = await fetch(url);

  const data = await response.json();

  // console.log(data[0]['Linear'][0])



  // console.log(Object.keys(data).length)




  

  showLine(data.Linear.PengaruhC.C, data.Linear.PengaruhC.Akurasi, "hub_C_L", "C")
  showLine(data.Linear.PengaruhMaxItter.MaxItter, data.Linear.PengaruhMaxItter.Akurasi, "hub_MaxItter_L", "Max Itterasi")
  
  showLine(data.RBF.PengaruhC.C, data.RBF.PengaruhC.Akurasi, "hub_C_R", "C")
  showLine(data.RBF.PengaruhMaxItter.MaxItter, data.RBF.PengaruhMaxItter.Akurasi, "hub_MaxItter_R", "Max Itter")
  showLine(data.RBF.PengaruhGamma.Gamma, data.RBF.PengaruhGamma.Akurasi, "hub_Gamma_R", "Gamma")
  
  showLine(data.Sigmoid.PengaruhC.C, data.Sigmoid.PengaruhC.Akurasi, "hub_C_S", "C")
  showLine(data.Sigmoid.PengaruhMaxItter.MaxItter, data.Sigmoid.PengaruhMaxItter.Akurasi, "hub_MaxItter_S","Max Itter")
  showLine(data.Sigmoid.PengaruhGamma.Gamma, data.Sigmoid.PengaruhGamma.Akurasi, "hub_Gamma_S", "Gamma")
  showLine(data.Sigmoid.PengaruhCoef0.Degree, data.Sigmoid.PengaruhCoef0.Akurasi, "hub_Coef0_S", "Coef")
  
  showLine(data.Poly.PengaruhC.C, data.Poly.PengaruhC.Akurasi, "hub_C_P", "C")
  showLine(data.Poly.PengaruhMaxItter.MaxItter, data.Poly.PengaruhMaxItter.Akurasi, "hub_MaxItter_P", "Max Itter")
  showLine(data.Poly.PengaruhGamma.Gamma, data.Poly.PengaruhGamma.Akurasi, "hub_Gamma_P", "Gamma")
  showLine(data.Poly.PengaruhDegree.Degree, data.Poly.PengaruhDegree.Akurasi, "hub_Degree_P", "Degree")
  showLine(data.Poly.PengaruhCoef0.Coef0, data.Poly.PengaruhCoef0.Akurasi, "hub_Coef0_P", "Coef")

  showLine(data.Split.DataTest, data.Split.Akurasi, "split", "Data Test")

    console.log(data.Split.Akurasi, data.Split.DataTest)
}



// console.log(data)


// Area Chart Example
function showLine(dataX, dataY, element, labelX) {
  var ctx = document.getElementById(element);
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: dataX,
      datasets: [{
        label: "Sessions",
        lineTension: 0.3,
        backgroundColor: "rgba(2,117,216,0.2)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(188,138,228,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: dataY,
      }],
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
          scaleLabel:{
            display : true,
            labelString : labelX
          },
        }],
        yAxes: [{
          // ticks: {
          //   max: 1,
          //   maxTicksLimit: 2
          // },
          scaleLabel: {
            display :true,
            labelString : 'Akurasi'
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          }
        }],
      },
      legend: {
        display: false
      }
    }
  });
}

getDataLinear(link);