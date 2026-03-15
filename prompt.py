"""
BLUE JEANS SERIES ENGINE v1.0 — prompt.py
시리즈 작법 원칙 · 장르 규칙 · 프롬프트 빌더
© 2026 BLUE JEANS PICTURES
"""

# ──────────────────────────────────────────────
# 1. SYSTEM PROMPT — 시리즈 작법 핵심 원칙
# ──────────────────────────────────────────────

SYSTEM_PROMPT = """당신은 넷플릭스 미니시리즈/시리즈(시즌 1) 시나리오를 쓰는 전문 작가입니다.
BLUE JEANS PICTURES의 Series Engine으로서, 아래의 시리즈 작법 원칙을 반드시 지킵니다.

═══ 시리즈 작법 5대 원칙 ═══

1. THE ENGINE (시리즈의 엔진)
   모든 시리즈에는 매주 이야기를 생산하는 엔진이 있어야 한다.
   - 사건 엔진: 매 회 새로운 사건 (범죄수사, 의학)
   - 비밀 엔진: 숨겨진 진실이 하나씩 드러남 (미스터리, 스릴러)
   - 관계 엔진: 인물 간 관계가 매 회 변화 (드라마, 멜로)
   - 세계 엔진: 세계관의 새로운 층이 열림 (SF, 판타지)

2. PROMISE OF THE PILOT
   1화는 시리즈의 약속이다 — 매주 어떤 경험을 줄 것인지, 왜 8시간을 투자해야 하는지.

3. ESCALATION
   매 에피소드마다 판돈이 올라가야 한다.
   개인의 문제 → 가족의 문제 → 공동체의 문제 → 존재의 문제.

4. CHARACTER OVER PLOT
   시리즈는 "이 사람들에게 무슨 일이 벌어지는가"로 끈다.
   사건보다 그 사건이 인물에게 어떤 의미인지가 더 중요하다.

5. THE UNANSWERED QUESTION
   항상 하나 이상의 질문이 열려 있어야 한다.
   하나의 질문에 답하면 더 큰 질문이 열린다.

═══ 클리프행어 시스템 ═══

매 에피소드 끝에 반드시 클리프행어.
유형: Revelation / Threat / Choice / Betrayal / Reversal / Arrival / Question
- EP1~3: Revelation·Question (세계를 넓히는)
- EP4 Midpoint: Reversal·Betrayal (게임 체인저)
- EP5~7: Threat·Choice (판돈을 올리는)
- EP8 Finale: Resolution + 새로운 Question

═══ 비밀 경제 (Secret Economy) ═══

시리즈는 비밀의 생성·유지·폭로로 돈다.
- 시즌 비밀 (EP7~8 공개), 중간 비밀 (EP3~6), 에피소드 비밀 (매 회), 캐릭터 비밀
- 동시에 3~4개 비밀이 가동. 하나가 터지면 다른 하나가 시작.
- 관객이 아는 비밀 (Dramatic Irony) + 관객도 모르는 비밀 (Mystery Box) 혼합.

═══ 앙상블 캐릭터 ═══

4~8명 POV 로테이션. 매 에피소드마다 "이번 회의 주인공"이 있다.
역할: 주인공 / 적대자 / 동맹자 / 거울 / 비밀 보유자 / 새 인물 / 희생자 / 와일드카드
- 에피소드 아크 (소규모 변화) + 시즌 아크 (근본적 변화) 이중 구조.

═══ 멀티 스토리라인 직조 ═══

A-Story (40~50%) + B-Story (25~30%) + C-Story (15~20%) + D-Story (5~10%)
- A·B는 매 에피소드 교차. 씬 배치: A 2~3개 → B 1개 → A 2개 → C 1개
- 전환은 감정 대비로 (긴장→이완, 슬픔→유머)
- Midpoint(EP4)에서 A·B 충돌, Finale(EP8)에서 A·B·C 합류.

═══ 관객 심리 설계 ═══

기본 6원칙: Dramatic Irony / Information Gap / Zeigarnik Effect / Pattern & Violation / Delayed Gratification / Mystery Box
시리즈 특화: Appointment Viewing (다음 회를 기다리게) / Water Cooler Moment (에피소드당 최소 1개) / Rewatchability (복선 재발견)

═══ 콜드 오프닝 ═══

EP1: 시리즈 전체 톤과 장르를 3분 안에 확립
EP2~: 직전 클리프행어 연결 또는 새로운 훅
콜드 오프닝 끝에 미니 클리프행어 (타이틀 전환 순간의 긴장)

═══ 시나리오 형식 ═══

한국어 시나리오 표준 형식으로 작성:
- 씬 헤더: S#번호. 장소 / 시간
- 지문은 현재형, 간결, 시각적. 감정을 직접 서술하지 않는다.
- 대사는 인물명 뒤에 작성. 괄호 안에 톤/행동 지시.
- 절대 금지: 소설적 서술, 심리 독백, ~것이었다 어미, 분위기 채움 문장.
"""

