import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt    

class Management:

    def __init__(self):
        self.add_commodity() 

    def add_commodity(self):
        st.title('Gerenciamento de commodities')
        first_column, second_column = st.columns(2)

        if 'commodities_list' not in st.session_state:
            st.session_state.commodities_list = []

        with first_column:
            commodity_name = st.text_input('Insira o nome da commodity')
        
        with second_column:
            commodity_price = st.number_input('Insira o preço da commodity')
        
        if st.button('Adicionar commodity'):
            st.session_state.commodities_list.append((commodity_name, commodity_price))

        self.create_table(st.session_state.commodities_list)

    def create_table(self, commodities_list):
        #criando tabela
        commodities_df = pd.DataFrame(commodities_list, columns=['Commodity_name', 'Price'])
        st.dataframe(commodities_df)
        self.create_graph(commodities_df)
    
    def create_graph(self, commodities_df):
        #criando gráfico
        if st.checkbox('Exibir gráfico'):
            fig, ax = plt.subplots()
            ax.scatter(commodities_df['Commodity_name'], commodities_df['Price'])
            st.pyplot(fig)