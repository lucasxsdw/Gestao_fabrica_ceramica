// traduz os elementos da tabela para português
$(document).ready(function () {
  $('#dataTable').DataTable({
    language: {
      url: '/static/vendor/datatables/pt-BR.json'
    }
  });
});


// recebe a url do botão de exclusão para o botão de confirmação do modal
$('#modalConfirmacaoExclusao').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) 
  var url = button.data('url') 
  var modal = $(this)
  modal.find('#botaoExclusao').attr('href', url);
})

// obtém a data de devolução de um material
let selecao = document.querySelector('#id_material');
let campoDataEmprestimo = document.querySelector('#id_data_emprestimo');
let campoDataDevolucao = document.querySelector('#id_data_devolucao');

selecao?.addEventListener('change', definirDataDevolucao);
campoDataEmprestimo?.addEventListener('change', definirDataDevolucao);

function definirDataDevolucao(){
  
  if(selecao.value == '' || campoDataEmprestimo.value == ''){
    return;
  }

  fetch( `/material/${selecao.value}/quantidade_dias_emprestimo`)
  .then(res => {
    if (res.ok){
      return res.json();
    } else {
      throw new Error('Erro ao obter a quantidade de dias');
    }
  })
  .then(dado => {
    let data = calcularData(campoDataEmprestimo.value, dado['quantidade_dias']);
    campoDataDevolucao.value = formatarData(data);
  })
}

function calcularData(data, quantidadeDias){
  let dataEntrega = new Date(data);
  dataEntrega.setUTCDate(dataEntrega.getUTCDate() + quantidadeDias);
  return dataEntrega;
}

function formatarData(data) {
  let dia = data.getUTCDate();
  let mes = data.getUTCMonth() + 1;
  let ano = data.getUTCFullYear();
  
  dia = String(dia).padStart(2, '0');
  mes = String(mes).padStart(2, '0');
  
  return `${ano}-${mes}-${dia}`;
}

//adiciona a classe active ao link corresponde à página atual na barra lateral
(function(){
    const path = window.location.pathname;

    if (path.charAt(0) !== '/') {
        path = '/' + path;
    }

    const links = document.querySelectorAll('ul.sidebar li a');
    
    const origin = window.location.origin;

    links.forEach(elemento => {
      let href = elemento.href;
      href = href.replace(origin, '')
      
      if(href == path){
        elemento.parentElement.classList.add('active');
      }
    })
})(); 