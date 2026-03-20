"""
👖 BLUE JEANS SERIES ENGINE v1.3 — main.py
시즌 아크 → 에피소드 씬 플랜 → 비트 집필 파이프라인
© 2026 BLUE JEANS PICTURES
"""

import streamlit as st
import anthropic
import io
import re
from datetime import datetime

from prompt import (
    SYSTEM_PROMPT,
    GENRE_RULES,
    SEASON_BEATS_8,
    SEASON_BEATS_6,
    EPISODE_BEATS,
    build_season_arc_prompt,
    build_extract_elements_prompt,
    build_episode_plan_prompt,
    build_write_episode_beat_prompt,
    build_rewrite_prompt,
)

# ──────────────────────────────────────────────
# Page Config
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="BLUE JEANS · Series Engine",
    page_icon="👖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────
# Custom CSS — Creator Engine 디자인 시스템 통일
# ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
@import url('https://cdn.jsdelivr.net/gh/projectnoonnu/2408-3@latest/Paperlogy.css');
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&display=swap');

:root {
    --navy: #191970;
    --y: #FFCB05;
    --bg: #F7F7F5;
    --card: #FFFFFF;
    --card-border: #E2E2E0;
    --t: #1A1A2E;
    --r: #D32F2F;
    --g: #2EC484;
    --dim: #8E8E99;
    --light-bg: #EEEEF6;
    --serif: 'Paperlogy', 'Noto Serif KR', 'Georgia', serif;
    --display: 'Playfair Display', 'Paperlogy', 'Georgia', serif;
    --body: 'Pretendard', -apple-system, sans-serif;
    --heading: 'Paperlogy', 'Pretendard', sans-serif;
}

/* ── 기본 타이포 ── */
html, body, [class*="css"] {
    font-family: var(--body);
    color: var(--t);
    -webkit-font-smoothing: antialiased;
}

/* ══ 라이트모드 강제 ══ */
.stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"],
[data-testid="stMainBlockContainer"], [data-testid="stHeader"],
[data-testid="stBottom"] {
    background-color: var(--bg) !important;
    color: var(--t) !important;
}
.stMarkdown, .stText, .stCode {
    color: var(--t) !important;
}
h1, h2, h3, h4, h5, h6 { color: var(--navy) !important; font-family: var(--heading) !important; }
p, span, label, div, li { color: inherit; }

/* ── 사이드바 숨김 ── */
section[data-testid="stSidebar"] { display: none; }