# ──────────────────────────────────────────────
# 2. 장르별 시리즈 규칙
# ──────────────────────────────────────────────

GENRE_RULES = {
    "범죄/스릴러": """[범죄/스릴러 시리즈 규칙]
- 사건 엔진: 매 회 수사 진전 + 새로운 용의자/증거
- 시즌 질문: "범인은 누구인가?" 또는 "주인공은 살아남는가?"
- EP1: 사건 발생 + 수사 시작
- EP4: 1차 용의자 반전 (진범이 아님)
- EP7: 진범 정체 공개
- EP8: 최종 대결 + 도덕적 대가
- 클리프행어: 새로운 증거/용의자/위협
- 금지: 수사관의 독백으로 사건 정리, 우연의 단서 발견""",

    "드라마": """[드라마 시리즈 규칙]
- 관계 엔진: 매 회 관계의 균열·복원·변화
- 시즌 질문: "이 가족/공동체는 다시 하나가 될 수 있는가?"
- 캐릭터 아크가 플롯보다 중요
- 클리프행어: 관계의 균열 / 숨겨진 진실 폭로 / 선택의 순간
- 금지: 감정을 직접 말하는 대사 (Too Wet), 갈등 없는 화해""",

    "호러": """[호러 시리즈 규칙]
- 비밀 엔진 + 규칙 발견: 매 회 공포의 규칙이 하나씩 드러남
- 시즌 질문: "이 저주/위협에서 벗어날 수 있는가?"
- EP1: 프롤로그 킬 + 일상의 균열
- EP3~4: 공포의 규칙 발견
- EP6: 규칙 위반 → 대가
- EP8: 최종 대면
- 클리프행어: 가짜 안도 후 진짜 공포 / 새로운 위협의 징후
- 금지: 공포 원인의 과잉 설명, jump scare만 반복""",

    "SF/판타지": """[SF/판타지 시리즈 규칙]
- 세계 엔진: 매 회 세계관의 새로운 층이 열림
- 시즌 질문: "이 세계의 진짜 규칙은 무엇인가?"
- EP1: 세계 진입 + 규칙 1개 발견
- EP4: 세계관의 진실이 뒤집힘
- EP8: 규칙의 대가를 치르고 새로운 질서
- 클리프행어: 세계관 반전 / 능력의 대가 / 새로운 규칙 발견
- 금지: 세계관 설명 강의, 대가 없는 능력, 데우스 엑스 마키나""",

    "로맨스/멜로": """[로맨스/멜로 시리즈 규칙]
- 관계 엔진: 매 회 두 사람의 거리가 진동
- 시즌 질문: "이 두 사람은 결국 함께할 수 있는가?"
- 밀당의 리듬: 가까워짐 → 벽 → 더 가까워짐 → 더 큰 벽
- 클리프행어: 오해 / 제3자 등장 / 진심 고백 직전 중단
- 금지: 오해가 대화 한 마디로 해결, 삼각관계 기계적 반복""",
}

# ──────────────────────────────────────────────
# 3. 시즌 비트 / 에피소드 비트 정의
# ──────────────────────────────────────────────

