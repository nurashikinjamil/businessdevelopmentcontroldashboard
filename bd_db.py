import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd



html_header="""
<head>
<title>BDControlDB</title>
<meta charset="utf-8">
<meta name="keywords" content="business development control, dashboard, management, EVA">
<meta name="description" content="business development control dashboard">
<meta name="author" content="Nur Ashikin Jamil">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:#008080; font-family:Georgia"> BUSINESS DEVELOPMENT CONTROL <br>
 <h2 style="color:#008080; font-family:Georgia"> DASHBOARD</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""
st.set_page_config(page_title="Business Development Control Dashboard", page_icon="", layout="wide")
st.markdown('<style>body{background-color: #fbfff0}</style>',unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
data=pd.read_excel('curva.xlsx')

html_card_header1="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Total Tender/RFQ Year 2021</h3>
  </div>
</div>
"""
html_card_footer1="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value</p>
  </div>
</div>
"""
html_card_header2="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Participated</h3>
  </div>
</div>
"""
html_card_footer2="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value</p>
  </div>
</div>
"""
html_card_header3="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Won</h3>
  </div>
</div>
"""
html_card_footer3="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value≤</p>
  </div>
</div>
"""
html_card_header4="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Lost</h3>
  </div>
</div>
"""
html_card_footer4="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value≤</p>
  </div>
</div>
"""
html_card_header5="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Under Evaluation</h3>
  </div>
</div>
"""
html_card_footer5="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value≤</p>
  </div>
</div>
"""
html_card_header6="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Retender</h3>
  </div>
</div>
"""
html_card_footer6="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value≤</p>
  </div>
</div>
"""
html_card_header7="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Opportunities</h3>
  </div>
</div>
"""
html_card_footer7="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value≤</p>
  </div>
</div>
"""
html_card_header8="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Declined</h3>
  </div>
</div>
"""
html_card_footer8="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Value≤</p>
  </div>
</div>
"""
### Block 1#########################################################################################
with st.beta_container():
    col1, col2, col3, col4, col5, col6, col7 = st.beta_columns([1,10,1,10,1,20,1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header1, unsafe_allow_html=True)
        fig_cv = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=1.05,
            number={"font": {"size": 22, 'color': "#008080", 'family': "Arial"}, "valueformat": "#,##0"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [None, 1.5], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "#06282d"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 1], 'color': '#FF4136'},
                    {'range': [1, 1.5], 'color': '#3D9970'}]}))

        fig_cv.update_layout(paper_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Arial"}, height=135, width=250,
                             margin=dict(l=10, r=10, b=15, t=20))
        st.plotly_chart(fig_cv)
        st.markdown(html_card_footer1, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header2, unsafe_allow_html=True)
        fig_sv = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=0.95,
            number={"font": {"size": 22, 'color': "#008080", 'family': "Arial"}, "valueformat": "#,##0"},
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [None, 1.5], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "#06282d"},
                'bgcolor': "white",
                'steps': [
                    {'range': [0, 1], 'color': '#FF4136'},
                    {'range': [1, 1.5], 'color': '#3D9970'}]}))
        fig_sv.update_layout(paper_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Arial"}, height=135, width=250,
                             margin=dict(l=10, r=10, b=15, t=20))
        st.plotly_chart(fig_sv)
        st.markdown(html_card_footer2, unsafe_allow_html=True)
    with col5:
        st.write("")
    with col6:
        y = data.loc[data.Sector == 'Total']
        y = data.loc[data.Sector == 'Total']
        fig_hh = go.Figure()
        fig_hh.add_trace(go.Bar(
            x=y['Date of submission'],
            y=y['Value(RM)],
            name='Value(RM)',
            marker_color='#FF4136'
        ))
        fig_hh.update_layout(barmode='group', title={'text': 'List of Tender 2021', 'x': 0.5}, paper_bgcolor="#fbfff0",
                             plot_bgcolor="#fbfff0", font={'color': "#008080", 'family': "Georgia"}, height=250, width=540,
                             legend=dict(orientation="h",
                                         yanchor="top",
                                         y=0.99,
                                         xanchor="left",
                                         x=0.01),
                             margin=dict(l=5, r=1, b=1, t=25))
        fig_hh.update_xaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=6, rangemode="tozero",
                            showgrid=False, gridwidth=0.5, gridcolor='#F7F7F7')
        fig_hh.update_yaxes(showline=True, linewidth=1, linecolor='#F7F7F7', mirror=True, nticks=10, rangemode="tozero",
                            showgrid=False, gridwidth=0.5, gridcolor='#F7F7F7')
        st.plotly_chart(fig_hh)
    with col7:
        st.write("")

html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_subtitle="""
<h2 style="color:#008080; font-family:Georgia;"> List of Tender 2021: </h2>
"""
st.markdown(html_subtitle, unsafe_allow_html=True)

html_table=""" 
<table>
  <tr style="background-color:#eef9ea; color:#008080; font-family:Georgia; font-size: 15px">
    <th style="width:130px"></th>
    <th style="width:90px">PIC</th>
    <th style="width:90px">Stage of Sale</th>
    <th style="width:90px">Probability</th>
    <th style="width:90px">Priority Status</th>
    <th style="width:90px">Category</th>
    <th style="width:90px">Industries</th>
  </tr>
  <tr style="height: 40px; color:#008080; font-size: 14px">
    <th>ICT</th>
    <th>70,00%</th>
    <th>68,50%</th>
    <th>70.000</th>
    <th>0,99</th>
    <th>1,09</th>
  </tr>
  <tr style="background-color:#eef9ea; height: 40px; color:#008080; font-size: 14px">
    <th>Comms</th>
    <th>50,00%</th>
    <th>45,50%</th>
    <th>10.000</th>
    <th>0,95</th>
    <th>0,98</th>
  </tr>
  <tr style="height: 40px; color:#008080; font-size: 14px">
    <th>EPC</th>
    <th>30,00%</th>
    <th>30,00%</th>
    <th>60.000</th>
    <th>0,99</th>
    <th>1,01</th>
  </tr>
  <tr style="background-color:#eef9ea; height: 40px; color:#008080; font-size: 14px">
    <th>Power</th>
    <th>20,00%</th>
    <th>15,00%</th>
    <th>40.000</th>
    <th>0,90</th>
    <th>0,98</th>
  </tr>
