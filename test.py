import streamlit as st

st.set_page_config(page_title="스킨케어 & 메이크업 추천", page_icon="💅", layout="wide")

st.markdown("<h1 style='text-align: center;'>✨ 맞춤형 스킨케어 & 메이크업 추천 💖</h1>", unsafe_allow_html=True)
st.write("피부 타입과 톤에 맞는 뷰티 루틴을 추천해드려요 🧴💄")

st.image("https://cdn-icons-png.flaticon.com/512/10647/10647465.png", width=120)

# 1️⃣ 피부 타입 알기
st.subheader("🧴 Step 1. 피부 타입 확인하기")
know_type = st.radio("피부 타입을 알고 계신가요?", ["네, 알고 있어요", "아니요, 잘 모르겠어요"])

if know_type == "네, 알고 있어요":
    skin_type = st.selectbox("👉 피부 타입을 선택하세요", 
                             ["건성", "지성", "수분부족지성", "복합성", "민감성", "중성"])
else:
    st.write("피부 특징을 선택해 주세요 👇")
    dry = st.checkbox("세안 후 피부가 자주 땅긴다")
    oily = st.checkbox("얼굴에 유분기가 쉽게 올라온다")
    combo = st.checkbox("T존은 번들, U존은 건조하다")
    sensitive = st.checkbox("피부가 민감하고 자극에 예민하다")
    tight_and_oily = st.checkbox("겉은 번들거리는데 속은 건조하다")

    if dry and not oily:
        skin_type = "건성"
    elif oily and not dry and not tight_and_oily:
        skin_type = "지성"
    elif combo:
        skin_type = "복합성"
    elif tight_and_oily:
        skin_type = "수분부족지성"
    elif sensitive:
        skin_type = "민감성"
    else:
        skin_type = "중성"

st.success(f"👉 당신의 피부 타입은 **{skin_type}** 입니다!")

# 2️⃣ 루틴 선택
st.subheader("⏰ Step 2. 루틴 선택하기")
routine = st.radio("어떤 루틴이 필요하신가요?", ["🌞 모닝 루틴", "🌙 나이트 루틴"])

# 3️⃣ 스킨케어 추천
st.subheader("💆 Step 3. 맞춤 스킨케어 추천")

def skincare_recommend(skin_type, routine):
    if routine == "🌞 모닝 루틴":
        if skin_type == "건성":
            return [
                {"name": "크림 클렌저", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234318.png"},
                {"name": "그린티 토너", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234333.png"},
                {"name": "수분크림", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234323.png"},
                {"name": "선크림", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234342.png"}
            ]
        elif skin_type == "지성":
            return [
                {"name": "폼 클렌저", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234318.png"},
                {"name": "진정 토너", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234333.png"},
                {"name": "젤 크림", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234323.png"},
                {"name": "산뜻한 선크림", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234342.png"}
            ]
        else:
            return [
                {"name": "기본 클렌저", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234318.png"},
                {"name": "기본 토너", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234333.png"},
                {"name": "기본 크림", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234323.png"},
                {"name": "기본 선크림", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234342.png"}
            ]
    else:  # 🌙 나이트 루틴
        return [
            {"name": "저녁 클렌저", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234318.png"},
            {"name": "저녁 토너", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234333.png"},
            {"name": "에센스", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234323.png"},
            {"name": "나이트 크림", "img": "https://cdn-icons-png.flaticon.com/512/5234/5234342.png"}
        ]

for item in skincare_recommend(skin_type, routine):
    col1, col2 = st.columns([1,4])
    with col1:
        st.image(item["img"], width=60)
    with col2:
        st.write(item["name"])

# 4️⃣ 색조 화장품 추천
st.subheader("💄 Step 4. 색조 화장품 추천")
skin_tone = st.radio("피부 톤을 선택하세요", ["쿨톤 ❄️", "웜톤 🌞", "뉴트럴 🌸"])
favorite_color = st.color_picker("어울리고 싶은 색상 선택 🎨", "#ff69b4")
st.markdown(f"선택한 색상: <span style='color:{favorite_color}; font-size:20px;'>⬤</span>", unsafe_allow_html=True)

if skin_tone == "쿨톤 ❄️":
    st.write("💋 립 : 맥 Ruby Woo")
    st.write("🧴 쿠션 : 헤라 블랙 쿠션")
    st.write("🍑 블러셔 : 나스 Orgasm")
    st.write("👁️ 섀도우 : 클리오 쿨톤 팔레트")
elif skin_tone == "웜톤 🌞":
    st.write("💋 립 : 에스쁘아 오렌지 립스틱")
    st.write("🧴 쿠션 : 에스쁘아 프로 테일러 쿠션")
    st.write("🍑 블러셔 : 투쿨포스쿨 체리 블러셔")
    st.write("👁️ 섀도우 : 클리오 웜톤 팔레트")
else:
    st.write("💋 립 : 입생로랑 MLBB")
    st.write("🧴 쿠션 : 설화수 퍼펙팅 쿠션")
    st.write("🍑 블러셔 : 샤넬 Rose Initiale")
    st.write("👁️ 섀도우 : 어반디케이 네이키드 팔레트")

st.balloons()
st.success("✨ 모든 추천이 완료되었습니다! ✨")