SEASON_BEATS_8 = [
    {"ep": 1, "beat": "Pilot / Hook",      "role": "세계·인물·갈등 설정. 시리즈의 약속. 시즌 질문 제시."},
    {"ep": 2, "beat": "Expansion",          "role": "세계 확장. 새 인물 등장. 규칙 발견. 앙상블 확립."},
    {"ep": 3, "beat": "Deepening",          "role": "인물 내면 심화. 비밀의 첫 번째 균열. 관계 복잡화."},
    {"ep": 4, "beat": "Midpoint Shift",     "role": "게임의 규칙이 바뀜. 가짜 승리 또는 가짜 패배. 시즌 반환점."},
    {"ep": 5, "beat": "Consequences",       "role": "미드포인트의 여파. 동맹 균열. 비밀이 하나 터짐."},
    {"ep": 6, "beat": "Darkest Point",      "role": "가장 낮은 지점. 주인공이 모든 것을 잃는다. All Is Lost."},
    {"ep": 7, "beat": "Convergence",        "role": "모든 스토리라인이 합류. 최종 대결 준비. 마지막 비밀 폭로."},
    {"ep": 8, "beat": "Finale",             "role": "시즌 질문에 답. 캐릭터 아크 완성. 새 질문 열기 (시즌 2 가능)."},
]

SEASON_BEATS_6 = [
    {"ep": 1, "beat": "Pilot / Hook",                   "role": "세계·인물·갈등 설정. 시리즈의 약속. 시즌 질문 제시."},
    {"ep": 2, "beat": "Expansion + Deepening",           "role": "세계 확장 + 인물 내면 심화. 앙상블 확립. 비밀 첫 균열."},
    {"ep": 3, "beat": "Midpoint Shift",                  "role": "게임의 규칙이 바뀜. 가짜 승리 또는 가짜 패배. 시즌 반환점."},
    {"ep": 4, "beat": "Consequences + Darkest Point",    "role": "미드포인트 여파 + 최저점. 동맹 균열. 비밀 폭발. All Is Lost."},
    {"ep": 5, "beat": "Convergence",                     "role": "모든 스토리라인이 합류. 최종 대결 준비. 마지막 비밀 폭로."},
    {"ep": 6, "beat": "Finale",                          "role": "시즌 질문에 답. 캐릭터 아크 완성. 새 질문 열기 (시즌 2 가능)."},
]

EPISODE_BEATS = [
    {"beat": 0, "name": "Cold Opening",  "minutes": "2~5분",  "role": "관객을 즉시 잡는 훅. 타이틀 전 시퀀스."},
    {"beat": 1, "name": "Act 1 - Setup", "minutes": "~8분",   "role": "에피소드 질문 제시. 상황 설정."},
    {"beat": 2, "name": "Act 1 - Hook",  "minutes": "~7분",   "role": "에피소드의 방향 확립. A-Story 촉발."},
    {"beat": 3, "name": "Act 2A - Rising","minutes": "~8분",  "role": "갈등 심화. B/C 스토리 전개."},
    {"beat": 4, "name": "Act 2A - Twist", "minutes": "~7분",  "role": "예상 못한 전환. 감정 대비."},
    {"beat": 5, "name": "Act 2B - Crisis", "minutes": "~8분", "role": "위기 고조. 에피소드 클라이맥스 준비."},
    {"beat": 6, "name": "Act 2B - Peak",   "minutes": "~7분", "role": "에피소드 클라이맥스. 반전."},
    {"beat": 7, "name": "Act 3 + Cliffhanger", "minutes": "~10분", "role": "에피소드 질문 (부분) 해결 + 클리프행어."},
]

CLIFFHANGER_TYPES = [
    {"type": "Revelation",  "desc": "숨겨진 정보가 드러남"},
    {"type": "Threat",      "desc": "새로운 위험이 등장"},
    {"type": "Choice",      "desc": "불가능한 선택 앞에 놓임"},
    {"type": "Betrayal",    "desc": "믿었던 인물의 배신"},
    {"type": "Reversal",    "desc": "상황이 완전히 뒤집힘"},
    {"type": "Arrival",     "desc": "예상 못한 인물/사건 등장"},
    {"type": "Question",    "desc": "대답할 수 없는 질문"},
]


# ──────────────────────────────────────────────
# 4. 프롬프트 빌더 함수들
# ──────────────────────────────────────────────

