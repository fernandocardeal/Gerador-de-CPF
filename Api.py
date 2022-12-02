from flask import Flask, jsonify
from cpf import CPF

my_app = Flask(__name__)
cpf_tool = CPF()

@my_app.route("/")
def cpf_geral():
    cpf = cpf_tool.cpf_generator()
    return jsonify({0: cpf_tool.cpf_formatter(cpf), 1: cpf})

@my_app.route("/<estado>")
def cpf_condicional(estado):
    try:
        cpf = cpf_tool.cpf_generator(estado.upper())
        return jsonify({0: cpf_tool.cpf_formatter(cpf), 1: cpf})
    except:
        cpf_geral()

if __name__ == "__main__":
    my_app.run() #https://cpftools.fernandosanto27.repl.co/
