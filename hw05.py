import streamlit as st
import pandas as pd

st.set_page_config(page_title="품목군별 데이터 분석", layout="wide")

st.title("품목군별 데이터 분석")
st.markdown("이 애플리케이션은 품목군별 데이터에 대한 정보를 제공합니다. 품목군을 선택하여 관련 데이터를 확인하세요.")

data = pd.read_csv('income.csv', encoding='utf-8', skiprows=1)

st.sidebar.header("품목 선택")
품목군별1 = st.sidebar.selectbox("품목군별(1) 선택", data["품목군별(1)"].unique())
품목군별2 = st.sidebar.selectbox("품목군별(2) 선택", data[data["품목군별(1)"] == 품목군별1]["품목군별(2)"].unique())

# 선택된 데이터 필터링
filtered_data = data[(data["품목군별(1)"] == 품목군별1) & (data["품목군별(2)"] == 품목군별2)]

# 결과 출력
st.markdown("---")
if not filtered_data.empty:
    st.header(f"선택된 데이터: {품목군별2}")

    # 주요 통계 정보 카드 형식으로 출력
    st.subheader("주요 통계 정보")
    total_quantity = filtered_data["수량"].values[0] if filtered_data["수량"].values[0] != '-' else 'N/A'
    total_income = filtered_data["총수입 (원)"].values[0]
    management_cost = filtered_data["경영비 (원)"].values[0]
    income = filtered_data["소득 (원)"].values[0]
    income_rate = filtered_data["소득률 (%)"].values[0]

    st.markdown(f"""
    - **수량**: {total_quantity}
    - **총수입 (원)**: {total_income:,}
    - **경영비 (원)**: {management_cost:,}
    - **소득 (원)**: {income:,}
    - **소득률 (%)**: {income_rate}%
    """)
else:
    st.warning("선택한 품목에 대한 데이터가 없습니다.")