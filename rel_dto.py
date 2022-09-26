import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import pip
pip.main(["install", "openpyxl"])
PAGE_CONFIG = {"page_title": "CIA - Centro de Inteligência do Apoio ao aluno", "page_icon": ":globe_with_meridians:", "layout": "wide"}
st.set_page_config(**PAGE_CONFIG)



#Base
df1 = pd.read_excel('df_geral.xlsx')
dfa = pd.read_excel('disciplina_dto.xlsx')
df2 = dfa.drop(dfa[dfa.RA == 40456].index)
df2["Frequencia"]= (df2["Percentual de Frequencia"]*10)

df4 = df2.drop(['Percentual de Frequencia','Unnamed: 0'], axis=1)

df_long = df4.melt(id_vars=['CODPERLET','PERIODO','RA','NOME','COMPLEMENTO','CODTURMA','DISCIPLINA','SIT_DISC','TIPOETAPA'],
             var_name="PROVA",  # rename
             value_name="NOTA")

#colunas
col1,col2,col3 = st.columns((0.2,8,1))

#Botão


with col2:
    #Titulo
    st.subheader('Relatório Direito')
    periodo = sorted(df1.CODPERLET.unique())
    periodo_selecionado = st.selectbox('Periodo',periodo)
    df_periodo = df1.query('CODPERLET == @periodo_selecionado ')
    #grafico
    grafico_dispersao = alt.Chart(df_periodo).mark_circle(size=100).encode(
        alt.X('Percentual de Frequencia',scale=alt.Scale(zero=False),axis=alt.Axis(format='%', title='Frequência') ),
        alt.Y('Média Final',scale=alt.Scale(zero=False) ,axis=alt.Axis(title='Nota', orient = "left") ),
        tooltip = ['NOME','RA'] ).interactive().properties(width=900,height=400)  

    st.altair_chart(grafico_dispersao, use_container_width=True)


    with st.expander("Ver base"):
        st.write("""
            Base de dados extraída do totvs em 23/09/2022
        """)
        st.table(df_periodo)

    st.write(" ")
    st.write(" ")
#Aluno

    aluno = sorted(df_long.NOME.unique())
    aluno_selecionado = st.selectbox('Aluno',aluno)
    base_aluno = df_long.query('NOME == @aluno_selecionado')
    st.write(" Nota ")



colb1, colb2, colb3 = st.columns((2,2,1))
with colb1:
    cod1 = 20211
    sem1 = base_aluno.query('CODPERLET == @cod1')
    st.markdown("<h5 style='text-align: center; color: black;'>20211</h5>", unsafe_allow_html=True)
    b = alt.Chart(sem1).mark_bar().encode(
            x=alt.X('PROVA', title=None,axis=alt.Axis(labels=False)),
            y=alt.Y('NOTA'),
            color=alt.Color('PROVA:N',legend=None),
            column=alt.Column('DISCIPLINA:N', title = None, header=alt.Header(labelAngle=-90, labelAlign='right', labelFontSize=12))
        ).properties(width=50, height=150)
    st.altair_chart(b, use_container_width=False)

with colb2:

    st.markdown("<h5 style='text-align: center; color: black;'>20212</h5>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    cod2 = 20212
    sem2 = base_aluno.query('CODPERLET == @cod2')
    c = alt.Chart(sem2).mark_bar().encode(
            x=alt.X('PROVA', title = None,axis=alt.Axis(labels=False)),
            y=alt.Y('NOTA'),
            color='PROVA:N',
            column=alt.Column('DISCIPLINA:N', title = None, header=alt.Header(labelAngle=-90, labelAlign='right',labelFontSize=12))
        ).properties(width=50, height=150)
    st.altair_chart(c, use_container_width=False)

#colc1, colc2 = st.columns((2,2))
with colb1:
    st.markdown("<h5 style='text-align: center; color: black;'>20221</h5>", unsafe_allow_html=True)    
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    cod3 = 20221
    sem3 = base_aluno.query('CODPERLET == @cod3')

    c = alt.Chart(sem3).mark_bar().encode(
            x=alt.X('PROVA', title=None,axis=alt.Axis(labels=False)),
            y=alt.Y('NOTA'),
            color=alt.Color('PROVA:N',legend=None),
            column=alt.Column('DISCIPLINA:N', title = None, header=alt.Header(labelAngle=-90, labelAlign='right',labelFontSize=12))
        ).properties(width=40, height=150)
    st.altair_chart(c, use_container_width=False)

with colb2:
    cod4 = 20222
    sem4 = base_aluno.query('CODPERLET == @cod4')
    st.markdown("<h5 style='text-align: center; color: black;'>20222</h5>", unsafe_allow_html=True)
    d = alt.Chart(sem4).mark_bar().encode(
            x=alt.X('PROVA', title=None,axis=alt.Axis(labels=False)),
            y=alt.Y('NOTA'),
            color=alt.Color('PROVA:N',legend=None),
            column=alt.Column('DISCIPLINA:N', title = None, header=alt.Header(labelAngle=-90, labelAlign='right',labelFontSize=12))
        ).properties(width=30, height=150)
    st.altair_chart(d, use_container_width=False)

with st.expander("Ver base:"):
        st.write("""
            Base de dados extraída do totvs em 23/09/2022
        """)
        st.table(base_aluno)
