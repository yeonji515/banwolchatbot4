import streamlit as st

# 선생님 데이터 (이름, 과목, 부서, 담임학급)
teachers = {
    "김대호": {"subject": "역사", "department": "교무기획부", "class": None,"office": "3층 제1교무실"},
    "서은진": {"subject": "국어", "department": "미래연구부", "class": None,"office": "3층 제1교무실"},
    "황하늬": {"subject": "음악", "department": "학생안전부", "class": None,"office": "1층 행정실 옆"},
    "정호윤": {"subject": "영어", "department": "교육과정부", "class": None,"office": "3층 제1교무실"},
    "엄기영": {"subject": "영어", "department": "인문사회부", "class": None,"office": "3층 제2교무실"},
    "박미정": {"subject": "통과", "department": "자연과학부", "class": None,"office": "3층 제2교무실"},
    "오정아": {"subject": "체육", "department": "예술체육부", "class": None,"office": "3층 제2교무실"},
    "배경미": {"subject": "정보", "department": "교육정보부", "class": None,"office": "2층 도서관 옆"},
    "김지현": {"subject": "진로", "department": "진로진학부", "class": None,"office": "4층"},
    "김혜선": {"subject": "수학", "department": "1학년부", "class": None,"office": "2층 교무실"},
    "송인필": {"subject": "물리", "department": "2학년부", "class": None,"office": "4층 교무실"},
    "유형우": {"subject": "수학", "department": "3학년부", "class": None,"office": "5층 교무실"},
    "편경림": {"subject": "영어", "department": "교무기획부", "class": None,"office": "3층 제1교무실"},
    "김경희": {"subject": "영어", "department": "미래연구부", "class": None,"office": "3층 제1교무실"},
    "윤효근": {"subject": "통사", "department": "학생안전부", "class": None,"office": "1층 행정실 옆"},
    "한숙희": {"subject": "지리", "department": "교육과정부", "class": None,"office": "3층 제1교무실"},
    "박병찬": {"subject": "지리", "department": "인문사회부", "class": None,"office": "3층 제2교무실"},
    "이지선": {"subject": "생과", "department": "자연과학부", "class": None,"office": "3층 제2교무실"},
    "임종수": {"subject": "체육", "department": "예술체육부", "class": None,"office": "3층 제2교무실"},
    "김진옥": {"subject": "화학", "department": "교육정보부", "class": None,"office": "2층 도서관 옆"},
    "어경선": {"subject": "수학", "department": "진로진학부", "class": None,"office": "4층"},
    "이지수": {"subject": "통사", "department": "1학년부", "class": "1학년 1반","office": "2층 교무실"},
    "유의영": {"subject": "수학", "department": "2학년부", "class": "2학년 1반","office": "4층 교무실"},
    "최영주": {"subject": "일사", "department": "3학년부", "class": "3학년 1반","office": "5층 교무실" },
    "김현미": {"subject": "일사", "department": "교무기획부", "class": None,"office": "3층 제1교무실"},
    "김지선": {"subject": "수학", "department": "미래연구부", "class": None,"office": "3층 제1교무실"},
    "김종규": {"subject": "윤리", "department": "학생안전부", "class": None,"office": "1층 행정실 옆"},
    "서은영": {"subject": "일본어", "department": "교육과정부", "class": None,"office": "3층 제1교무실"},
    "정고은": {"subject": "보건", "department": "예술체육부", "class": None,"office": "3층 제2교무실"},
    "강자은": {"subject": "음악", "department": "1학년부", "class": "1학년 2반","office": "2층 교무실"},
    "김상길": {"subject": "지학", "department": "2학년부", "class": "2학년 2반","office": "4층 교무실"},
    "이지우": {"subject": "영어", "department": "3학년부", "class": "3학년 2반","office": "5층 교무실"},
    "이수정": {"subject": "영양", "department": "예술체육부", "class": None,"office": "3층 제2교무실"},
    "안진희": {"subject": "수학", "department": "1학년부", "class": "1학년 3반","office": "2층 교무실"},
    "김성혜": {"subject": "생과", "department": "2학년부", "class": "2학년 3반","office": "4층 교무실"},
    "신선임": {"subject": "국어", "department": "3학년부", "class": "3학년 3반","office": "5층 교무실"},
    "이유진": {"subject": "영어", "department": "교무기획부", "class": None,"office": "3층 제1교무실"},
    "이보향": {"subject": "영어", "department": "미래연구부", "class": None,"office": "3층 제1교무실"},
    "유호진": {"subject": "체육", "department": "학생안전부", "class": None,"office": "1층 행정실 옆"},
    "조영은": {"subject": "수학", "department": "교무기획부", "class": None,"office": "3층 제1교무실"},
    "김아름": {"subject": "상담", "department": "학생안전부", "class": None,"office": "1층 행정실 옆"},
    "송유빈": {"subject": "국어", "department": "1학년부", "class": "1학년 4반","office": "2층 교무실"},
    "성지은": {"subject": "영어", "department": "2학년부", "class": "2학년 4반","office": "4층 교무실"},
    "장윤경": {"subject": "국어", "department": "3학년부", "class": "3학년 4반","office": "5층 교무실"},
    "서산나": {"subject": "특수", "department": "교무기획부", "class": None,"office": "3층 제1교무실"},
    "조성분": {"subject": "통과", "department": "1학년부", "class": "1학년 5반","office": "2층 교무실"},
    "김가희A": {"subject": "국어", "department": "2학년부", "class": "2학년 5반","office": "4층 교무실"},
    "남유정": {"subject": "화학", "department": "3학년부", "class": "3학년 5반","office": "5층 교무실"},
    "김동건": {"subject": "특수", "department": "교무기획부", "class": None,"office": "3층 제1교무실"},
    "남현지": {"subject": "미술", "department": "1학년부", "class": "1학년 6반","office": "2층 교무실"},
    "성지영": {"subject": "체육", "department": "2학년부", "class": "2학년 6반","office": "4층 교무실"},
    "도만구": {"subject": "물리", "department": "3학년부", "class": "3학년 6반","office": "5층 교무실"},
    "김나연": {"subject": "국어", "department": "1학년부", "class": "1학년 7반","office": "2층 교무실"},
    "강영미": {"subject": "국어", "department": "2학년부", "class": "2학년 7반","office": "4층 교무실"},
    "이동현": {"subject": "지학", "department": "3학년부", "class": "3학년 7반","office": "5층 교무실"},
    "김지연": {"subject": "역사", "department": "1학년부", "class": "1학년 8반","office": "2층 교무실"},
    "조준": {"subject": "중국어", "department": "2학년부", "class": "2학년 8반","office": "4층 교무실"},
    "강미현": {"subject": "윤리", "department": "3학년부", "class": "3학년 8반","office": "5층 교무실"},
    "김가희B": {"subject": "국어", "department": "1학년부", "class": "1학년 9반","office": "2층 교무실"},
    "주효진": {"subject": "일사", "department": "2학년부", "class": "2학년 9반","office": "4층 교무실"},
    "문숙희": {"subject": "국어", "department": "3학년부", "class": "3학년 9반","office": "5층 교무실"},
    "고태열": {"subject": "기술", "department": "1학년부", "class": "1학년 10반","office": "2층 교무실"},
    "문주희": {"subject": "윤리", "department": "2학년부", "class": "2학년 10반","office": "4층 교무실"},
    "호가영": {"subject": "수학", "department": "3학년부", "class": "3학년 10반","office": "5층 교무실"}
}
import streamlit as st