/* ══ 입력 위젯 ══ */
.stTextInput input, .stTextArea textarea,
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
    background-color: var(--card) !important;
    color: var(--t) !important;
    border: 1.5px solid var(--card-border) !important;
    border-radius: 8px !important;
    font-family: var(--body) !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 0.8rem !important;
    transition: border-color 0.2s;
}
.stTextInput input:focus, .stTextArea textarea:focus,
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus {
    border-color: var(--navy) !important;
    box-shadow: 0 0 0 2px rgba(25,25,112,0.08) !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder,
[data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder {
    color: var(--dim) !important;
    font-size: 0.85rem !important;
}
/* selectbox */
.stSelectbox > div > div, [data-baseweb="select"] > div, [data-baseweb="select"] input {
    background-color: var(--card) !important;
    color: var(--t) !important;
    border-color: var(--card-border) !important;
    border-radius: 8px !important;
}
[data-baseweb="popover"], [data-baseweb="menu"], [role="listbox"], [role="option"] {
    background-color: var(--card) !important;
    color: var(--t) !important;
}
[role="option"]:hover { background-color: var(--light-bg) !important; }
/* label */
.stTextInput label, .stTextArea label, .stSelectbox label, .stRadio label {
    color: var(--t) !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    margin-bottom: 0.3rem !important;
}

/* ══ 버튼 ══ */
.stButton > button {
    color: var(--t) !important;
    border: 1.5px solid var(--card-border) !important;
    background-color: var(--card) !important;
    border-radius: 8px !important;
    font-family: var(--body) !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    padding: 0.5rem 1.2rem !important;
    transition: all 0.2s;
}
.stButton > button:hover {
    border-color: var(--navy) !important;
    box-shadow: 0 2px 8px rgba(25,25,112,0.08) !important;
}
.stButton > button[kind="primary"],
.stButton > button[data-testid="stBaseButton-primary"] {
    background-color: var(--y) !important;
    color: var(--navy) !important;
    border-color: var(--y) !important;
    font-weight: 700 !important;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="stBaseButton-primary"]:hover {
    background-color: #E8B800 !important;
    box-shadow: 0 2px 12px rgba(255,203,5,0.3) !important;
}

/* ══ Expander ══ */
.stExpander, details, details summary {
    background-color: var(--card) !important;
    color: var(--t) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: 8px !important;
}
details[open] > div { background-color: var(--card) !important; }
.stExpander summary, .stExpander summary span { color: var(--t) !important; }

/* ══ Alert ══ */
.stAlert { color: var(--t) !important; border-radius: 8px !important; }

/* ══ 내부 컨테이너 투명 ══ */
[data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"],
[data-testid="stColumn"] { background-color: transparent !important; }

/* ══ Metric ══ */
[data-testid="stMetric"] { background-color: var(--card) !important; color: var(--t) !important; }
[data-testid="stMetric"] label { color: var(--dim) !important; }
.stCaption, small { color: var(--dim) !important; }

/* ═══════════════════════════════════
   브랜딩 & 커스텀 컴포넌트
   ═══════════════════════════════════ */

.header {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--navy);
    letter-spacing: 0.15em;
    margin-bottom: 0;
    font-family: var(--heading);
}

.brand-title {
    font-size: 2.6rem;
    font-weight: 900;
    color: var(--navy);
    font-family: var(--display);
    letter-spacing: -0.02em;
    margin-bottom: 0.15rem;
    position: relative;
    display: inline-block;
}
.brand-title::after {
    content: '';
    position: absolute;
    bottom: 2px;
    left: 0;
    width: 100%;
    height: 4px;
    background: var(--y);
    border-radius: 2px;
}

.sub {
    font-size: 0.7rem;
    color: var(--dim);
    letter-spacing: 0.15em;
    margin-top: 0.5rem;
    margin-bottom: 1.5rem;
}

/* ── 카드 ── */
.card {
    background: var(--card);
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 1.2rem;
    margin-bottom: 0.8rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.03);
    transition: all 0.2s;
}
.card:hover {
    border-color: var(--navy);
    box-shadow: 0 3px 12px rgba(25,25,112,0.07);
    transform: translateY(-1px);
}

/* ── 콜아웃 ── */
.callout {
    background: var(--light-bg);
    border-left: 4px solid var(--navy);
    padding: 0.9rem 1.1rem;
    margin: 0.5rem 0;
    border-radius: 0 8px 8px 0;
    font-size: 0.88rem;
    color: var(--t);
}

/* ── 섹션 라벨 ── */
.cl {
    color: var(--navy);
    font-weight: 700;
    font-size: 0.72rem;
    letter-spacing: 0.03em;
    margin-bottom: 0.3rem;
    text-transform: uppercase;
}

/* ── 정보 블록 ── */
.ri {
    background: var(--light-bg);
    border-radius: 8px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.5rem;
    font-size: 0.88rem;
    line-height: 1.6;
}
.rl {
    color: var(--navy);
    font-weight: 700;
    font-size: 0.72rem;
    letter-spacing: 0.02em;
}

/* ── 뱃지 ── */
.badge {
    display: inline-block;
    padding: 0.2rem 0.6rem;
    border-radius: 5px;
    font-size: 0.7rem;
    font-weight: 600;
}
.b-done { background: var(--g); color: #fff; }
.b-run  { background: var(--y); color: var(--navy); }
.b-not  { background: #E8E8F0; color: var(--dim); }

/* ── 노란 섹션 헤더 ── */
.section-header {
    background: var(--y);
    color: var(--navy);
    padding: 0.6rem 1rem;
    border-radius: 6px;
    font-weight: 800;
    font-size: 1rem;
    font-family: var(--heading);
    margin: 1.5rem 0 0.8rem 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.section-header .en {
    font-family: var(--display);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    opacity: 0.7;
}

/* ══ Stepper ══ */
.stepper {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 1.5rem 0 2rem 0;
    gap: 0;
}
.step-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.step-circle {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.78rem;
    font-weight: 700;
    flex-shrink: 0;
    border: 2px solid transparent;
    transition: all 0.2s;
}
.step-circle.active {
    background: var(--y);
    color: var(--navy);
    border-color: var(--y);
    box-shadow: 0 0 0 4px rgba(255,203,5,0.2);
}
.step-circle.done {
    background: var(--g);
    color: #fff;
    border-color: var(--g);
}
.step-circle.upcoming {
    background: #EDEDF0;
    color: var(--dim);
    border-color: #D8D8E0;
}
.step-label {
    font-size: 0.6rem;
    margin-top: 0.35rem;
    text-align: center;
    width: 55px;
    font-weight: 500;
}
.step-label.active { color: var(--navy); font-weight: 700; }
.step-label.done { color: var(--g); font-weight: 600; }
.step-label.upcoming { color: var(--dim); }
.step-line {
    width: 30px;
    height: 2px;
    margin: 0 2px;
    flex-shrink: 0;
    border-radius: 1px;
}
.step-line.done { background: var(--g); }
.step-line.upcoming { background: #D8D8E0; }

/* ══ 에피소드 탭 ══ */
.ep-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: 0.8rem 0;
}
.ep-tab {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.35rem 0.9rem;
    border-radius: 6px;
    font-size: 0.78rem;
    font-weight: 700;
    font-family: var(--body);
    transition: all 0.2s;
}
.ep-tab.done { background: var(--g); color: #fff; }
.ep-tab.current { background: var(--y); color: var(--navy); box-shadow: 0 0 0 3px rgba(255,203,5,0.2); }
.ep-tab.pending { background: #EDEDF0; color: var(--dim); }

/* ══ 비트 프로그레스 ══ */
.beat-row {
    display: flex;
    gap: 0.35rem;
    flex-wrap: wrap;
    margin: 0.8rem 0;
}
.beat-dot {
    width: 2.2rem;
    height: 2.2rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: 700;
    font-family: var(--body);
    transition: all 0.2s;
    border: 2px solid transparent;
}
.beat-dot.done { background: var(--g); color: #fff; border-color: var(--g); }
.beat-dot.current { background: var(--y); color: var(--navy); border-color: var(--y); box-shadow: 0 0 0 3px rgba(255,203,5,0.2); }
.beat-dot.pending { background: #EDEDF0; color: var(--dim); border-color: #D8D8E0; }

/* ══ 프로그레스 바 ══ */
.progress-track {
    flex: 1;
    background: #E8E8F0;
    border-radius: 4px;
    height: 8px;
    margin: 0 0.5rem;
}
.progress-fill {
    height: 100%;
    background: var(--y);
    border-radius: 4px;
    transition: width 0.3s;
}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# 브랜드 헤더 — Creator Engine과 동일 패턴
# ──────────────────────────────────────────────
st.markdown(
    '<div style="text-align:center;padding:1rem 0 0 0">'
    '<div class="header">B L U E &nbsp; J E A N S &nbsp; P I C T U R E S</div>'
    '<div class="brand-title">SERIES ENGINE</div>'
    '<div class="sub">Y O U N G &nbsp; · &nbsp; V I N T A G E &nbsp; · &nbsp; F R E E &nbsp; · &nbsp; I N N O V A T I V E</div>'
    '</div>',
    unsafe_allow_html=True
)


# ──────────────────────────────────────────────
# API 클라이언트
# ──────────────────────────────────────────────
MODEL = "claude-sonnet-4-6"
MAX_TOKENS_ARC = 8000
MAX_TOKENS_PLAN = 8000
MAX_TOKENS_BEAT = 16000
MAX_TOKENS_REWRITE = 16000


@st.cache_resource
def get_client():
    api_key = st.secrets.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        st.error("🔑 `ANTHROPIC_API_KEY`를 Streamlit Secrets에 설정하세요.")
        st.stop()
    return anthropic.Anthropic(api_key=api_key)


def stream_response(system: str, user_prompt: str, max_tokens: int):
    """Claude API 스트리밍 호출."""
    client = get_client()
    collected = []
    placeholder = st.empty()
    with client.messages.stream(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user_prompt}],
    ) as stream:
        for text in stream.text_stream:
            collected.append(text)
            placeholder.markdown("".join(collected))
    return "".join(collected)


# ──────────────────────────────────────────────
# 세션 스테이트
# ──────────────────────────────────────────────
DEFAULTS = {
    "inputs": {
        "logline": "", "intention": "", "gns": "",
        "characters": "", "world": "", "structure": "",
        "scenes": "", "treatment": "", "tone": "",
    },
    "num_episodes": 8,
    "duration": 50,
    "genre": "범죄/스릴러",
    "season_arc": "",
    "story_elements": "",
    "episode_plans": {},
    "episode_beats": {},
}

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        if isinstance(v, dict):
            st.session_state[k] = dict(v)
        else:
            st.session_state[k] = v


# ──────────────────────────────────────────────
# Stepper (5단계)
# ──────────────────────────────────────────────
STEPS = [
    ("input",   "자료입력"),
    ("arc",     "시즌아크"),
    ("plan",    "씬플랜"),
    ("write",   "집필"),
    ("export",  "다운로드"),
]


def get_current_step() -> int:
    if len(st.session_state["episode_beats"]) > 0:
        return 3
    if len(st.session_state["episode_plans"]) > 0:
        return 2
    if st.session_state["season_arc"]:
        return 1
    return 0


def get_done_step() -> int:
    ne = st.session_state["num_episodes"]
    total_beats = ne * 8
    done_beats = len(st.session_state["episode_beats"])
    if done_beats >= total_beats:
        return 4
    if done_beats > 0:
        return 3
    if len(st.session_state["episode_plans"]) > 0:
        return 2
    if st.session_state["season_arc"]:
        return 1
    return -1


def render_stepper():
    current_idx = get_current_step()
    done_idx = get_done_step()
    html_parts = []
    for i, (key, label) in enumerate(STEPS):
        if i <= done_idx and i < current_idx:
            state = "done"
        elif i == current_idx:
            state = "active"
        else:
            state = "upcoming"
        circle = "✓" if state == "done" else str(i + 1)
        html_parts.append(
            f'<div class="step-wrap">'
            f'<div class="step-circle {state}">{circle}</div>'
            f'<div class="step-label {state}">{label}</div>'
            f'</div>'
        )
        if i < len(STEPS) - 1:
            line_state = "done" if i < current_idx and i <= done_idx else "upcoming"
            html_parts.append(f'<div class="step-line {line_state}"></div>')
    st.markdown('<div class="stepper">' + ''.join(html_parts) + '</div>', unsafe_allow_html=True)


render_stepper()


# ──────────────────────────────────────────────
# 유틸리티
# ──────────────────────────────────────────────

def bk(ep: int, beat: int) -> str:
    return f"{ep}_{beat}"


def get_all_episode_text(ep: int) -> str:
    parts = []
    for b in range(8):
        key = bk(ep, b)
        if key in st.session_state["episode_beats"]:
            parts.append(st.session_state["episode_beats"][key])
    return "\n\n".join(parts)


def get_full_season_text() -> str:
    ne = st.session_state["num_episodes"]
    parts = []
    for ep in range(1, ne + 1):
        ep_text = get_all_episode_text(ep)
        if ep_text:
            parts.append(f"{'='*60}\nEPISODE {ep}\n{'='*60}\n\n{ep_text}")
    return "\n\n\n".join(parts)


def build_txt_download(text: str, filename: str):
    st.download_button(
        label=f"📄 {filename}",
        data=text.encode("utf-8"),
        file_name=filename,
        mime="text/plain",
    )


def build_docx_download(text: str, filename: str, title: str = ""):
    try:
        from docx import Document as DocxDocument
        from docx.shared import Pt, RGBColor
        from docx.enum.text import WD_ALIGN_PARAGRAPH

        doc = DocxDocument()
        style = doc.styles["Normal"]
        style.font.name = "맑은 고딕"
        style.font.size = Pt(10)
        style.paragraph_format.space_after = Pt(4)
        style.paragraph_format.line_spacing = 1.5

        if title:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(title)
            run.font.size = Pt(16)
            run.font.bold = True
            run.font.color.rgb = RGBColor(0x19, 0x19, 0x70)
            doc.add_paragraph()

        for line in text.split("\n"):
            stripped = line.strip()
            if re.match(r"^S#\d+\.", stripped):
                p = doc.add_paragraph()
                run = p.add_run(stripped)
                run.font.bold = True
                run.font.size = Pt(11)
                run.font.color.rgb = RGBColor(0x19, 0x19, 0x70)
            elif stripped.startswith("=" * 10):
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(stripped)
                run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)
            elif stripped.startswith("EPISODE "):
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(stripped)
                run.font.size = Pt(14)
                run.font.bold = True
            elif stripped == "--- TITLE ---":
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run("— TITLE —")
                run.font.italic = True
                run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
            else:
                doc.add_paragraph(line)

        section = doc.sections[0]
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        fr = fp.add_run("BLUE JEANS SERIES ENGINE v1.3 · BLUE JEANS PICTURES")
        fr.font.size = Pt(7)
        fr.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

        buf = io.BytesIO()
        doc.save(buf)
        buf.seek(0)
        st.download_button(
            label=f"📘 {filename}",
            data=buf.getvalue(),
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
    except ImportError:
        st.warning("python-docx가 설치되지 않았습니다. TXT 다운로드를 이용하세요.")


# ══════════════════════════════════════════════
# STEP 1: 자료 입력
# ══════════════════════════════════════════════

st.markdown(
    '<div class="section-header">📋 자료 입력 <span class="en">STEP 1 · INPUT</span></div>',
    unsafe_allow_html=True,
)

col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.session_state["num_episodes"] = st.selectbox(
        "🎞️ 에피소드 수", [6, 8],
        index=1 if st.session_state["num_episodes"] == 8 else 0,
    )
with col_s2:
    dur_options = [40, 50, 60]
    st.session_state["duration"] = st.selectbox(
        "⏱️ 에피소드 분량 (분)", dur_options,
        index=dur_options.index(st.session_state["duration"]),
    )
with col_s3:
    genre_options = list(GENRE_RULES.keys())
    st.session_state["genre"] = st.selectbox(
        "🎬 장르", genre_options,
        index=genre_options.index(st.session_state["genre"]) if st.session_state["genre"] in genre_options else 0,
    )

INPUT_FIELDS = [
    ("logline",    "① 로그라인",           "Creator Engine의 Logline Pack (시리즈용, 시즌 질문 포함)"),
    ("intention",  "② 기획의도",           "Creator Engine의 KEY POINTS"),
    ("gns",        "③ GNS",               "Goal / Need / Strategy"),
    ("characters", "④ 캐릭터 + 바이블",    "앙상블 4~8인의 캐릭터 설정 + 바이블 (말투·성격·어휘)"),
    ("world",      "⑤ 세계관",             "World Building"),
    ("structure",  "⑥ 구조",               "Synopsis + Storyline + Beat Sheet (시즌 아크 기준)"),
    ("scenes",     "⑦ 장면 설계",          "에피소드별 핵심 장면"),
    ("treatment",  "⑧ 트리트먼트",         "에피소드별 분할 트리트먼트"),
    ("tone",       "⑨ 톤 문서",            "Tone Document (시리즈 톤 지속성 규칙 포함)"),
]

with st.expander("📝 Creator Engine 결과 붙여넣기 (9칸)", expanded=not st.session_state["season_arc"]):
    for key, label, placeholder in INPUT_FIELDS:
        height = 200 if key == "characters" else 120
        st.session_state["inputs"][key] = st.text_area(
            label, value=st.session_state["inputs"][key],
            height=height, placeholder=placeholder, key=f"input_{key}",
        )


# ══════════════════════════════════════════════
# STEP 2: 시즌 아크
# ══════════════════════════════════════════════

st.markdown(
    '<div class="section-header">🏗️ 시즌 아크 설계 <span class="en">STEP 2 · SEASON ARC</span></div>',
    unsafe_allow_html=True,
)

ne = st.session_state["num_episodes"]
dur = st.session_state["duration"]
genre = st.session_state["genre"]

if st.session_state["season_arc"]:
    with st.expander("✅ 시즌 아크 (완료)", expanded=False):
        st.markdown(st.session_state["season_arc"])
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            build_txt_download(st.session_state["season_arc"], "season_arc.txt")
        with col_d2:
            build_docx_download(
                st.session_state["season_arc"], "season_arc.docx",
                title=f"시즌 아크 — {ne}부작 · {genre}",
            )
else:
    has_input = any(v.strip() for v in st.session_state["inputs"].values())

    st.markdown(
        f'<div class="callout">'
        f'<div class="cl">시즌 설정</div>'
        f'{ne}부작 · 에피소드당 {dur}분 · {genre}'
        f'</div>',
        unsafe_allow_html=True,
    )

    if st.button(f"🎬 {ne}부작 시즌 아크 설계 시작", disabled=not has_input, type="primary", use_container_width=True):
        prompt = build_season_arc_prompt(
            st.session_state["inputs"], ne, dur, genre,
        )
        with st.spinner("시즌 아크를 설계하고 있습니다..."):
            result = stream_response(SYSTEM_PROMPT, prompt, MAX_TOKENS_ARC)
        st.session_state["season_arc"] = result
        st.rerun()


# ══════════════════════════════════════════════
# STEP 2.5: 핵심 요소 추출 (자동)
# ══════════════════════════════════════════════

if st.session_state["season_arc"] and not st.session_state["story_elements"]:
    st.markdown(
        '<div class="section-header">🔍 핵심 요소 추출 <span class="en">STORY ELEMENTS</span></div>',
        unsafe_allow_html=True,
    )
    st.caption("맥거핀 · 캐릭터 비밀 · 전술 · 핵심 장소 · 모티프 — 매 비트 집필 시 강제 주입됩니다.")

    if st.button("🔍 핵심 요소 추출", type="primary", use_container_width=True):
        prompt = build_extract_elements_prompt(
            st.session_state["inputs"],
            st.session_state["season_arc"],
            genre,
        )
        with st.spinner("핵심 요소를 추출하고 있습니다..."):
            result = stream_response(SYSTEM_PROMPT, prompt, MAX_TOKENS_ARC)
        st.session_state["story_elements"] = result
        st.rerun()

elif st.session_state["story_elements"]:
    with st.expander("🔍 핵심 요소 (완료)", expanded=False):
        st.markdown(st.session_state["story_elements"])


# ══════════════════════════════════════════════
# STEP 3: 에피소드별 씬 플랜
# ══════════════════════════════════════════════

if st.session_state["season_arc"]:
    st.markdown(
        '<div class="section-header">📑 에피소드별 씬 플랜 <span class="en">STEP 3 · SCENE PLAN</span></div>',
        unsafe_allow_html=True,
    )

    ep_html = '<div class="ep-tabs">'
    for ep in range(1, ne + 1):
        if ep in st.session_state["episode_plans"]:
            ep_html += f'<div class="ep-tab done">EP{ep} ✓</div>'
        else:
            prev_done = (ep == 1) or ((ep - 1) in st.session_state["episode_plans"])
            cls = "current" if prev_done else "pending"
            ep_html += f'<div class="ep-tab {cls}">EP{ep}</div>'
    ep_html += '</div>'
    st.markdown(ep_html, unsafe_allow_html=True)

    for ep in range(1, ne + 1):
        if ep in st.session_state["episode_plans"]:
            with st.expander(f"✅ EP{ep} 씬 플랜", expanded=False):
                st.markdown(st.session_state["episode_plans"][ep])
                build_txt_download(st.session_state["episode_plans"][ep], f"EP{ep}_scene_plan.txt")

    next_ep = None
    for ep in range(1, ne + 1):
        if ep not in st.session_state["episode_plans"]:
            next_ep = ep
            break

    if next_ep:
        prev_plan = st.session_state["episode_plans"].get(next_ep - 1, "")
        prev_last_scene = ""
        if next_ep > 1 and bk(next_ep - 1, 7) in st.session_state["episode_beats"]:
            full = st.session_state["episode_beats"][bk(next_ep - 1, 7)]
            prev_last_scene = full[-1500:] if len(full) > 1500 else full

        beats_ref = SEASON_BEATS_8 if ne == 8 else SEASON_BEATS_6
        season_beat_info = ""
        for b in beats_ref:
            if b["ep"] == next_ep:
                season_beat_info = f"{b['beat']} — {b['role']}"
                break

        st.markdown(
            f'<div class="callout">'
            f'<div class="cl">EP{next_ep}</div>'
            f'{season_beat_info}'
            f'</div>',
            unsafe_allow_html=True,
        )

        if st.button(
            f"📝 EP{next_ep} 씬 플랜 생성",
            key=f"gen_plan_{next_ep}",
            type="primary",
            use_container_width=True,
        ):
            prompt = build_episode_plan_prompt(
                st.session_state["inputs"],
                st.session_state["season_arc"],
                next_ep, ne, dur, genre,
                prev_episode_plan=prev_plan,
                prev_episode_last_scene=prev_last_scene,
            )
            with st.spinner(f"EP{next_ep} 씬 플랜을 작성하고 있습니다..."):
                result = stream_response(SYSTEM_PROMPT, prompt, MAX_TOKENS_PLAN)
            st.session_state["episode_plans"][next_ep] = result
            st.rerun()


# ══════════════════════════════════════════════
# STEP 4: 비트별 집필
# ══════════════════════════════════════════════

if st.session_state["episode_plans"]:
    st.markdown(
        '<div class="section-header">✍️ 비트별 집필 <span class="en">STEP 4 · WRITING</span></div>',
        unsafe_allow_html=True,
    )

    available_eps = sorted(st.session_state["episode_plans"].keys())
    selected_ep = st.selectbox(
        "집필할 에피소드 선택",
        available_eps,
        format_func=lambda x: f"EP{x}",
        key="write_ep_select",
    )

    if selected_ep:
        next_beat = None
        beat_html = '<div class="beat-row">'
        for b in range(8):
            key = bk(selected_ep, b)
            if key in st.session_state["episode_beats"]:
                beat_html += f'<div class="beat-dot done">✓</div>'
            elif next_beat is None:
                beat_html += f'<div class="beat-dot current">{b}</div>'
                next_beat = b
            else:
                beat_html += f'<div class="beat-dot pending">{b}</div>'
        beat_html += '</div>'
        st.markdown(beat_html, unsafe_allow_html=True)

        st.caption(" · ".join([f"B{b['beat']}={b['name']}" for b in EPISODE_BEATS]))

        for b in range(8):
            key = bk(selected_ep, b)
            if key in st.session_state["episode_beats"]:
                beat_name = EPISODE_BEATS[b]["name"] if b < len(EPISODE_BEATS) else f"Beat {b}"
                with st.expander(f"✅ Beat {b} — {beat_name}", expanded=False):
                    st.markdown(st.session_state["episode_beats"][key])

        if next_beat is not None:
            beat_info = EPISODE_BEATS[next_beat] if next_beat < len(EPISODE_BEATS) else EPISODE_BEATS[-1]

            st.markdown(
                f'<div class="callout" style="border-left-color:var(--y)">'
                f'<div class="cl">EP{selected_ep} · Beat {next_beat}</div>'
                f'{beat_info["name"]} — {beat_info["minutes"]} — {beat_info["role"]}'
                f'</div>',
                unsafe_allow_html=True,
            )

            prev_beat_text = ""
            if next_beat > 0:
                prev_beat_text = st.session_state["episode_beats"].get(bk(selected_ep, next_beat - 1), "")
            elif selected_ep > 1:
                prev_beat_text = st.session_state["episode_beats"].get(bk(selected_ep - 1, 7), "")

            char_bible = st.session_state["inputs"].get("characters", "")

            if st.button(
                f"🖊️ EP{selected_ep} Beat {next_beat} [{beat_info['name']}] 집필",
                key=f"write_{selected_ep}_{next_beat}",
                type="primary",
                use_container_width=True,
            ):
                prompt = build_write_episode_beat_prompt(
                    st.session_state["inputs"],
                    st.session_state["season_arc"],
                    st.session_state["episode_plans"][selected_ep],
                    selected_ep, next_beat, ne, dur, genre,
                    prev_beat_text=prev_beat_text,
                    character_bible=char_bible,
                    story_elements=st.session_state.get("story_elements", ""),
                )
                with st.spinner(f"EP{selected_ep} Beat {next_beat}을 집필하고 있습니다..."):
                    result = stream_response(SYSTEM_PROMPT, prompt, MAX_TOKENS_BEAT)
                st.session_state["episode_beats"][bk(selected_ep, next_beat)] = result
                st.rerun()
        else:
            st.markdown(
                f'<div class="callout" style="border-left-color:var(--g)">'
                f'<div class="cl">🎉 완료</div>'
                f'EP{selected_ep} 전체 집필 완료!'
                f'</div>',
                unsafe_allow_html=True,
            )

        # 다시 쓰기
        st.markdown("---")
        last_done = None
        for b in range(7, -1, -1):
            if bk(selected_ep, b) in st.session_state["episode_beats"]:
                last_done = b
                break

        if last_done is not None:
            st.markdown('<div class="cl">🔄 마지막 비트 다시 쓰기</div>', unsafe_allow_html=True)
            rewrite_instruction = st.text_area(
                f"EP{selected_ep} Beat {last_done} 수정 지시",
                placeholder="예: 대사를 더 날카롭게, 클리프행어를 Betrayal로 변경, S#15 삭제...",
                height=80,
                key="rewrite_inst",
            )
            if st.button(
                f"🔄 Beat {last_done} 다시 쓰기",
                key="rewrite_btn",
                disabled=not rewrite_instruction.strip() if isinstance(rewrite_instruction, str) else True,
            ):
                original = st.session_state["episode_beats"][bk(selected_ep, last_done)]
                prompt = build_rewrite_prompt(original, rewrite_instruction, genre, character_bible=char_bible)
                with st.spinner(f"Beat {last_done}을 다시 쓰고 있습니다..."):
                    result = stream_response(SYSTEM_PROMPT, prompt, MAX_TOKENS_REWRITE)
                st.session_state["episode_beats"][bk(selected_ep, last_done)] = result
                st.rerun()


# ══════════════════════════════════════════════
# STEP 5: 다운로드
# ══════════════════════════════════════════════

has_any_beats = len(st.session_state["episode_beats"]) > 0

if has_any_beats:
    st.markdown(
        '<div class="section-header">💾 다운로드 <span class="en">STEP 5 · EXPORT</span></div>',
        unsafe_allow_html=True,
    )

    timestamp = datetime.now().strftime("%Y%m%d")

    st.markdown('<div class="cl">에피소드별</div>', unsafe_allow_html=True)
    dl_cols = st.columns(min(ne, 4))
    for idx, ep in enumerate(range(1, ne + 1)):
        ep_text = get_all_episode_text(ep)
        if ep_text:
            with dl_cols[idx % min(ne, 4)]:
                build_txt_download(ep_text, f"EP{ep}_{timestamp}.txt")
                build_docx_download(ep_text, f"EP{ep}_{timestamp}.docx", title=f"EPISODE {ep}")

    full_text = get_full_season_text()
    if full_text:
        st.markdown('<div class="cl" style="margin-top:1rem">시즌 전체</div>', unsafe_allow_html=True)
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            build_txt_download(full_text, f"SEASON1_FULL_{timestamp}.txt")
        with col_f2:
            build_docx_download(full_text, f"SEASON1_FULL_{timestamp}.docx", title=f"시즌 1 — {ne}부작 · {genre}")


# ══════════════════════════════════════════════
# 전체 초기화
# ══════════════════════════════════════════════

st.markdown("---")
with st.expander("⚠️ 전체 초기화", expanded=False):
    st.warning("모든 진행 사항이 삭제됩니다.")
    if st.button("🗑️ 전체 초기화 실행"):
        for k, v in DEFAULTS.items():
            if isinstance(v, dict):
                st.session_state[k] = dict(v)
            else:
                st.session_state[k] = v
        st.rerun()

st.markdown("---")
st.caption("© 2026 BLUE JEANS PICTURES · Series Engine v1.3")
