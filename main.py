import streamlit as st

def main():
    st.set_page_config(page_title="Ferramentas PDF e Imagem", layout="wide", page_icon="🖇")

    st.markdown(
        """
        <style>
            .main { background-color: #f0fff0; }
            .sidebar .sidebar-content { background-color: #d8f3dc; }
            .stButton>button { background-color: #95d5b2; color: black; }
            .stButton>button:hover { background-color: #74c69d; color: white; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Ferramentas para PDF e Imagem")
    
    with st.sidebar:
        st.header("Menu")
        menu_option = st.selectbox("Escolha uma opção:", [
            "PDF para Word",
            "Extrair imagens de PDF",
            "Extrair textos de PDF imagem",
            "Extrair texto de imagem",
            "Extrair planilhas de PDF",
            "Salvar tabelas de sites em planilhas Excel"
        ])

    if menu_option == "PDF para Word":
        pdf_to_word()
    elif menu_option == "Extrair imagens de PDF":
        extract_images_from_pdf()
    elif menu_option == "Extrair textos de PDF imagem":
        extract_text_from_pdf_image()
    elif menu_option == "Extrair texto de imagem":
        extract_text_from_image()
    elif menu_option == "Extrair planilhas de PDF":
        extract_spreadsheets_from_pdf()
    elif menu_option == "Salvar tabelas de sites em planilhas Excel":
        save_tables_from_web_to_excel()

def pdf_to_word():
    st.subheader("PDF para Word")
    st.write("Converta arquivos PDF em documentos Word editáveis.")
    uploaded_file = st.file_uploader("Envie o arquivo PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("Processando o arquivo...")
        # Aqui será implementada a funcionalidade de conversão

def extract_images_from_pdf():
    st.subheader("Extrair Imagens de PDF")
    st.write("Extraia todas as imagens contidas em um arquivo PDF.")
    uploaded_file = st.file_uploader("Envie o arquivo PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("Processando o arquivo...")
        # Aqui será implementada a funcionalidade de extração de imagens

def extract_text_from_pdf_image():
    st.subheader("Extrair Texto de PDF Imagem")
    st.write("Extraia textos de PDFs escaneados ou baseados em imagem.")
    uploaded_file = st.file_uploader("Envie o arquivo PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("Processando o arquivo...")
        # Aqui será implementada a funcionalidade de OCR para PDFs

def extract_text_from_image():
    st.subheader("Extrair Texto de Imagem")
    st.write("Extraia textos diretamente de imagens.")
    uploaded_file = st.file_uploader("Envie a imagem", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.write("Processando a imagem...")
        # Aqui será implementada a funcionalidade de OCR para imagens

def extract_spreadsheets_from_pdf():
    st.subheader("Extrair Planilhas de PDF")
    st.write("Extraia dados tabulares de arquivos PDF para planilhas.")
    uploaded_file = st.file_uploader("Envie o arquivo PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("Processando o arquivo...")
        # Aqui será implementada a funcionalidade de extração de tabelas

def save_tables_from_web_to_excel():
    st.subheader("Salvar Tabelas de Sites em Planilhas Excel")
    st.write("Extraia tabelas de páginas da web e salve como arquivos Excel.")
    url = st.text_input("Insira a URL do site contendo a tabela:")
    if url:
        st.write("Processando a URL...")
        # Aqui será implementada a funcionalidade de extração de tabelas da web

if __name__ == "__main__":
    main()
