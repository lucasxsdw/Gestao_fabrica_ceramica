Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

const cores = ["orange", "cyan", "lime", "red", "yellow", "purple", "pink", "blue"];

let vetor = [];
for(let i = 1; i < 30; i++){
  vetor[i - 1] = `${i}/30`
}

let dados = [];
for(let i = 1; i < 30; i++){
  dados[i - 1] = `${Math.round(i * Math.random())}`
}

const grafico1 = document.getElementById("grafico1");
const graficoDeBarras = new Chart(grafico1, {
  type: 'bar',
  data: {
    labels: vetor,
    datasets: [{
      label: "Unidades produzidas",
      data: dados,
      backgroundColor: cores[0]
    }],
  },
  options: {
    maintainAspectRatio: false,
    legend:{
      display: true
    },
  }
});


var grafico2 = document.getElementById("grafico2");
var graficoDePizza = new Chart(grafico2, {
  type: 'pie',
  data: {
    labels: ["Bloco", "Tijolo"],
    datasets: [{
      data: [55, 30],
      backgroundColor: cores
    }],
  },
  options: {
    maintainAspectRatio: false
  },
});