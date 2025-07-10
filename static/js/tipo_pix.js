document.addEventListener('DOMContentLoaded', function () {
  const tipoSelect = document.getElementById('id_tipo_chave_pix');
  const chaveInput = document.getElementById('id_chave_pix');
  const cpfInput = document.getElementById('id_cpf');
  const contatoInput = document.getElementById('id_contato');
  const salarioInput = document.getElementById('id_salario');

 

  // Máscara para CPF
  if (cpfInput) {
    IMask(cpfInput, {
      mask: '000.000.000-00'
    });

    cpfInput.addEventListener('blur', function () {
      const cpf = cpfInput.value.replace(/[^\d]+/g, '');
      if (cpf.length !== 11) {
        cpfInput.classList.add('is-invalid');
      } else {
        cpfInput.classList.remove('is-invalid');
      }
    });
  }

  // Máscara para Telefone
  if (contatoInput) {
    IMask(contatoInput, {
      mask: '(00) 00000-0000'
    });

    contatoInput.addEventListener('blur', function () {
      const telefone = contatoInput.value.replace(/[^\d]+/g, '');
      if (telefone.length !== 11) {
        contatoInput.classList.add('is-invalid');
      } else {
        contatoInput.classList.remove('is-invalid');
      }
    });
  }

  // Atualiza chave PIX conforme tipo
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
    atualizarChavePix(); // Executa ao carregar
  } else {
    console.warn("Um ou mais campos PIX não foram encontrados.");
  }
});
