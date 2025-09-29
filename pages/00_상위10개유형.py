import streamlit as st
import pandas as pd
import altair as alt

# 제목
st.title("MBTI 유형별 상위 10개 국가 분포")

# CSV 파일 불러오기
df = pd.read_csv("countriesMBTI_16types.csv")

# MBTI 컬럼 목록 (Country 제외)
mbti_types = df.columns[1:]

# 사용자 선택
selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

# 상위 10개 추출
top10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)

# Altair 막대 그래프
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_type, title=f"{selected_type} 비율"),
        y=alt.Y("Country", sort='-x', title="국가"),
        tooltip=["Country", selected_type]
    )
    .properties(width=600, height=400, title=f"{selected_type} 상위 10개 국가")
)

st.altair_chart(chart, use_container_width=True)
