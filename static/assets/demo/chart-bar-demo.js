// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';



link = "/api/featureImportance/";



async function getDataBar(url) 
{
  const response = await fetch(url);

  const data = await response.json();

  // console.log(data[0]['Linear'][0])

  // console.log(data.terrendah.gejala)

  // console.log(Object.keys(data).length)

  showBar(data.tertinggi.nilai ,data.tertinggi.gejala, "nilaiTertinggi")
  showBar(data.terrendah.nilai ,data.terrendah.gejala, "nilaiTerrendah")
  

}


function showBar(data, label, element){
var ctx = document.getElementById(element);
var myLineChart = new Chart(ctx, {
  type: 'horizontalBar',
  data: {
    labels: label,
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: data
    }],
  },
  options: {
    scales: {
      xAxes: [{
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        },
        scaleLabel:{
          display :true,
          labelString : 'nilai'
        },

      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 150,
          maxTicksLimit: 10
        },
        scaleLabel: {
          display :true,
          labelString : 'Gejala'
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
}

getDataBar(link)