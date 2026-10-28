import streamlit as st
import re
from collections import Counter

# 페이지 설정
st.set_page_config(page_title="유튜브 핫스팟 탐색기", page_icon="🔥")

st.title("🔥 유튜브 핫스팟 (타임스탬프) 탐색기")
st.write("테스트용 가상 댓글 데이터에서 가장 많이 언급된 시간을 추출합니다.")

# 가상의 댓글 데이터 예시
comments = [
    "12:34 여기 진짜 레전드 ㅋㅋㅋ",
    "아 05:12 이 부분 너무 웃겨요",
    "12:34 다시 봐도 미쳤다",
    "1:02:45 쯤에 나오는 노래 뭔가요?"
]

# 타임스탬프 추출 패턴 및 빈도수 계산
pattern = r'\b(?:\d{1,2}:)?\d{1,2}:\d{2}\b'
timestamps = []

for comment in comments:
    found_times = re.findall(pattern, comment)
    timestamps.extend(found_times)

time_counts = Counter(timestamps)
top_hotspots = time_counts.most_common(3)

# 웹 화면에 결과 출력하기
st.subheader("🏆 하이라이트 구간 Top 3")
for rank, (time, count) in enumerate(top_hotspots, 1):
    st.success(f"**{rank}위:** {time} ({count}회 언급)")
