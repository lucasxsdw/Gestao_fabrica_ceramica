document.addEventListener('DOMContentLoaded', function () {
  const tipoSelect = document.getElementById('id_tipo_chave_pix');
  const chaveInput = document.getElementById('id_chave_pix');
  const cpfInput = document.getElementById('id_cpf');
  const contatoInput = document.getElementById('id_contato');
  const salarioInput = document.getElementById('id_salario');

  // Aplicar máscara de CPF com IMask
  if (cpfInput) {
    IMask(cpfInput, {
      mask: '000.000.000-00'
    });

    cpfInput.addEventListener('blur', function () {
      const cpf = cpfInput.value.replace(/[^\d]+/g, '');
      cpfInput.classList.toggle('is-invalid', cpf.length !== 11);
    });
  }

  // Aplicar máscara de Telefone com IMask
  if (contatoInput) {
    IMask(contatoInput, {
      mask: '(00) 00000-0000'
    });

    contatoInput.addEventListener('blur', function () {
      const tel = contatoInput.value.replace(/[^\d]+/g, '');
      contatoInput.classList.toggle('is-invalid', tel.length !== 11);
    });
  }

  // Atualizar chave pix automaticamente
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
    atualizarChavePix();
  } else {
    console.warn("Alguns campos para PIX não foram encontrados.");
  }
});
