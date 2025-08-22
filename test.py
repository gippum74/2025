import streamlit as st

st.set_page_config(page_title="스킨케어 & 메이크업 추천💄", page_icon="💅", layout="wide")

st.markdown("<h1 style='text-align: center;'>🌸✨ 맞춤형 스킨케어 & 메이크업 추천 💖💄</h1>", unsafe_allow_html=True)
st.write("당신만의 피부 타입과 톤을 찾아서 ✨ 완벽한 뷰티 루틴 ✨을 만들어드려요 🧴💋🌈")

# 1️⃣ 피부 타입 알기
st.markdown("## 🧴 1️⃣ 피부 타입 확인하기")
know_type = st.radio("피부 타입을 알고 계신가요? 🤔", ["네, 알고 있어요 😎", "아니요, 잘 모르겠어요 🙈"])

if know_type == "네, 알고 있어요 😎":
    skin_type = st.selectbox("👉 피부 타입을 선택하세요!", 
                             ["건성 🌵", "지성 💦", "수분부족지성 🌊💧", "복합성 ⚖️", "민감성 🌸", "중성 🌿"])
else:
    st.write("피부 특징을 선택해 주세요 👇")
    dry = st.checkbox("😖 세안 후 피부가 자주 땅긴다")
    oily = st.checkbox("😅 얼굴에 유분기가 쉽게 올라온다")
    combo = st.checkbox("🤔 T존은 번들, U존은 건조하다")
    sensitive = st.checkbox("🥺 피부가 민감하고 자극에 예민하다")
    tight_and_oily = st.checkbox("😵 겉은 번들거리는데 속은 건조하고 당긴다")

    # 피부 타입 매칭 로직
    if dry and not oily:
        skin_type = "건성 🌵"
    elif oily and not dry and not tight_and_oily:
        skin_type = "지성 💦"
    elif combo:
        skin_type = "복합성 ⚖️"
    elif tight_and_oily:
        skin_type = "수분부족지성 🌊💧"
    elif sensitive:
        skin_type = "민감성 🌸"
    else:
        skin_type = "중성 🌿"

st.success(f"👉 당신의 피부 타입은 **{skin_type}** 입니다! 🎉")

# 2️⃣ 루틴 선택
st.markdown("## ⏰ 2️⃣ 루틴 선택하기")
routine = st.radio("어떤 루틴이 필요하신가요? ✨", ["모닝 루틴 ☀️", "나이트 루틴 🌙"])

# 3️⃣ 스킨케어 추천
st.markdown("## 💆‍♀️ 3️⃣ 맞춤 스킨케어 추천")

def skincare_recommend(skin_type, routine):
    if routine == "모닝 루틴 ☀️":
        if "건성" in skin_type:
            return [
                "🧴 라네즈 크림 클렌저",
                "🌱 이니스프리 그린티 토너",
                "💧 닥터지 수분크림",
                "🌞 라로슈포제 안뗄리오스 선크림"
            ]
        elif "지성" in skin_type:
            return [
                "🌾 한율 쌀 클렌징폼",
                "🌊 아벤느 클린앙스 토너",
                "🔵 라로슈포제 에빠끌라 젤 크림",
                "🕶️ 비오템 아쿠아 수분 선크림"
            ]
        elif "수분부족지성" in skin_type:
            return [
                "🌿 약산성 젠틀 클렌저",
                "💧 히알루론산 토너",
                "✨ 하다라보 수퍼 히알루론산 에센스",
                "🌞 닥터지 그린마일드 업 선크림"
            ]
        elif "복합성" in skin_type:
            return [
                "🌋 이니스프리 화산송이 클렌저",
                "🌼 키엘 칼렌듈라 토너",
                "❄️ 아이오페 젤크림",
                "🌊 에스쁘아 워터 스플래쉬 선크림"
            ]
        elif "민감성" in skin_type:
            return [
                "🌱 시드물 무자극 클렌저",
                "🌊 아벤느 진정 토너",
                "🌿 시카페어 크림",
                "🌞 이지듀 센서티브 선크림"
            ]
        else:
            return [
                "🧴 크리니크 젠틀 클렌저",
                "🌸 키엘 울트라 토너",
                "💧 시세이도 모이스처 크림",
                "🌞 헤라 UV 미스트 쿠션"
            ]
    else: # 나이트 루틴 🌙
        if "건성" in skin_type:
            return [
                "🧴 크리니크 마일드 클렌저",
                "🌼 키엘 칼렌듈라 토너",
                "✨ SK-II 피테라 에센스",
                "🌙 에스티로더 나이트 리페어",
                "💦 라네즈 수분 슬리핑팩"
            ]
        elif "지성" in skin_type:
            return [
                "🌋 이니스프리 화산송이 클렌저",
                "💧 라로슈포제 토너",
                "🌟 아이오페 바이오 에센스",
                "❄️ CNP 젤 크림"
            ]
        elif "수분부족지성" in skin_type:
            return [
                "🌿 약산성 젠틀 클렌저",
                "💧 히알루론산 토너",
                "🌙 미샤 타임레볼루션 나이트리페어",
                "🧴 닥터자르트 세라마이딘 크림"
            ]
        elif "복합성" in skin_type:
            return [
                "🌿 네이처리퍼블릭 약산성 클렌저",
                "⚖️ 아벤느 밸런싱 토너",
                "✨ 비오템 아쿠아 수르스",
                "💧 키엘 수분 크림"
            ]
        elif "민감성" in skin_type:
            return [
                "🌸 벨리프 젠틀 클렌저",
                "🌊 라로슈포제 토너",
                "🌿 시카페어 세럼",
                "🌼 아벤느 시칼파트 크림"
            ]
        else:
            return [
                "🧴 크리니크 폼 클렌저",
                "🌺 설화수 윤조 토너",
                "✨ 록시땅 이모르뗄 에센스",
                "🌙 시세이도 나이트 크림"
            ]

