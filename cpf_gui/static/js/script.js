var cpfData = ["00000000000","000.000.000-00"]
document.getElementById("cpf-box").value = cpfData[0]
var estado;

const gerarCpf = () => {
    var select = document.getElementById("estados");
    estado = select.options[select.selectedIndex].value;
    fetch(`http://127.0.0.1:8000/api/cpf/gerar/?estado=${estado}`)
    .then(response => {
        if(!response.ok) {
            throw new Error("Erro na requisição")
        }
        return response.json()
    })
    .then(data => {
        document.getElementById("cpf-box").style.borderColor = "white"
        mostrarCpf(coletarCpf() === cpfData[0] ? data[0]: data[1])
        cpfData = Object.values(data)
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
    if(cpfData.indexOf(cpf) !== -1) {
        mostrarCpf(cpf === cpfData[0] ? cpfData[1]: cpfData[0])
    } else {
        cpfData = [
            cpf.replace(/\D/g, ""), 
            cpf.replace(/\D/g, "").replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4')
        ]
        mostrarCpf(cpf === cpfData[0] ? cpfData[1]: cpfData[0])
    }
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
        cpfBox.style.borderColor = data["estado"] ? "limegreen": "red"
    })
    .catch(error => {
        console.error("Erro:", error)
    })
}