</table>
"""
### Block 2#########################################################################################
with st.beta_container():
    col1, col2, col3 = st.beta_columns([12,1,12])
    with col1:
        st.markdown(html_table, unsafe_allow_html=True)
    with col2:
        st.write("")
    with col3:
        # *******Gantt Chart
        df = pd.DataFrame([
            dict(Disc="PIC", Start='2021-01-04', Finish='2021-08-10'),
            dict(Disc="SS", Name='Unsolicated proposal', Name='Potential',Name='Submitted',Name='Accepted',Name='Rejected',Name='Under evaluation',Name='Future'),
            dict(Disc="Prob", Start='0%', Finish='100%'),
            dict(Disc="Prio", Start='High', Finish='Low'),
            dict(Disc="CTG", Name='Leasing', Name='Main Contractor', Name='Trading', Name='Sub-contractor', Name='Maintenance'),
            dict(Disc="IDSTRY", Name='Railway', Name='IT', Name='Info-comm', Name='Power', Name='Telecommunication', Name='Big Data'),   
        ])
        fig2 = px.timeline(df, x_start="Start", x_end="Finish", y='Disc')
        fig2.update_yaxes(autorange="reversed")
        fig2.update_layout(title={'text': "Main dates", 'x': 0.5}, plot_bgcolor="#eef9ea", paper_bgcolor="#eef9ea",
                           font={'color': "#008080", 'family': "Georgia"}, height=340, width=550, margin=dict(
                l=51, r=5, b=10, t=50))
        fig2.update_traces(marker_color='#17A2B8', selector=dict(type='bar'))
        st.plotly_chart(fig2)

disciplinas= ['ICT', 'Comms', 'EPC', 'Power']

selected_disc = st.selectbox(' Select discipline', disciplinas)
html_br="""
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

html_card_header4="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 10px; width: 250px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 5px 0;">Progress For Selected Discipline</h5>
  </div>
</div>
"""
html_card_footer4="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Value (%)</p>
  </div>
</div>
"""
html_card_header5="""
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 10px; width: 250px;
   height: 50px;">
    <h5 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 5px 0;">Spend Hours For Selected Discipline</h5>
  </div>
</div>
"""
html_card_footer5="""
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 250px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Montly Relative Change (%)</p>
  </div>
</div>
"""
st.markdown(html_line, unsafe_allow_html=True)