def _format_season_beats(num_episodes: int) -> str:
    """시즌 비트 테이블을 문자열로 포맷."""
    beats = SEASON_BEATS_8 if num_episodes == 8 else SEASON_BEATS_6
    lines = []
    for b in beats:
        lines.append(f"EP{b['ep']} — {b['beat']}: {b['role']}")
    return "\n".join(lines)


def _format_episode_beats() -> str:
    """에피소드 내부 비트 테이블을 문자열로 포맷."""
    lines = []
    for b in EPISODE_BEATS:
        lines.append(f"Beat {b['beat']} [{b['name']}] ({b['minutes']}): {b['role']}")
    return "\n".join(lines)


def _format_cliffhangers() -> str:
    """클리프행어 유형 목록."""
    return "\n".join([f"- {c['type']}: {c['desc']}" for c in CLIFFHANGER_TYPES])


def _format_inputs(inputs: dict) -> str:
    """9칸 입력 필드를 정리."""
    labels = [
        ("logline", "로그라인"),
        ("intention", "기획의도"),
        ("gns", "GNS (Goal/Need/Strategy)"),
        ("characters", "캐릭터 + 바이블"),
        ("world", "세계관"),
        ("structure", "구조 (시놉시스/스토리라인/비트시트)"),
        ("scenes", "장면 설계"),
        ("treatment", "트리트먼트"),
        ("tone", "톤 문서"),
    ]
    parts = []
    for key, label in labels:
        val = inputs.get(key, "").strip()
        if val:
            parts.append(f"[{label}]\n{val}")
    return "\n\n".join(parts)


# ──────────────────────────────────────────────
# 4-1. 시즌 아크 설계
# ──────────────────────────────────────────────

def build_season_arc_prompt(
    inputs: dict,
    num_episodes: int,
    duration: int,
    genre: str,
) -> str:
    """STEP 2: 시즌 아크 설계 프롬프트."""

    genre_rule = GENRE_RULES.get(genre, "")
    season_beats = _format_season_beats(num_episodes)
    cliffhangers = _format_cliffhangers()

    return f"""아래 기획 자료를 바탕으로 {num_episodes}부작 시리즈(에피소드당 {duration}분)의 **시즌 아크**를 설계하라.

══ 기획 자료 ══
{_format_inputs(inputs)}

══ 장르 ══
{genre}
{genre_rule}

══ 시즌 비트 구조 ({num_episodes}부작) ══
{season_beats}

══ 클리프행어 유형 ══
{cliffhangers}

═══ 출력 형식 (반드시 이 구조를 따를 것) ═══

### 1. 시리즈 엔진
이 시리즈를 매 회 굴리는 엔진은 무엇인가? (사건/비밀/관계/세계 중 택1 + 구체 설명)

### 2. 시즌 질문
시즌 전체를 관통하는 대질문 1개.

### 3. 에피소드별 시즌 비트
EP1부터 EP{num_episodes}까지, 각 에피소드의:
- 시즌 비트 이름
- 에피소드 질문 (이 회에서 열리고 닫히는 질문)
- A/B/C/D 스토리라인 진행 요약 (각 1~2줄)
- 핵심 사건 (3~5줄)
- 클리프행어 (유형 명시 + 구체 내용)
- 시즌 질문 진전도 (이 회에서 시즌 질문이 얼마나 전진하는가)

### 4. 캐릭터별 시즌 아크
앙상블 전원(4~8명)의:
- 역할 (주인공/적대자/동맹자/거울/비밀보유자/새인물/희생자/와일드카드)
- EP1 출발점 → EP{num_episodes} 도착점 (시즌 아크)
- POV 에피소드 (이 인물이 주인공인 회차)

### 5. Secret Map (비밀 지도)
비밀 A: [내용] — 소유자: 인물X — 공개: EP? — 폭발: ?
비밀 B: ...
(최소 4개, 시즌·중간·에피소드·캐릭터 비밀 혼합)

### 6. 멀티 스토리라인 배분
A-Story: [핵심 설명] (비중 40~50%)
B-Story: [핵심 설명] (비중 25~30%)
C-Story: [핵심 설명] (비중 15~20%)
D-Story: [핵심 설명] (비중 5~10%)

### 7. 에스컬레이션 곡선
EP1 → EP{num_episodes} 판돈 상승 경로를 한 줄씩.

한국어로 작성하라. 시나리오 전문 작가의 언어로, 간결하고 명확하게."""


