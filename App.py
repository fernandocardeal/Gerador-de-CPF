import streamlit as st
from cpf import CPF

cpf_tool = CPF()

def App():
    st.title('CPF Tools')
    with st.sidebar:
        opcao = st.radio('Escolha a ferramenta', ['Gerar CPF', 'Validar CPF'])
    if opcao == 'Validar CPF':
        Validar_CPF()
    elif opcao == 'Gerar CPF':
        Gerar_CPF()

def Validar_CPF():
    st.subheader('Validador de CPF')
    cpf = st.text_input('Insira o CPF para ser validado', placeholder = '999.999.999-99', max_chars = 14)
    container = st.container()
    if st.button('Validar'):
        with container:
            if cpf_tool.cpf_validator(cpf):
                st.success('CPF Válido!', icon="✅")
            else:
                st.error('CPF Inválido', icon="🚨")

def Gerar_CPF():
    st.subheader('Gerador de CPF')
    estado = st.selectbox('Escolha o estado', ['QUALQUER UM'] + list(cpf_tool.estados.keys()))
    formatar =  st.radio('Formatar CPF', ['Sim', 'Não'], horizontal = True)
    container = st.container()
    if st.button('Gerar CPF'):
        cpf = cpf_tool.cpf_generator(estado = estado)
        with container:
            if formatar == 'Sim':
                st.markdown('### CPF Formatado')
                st.markdown(f'#### {cpf_tool.cpf_formatter(cpf)}')
            else:
                st.markdown('### CPF Não Formatado')
                st.markdown(f'### {cpf}')

if __name__ == '__main__':
    App()
