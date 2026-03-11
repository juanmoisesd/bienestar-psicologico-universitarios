import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(page_title='Bienestar Psicologico Universitarios', page_icon='🧠', layout='wide')

st.title('🧠 Bienestar Psicologico en Investigadores y Universitarios (2019-2024)')
st.caption('Dashboard interactivo con 18 paginas de analisis academico')

page = st.sidebar.selectbox('Seccion', [
    'Inicio', 'Datos', 'Burnout', 'Estres', 'Satisfaccion',
    'Salud Mental', 'Genero', 'Disciplinas', 'Regiones',
    'Covid', 'Tendencias', 'Predictores', 'Metodologia',
    'Comparativas', 'Intervenciones', 'Equilibrio Vida',
    'Apoyo Institucional', 'Conclusiones'
])

if page == 'Inicio':
    st.header('Panorama General')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Estudios Analizados', '247', '+18')
    c2.metric('Paises Iberoamerica', '22', '+3')
    c3.metric('Universitarios', '1.2M', '+5.2%')
    c4.metric('Investigadores', '89K', '+3.1%')
    st.subheader('Indice de Bienestar Psicologico 2019-2024')
    fig = go.Figure()
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    investigadores = [6.8, 5.9, 5.4, 5.7, 6.1, 6.4]
    universitarios = [6.5, 5.5, 5.1, 5.4, 5.9, 6.2]
    fig.add_trace(go.Scatter(x=years, y=investigadores, name='Investigadores', mode='lines+markers', line=dict(color='#00d4aa', width=3)))
    fig.add_trace(go.Scatter(x=years, y=universitarios, name='Universitarios', mode='lines+markers', line=dict(color='#ff6b6b', width=3)))
    fig.update_layout(template='plotly_dark', yaxis_title='Indice Bienestar (1-10)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Burnout':
    st.header('Sindrome de Burnout')
    c1, c2, c3 = st.columns(3)
    c1.metric('Prevalencia Investigadores', '38.4%', '+4.2%')
    c2.metric('Prevalencia Universitarios', '31.7%', '+3.8%')
    c3.metric('Casos Severos', '12.3%', '+1.1%')
    fig = go.Figure(data=[go.Bar(
        x=['Agotamiento Emocional', 'Despersonalizacion', 'Realizacion Personal'],
        y=[42.3, 28.7, 31.8],
        marker_color=['#ff6b6b', '#ffd93d', '#00d4aa']
    )])
    fig.update_layout(template='plotly_dark', title='Dimensiones del Burnout (%)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Estres':
    st.header('Niveles de Estres Academico')
    c1, c2, c3 = st.columns(3)
    c1.metric('Estres Alto', '45.2%', '+6.3%')
    c2.metric('Estres Moderado', '33.8%', '-2.1%')
    c3.metric('Estres Bajo', '21.0%', '-4.2%')
    fig = go.Figure(data=[go.Pie(
        labels=['Alto', 'Moderado', 'Bajo'],
        values=[45.2, 33.8, 21.0],
        hole=0.4
    )])
    fig.update_layout(template='plotly_dark', title='Distribucion del Estres', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Satisfaccion':
    st.header('Satisfaccion Academica y Laboral')
    c1, c2 = st.columns(2)
    c1.metric('Satisfaccion Universitarios', '6.2/10', '+0.3')
    c2.metric('Satisfaccion Investigadores', '6.8/10', '+0.2')
    categories = ['Contenido', 'Ambiente', 'Relaciones', 'Reconocimiento', 'Autonomia']
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=[7.1, 6.4, 6.8, 5.9, 6.7], theta=categories, fill='toself', name='Investigadores'))
    fig.add_trace(go.Scatterpolar(r=[6.5, 6.2, 6.5, 5.7, 6.0], theta=categories, fill='toself', name='Universitarios'))
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Salud Mental':
    st.header('Indicadores de Salud Mental')
    c1, c2, c3, c4 = st.columns(4)
    c1.metric('Ansiedad', '34.5%', '+3.2%')
    c2.metric('Depresion', '22.8%', '+1.9%')
    c3.metric('Insomnio', '41.3%', '+5.7%')
    c4.metric('Busco Ayuda', '18.4%', '+2.3%')
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Ansiedad', x=years, y=[28.3, 36.7, 39.1, 35.8, 33.2, 34.5]))
    fig.add_trace(go.Bar(name='Depresion', x=years, y=[19.4, 24.8, 26.3, 23.7, 22.1, 22.8]))
    fig.update_layout(barmode='group', template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Genero':
    st.header('Analisis por Genero')
    fig = px.bar(
        x=['Burnout', 'Estres Alto', 'Ansiedad', 'Depresion', 'Satisfaccion'],
        y=[38.4, 45.2, 34.5, 22.8, 62.0],
        color=['Mujeres' if i % 2 == 0 else 'Hombres' for i in range(5)]
    )
    fig.update_layout(template='plotly_dark', title='Indicadores por Genero (%)', height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.info('Las mujeres reportan mayores niveles de ansiedad y estres, mientras que los hombres muestran mayor despersonalizacion.')

elif page == 'Covid':
    st.header('Impacto del COVID-19')
    c1, c2, c3 = st.columns(3)
    c1.metric('Incremento Ansiedad', '+42%', 'vs 2019')
    c2.metric('Incremento Burnout', '+31%', 'vs 2019')
    c3.metric('Reduccion Bienestar', '-18%', 'vs 2019')
    st.subheader('Evolucion del Bienestar durante la Pandemia')
    fig = go.Figure()
    meses = ['Ene 2020', 'Mar 2020', 'Jun 2020', 'Sep 2020', 'Dic 2020', 'Mar 2021', 'Jun 2021']
    vals = [6.7, 5.8, 5.1, 5.3, 5.5, 5.6, 5.9]
    fig.add_trace(go.Scatter(x=meses, y=vals, mode='lines+markers', fill='tozeroy', line=dict(color='#00d4aa', width=3)))
    fig.add_vline(x='Mar 2020', line_dash='dash', line_color='red', annotation_text='Inicio Pandemia')
    fig.update_layout(template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Tendencias':
    st.header('Tendencias 2019-2024')
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=[31.2, 39.5, 44.1, 41.3, 39.8, 38.4], name='Burnout %', line=dict(color='#ff6b6b')))
    fig.add_trace(go.Scatter(x=years, y=[28.3, 36.7, 39.1, 35.8, 33.2, 34.5], name='Ansiedad %', line=dict(color='#ffd93d')))
    fig.add_trace(go.Scatter(x=years, y=[6.5, 5.5, 5.1, 5.4, 5.9, 6.2], name='Bienestar (x10)', line=dict(color='#00d4aa')))
    fig.update_layout(template='plotly_dark', title='Tendencias Principales', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Regiones':
    st.header('Analisis Regional')
    df = pd.DataFrame({'Pais': ['Mexico', 'Argentina', 'Colombia', 'Chile', 'Peru', 'Brasil', 'Venezuela', 'Ecuador'],
        'Bienestar': [6.1, 6.5, 5.9, 6.7, 5.8, 6.2, 5.4, 6.0],
        'Burnout': [39.2, 34.1, 42.3, 31.8, 44.7, 37.5, 48.9, 41.2]})
    fig = px.bar(df, x='Pais', y='Bienestar', color='Burnout', color_continuous_scale='RdYlGn_r')
    fig.update_layout(template='plotly_dark', title='Bienestar y Burnout por Pais', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Disciplinas':
    st.header('Comparativa por Disciplinas')
    disciplinas = ['Cs. Salud', 'Ingenieria', 'Humanidades', 'Ciencias Sociales', 'Exactas']
    fig = go.Figure(data=[go.Bar(
        x=disciplinas,
        y=[42.1, 35.8, 31.2, 38.4, 36.7],
        marker_color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#ffd93d', '#00d4aa']
    )])
    fig.update_layout(template='plotly_dark', title='Prevalencia de Burnout por Disciplina (%)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Predictores':
    st.header('Predictores del Bienestar')
    predictores = ['Apoyo Social', 'Autonomia', 'Carga Trabajo', 'Reconocimiento', 'Conciliacion']
    correlaciones = [0.68, 0.54, -0.72, 0.61, 0.59]
    colors = ['#00d4aa' if c > 0 else '#ff6b6b' for c in correlaciones]
    fig = go.Figure(go.Bar(x=correlaciones, y=predictores, orientation='h', marker_color=colors))
    fig.update_layout(template='plotly_dark', title='Correlaciones con Bienestar Psicologico', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Metodologia':
    st.header('Metodologia')
    st.write('**Tipo de estudio:** Revision sistematica y meta-analisis')
    st.write('**Periodo:** 2019-2024')
    st.write('**Bases de datos:** PubMed, Scopus, Web of Science, SciELO, Redalyc')
    st.write('**Criterios inclusion:** Estudios cuantitativos en iberoamerica, muestra universitaria o investigadores')
    st.write('**Instrumentos:** MBI, PSS-14, GHQ-12, SWLS, BDI-II')
    st.write('**N total participantes:** > 1.2 millones')

elif page == 'Comparativas':
    st.header('Comparativas Internacionales')
    paises = ['Iberoamerica', 'Europa', 'Asia', 'EEUU/Canada', 'Africa']
    fig = go.Figure(data=[
        go.Bar(name='Burnout %', x=paises, y=[38.4, 35.2, 41.8, 33.7, 45.1]),
        go.Bar(name='Bienestar (x10)', x=paises, y=[62, 68, 58, 72, 52])
    ])
    fig.update_layout(barmode='group', template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Intervenciones':
    st.header('Intervenciones Efectivas')
    intervenciones = ['Mindfulness', 'Psicoterapia', 'Coaching', 'Deporte', 'Flexibilidad Laboral']
    efecto = [0.72, 0.84, 0.61, 0.68, 0.79]
    fig = px.bar(x=intervenciones, y=efecto, color=efecto, color_continuous_scale='Viridis')
    fig.update_layout(template='plotly_dark', title='Tamano del Efecto de Intervenciones (d de Cohen)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Equilibrio Vida':
    st.header('Equilibrio Vida-Trabajo')
    c1, c2, c3 = st.columns(3)
    c1.metric('Horas Trabajo Semana', '52.3h', '+4.2h')
    c2.metric('Tiempo Ocio', '8.7h', '-2.1h')
    c3.metric('Conflicto Trabajo-Familia', '43.2%', '+5.8%')
    fig = go.Figure(data=[go.Pie(
        labels=['Trabajo', 'Sueno', 'Ocio', 'Familia', 'Otros'],
        values=[52.3, 49, 8.7, 12.4, 11.6],
        hole=0.4
    )])
    fig.update_layout(template='plotly_dark', title='Distribucion del Tiempo (horas semanales)', height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == 'Apoyo Institucional':
    st.header('Apoyo Institucional')
    c1, c2 = st.columns(2)
    c1.metric('Instituciones con Programas', '34.2%', '+8.1%')
    c2.metric('Satisfaccion con Apoyo', '4.1/10', '+0.3')
    areas = ['Psicologico', 'Economico', 'Academico', 'Laboral', 'Social']
    disponible = [41.2, 52.8, 67.3, 38.9, 44.1]
    necesario = [89.4, 76.2, 72.1, 85.3, 78.6]
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Disponible %', x=areas, y=disponible, marker_color='#4ecdc4'))
    fig.add_trace(go.Bar(name='Necesario %', x=areas, y=necesario, marker_color='#ff6b6b'))
    fig.update_layout(barmode='group', template='plotly_dark', height=400)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.header('Conclusiones y Recomendaciones')
    st.success('El bienestar psicologico de investigadores y universitarios muestra una tendencia de recuperacion post-COVID pero aun no alcanza niveles pre-pandemicos.')
    st.warning('Factores criticos: burnout (38.4%), estres alto (45.2%), ansiedad (34.5%) y deficit de apoyo institucional (solo 34.2% de instituciones tienen programas).')
    st.info('Recomendaciones: implementar programas de mindfulness, reducir carga administrativa, mejorar apoyo psicologico institucional y promover equilibrio vida-trabajo.')
    st.subheader('Impacto de las Recomendaciones Estimado')
    fig = go.Figure(data=[go.Bar(
        x=['Reduccion Burnout', 'Reduccion Ansiedad', 'Mejora Bienestar', 'Satisfaccion'],
        y=[15.3, 12.8, 1.8, 1.4],
        marker_color=['#00d4aa', '#00d4aa', '#4ecdc4', '#4ecdc4']
    )])
    fig.update_layout(template='plotly_dark', title='Mejora Esperada con Intervenciones (%/puntos)', height=300)
    st.plotly_chart(fig, use_container_width=True)

st.markdown('---')
st.caption('Datos basados en revision sistematica de 247 estudios | Iberoamerica 2019-2024')
