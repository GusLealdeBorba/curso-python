const element = document.getElementById('id_cep');
const maskOptions = {mask: '00.000-000'};
const mask = IMask(element, maskOptions);


function consultarCep(elemento){
    let inputCep = elemento.target;
    let cep = inputCep.value.replace(".","").replace("-", "");
    if (cep.length !== 8)
        return

    fetch( `https://viacep.com.br/ws/${cep}/json`)
        .then((response ) => response.json())
        .then((data) => {
            if (data["erro"] === "true") {
                alert("CEP inexistente")
                document.getElementById("id_cep").select()
                document.getElementById("id_cep").focus()
                return
            }
            document.getElementById("id_uf").value = data["uf"]
            document.getElementById("id_cidade").value = data["localidade"]
            document.getElementById("id_bairro").value = data["bairro"]
            document.getElementById("id_rua").value = data["logradouro"]
            document.getElementById("id_numero").focus()
        })
        .catch((error) => {
            alert("Não foi possível buscar o endereço")
            console.error(error)
        })
}

document.getElementById("id_cep").onblur = consultarCep;

function submitFormDadosEndereco(event){
    let form = document.getElementById("form-endereco");
    // Verificar se o form está válido
    if (!form.checkValidity()){
        // Obter tag que está inválida
        let invalido = form.querySelector(":invalid")
        // Exibir mensagem de erro
        invalido.reportValidity();
        return;
    }
    form.submit()
}

document.getElementById("form-endereco-botao-cadastrar").onclick = submitFormDadosEndereco
document.getElementById("id_cep").onkeyup = consultarCep;