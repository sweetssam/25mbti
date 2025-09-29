import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("🌍 국가별 MBTI 분포 대시보드 ✨")

# CSV 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# 국가 선택 박스
country = st.selectbox("📌 나라를 선택하세요:", df["Country"].sort_values())

# 해당 국가 데이터 선택
country_data = df[df["Country"] == country].melt(
    id_vars=["Country"], var_name="MBTI", value_name="비율"
)

# Plotly 막대 그래프
fig = px.bar(
    country_data,
    x="MBTI",
    y="비율",
    text="비율",
    color="MBTI",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title=f"🇨🇳 {country}의 MBTI 분포 💡"
)

# 그래프 꾸미기
fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
fig.update_layout(
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    title_x=0.5,
    bargap=0.3,
    plot_bgcolor="white"
)

# 출력
st.plotly_chart(fig, use_container_width=True)
