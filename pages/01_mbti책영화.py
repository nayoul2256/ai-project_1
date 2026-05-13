import streamlit as st

st.set_page_config(page_title="MBTI 책 & 영화 추천", page_icon="📚", layout="centered")

recommend_data = {
    "INTJ": {
        "book": "연금술사",
        "book_year": "1993",
        "book_reason": "깊은 의미를 생각하고 스스로의 길을 찾는 것을 좋아하는 사람에게 잘 맞습니다.",
        "movie": "인셉션",
        "movie_year": "2010",
        "movie_reason": "복잡한 구조와 논리적인 전개를 좋아하는 사람에게 적합합니다."
    },
    "INTP": {
        "book": "모모",
        "book_year": "1990년대 꾸준한 인기",
        "book_reason": "생각이 많고 본질을 탐구하는 성격의 사람에게 잘 맞습니다.",
        "movie": "인터스텔라",
        "movie_year": "2014",
        "movie_reason": "과학적 사고와 철학적인 질문을 좋아하는 사람에게 적합합니다."
    },
    "ENTJ": {
        "book": "누가 내 치즈를 옮겼을까",
        "book_year": "1998",
        "book_reason": "목표 지향적이고 변화를 빠르게 받아들이는 사람에게 추천됩니다.",
        "movie": "악마는 프라다를 입는다",
        "movie_year": "2006",
        "movie_reason": "리더십과 성공을 중요하게 생각하는 사람에게 잘 맞습니다."
    },
    "ENTP": {
        "book": "갈매기의 꿈",
        "book_year": "1990년대 재인기",
        "book_reason": "새로운 도전과 자유를 좋아하는 성격에 잘 어울립니다.",
        "movie": "아이언맨",
        "movie_year": "2008",
        "movie_reason": "창의적이고 도전적인 사람에게 적합합니다."
    },
    "INFJ": {
        "book": "어린 왕자",
        "book_year": "1990년대 꾸준한 인기",
        "book_reason": "감성적이고 깊이 있는 관계를 중요하게 생각하는 사람에게 추천됩니다.",
        "movie": "죽은 시인의 사회",
        "movie_year": "2000년대 재조명",
        "movie_reason": "의미 있는 삶과 가치관을 중요하게 생각하는 사람에게 적합합니다."
    },
    "INFP": {
        "book": "나의 라임오렌지나무",
        "book_year": "1990년대 인기",
        "book_reason": "감수성이 풍부하고 따뜻한 마음을 가진 사람에게 잘 맞습니다.",
        "movie": "월플라워",
        "movie_year": "2012",
        "movie_reason": "감정선이 섬세한 이야기를 좋아하는 사람에게 적합합니다."
    },
    "ENFJ": {
        "book": "아낌없이 주는 나무",
        "book_year": "1990년대 인기",
        "book_reason": "타인을 돕고 공감하는 것을 좋아하는 사람에게 추천됩니다.",
        "movie": "코코",
        "movie_year": "2017",
        "movie_reason": "사람 사이의 관계와 따뜻한 메시지를 중요하게 생각하는 사람에게 적합합니다."
    },
    "ENFP": {
        "book": "해리포터와 마법사의 돌",
        "book_year": "1998",
        "book_reason": "상상력이 풍부하고 새로운 세계를 좋아하는 사람에게 잘 맞습니다.",
        "movie": "라라랜드",
        "movie_year": "2016",
        "movie_reason": "꿈과 열정을 중요하게 생각하는 사람에게 적합합니다."
    },
    "ISTJ": {
        "book": "국화꽃 향기",
        "book_year": "2000 직전 인기",
        "book_reason": "책임감 있고 진중한 성격의 사람에게 추천됩니다.",
        "movie": "포레스트 검프",
        "movie_year": "2000년대 꾸준한 인기",
        "movie_reason": "성실함과 꾸준함의 가치를 중요하게 생각하는 사람에게 적합합니다."
    },
    "ISFJ": {
        "book": "괭이부리말 아이들",
        "book_year": "2000 전후 인기",
        "book_reason": "배려심 많고 따뜻한 사람에게 잘 맞습니다.",
        "movie": "인사이드 아웃",
        "movie_year": "2015",
        "movie_reason": "감정과 공감을 중요하게 생각하는 사람에게 적합합니다."
    },
    "ESTJ": {
        "book": "삼국지",
        "book_year": "1990년대 인기",
        "book_reason": "체계적이고 리더십이 강한 사람에게 추천됩니다.",
        "movie": "머니볼",
        "movie_year": "2011",
        "movie_reason": "전략적 사고와 현실적인 판단을 좋아하는 사람에게 적합합니다."
    },
    "ESFJ": {
        "book": "봉순이 언니",
        "book_year": "1998",
        "book_reason": "사람들과의 관계를 중요하게 생각하는 사람에게 잘 맞습니다.",
        "movie": "기적",
        "movie_year": "2021",
        "movie_reason": "따뜻한 인간관계를 좋아하는 사람에게 적합합니다."
    },
    "ISTP": {
        "book": "로빈슨 크루소",
        "book_year": "1990년대 꾸준한 인기",
        "book_reason": "독립적이고 현실적인 성격의 사람에게 추천됩니다.",
        "movie": "마션",
        "movie_year": "2015",
        "movie_reason": "문제를 직접 해결하는 스타일의 사람에게 적합합니다."
    },
    "ISFP": {
        "book": "키다리 아저씨",
        "book_year": "1990년대 인기",
        "book_reason": "조용하고 감성적인 사람에게 잘 맞습니다.",
        "movie": "미드나잇 인 파리",
        "movie_year": "2011",
        "movie_reason": "예술적 감성과 분위기를 좋아하는 사람에게 적합합니다."
    },
    "ESTP": {
        "book": "톰 소여의 모험",
        "book_year": "1990년대 인기",
        "book_reason": "활동적이고 즉흥적인 성격의 사람에게 추천됩니다.",
        "movie": "분노의 질주",
        "movie_year": "2001",
        "movie_reason": "스릴과 속도감을 즐기는 사람에게 적합합니다."
    },
    "ESFP": {
        "book": "오즈의 마법사",
        "book_year": "1990년대 인기",
        "book_reason": "밝고 사교적인 사람에게 잘 맞습니다.",
        "movie": "맘마미아!",
        "movie_year": "2008",
        "movie_reason": "즐겁고 에너지 넘치는 분위기를 좋아하는 사람에게 적합합니다."
    }
}

st.title("📚 MBTI 기반 책 & 영화 추천 프로그램")
st.write("MBTI를 선택하면 90년대 책 1권과 2000년대 영화 1편을 추천해드립니다!")

mbti_list = list(recommend_data.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if selected_mbti:
    data = recommend_data[selected_mbti]

    st.subheader(f"✨ {selected_mbti} 추천 결과")

    st.markdown("## 📖 추천 책 (90년대)")
    st.write(f"**책 제목:** {data['book']}")
    st.write(f"**출간 시기:** {data['book_year']}")
    st.write(f"**어떤 성격에 적합한가요?** {data['book_reason']}")

    st.divider()

    st.markdown("## 🎬 추천 영화 (2000년대)")
    st.write(f"**영화 제목:** {data['movie']}")
    st.write(f"**개봉 시기:** {data['movie_year']}")
    st.write(f"**어떤 사람에게 적합한가요?** {data['movie_reason']}")
