var cpf_formatado = "000.000.000-00"
var cpf_nao_formatado = "00000000000"
document.getElementById("cpf-box").value = cpf_formatado

const gerarCpf = () => {
    fetch("http://127.0.0.1:8000/api/cpf/gerar/")
    .then(response => {
        if(!response.ok) {
            throw new Error("Erro na requisição")
        }
        return response.json()
    })
    .then(data => {
        document.getElementById("cpf-box").style.borderColor = "white"
        mostrarCpf(coletarCpf() === cpf_nao_formatado ? data[0]: data[1])
        cpf_nao_formatado = data[0]
        cpf_formatado = data[1]
    })
    .catch(error => {
        console.error("Erro:", error)
    })
}

const mostrarCpf = (cpf) => {
    let cpfBox = document.getElementById("cpf-box")
    cpfBox.value = cpf
}


const coletarCpf = () => {
    let cpfBox = document.getElementById("cpf-box")
    return cpfBox.value
}

const formatarCpf = () => {
    let cpf = coletarCpf()
    mostrarCpf(cpf === cpf_nao_formatado ? cpf_formatado: cpf_nao_formatado)
}

const validarCpf = () => {
    let cpf = coletarCpf().replace(/\D/g, "")
    fetch(`http://127.0.0.1:8000/api/cpf/validar/?cpf=${cpf}`)
    .then(response => {
        if(!response.ok) {
            throw new Error("Erro na requisição")
        }
        return response.json()
    })
    .then(data => {
        let cpfBox = document.getElementById("cpf-box")
        if(data["estado"]) {
            cpfBox.style.borderColor = "limegreen"
        } else {
            cpfBox.style.borderColor = "red"
        }
    })
    .catch(error => {
        console.error("Erro:", error)
    })
}