Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

const cores = ["orange", "cyan", "lime", "red", "yellow", "purple", "pink", "blue"];

const producoes_diarias = JSON.parse(document.querySelector("#producoes_diarias").textContent);
const rotulos1 = producoes_diarias.map(producao => producao['data']);
const valores1 = producoes_diarias.map(producao => producao['total']);

const grafico1 = document.getElementById("grafico1");
const graficoDeBarras = new Chart(grafico1, {
  type: 'bar',
  data: {
    labels: rotulos1,
    datasets: [{
      label: "Unidades produzidas",
      data: valores1,
      backgroundColor: cores[0]
    }],
  },
  options: {
    maintainAspectRatio: false,
    scales: {
      yAxes: [{
        display: true,
        ticks: {
          beginAtZero: true
        }
      }]
    },
    legend:{
      display: true
    },
  }
});

const producoes_por_produto = JSON.parse(document.querySelector("#producoes_por_produto").textContent);
const rotulos2 = producoes_por_produto.map(producao => producao['produto__nome']);
const valores2 = producoes_por_produto.map(producao => producao['total']);

var grafico2 = document.getElementById("grafico2");
var graficoDePizza = new Chart(grafico2, {
  type: 'pie',
  data: {
    labels: rotulos2,
    datasets: [{
      data: valores2,
      backgroundColor: cores
    }],
  },
  options: {
    maintainAspectRatio: false
  },
});