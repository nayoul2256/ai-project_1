import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌱", layout="centered")

career_data = {
    "INTJ": [
        {
            "job": "데이터 분석가",
            "major": "통계학과, 컴퓨터공학과",
            "personality": "논리적이고 계획적인 사람, 혼자 깊이 생각하는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "연구원",
            "major": "생명과학과, 화학과",
            "personality": "탐구심이 강하고 문제 해결을 좋아하는 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "INTP": [
        {
            "job": "프로그래머",
            "major": "컴퓨터공학과",
            "personality": "창의적이고 분석적인 사람",
            "salary": "평균 연봉 약 4,600만원"
        },
        {
            "job": "교수",
            "major": "교육학과, 전공 관련 학과",
            "personality": "지식을 깊게 탐구하고 설명하는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 5,500만원"
        }
    ],
    "ENTJ": [
        {
            "job": "경영 컨설턴트",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표 지향적인 사람",
            "salary": "평균 연봉 약 5,200만원"
        },
        {
            "job": "기업 관리자",
            "major": "경영학과, 경제학과",
            "personality": "결단력이 있고 조직 운영을 잘하는 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ENTP": [
        {
            "job": "마케팅 기획자",
            "major": "광고홍보학과",
            "personality": "아이디어가 많고 도전을 즐기는 사람",
            "salary": "평균 연봉 약 4,300만원"
        },
        {
            "job": "창업가",
            "major": "경영학과",
            "personality": "새로운 시도를 좋아하고 추진력이 강한 사람",
            "salary": "평균 연봉 약 5,000만원 이상"
        }
    ],
    "INFJ": [
        {
            "job": "상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어나고 사람을 돕는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 3,800만원"
        },
        {
            "job": "작가",
            "major": "문예창작과",
            "personality": "깊은 사고와 표현을 좋아하는 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],
    "INFP": [
        {
            "job": "디자이너",
            "major": "시각디자인과",
            "personality": "감수성이 풍부하고 창의적인 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "사회복지사",
            "major": "사회복지학과",
            "personality": "배려심이 많고 따뜻한 사람",
            "salary": "평균 연봉 약 3,400만원"
        }
    ],
    "ENFJ": [
        {
            "job": "교사",
            "major": "교육학과",
            "personality": "사람을 이끄는 것을 좋아하고 책임감이 강한 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "인사담당자",
            "major": "경영학과",
            "personality": "소통 능력이 좋고 협력을 중요하게 생각하는 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ENFP": [
        {
            "job": "크리에이터",
            "major": "미디어학과",
            "personality": "활발하고 표현력이 좋은 사람",
            "salary": "평균 연봉 다양함"
        },
        {
            "job": "기획자",
            "major": "문화콘텐츠학과",
            "personality": "새로운 아이디어를 즐기는 사람",
            "salary": "평균 연봉 약 4,200만원"
        }
    ],
    "ISTJ": [
        {
            "job": "공무원",
            "major": "행정학과",
            "personality": "성실하고 책임감이 강한 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 체계적인 사람",
            "salary": "평균 연봉 약 6,000만원"
        }
    ],
    "ISFJ": [
        {
            "job": "간호사",
            "major": "간호학과",
            "personality": "배려심이 많고 책임감 있는 사람",
            "salary": "평균 연봉 약 4,300만원"
        },
        {
            "job": "유치원 교사",
            "major": "유아교육과",
            "personality": "인내심이 많고 따뜻한 사람",
            "salary": "평균 연봉 약 3,500만원"
        }
    ],
    "ESTJ": [
        {
            "job": "경찰관",
            "major": "경찰행정학과",
            "personality": "규칙을 중요하게 여기고 책임감 있는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "관리자",
            "major": "경영학과",
            "personality": "리더십과 실행력이 좋은 사람",
            "salary": "평균 연봉 약 5,000만원"
        }
    ],
    "ESFJ": [
        {
            "job": "승무원",
            "major": "항공서비스과",
            "personality": "친절하고 서비스 정신이 강한 사람",
            "salary": "평균 연봉 약 4,200만원"
        },
        {
            "job": "간호사",
            "major": "간호학과",
            "personality": "사람을 돕는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 4,300만원"
        }
    ],
    "ISTP": [
        {
            "job": "정비사",
            "major": "자동차공학과",
            "personality": "손으로 직접 해결하는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 4,000만원"
        },
        {
            "job": "엔지니어",
            "major": "기계공학과",
            "personality": "실용적이고 분석적인 사람",
            "salary": "평균 연봉 약 4,800만원"
        }
    ],
    "ISFP": [
        {
            "job": "플로리스트",
            "major": "원예학과",
            "personality": "감각적이고 조용한 사람",
            "salary": "평균 연봉 약 3,300만원"
        },
        {
            "job": "패션 디자이너",
            "major": "패션디자인과",
            "personality": "미적 감각이 뛰어난 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ],
    "ESTP": [
        {
            "job": "영업 전문가",
            "major": "경영학과",
            "personality": "활동적이고 사람 만나는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 4,500만원"
        },
        {
            "job": "스포츠 트레이너",
            "major": "체육학과",
            "personality": "에너지가 많고 실전형인 사람",
            "salary": "평균 연봉 약 3,800만원"
        }
    ],
    "ESFP": [
        {
            "job": "배우",
            "major": "연극영화과",
            "personality": "표현력이 풍부하고 사교적인 사람",
            "salary": "평균 연봉 다양함"
        },
        {
            "job": "이벤트 플래너",
            "major": "관광경영학과",
            "personality": "밝고 사람들과 어울리는 것을 좋아하는 사람",
            "salary": "평균 연봉 약 4,000만원"
        }
    ]
}

st.title("🌱 MBTI 기반 진로 추천 프로그램")
st.write("MBTI를 선택하면 추천 진로 2가지를 알려드립니다!")

mbti_list = list(career_data.keys())
selected_mbti = st.selectbox("MBTI를 선택하세요", mbti_list)

if selected_mbti:
    st.subheader(f"📘 {selected_mbti} 추천 진로")

    for idx, career in enumerate(career_data[selected_mbti], start=1):
        st.markdown(f"### {idx}. {career['job']}")
        st.write(f"**적합한 학과:** {career['major']}")
        st.write(f"**적합한 성격:** {career['personality']}")
        st.write(f"**평균 연봉:** {career['salary']}")
        st.divider()
