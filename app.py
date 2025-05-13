import streamlit as st
from PIL import Image
from rembg import remove

st.set_page_config(page_title="🍽️ 음식 배경 변경기", layout="centered")
st.title("🍽️ AI 음식 배경 변경기")

uploaded_food = st.file_uploader("▶ 음식 이미지를 업로드하세요", type=["jpg", "png"])
uploaded_bg = st.file_uploader("▶ 새 배경 이미지를 업로드하세요", type=["jpg", "png"])

if uploaded_food and uploaded_bg:
    food = Image.open(uploaded_food)
    bg = Image.open(uploaded_bg).convert("RGBA")
    food_no_bg = remove(food).convert("RGBA")
    bg = bg.resize(food_no_bg.size)
    result = Image.alpha_composite(bg, food_no_bg)

    st.subheader("🖼️ 결과 이미지")
    st.image(result)

    result.save("result.png")
    with open("result.png", "rb") as file:
        st.download_button("📥 이미지 다운로드", file, "food_with_new_bg.png")
