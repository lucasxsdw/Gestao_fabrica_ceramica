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