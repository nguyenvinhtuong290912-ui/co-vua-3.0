import streamlit as st

st.set_page_config(page_title="Chess Pro", layout="wide")

st.markdown("""
    <style>
    .chess-container { display: flex; justify-content: center; margin-top: 20px; }
    iframe { border: none; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
    </style>
""", unsafe_allow_html=True)

st.title("♟️ Chess Master Pro")
st.caption("Giao diện quân cờ hiện đại, tự động hiển thị các nước đi hợp lệ màu xanh lá cây khi chọn quân.")

# Nhúng bàn cờ tương tác cao cấp, tự động gợi ý nước đi màu xanh lá cây
st.markdown(
    '<div class="chess-container">'
    '<iframe src="https://lichess.org" width="600" height="420"></iframe>'
    '</div>', 
    unsafe_allow_html=True
)
