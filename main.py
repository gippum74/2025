import streamlit as st

# MBTI별 추천 여행지 데이터 (예시)
mbti_destinations = {
    "INTJ": ["아이슬란드 - 고요한 자연", "교토 - 전통과 사색의 도시"],
    "INFP": ["발리 - 자연과 휴양", "프라하 - 감성적인 도시"],
    "ENTP": ["뉴욕 - 다이나믹한 도시", "베를린 - 자유로운 예술의 도시"],
    "ESFP": ["하와이 - 파티와 휴양", "바르셀로나 - 활기찬 해변 도시"],
    # 필요에 따라 더 추가
}

st.title("🌍 MBTI 여행지 추천기")
st.write("당신의 MBTI를 선택하면, 어울리는 여행지를 추천해드립니다!")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요", list(mbti_destinations.keys()))

# 추천 결과 출력
if mbti:
    st.subheader(f"✨ {mbti} 유형 추천 여행지")
    destinations = mbti_destinations[mbti]
    for d in destinations:
        st.write(f"- {d}")
