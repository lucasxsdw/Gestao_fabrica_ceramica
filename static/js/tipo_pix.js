document.addEventListener('DOMContentLoaded', function () {
  const tipoSelect = document.getElementById('id_tipo_chave_pix');
  const chaveInput = document.getElementById('id_chave_pix');
  const cpfInput = document.getElementById('id_cpf');
  const contatoInput = document.getElementById('id_contato');

  function atualizarChavePix() {
    const tipo = tipoSelect.value;

    if (tipo === 'CPF') {
      chaveInput.value = cpfInput.value;
    } else if (tipo === 'TELEFONE') {
      chaveInput.value = contatoInput.value;
    } else {
      chaveInput.value = '';
    }
  }

  if (tipoSelect && chaveInput && cpfInput && contatoInput) {
    tipoSelect.addEventListener('change', atualizarChavePix);
    cpfInput.addEventListener('input', atualizarChavePix);
    contatoInput.addEventListener('input', atualizarChavePix);

    atualizarChavePix(); // Atualiza na carga da página
  } else {
    console.warn("Um ou mais campos não foram encontrados.");
  }
});