# ──────────────────────────────────────────────
# 4-2. 에피소드별 씬 플랜
# ──────────────────────────────────────────────

def build_episode_plan_prompt(
    inputs: dict,
    season_arc: str,
    ep_num: int,
    num_episodes: int,
    duration: int,
    genre: str,
    prev_episode_plan: str = "",
    prev_episode_last_scene: str = "",
) -> str:
    """STEP 3: 에피소드별 씬 플랜 프롬프트."""

    genre_rule = GENRE_RULES.get(genre, "")
    ep_beats = _format_episode_beats()

    # 씬 수 가이드
    scene_count = {40: "30~40", 50: "40~50", 60: "50~60"}.get(duration, "40~50")

    continuity = ""
    if prev_episode_plan:
        continuity = f"""══ 직전 에피소드(EP{ep_num - 1}) 씬 플랜 ══
{prev_episode_plan}
"""
    if prev_episode_last_scene:
        continuity += f"""══ 직전 에피소드 마지막 씬/클리프행어 ══
{prev_episode_last_scene}
→ 이 에피소드의 콜드 오프닝은 위의 클리프행어와 연결되어야 한다.
"""

    return f"""아래 시즌 아크와 기획 자료를 바탕으로 **EP{ep_num}의 씬 플랜**을 작성하라.

══ 기획 자료 (요약) ══
{_format_inputs(inputs)}

══ 시즌 아크 ══
{season_arc}

══ 장르 ══
{genre}
{genre_rule}

{continuity}

══ 에피소드 내부 비트 구조 ══
{ep_beats}

══ EP{ep_num} 씬 플랜 작성 규칙 ══

분량: {duration}분, 씬 수: {scene_count}씬

출력 형식:

### EP{ep_num} 씬 플랜 — [에피소드 부제]

**에피소드 질문**: [이 회에서 열리는 질문]
**POV 인물**: [이번 회의 주인공]
**클리프행어 유형**: [Revelation/Threat/Choice/Betrayal/Reversal/Arrival/Question]

[Cold Opening]
S#1. 장소 / 시간 — 스토리라인(A/B/C/D) — 인물
  요약 (2~3줄)

[Beat 1 — Act 1 Setup]
S#2. 장소 / 시간 — 스토리라인 — 인물
  요약
S#3. ...
...

[Beat 7 — Act 3 + Cliffhanger]
S#마지막. 장소 / 시간 — 스토리라인 — 인물
  요약 + ★클리프행어 상세

---
**에피소드 종료 시 열린 질문**: [다음 회로 이어지는 미해결 사항]
**시즌 질문 진전**: [이 회에서 시즌 질문이 얼마나 전진했는가]
**비밀 경제 현황**: [이 회에서 터진 비밀 / 새로 생긴 비밀 / 유지 중인 비밀]

한국어로 작성. 간결하고 시각적인 시나리오 작가의 언어로."""


# ──────────────────────────────────────────────
# 4-3. 비트별 집필
# ──────────────────────────────────────────────

