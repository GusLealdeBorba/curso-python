function obterDadosContato() {
    let idContato = 1
    fetch(`/publico/contato/${idContato}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            document.getElementById("id_valor"). value = data.valor
            document.getElementById("id_tipo"). value = data.tipo
        })
        .catch(error => {
            console.log(error)
            alert("Ocorreu um erro ao carregar os dados do contato")
        })
}