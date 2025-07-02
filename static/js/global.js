// traduz os elementos da tabela para português
$(document).ready(function () {
  $('.table').DataTable({
    language: {
        url: '//cdn.datatables.net/plug-ins/2.3.2/i18n/pt-BR.json',
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

selecao.addEventListener('change', definirDataDevolucao);
campoDataEmprestimo.addEventListener('change', definirDataDevolucao);

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
  dataEntrega.setDate(dataEntrega.getDate() + quantidadeDias);
  return dataEntrega;
}

function formatarData(data) {
  let dia = data.getDate();
  let mes = data.getMonth() + 1;
  let ano = data.getFullYear();
  
  dia = String(dia).padStart(2, '0');
  mes = String(mes).padStart(2, '0');

  console.log(`${dia}/${mes}/${ano}`);
  
  return `${dia}/${mes}/${ano}`;
}