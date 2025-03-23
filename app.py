import streamlit as st
from datetime import date

st.title("🐾 ペット体調管理アプリ")

st.header("📋 今日の健康記録")

name = st.text_input("ペットの名前")
weight = st.number_input("体重 (kg)", min_value=0.0, step=0.1)
record_date = st.date_input("記録日", value=date.today())

if st.button("記録内容を確認"):
    st.subheader("✅ 入力された内容")
    st.write(f"名前: {name}")
    st.write(f"日付: {record_date}")
    st.write(f"体重: {weight} kg")
