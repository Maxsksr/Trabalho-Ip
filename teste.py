import streamlit as st
import random

@st.cache_data
def escolher_pais():
    paises = ['Suriname', 'Brasil', 'Argentina', 'Uruguai', 'Peru', 'Colômbia', 'Bolívia', 'Paraguai', 'Equador', 'Guiana', 'Chile', 'Venezuela']
    return random.choice(paises).lower()

def embaralhar_palavra(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    return ''.join(letras)

def main():
    tentativas_restantes = 3
    pontuacao = 0
    
    st.title("Jogo de Anagrama")
    st.write(f"Pontuação: {pontuacao}")
    st.text(f"Tentativas restantes: {tentativas_restantes}")

    jogo_iniciado = False

    if not jogo_iniciado:
        jogo_iniciado = True

    if jogo_iniciado:
        if tentativas_restantes > 0:
            pais_selecionado = escolher_pais()
            palavra_embaralhada = embaralhar_palavra(pais_selecionado)

            st.write("Tente adivinhar o país!")
            st.write("Palavra Embaralhada: ", palavra_embaralhada.capitalize())
            palpite = st.text_input("Insira seu palpite:").lower()

            feedback_placeholder = st.empty()

            if st.button("Confirmar"):
                if palpite == pais_selecionado:
                    feedback_placeholder.success("Parabéns! Você acertou o país: " + pais_selecionado.capitalize())
                    jogo_iniciado = False
                    st.cache_data.clear()
                else:
                    tentativas_restantes -= 1
                    feedback_placeholder.warning("Palpite incorreto. Tente novamente!")
                if tentativas_restantes == 0:
                        st.error("Número máximo de tentativas alcançados. Jogo encerrado")
                        st.cache_data.clear()
                        tentativas_restantes = 3
                if pontuacao == 12:
                    st.success("Você ganhou. Parabéns!")
                    st.cache_data.clear()
                    tentativas_restantes = 3
if __name__ == "_main_":
    main()