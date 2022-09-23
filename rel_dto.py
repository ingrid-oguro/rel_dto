import pandas as pd
import altair as alt
import streamlit as st
import pip
pip.main(["install", "openpyxl"])
df1 = pd.read_excel('/content/drive/MyDrive/Relatórios_20222/Relatório turma de direito/base_disciplina.xlsx')
df2 = pd.read_excel('/content/drive/MyDrive/Relatórios_20222/Relatório turma de direito/df_geral.xlsx')

periodo = sorted(df1.CODPERLET.unique())
periodo_selecionado = st.selectbox('Periodo',periodo)
df_periodo = df1.query('CODPERLET == @periodo_selecionado ')


grafico_dispersao = alt.Chart(df_periodo).mark_circle(size=100).encode(
    alt.X('Percentual de Frequencia',axis=alt.Axis(format='%', title='Frequência') ),
    alt.Y('Média Final',axis=alt.Axis(title='Nota', orient = "left") ),
    tooltip = ['NOME','RA'] ).interactive()

st.altair_chart(grafico_dispersao, use_container_width=True)



aluno = sorted(df2.NOME.unique())
aluno_selecionado = st.selectbox('Aluno',aluno)
base_aluno = df2.query('NOME == @aluno_selecionado')

grafico_barra = alt.Chart(base_aluno).mark_bar().encode(
        y=alt.Y('Média Final'),
        x=alt.X('DISCIPLINA', title = None), 
        color=alt.Color('SIT_DISC:N'),
        ).properties(width=260, height=300).facet(
        column=alt.Column('CODPERLET:N', title = None),
        ).resolve_scale(x='independent')
st.altair_chart(grafico_barra, use_container_width=True)
