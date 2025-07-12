const produtoSelecionado = document.querySelector("#produtos");
const dataInicial = document.querySelector("#data-inicial");
const dataFinal = document.querySelector("#data-final");
const botaoFiltrar = document.querySelector("#filtrar");

const tabela = $('#dataTableNoSearch').DataTable({
    language: {
        url: '//cdn.datatables.net/plug-ins/2.3.2/i18n/pt-BR.json',
    }
});

let botaoVer = id => `<a href="/producao/${id}" class="btn btn-warning btn-sm mx-1" aria-label="Ver"><i class="fas fa-eye"></i></a>`;
let botaoEditar = id => `<a href="/producao/editar/${id}/" class="btn btn-info btn-sm mx-1" aria-label="Editar"><i class="fas fa-edit"></i></a>`;
let botaoExcluir = id => `<button class="btn btn-danger btn-sm mx-1" aria-label="Excluir" data-toggle="modal" data-target="#modalConfirmacaoExclusao" data-url="/producao/excluir/${id}/"><i class="fas fa-trash"></i></button>`;

botaoFiltrar.addEventListener('click', () => {
    const parametros = new URLSearchParams();
    
    if(produtoSelecionado.value){
        parametros.set('produto', produtoSelecionado.value);
    }
    if(dataInicial.value){
        parametros.set('data_inicial', dataInicial.value);
    }
    if(dataFinal.value){
        parametros.set('data_final', dataFinal.value);
    }    

    fetch('/producao/?' + parametros.toString())
        .then(resposta => {
            if(!resposta.ok){
                throw new Error(`Erro ao obter os dados. Status: ${resposta.status}. Mensagem: ${resposta.statusText}`);
            }

            return resposta.json();
        })
        .then(dados => {
            tabela.clear();

            const linhas = [];
            dados.forEach(elemento => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${elemento.produto__nome}</td>
                    <td>${elemento.quantidade_produzida}</td>
                    <td>${elemento.data}</td>
                    <td class="d-flex justify-content-center align-items-center gap-1">
                        ${botaoVer(elemento.id)}
                        ${botaoEditar(elemento.id)}
                        ${botaoExcluir(elemento.id)}
                    </td>
                `;
                linhas.push(tr);
            });
            tabela.rows.add(linhas).draw();
        })
        .catch(erro => {
            console.error(erro);
        })

});