# 🎉 행사 일정 데이터
events = {
    "2차 지필평가": "6월 26일 ~ 7월 1일",
    "SW·AI 캠프": "7월 2일 ~ 7월 3일",
    "직업탐색 프로그램": "7월 8일",
    "3학년 전국연합학력평가": "7월 10일",
    "학교자율교육과정": "7월 8일 ~ 7월 11일",
    "방학식": "7월 18일"
}

# 📘 담임 검색 함수
for name in teachers:
        if name in user_input:
            info = teachers[name]
            st.success(f"👩‍🏫 {name} 선생님 정보")
            st.write(f"과목: {info['subject']}")
            st.write(f"담당학년: {info['grade']}")
            st.write(f"교무실: {info['office']}")
            found = True
            break

    # 🔍 과목 검색
    if not found:
        for subject in subjects:
            if subject in user_input:
                st.success(f"📘 '{subject}' 과목 담당 선생님:")
                for t in subjects[subject]:
                    st.write(f"- {t['grade']} {t['teacher']} 선생님 (교무실: {t['office']})")
                found = True
                break

# 🎯 행사 검색 함수
def search_events(user_input):
    for event_name, event_date in events.items():
        if event_name in user_input:
            return f"🎉 {event_name}: {event_date}"
    return None

# 🖥️ Streamlit UI
st.title("🏫 화성반월고 챗봇")
st.write("학교 생활에 필요한 정보를 알려드릴게요!")

user_input = st.text_input("무엇이 궁금한가요? 예: '고태열 선생님', '국어', '방학식 언제야'")
if user_input:
    found = False

    # 🔍 선생님 이름 검색
    for name in teachers:
        if name in user_input:
            info = teachers[name]
            st.success(f"👩‍🏫 {name} 선생님은 {info['grade']} '{info['subject']}' 과목을 담당하고, 교무실은 '{info['office']}'에 있습니다.")
            found = True
            break

    # 🔍 과목명 검색
    if not found:
        for subject in subjects:
            if subject in user_input:
                st.success(f"📘 '{subject}' 과목 담당 선생님:")
                for t in subjects[subject]:
                    st.write(f"- {t['grade']} {t['teacher']} 선생님 (교무실: {t['office']})")
                found = True
                break

    # 🔍 학교 행사 검색
    if not found:
        for event in school_events:
            if event in user_input:
                st.success(f"🎉 {event}: {school_events[event]}")
                found = True
                break

    # ❌ 정보가 없을 때
    if not found:
        st.error("죄송해요, 해당 정보를 찾을 수 없어요.")