def build_write_episode_beat_prompt(
    inputs: dict,
    season_arc: str,
    episode_plan: str,
    ep_num: int,
    beat_num: int,
    num_episodes: int,
    duration: int,
    genre: str,
    prev_beat_text: str = "",
    character_bible: str = "",
) -> str:
    """STEP 4: 에피소드 내 비트 집필 프롬프트."""

    genre_rule = GENRE_RULES.get(genre, "")
    beat_info = EPISODE_BEATS[beat_num] if beat_num < len(EPISODE_BEATS) else EPISODE_BEATS[-1]

    continuity = ""
    if prev_beat_text:
        # 직전 비트 마지막 500자만 전달 (연속성)
        tail = prev_beat_text[-2000:] if len(prev_beat_text) > 2000 else prev_beat_text
        continuity = f"""══ 직전 비트(Beat {beat_num - 1}) 마지막 부분 ══
{tail}
→ 이 비트는 위의 마지막 씬에서 자연스럽게 이어져야 한다.
"""

    char_section = ""
    if character_bible:
        char_section = f"""══ 캐릭터 바이블 ══
{character_bible}
→ 모든 대사는 이 바이블의 말투·성격·어휘를 반영해야 한다.
"""

    is_cliffhanger_beat = (beat_num == 7)
    cliffhanger_instruction = ""
    if is_cliffhanger_beat:
        cliffhanger_instruction = """
★★★ 이 비트는 에피소드 마지막 비트다 ★★★
- 에피소드 질문을 (부분적으로) 해결하라.
- 반드시 클리프행어로 끝내라. 씬 플랜에 명시된 클리프행어 유형과 내용을 따르라.
- 클리프행어는 마지막 씬의 마지막 줄이어야 한다.
- "다음 에피소드를 안 볼 수 없는" 수준의 긴장으로 끝내라.
"""

    is_cold_open = (beat_num == 0)
    cold_open_instruction = ""
    if is_cold_open:
        cold_open_instruction = """
★★★ 이 비트는 콜드 오프닝이다 ★★★
- 타이틀 전 시퀀스. 2~5분 분량.
- 관객을 즉시 잡는 훅으로 시작하라.
- 콜드 오프닝 끝에 미니 클리프행어 (타이틀 전환 순간의 긴장).
- "--- TITLE ---" 라인으로 콜드 오프닝 종료를 표시하라.
"""

    return f"""아래 자료를 바탕으로 **EP{ep_num} Beat {beat_num} [{beat_info['name']}]**의 시나리오를 작성하라.

══ 장르 ══
{genre}
{genre_rule}

══ 시즌 아크 (요약) ══
{season_arc[:3000]}

══ EP{ep_num} 씬 플랜 ══
{episode_plan}

{char_section}
{continuity}
{cold_open_instruction}
{cliffhanger_instruction}

══ 현재 비트 정보 ══
Beat {beat_num} [{beat_info['name']}] — {beat_info['minutes']} — {beat_info['role']}

══ 시나리오 작성 규칙 ══

1. 형식:
   S#번호. 장소 / 시간

   (지문: 현재형, 간결, 시각적)

   인물명
   대사 내용. (괄호 안에 톤/행동)

2. 절대 금지:
   - 소설적 서술 ("그는 슬픔을 느꼈다" ← 금지)
   - ~것이었다 어미
   - 심리 독백
   - 분위기 채움 문장 (빈 수사)
   - 감정을 직접 서술 → 행동과 대사로 보여줘라

3. 대사 규칙:
   - 각 인물의 말투·어휘·리듬이 구별되어야 한다
   - 서브텍스트: 말하는 것과 의미하는 것이 다르다
   - 시리즈 대사는 캐릭터의 "시그니처"가 되어야 한다

4. 씬 전환:
   - A→B→A→C 스토리라인 교차 패턴
   - 전환마다 감정 대비 (Curtis 감정 연쇄)
   - 컷 전환 시 에너지 흐름을 끊지 마라

5. 이 비트에 해당하는 씬들만 작성하라 (씬 플랜 참조).

한국어 시나리오로 작성. 프로 시나리오 작가 수준."""


# ──────────────────────────────────────────────
# 4-4. 비트 다시 쓰기
# ──────────────────────────────────────────────

def build_rewrite_prompt(
    beat_text: str,
    instruction: str,
    genre: str = "",
) -> str:
    """비트 다시 쓰기 프롬프트."""
    genre_rule = GENRE_RULES.get(genre, "")

    return f"""아래 시나리오 비트를 수정 지시에 따라 다시 작성하라.

══ 장르 ══
{genre}
{genre_rule}

══ 원본 비트 ══
{beat_text}

══ 수정 지시 ══
{instruction}

══ 규칙 ══
- 수정 지시에 해당하는 부분만 변경하고, 나머지는 원본 유지.
- 씬 번호 체계를 유지하라.
- 시나리오 형식(씬 헤더, 지문, 대사)을 유지하라.
- 소설적 서술, ~것이었다 어미, 심리 독백 금지.

다시 작성한 전체 비트를 출력하라."""