for step in skincare_recommend(skin_type, routine):
    st.markdown(f"<div style='padding:6px; border-radius:10px; background-color:#f8f9fa; margin-bottom:5px;'>{step}</div>", unsafe_allow_html=True)

# 4️⃣ 색조 화장품 추천
st.markdown("## 💄 4️⃣ 색조 화장품 추천")
skin_tone = st.radio("피부 톤을 선택하세요 🎨", ["쿨톤 ❄️", "웜톤 ☀️", "뉴트럴 🌿"])
favorite_color = st.color_picker("당신이 어울리고 싶은 색은? 🎨", "#ff69b4")
st.markdown(f"🎨 선택한 색상: <span style='color:{favorite_color}; font-size:20px;'>⬤</span>", unsafe_allow_html=True)

if "쿨톤" in skin_tone:
    st.markdown("### 💋 립")
    st.write("- 맥 'Ruby Woo' 💄")
    st.write("- 롬앤 '제로 매트 립스틱 쿨톤 MLBB'")
    st.write("- 페리페라 '잉크 더 벨벳 쿨톤'")

    st.markdown("### 🧴 쿠션")
    st.write("- 헤라 블랙 쿠션 21C 쿨 바닐라")
    st.write("- 라네즈 네오 쿠션 매트 쿨톤")

    st.markdown("### 🍑 블러셔")
    st.write("- 나스 'Orgasm'")
    st.write("- 투쿨포스쿨 아트클래스 블러셔 로지")

    st.markdown("### 👁️ 섀도우")
    st.write("- 에뛰드 '플레이 컬러 아이즈 쿨톤'")
    st.write("- 클리오 '프로 아이 팔레트 쿨톤 무드'")

elif "웜톤" in skin_tone:
    st.markdown("### 💋 립")
    st.write("- 에스쁘아 '오렌지 립스틱' 🍊")
    st.write("- 클리오 '매드 매트 립'")
    st.write("- 롬앤 '제로 벨벳 립 웜톤 MLBB'")

    st.markdown("### 🧴 쿠션")
    st.write("- 에스쁘아 프로 테일러 쿠션 비 글로우")
    st.write("- 구달 청귤 비타C 쿠션")

    st.markdown("### 🍑 블러셔")
    st.write("- 투쿨포스쿨 '체리 블러셔' 🍒")
    st.write("- 3CE 무드 레시피 블러셔 피치")

    st.markdown("### 👁️ 섀도우")
    st.write("- 에뛰드 '플레이 컬러 아이즈 웜톤'")
    st.write("- 클리오 '프로 아이 팔레트 웜 브라운'")

else:
    st.markdown("### 💋 립")
    st.write("- 입생로랑 MLBB 립스틱 💄")
    st.write("- 디올 루즈 포에버 MLBB")

    st.markdown("### 🧴 쿠션")
    st.write("- 설화수 퍼펙팅 쿠션 뉴트럴")
    st.write("- 라네즈 네오 쿠션 글로우")

    st.markdown("### 🍑 블러셔")
    st.write("- 샤넬 'Rose Initiale' 🌹")
    st.write("- 맥 미네랄라이즈 블러셔")

    st.markdown("### 👁️ 섀도우")
    st.write("- 나스 '뉴트럴 섀도우 팔레트'")
    st.write("- 어반디케이 '네이키드 팔레트'")

st.balloons()
st.success("✨ 모든 추천이 완료되었습니다! ✨")
