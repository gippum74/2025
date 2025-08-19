import streamlit as st

# ---------------------------
# 데이터 준비
# ---------------------------
mbti_destinations = {
    "INTJ": {
        "title": "🧠✨ 전략가 INTJ",
        "places": [
            {"name": "❄️ 아이슬란드", "desc": "끝없는 고요와 오로라의 향연 🌌"},
            {"name": "⛩️ 교토", "desc": "전통과 사색의 고즈넉한 거리 🏯"}
        ]
    },
    "INFP": {
        "title": "🌸💭 몽상가 INFP",
        "places": [
            {"name": "🏝️ 발리", "desc": "자연과 휴양, 감성 충전 🌊"},
            {"name": "🏰 프라하", "desc": "감성을 자극하는 동화 같은 도시 ✨"}
        ]
    },
    "ENTP": {
        "title": "⚡🎭 아이디어 뱅크 ENTP",
        "places": [
            {"name": "🗽 뉴욕", "desc": "잠들지 않는 다이나믹한 도시 🌆"},
            {"name": "🎨 베를린", "desc": "자유와 예술이 살아 숨 쉬는 곳 🖌️"}
        ]
    },
    "ESFP": {
        "title": "🎉🌴 파티 피플 ESFP",
        "places": [
            {"name": "🌺 하와이", "desc": "끝없는 파티와 휴양 🌞"},
            {"name": "🏖️ 바르셀로나", "desc": "열정과 해변이 만나는 곳 🍷"}
        ]
    }
}

# ---------------------------
# UI 꾸미기
# ---------------------------
st.set_page_config(page_title="MBTI 여행 추천 ✈️", page_icon="🌍", layout="centered")

st.markdown(
    """
    <h1 style="text-align:center; font-size:50px;">
    🌈✨ MBTI 여행지 추천기 ✨🌈
    </h1>
    <p style="text-align:center; font-size:20px;">
    당신의 MBTI를 선택하면 <b>찰떡같은 여행지</b>를 추천해드립니다! 🚀🌍💖
    </p>
    """,
    unsafe_allow_html=True
)

# 선택 박스
mbti = st.selectbox("👉 당신의 MBTI를 골라주세요!", list(mbti_destinations.keys()))

if mbti:
    data = mbti_destinations[mbti]

    st.markdown(
        f"""
        <h2 style="text-align:center; font-size:40px;">{data['title']}</h2>
        """,
        unsafe_allow_html=True
    )

    for place in data["places"]:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
                padding: 20px; 
                border-radius: 20px; 
                margin: 15px 0; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                color: #333;
            ">
                <h3 style="font-size:28px;">{place['name']}</h3>
                <p style="font-size:18px;">{place['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
