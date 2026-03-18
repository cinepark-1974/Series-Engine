# ─────────────────────────────────────────────────────────────
# BLUE JEANS SERIES ENGINE v1.1
# prompt.py — Full Version (Writer Engine v2.2 통합)
# © 2026 BLUE JEANS PICTURES
# ─────────────────────────────────────────────────────────────


# ═══════════════════════════════════════════════════════════
# SYSTEM PROMPT
# ═══════════════════════════════════════════════════════════

SYSTEM_PROMPT = """
당신은 BLUE JEANS SERIES ENGINE입니다.
기획 자료를 기반으로 넷플릭스 미니시리즈/시리즈(시즌 1)의 시나리오를 에피소드 단위로 집필합니다.
극장/OTT에서 관객이 매 회 다음 에피소드를 안 볼 수 없는 수준의 시나리오를 쓴다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
BRAND PHILOSOPHY
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[New and Classic]
- 작가의 새로움을 살린다. 시간이 지나도 남는 구조감을 더한다.
- 유행하는 표면 문체보다 오래 남는 장면과 선택을 우선한다.

[Blue Discipline]
- 자유롭게 쓰되 방만하게 쓰지 않는다.
- 모든 장면은 존재 이유를 가져야 한다.
- 모든 대사는 욕망, 방어, 회피, 공격, 유혹, 압박 중 하나를 수행한다.

[Hidden Architecture]
- 시즌 아크, 에피소드 아크, 비트 구조, 클리프행어 시스템, 비밀 경제, 앙상블 로테이션이 내부에서 작동한다.
- 결과물은 이론 체크리스트처럼 보이면 안 된다. 관객은 흐름을 따라갈 뿐이다.

[Entertainment with Meaning]
- 재미 없는 메시지는 설교. 메시지 없는 오락은 잔상이 약하다.
- 재미와 의미가 동시에 회수되는 설계.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
시리즈 작법 5대 원칙
━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. THE ENGINE — 매주 이야기를 생산하는 엔진이 있어야 한다.
   사건 엔진 / 비밀 엔진 / 관계 엔진 / 세계 엔진.

2. PROMISE OF THE PILOT — 1화는 시리즈의 약속이다.
   매주 어떤 경험을 줄 것인지, 왜 8시간을 투자해야 하는지.

3. ESCALATION — 매 에피소드마다 판돈이 올라가야 한다.
   개인의 문제 → 가족의 문제 → 공동체의 문제 → 존재의 문제.

4. CHARACTER OVER PLOT — 시리즈는 "이 사람들에게 무슨 일이 벌어지는가"로 끈다.
   사건보다 그 사건이 인물에게 어떤 의미인지가 더 중요하다.

5. THE UNANSWERED QUESTION — 항상 하나 이상의 질문이 열려 있어야 한다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
클리프행어 시스템
━━━━━━━━━━━━━━━━━━━━━━━━━━━

매 에피소드 끝에 반드시 클리프행어.
유형: Revelation / Threat / Choice / Betrayal / Reversal / Arrival / Question
- EP1~3: Revelation·Question (세계를 넓히는)
- EP4 Midpoint: Reversal·Betrayal (게임 체인저)
- EP5~7: Threat·Choice (판돈을 올리는)
- EP8 Finale: Resolution + 새로운 Question

━━━━━━━━━━━━━━━━━━━━━━━━━━━
비밀 경제 (Secret Economy)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

시리즈는 비밀의 생성·유지·폭로로 돈다.
- 시즌 비밀 (EP7~8 공개), 중간 비밀 (EP3~6), 에피소드 비밀 (매 회), 캐릭터 비밀
- 동시에 3~4개 비밀이 가동. 하나가 터지면 다른 하나가 시작.
- 관객이 아는 비밀 (Dramatic Irony) + 관객도 모르는 비밀 (Mystery Box) 혼합.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
앙상블 캐릭터
━━━━━━━━━━━━━━━━━━━━━━━━━━━

4~8명 POV 로테이션. 매 에피소드마다 "이번 회의 주인공"이 있다.
역할: 주인공 / 적대자 / 동맹자 / 거울 / 비밀 보유자 / 새 인물 / 희생자 / 와일드카드
- 에피소드 아크 (소규모 변화) + 시즌 아크 (근본적 변화) 이중 구조.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
멀티 스토리라인 직조
━━━━━━━━━━━━━━━━━━━━━━━━━━━

A-Story (40~50%) + B-Story (25~30%) + C-Story (15~20%) + D-Story (5~10%)
- A·B는 매 에피소드 교차. 전환은 감정 대비로.
- Midpoint(EP4)에서 A·B 충돌, Finale(EP8)에서 A·B·C 합류.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENE RULES (씬 문법)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

모든 씬 필수 요소:
1. Scene Heading (S#번호. INT./EXT. 장소 — 시간)
2. Action (현재 시제, 영상적, 구체적)
3. Dialogue (캐릭터 보이스 구분)
4. Subtext (대사 아래 숨은 의도)
5. Turn (장면 내 반전 또는 변화)
6. Exit Hook (다음 장면 연결 압력)

Intention & Obstacle (드라이브샤프트):
- 모든 씬에서 "누가 무엇을 원하는가"와 "무엇이 막고 있는가"가 명확해야 한다.
- 이것이 씬의 엔진이다. 이것 없이 씬을 시작하지 마라.
- 판돈은 높고, 긴급하고, 납득 가능해야 한다.

Tactics = Character:
- 캐릭터를 정의하는 것은 프로필이 아니라 장애물을 넘는 방식이다.
- 위협으로 넘는 사람, 논리로 넘는 사람, 유혹으로 넘는 사람 — 전술이 곧 캐릭터다.
- 시리즈에서 이 전술은 에피소드마다 변화하며 시즌 아크를 만든다.

설계 순서: desire → obstacle → conflict → turn → emotional shift → exit pressure

Hook & Punch:
- Hook = 씬 첫 3줄 안에 관객의 주의를 잡는 장치
- Punch = 씬 마지막에 관객이 다음 씬을 보고 싶게 만드는 장치
- 모든 씬은 Hook으로 시작하고 Punch로 끝난다.

Drop in the Middle:
- 가능하면 대화의 중간에 관객을 던져라.
- EP1 첫 장면에서 시리즈 전체의 테마를 깔아라.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTION LINE (지문)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

지문은 카메라가 보는 것만 쓴다. 소설이 아니다.

[핵심 원칙]
- 한 단락 = 최대 3~4줄. 그 이상 길어지면 단락을 나눈다.
- 한 행동씩 줄바꿈하지 않는다. 흐름으로 묶어 쓴다.
- 보이는 것, 들리는 것만 쓴다. 인물의 내면 설명 금지.
- 불필요한 동작을 생략한다.
- 핵심 이미지 하나에 집중한다.
- 지문은 화면에서 재생되는 시간만큼만 읽히게 쓴다 (pithy).

[금지]
- "그는 ~한다. 그는 ~한다. 그는 ~한다." 반복 구조
- 행동의 모든 단계를 나열하는 것
- 감정을 지문으로 설명하는 것 ("그는 불안해하며")
- 카메라가 볼 수 없는 정보 ("그는 어젯밤 일을 떠올리며")

[좋은 지문]
"싱크대 앞의 지훈. 손을 문지른다 — 손금 사이 진흙이 지워지지 않는다. 수압을 올린다. 물소리가 주방을 채운다."

[나쁜 지문]
"그는 손을 물 아래에 넣는다. 손을 문지른다. 손바닥. 손등. 손가락 사이. 손톱 밑."

━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIALOGUE (대사)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

- 각 인물은 고유한 말투 리듬, 문장 길이, 공격/방어 스타일을 가진다.
- 캐릭터 바이블의 말투 규칙·대사 샘플을 반드시 참조하라.
- 누가 말해도 같은 말투이면 실패. 설명성 대사 금지. 서브텍스트 필수.
- 시리즈에서 대사는 캐릭터의 "시그니처"가 되어야 한다 — 8시간 동안 관객 귀에 남는 말투.

Dialogue = Music:
- 대사는 음악이다. 페이싱, 케이던스, 톤, 볼륨이 있다.
- 대사를 소리 내어 읽었을 때 리듬이 살아 있어야 한다.
- 현실 대화를 모방하지 마라. 현실보다 날카롭고, 압축되고, 집중된다.

"Too Wet" 금지:
- 관객이 느껴야 할 감정을 캐릭터가 직접 수행하면 안 된다.
- 슬픈 장면에서 캐릭터가 울면 관객은 울지 않는다.
- 감정을 참는 캐릭터가 감정을 터뜨리는 캐릭터보다 강하다.

대사 목적 (최소 하나):
seduction / evasion / interrogation / intimidation / masking_pain /
status_play / manipulation / confession_resisted / comic_misdirection / emotional_deflection

━━━━━━━━━━━━━━━━━━━━━━━━━━━
EMOTIONAL CHAIN (감정 연쇄 법칙)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

한 장면의 감정 톤이 틀리면 에피소드 끝까지 무너진다.
시리즈에서는 한 에피소드의 톤이 틀리면 시즌 전체가 무너진다.

[3% 법칙]
미스캐스팅 조금, 공간이 조금 다르고, 음악 톤이 살짝 빗나가면 — 3%씩 빗나간 것들이 쌓여
결국 의도와 정반대 작품이 된다. 모든 씬의 감정 톤은 전체 설계와 일치해야 한다.

[감정 연쇄]
- A 장면의 감정이 B 장면의 전제가 된다. 전제가 틀리면 결론이 작동하지 않는다.
- 에피소드 내: 씬 → 씬 간 감정 연쇄.
- 에피소드 간: 클리프행어의 감정이 다음 에피소드 콜드 오프닝의 전제.
- 시즌 전체: EP1의 톤이 EP8의 카타르시스를 결정한다.

[진정성]
- 추상적 설정이 아니라 구체적 경험에서 나오는 디테일이 장면을 살린다.
- 캐릭터가 어디서 장을 보고, 어릴 때 뭘 봤고, 어떤 학교를 다녔는지.
- 작가가 진짜 아는 감정, 진짜 겪은 관계에서 나온 장면이 가장 강하다.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
관객 심리 설계 (AUDIENCE ENGAGEMENT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

시나리오는 관객의 호기심을 설계하는 것이다.

[1. Dramatic Irony — 관객이 더 많이 안다]
관객이 캐릭터보다 더 많은 정보를 가질 때 긴장이 극대화된다.
시리즈 적용: 에피소드 단위로 관객이 먼저 아는 정보 관리. 캐릭터A는 모르지만 관객은 안다.

[2. Information Gap — 호기심의 간극]
시즌 질문 = 가장 큰 Gap. 에피소드마다 Gap을 좁히지만 완전히 닫지 않는다.
모든 비트에서 최소 1개의 "열린 질문"이 유지되어야 한다.

[3. Zeigarnik Effect — 미완성이 기억에 남는다]
클리프행어의 원리 그 자체. 미완성 = 기억 = 다음 회 시청.
매 비트 끝에 최소 1개의 미해결 질문 또는 중단된 행동을 남겨라.

[4. Pattern & Violation — 패턴을 만들고 깨뜨려라]
시리즈는 패턴을 만들 시간이 충분. EP1~3 패턴 확립 → EP4~5 파괴.
3번 반복하고 4번째에서 뒤집어라.

[5. Delayed Gratification — 지연된 보상]
시리즈에서 훨씬 오래 지연 가능. 시즌 전체에 걸친 지연이 최대 보상.
관객이 원하는 것을 바로 주지 마라. 다른 씬으로 전환하라.

[6. Mystery Box — 열리지 않은 상자]
비밀 경제와 직결. 상자를 하나 열면 더 큰 상자가 나타난다.
한꺼번에 다 열면 긴장이 사라진다.

시리즈 특화:
- Appointment Viewing — 다음 회를 기다리게 만드는 것. "알아야 한다"는 강박.
- Water Cooler Moment — 에피소드당 최소 1개의 화제 장면.
- Rewatchability — 시즌 끝까지 본 관객이 1화를 다시 보면 복선을 재발견.

[실패 신호]
- 관객이 이미 알고 있는 것을 캐릭터가 길게 설명 → 지루
- 질문을 던지고 즉시 답함 → 호기심 소멸
- 모든 비밀이 한 씬에서 다 드러남 → 긴장 붕괴
- 패턴 없이 무작위 사건만 나열 → 관객이 예측을 포기하고 이탈
- 관객이 아무것도 모른 채 20분 → 혼란, 즉시 이탈

━━━━━━━━━━━━━━━━━━━━━━━━━━━
NONSENSE FILTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━

절대 출력 금지:
목적 없는 장면 / 갈등 없는 대화 / 장르 효능 없는 장면 / 보이스 중복 /
전환 없는 장면 / 설명성 대사 과다 / 시즌 아크 무관 가지치기 / 설교 대사

Unified Plot Test:
- 이 씬을 빼면 에피소드가 작동하는가? → Yes면 삭제.
- 이 대사를 빼면 씬이 작동하는가? → Yes면 삭제.
- 시즌 질문과 무관한 것은 전부 깎아내라.

Probable Impossibility > Improbable Possibility:
- 믿을 수 있는 불가능(extraordinary but believable)은 허용한다.
- 억지스러운 우연(ordinary but forced coincidence)은 금지한다.
- 주인공이 우연이나 행운으로 구원받는 것(deus ex machina)은 절대 금지.

━━━━━━━━━━━━━━━━━━━━━━━━━━━
콜드 오프닝
━━━━━━━━━━━━━━━━━━━━━━━━━━━

EP1 콜드 오프닝 = 시리즈 전체 톤과 장르를 3분 안에 확립
EP2~ 콜드 오프닝 = 직전 클리프행어 연결 또는 새로운 훅
콜드 오프닝 끝에 미니 클리프행어 (타이틀 전환 순간의 긴장)

━━━━━━━━━━━━━━━━━━━━━━━━━━━
SAFETY & CONTENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━

이 엔진은 상업 시리즈 시나리오를 쓰는 전문 도구다.
시리즈 시나리오는 범죄, 폭력, 살인, 납치, 마약, 폭발, 자살 시도, 부패, 전쟁 등 어두운 소재를 다룬다.
이것은 허구적 서사 창작이며, 아래 원칙 안에서 자유롭게 집필한다.

[허용]
- 허구 시나리오 속 범죄/폭력/살인/마약/납치 묘사
- 악역의 범죄 계획이 서사적으로 제시되는 장면
- 스릴러/범죄/느와르/액션/호러 장르에 필요한 위협·충격·공포 묘사
- 성적 긴장, 유혹, 관계의 육체적 표현 (장르에 필요한 수준)
- 도덕적 타락, 부패, 배신, 죄책감 등의 인간 드라마
- 거친 언어, 욕설, 비속어 (캐릭터와 장르에 부합할 때)

[운영 원칙]
- 폭력/범죄 소재는 드라마 기능으로 다룬다 — 수법 자체보다 인물, 대가, 긴장, 윤리성 우선
- 묘사는 유지하되 실전 매뉴얼처럼 읽히지 않게 한다
- 고어/잔혹 수준은 장르와 톤에 맞춰 조절한다

[금지]
- 현실 범죄 실행을 위한 단계별 지침
- 무기·폭발물·독극물·마약의 구체적 제조법
- 고어 묘사 자체가 목적인 출력

━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORMAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━

한국어 출력. 한국 표준 시나리오 서식:

S#번호. INT./EXT. 장소 — 시간

(Action — 현재시제, 시각적, 3~4줄 단락)

    캐릭터명
    (parenthetical)
대사
""".strip()


# ═══════════════════════════════════════════════════════════
# GENRE RULE PACKS (5 시리즈 장르 — Writer Engine 구조 통일)
# ═══════════════════════════════════════════════════════════

GENRE_RULES = {
    "범죄/스릴러": {
        "en": "Crime / Thriller Series",
        "core": "정보 비대칭과 압박 설계로 매 회 관객 불안을 지속시키는 장르.",
        "engine": "사건 엔진 — 매 회 수사 진전 + 새로운 용의자/증거",
        "season_q": "\"범인은 누구인가?\" 또는 \"주인공은 살아남는가?\"",
        "opening": "사건의 결과부터 — 시체, 범죄 현장, 또는 사건의 여파를 먼저 보여주고 '어떻게?'로 끈다.",
        "ep_pattern": "EP1:사건발생+수사시작 / EP4:1차용의자반전(진범아님) / EP7:진범정체공개 / EP8:최종대결+도덕적대가",
        "items": [
            "pressure_escalation", "information_asymmetry", "clock_or_deadline",
            "threat_visibility_control", "suspicion_transfer", "moral_compromise",
            "false_safety", "reversal_pressure", "investigation_momentum", "dread_carry_over",
        ],
        "hooks": "시계가 돌아간다 / 누군가 지켜보고 있다 / 안전한 곳이 위험해진다",
        "punches": "단서가 뒤집힌다 / 믿었던 인물이 의심 대상 / 시간이 줄어든다",
        "cliffhangers": "새로운 증거/용의자/위협",
        "fails": ["압박 약함", "단서 평면적", "반전 억지", "인물이 너무 쉽게 말함"],
        "forbidden": "수사관의 독백으로 사건 정리, 우연의 단서 발견",
    },
    "드라마": {
        "en": "Drama Series",
        "core": "인간의 선택과 대가를 통해 관계의 진실에 도달하는 장르.",
        "engine": "관계 엔진 — 매 회 관계의 균열·복원·변화",
        "season_q": "\"이 가족/공동체는 다시 하나가 될 수 있는가?\"",
        "opening": "고요한 균열 — 평범한 일상인데 뭔가 하나가 어긋나 있다.",
        "ep_pattern": "캐릭터 아크가 플롯보다 중요. 매 회 관계가 전진하거나 후퇴.",
        "items": [
            "emotional_truth", "character_depth", "moral_complexity",
            "relationship_dynamics", "vulnerability_escalation", "quiet_power",
            "dialogue_weight", "consequence_chain", "identity_pressure", "catharsis_build",
        ],
        "hooks": "조용한 첫 이미지가 뒤집힐 것을 암시 / 인물의 일상 속 균열",
        "punches": "선택의 대가가 눈에 보이는 순간 / 관계가 돌이킬 수 없이 변하는 순간",
        "cliffhangers": "관계의 균열 / 숨겨진 진실 폭로 / 선택의 순간",
        "fails": ["감정이 표면적", "인물이 평면적", "관계 변화 없음", "대가 부재"],
        "forbidden": "감정을 직접 말하는 대사 (Too Wet), 갈등 없는 화해",
    },
    "호러": {
        "en": "Horror Series",
        "core": "공포의 예감과 축적으로 안전감을 체계적으로 파괴하는 장르.",
        "engine": "비밀 엔진 + 규칙 발견 — 매 회 공포의 규칙이 하나씩 드러남",
        "season_q": "\"이 저주/위협에서 벗어날 수 있는가?\"",
        "opening": "프롤로그 킬 — 본편 시작 전에 누군가 죽거나 사라진다. 위협의 규칙을 관객에게 먼저 보여준다.",
        "ep_pattern": "EP1:프롤로그킬+일상균열 / EP3~4:공포규칙발견 / EP6:규칙위반→대가 / EP8:최종대면",
        "items": [
            "fear_anticipation", "uncertainty", "sensory_unease",
            "threat_design", "dread_pacing", "violation_of_safety",
            "image_residue", "vulnerability", "false_relief", "terror_escalation",
        ],
        "hooks": "평범한 것이 이상하다 / 감각이 경고한다 / 보이지 않는 것의 존재감",
        "punches": "안전한 곳이 무너진다 / 보이지 않던 것이 보인다 / 가짜 안도 후 진짜 공포",
        "cliffhangers": "가짜 안도 후 진짜 공포 / 새로운 위협의 징후",
        "fails": ["놀람만 있고 공포 축적 없음", "위협 규칙 모호", "불안이 장면 밖으로 안 이어짐"],
        "forbidden": "공포 원인의 과잉 설명, jump scare만 반복",
    },
    "SF/판타지": {
        "en": "SF / Fantasy Series",
        "core": "세계의 규칙이 인간 드라마의 은유로 작동하는 장르.",
        "engine": "세계 엔진 — 매 회 세계관의 새로운 층이 열림",
        "season_q": "\"이 세계의 진짜 규칙은 무엇인가?\"",
        "opening": "세계 규칙 한 장면 — 이 세계가 우리와 다르다는 것을 첫 이미지로 보여준다.",
        "ep_pattern": "EP1:세계진입+규칙1개발견 / EP4:세계관진실뒤집힘 / EP8:규칙의대가+새질서",
        "items": [
            "world_rule_clarity", "wonder_value", "cost_of_rule",
            "ethical_implication", "rule_consistency", "novelty",
            "human_anchor", "visual_imagination", "mythic_depth", "payoff_of_world_rule",
        ],
        "hooks": "이 세계는 우리와 다르다 — 한 가지가 즉시 보인다 / 경이로운 이미지",
        "punches": "규칙의 대가가 드러난다 / 세계의 비밀이 인간 문제와 연결된다",
        "cliffhangers": "세계관 반전 / 능력의 대가 / 새로운 규칙 발견",
        "fails": ["룰 설명만 많음", "인간 드라마 약함", "세계관이 이야기보다 앞섬"],
        "forbidden": "세계관 설명 강의, 대가 없는 능력, 데우스 엑스 마키나",
    },
    "로맨스/멜로": {
        "en": "Romance / Melodrama Series",
        "core": "갈망의 축적과 감정의 지연이 만드는 아픔과 회수의 장르.",
        "engine": "관계 엔진 — 매 회 두 사람의 거리가 진동",
        "season_q": "\"이 두 사람은 결국 함께할 수 있는가?\"",
        "opening": "운명적 접점 또는 이별 직후 — 두 사람이 스쳐가거나, 이미 끝난 관계에서 시작한다.",
        "ep_pattern": "밀당의 리듬: 가까워짐→벽→더가까워짐→더큰벽",
        "items": [
            "desire_tension", "emotional_withholding", "longing_build",
            "vulnerability_reveal", "timing_misalignment", "intimacy_progression",
            "symbolic_motif", "ache_after_contact", "impossible_choice", "emotional_payoff",
        ],
        "hooks": "시선이 머무른다 / 닿을 듯 닿지 않는 거리 / 우연의 접근",
        "punches": "감정을 참는 순간 / 타이밍이 어긋나는 순간 / 작은 접촉의 전율",
        "cliffhangers": "오해 / 제3자 등장 / 진심 고백 직전 중단",
        "fails": ["고백만 많고 축적 없음", "끌림 이유 불명", "감정 온도 단조"],
        "forbidden": "오해가 대화 한 마디로 해결, 삼각관계 기계적 반복",
    },
}


def _genre_text(genre: str) -> str:
    """장르 Rule Pack → 프롬프트용 텍스트 (구체적 작동 지시 포함)."""
    r = GENRE_RULES.get(genre)
    if not r:
        return f"[장르: {genre}] — 범용 장르 규칙 적용."

    items_detail = "\n".join(f"  - {item}" for item in r["items"])

    return (
        f"[GENRE RULE: {genre} ({r['en']})]\n"
        f"\n"
        f"핵심 원칙: {r['core']}\n"
        f"시리즈 엔진: {r['engine']}\n"
        f"시즌 질문: {r['season_q']}\n"
        f"오프닝 전략: {r['opening']}\n"
        f"에피소드 패턴: {r['ep_pattern']}\n"
        f"\n"
        f"장르 필수 장치 (10개):\n"
        f"{items_detail}\n"
        f"\n"
        f"[장르 작동 규칙]\n"
        f"- 매 씬에서 위 10개 장치 중 최소 2개가 반드시 작동해야 한다.\n"
        f"- 비트 전체에서 10개 중 최소 5개 이상이 등장해야 한다.\n"
        f"- 장르 장치가 작동하지 않는 씬은 존재 이유가 없다.\n"
        f"\n"
        f"Hook (씬 시작): {r['hooks']}\n"
        f"Punch (씬 끝): {r['punches']}\n"
        f"클리프행어: {r['cliffhangers']}\n"
        f"\n"
        f"실패 신호: {' / '.join(r['fails'])}\n"
        f"금지: {r['forbidden']}"
    )


# ═══════════════════════════════════════════════════════════
# 시즌 비트 / 에피소드 비트 / 클리프행어
# ═══════════════════════════════════════════════════════════

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
    {"beat": 0, "name": "Cold Opening",       "minutes": "2~5분",  "role": "관객을 즉시 잡는 훅. 타이틀 전 시퀀스."},
    {"beat": 1, "name": "Act 1 - Setup",      "minutes": "~8분",   "role": "에피소드 질문 제시. 상황 설정."},
    {"beat": 2, "name": "Act 1 - Hook",       "minutes": "~7분",   "role": "에피소드의 방향 확립. A-Story 촉발."},
    {"beat": 3, "name": "Act 2A - Rising",    "minutes": "~8분",   "role": "갈등 심화. B/C 스토리 전개."},
    {"beat": 4, "name": "Act 2A - Twist",     "minutes": "~7분",   "role": "예상 못한 전환. 감정 대비."},
    {"beat": 5, "name": "Act 2B - Crisis",    "minutes": "~8분",   "role": "위기 고조. 에피소드 클라이맥스 준비."},
    {"beat": 6, "name": "Act 2B - Peak",      "minutes": "~7분",   "role": "에피소드 클라이맥스. 반전."},
    {"beat": 7, "name": "Act 3 + Cliffhanger","minutes": "~10분",  "role": "에피소드 질문 (부분) 해결 + 클리프행어."},
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


# ═══════════════════════════════════════════════════════════
# 에피소드 분량 기준
# ═══════════════════════════════════════════════════════════

EP_SCENE_TARGETS = {
    40: {"scenes": "30~40씬", "pages": "~40페이지", "beat_scenes": "4~5씬/비트"},
    50: {"scenes": "40~50씬", "pages": "~50페이지", "beat_scenes": "5~6씬/비트"},
    60: {"scenes": "50~60씬", "pages": "~60페이지", "beat_scenes": "6~7씬/비트"},
}


# ═══════════════════════════════════════════════════════════
# 유틸리티 함수
# ═══════════════════════════════════════════════════════════

def _format_season_beats(num_episodes: int) -> str:
    beats = SEASON_BEATS_8 if num_episodes == 8 else SEASON_BEATS_6
    return "\n".join(f"EP{b['ep']} — {b['beat']}: {b['role']}" for b in beats)

def _format_episode_beats() -> str:
    return "\n".join(
        f"Beat {b['beat']} [{b['name']}] ({b['minutes']}): {b['role']}"
        for b in EPISODE_BEATS
    )

def _format_cliffhangers() -> str:
    return "\n".join(f"- {c['type']}: {c['desc']}" for c in CLIFFHANGER_TYPES)

def _format_inputs(inputs: dict) -> str:
    labels = [
        ("logline", "LOGLINE"), ("intention", "기획의도"), ("gns", "GNS"),
        ("characters", "캐릭터+바이블"), ("world", "세계관"), ("structure", "구조"),
        ("scenes", "장면설계"), ("treatment", "트리트먼트"), ("tone", "톤문서"),
    ]
    parts = []
    for key, label in labels:
        val = inputs.get(key, "").strip()
        if val:
            parts.append(f"[{label}]\n{val}")
    return "\n\n".join(parts)


# ═══════════════════════════════════════════════════════════
# 1. 시즌 아크 설계
# ═══════════════════════════════════════════════════════════

def build_season_arc_prompt(
    inputs: dict, num_episodes: int, duration: int, genre: str,
) -> str:
    gr = _genre_text(genre)
    season_beats = _format_season_beats(num_episodes)
    cliffhangers = _format_cliffhangers()
    target = EP_SCENE_TARGETS.get(duration, EP_SCENE_TARGETS[50])

    return f"""아래 기획 자료를 바탕으로 {num_episodes}부작 시리즈(에피소드당 {duration}분, {target['scenes']})의 **시즌 아크**를 설계하라.

══ 기획 자료 ══
{_format_inputs(inputs)}

══ 장르 ══
{gr}

══ 시즌 비트 구조 ({num_episodes}부작) ══
{season_beats}

══ 클리프행어 유형 ══
{cliffhangers}

═══ 출력 형식 ═══

### 1. 시리즈 엔진
이 시리즈를 매 회 굴리는 엔진 (사건/비밀/관계/세계 중 택1 + 구체 설명)

### 2. 시즌 질문
시즌 전체를 관통하는 대질문 1개.

### 3. 에피소드별 시즌 비트
EP1~EP{num_episodes}, 각 에피소드:
- 시즌 비트 이름
- 에피소드 질문
- A/B/C/D 스토리라인 진행 요약 (각 1~2줄)
- 핵심 사건 (3~5줄)
- 클리프행어 (유형 명시 + 구체 내용)
- Water Cooler Moment (이 회의 화제 장면)
- 시즌 질문 진전도

### 4. 캐릭터별 시즌 아크
앙상블 전원(4~8명):
- 역할 (주인공/적대자/동맹자/거울/비밀보유자/새인물/희생자/와일드카드)
- 전술 (Tactics = Character: 장애물을 넘는 방식 3가지)
- EP1 출발점 → EP{num_episodes} 도착점 (시즌 아크)
- POV 에피소드

### 5. Secret Map (비밀 지도)
비밀 A: [내용] — 소유자 — 공개: EP? — 폭발: ?
(최소 4개. 관객이 아는 비밀 / 관객도 모르는 비밀 표기)

### 6. 멀티 스토리라인 배분
A/B/C/D 각 설명 + 비중

### 7. 에스컬레이션 곡선
EP1 → EP{num_episodes} 판돈 상승 경로.

### 8. 감정 연쇄 설계
시즌 전체의 감정 톤 흐름. EP1의 톤이 EP{num_episodes}의 카타르시스를 어떻게 결정하는가.

한국어로, 시나리오 전문 작가의 언어로."""


# ═══════════════════════════════════════════════════════════
# 1.5. 핵심 요소 추출 (Story Elements Extraction)
# ═══════════════════════════════════════════════════════════

def build_extract_elements_prompt(
    inputs: dict, season_arc: str, genre: str,
) -> str:
    """기획 자료 + 시즌 아크에서 시나리오 집필에 필수적인 핵심 요소를 추출한다.
    이 결과는 매 비트 집필 시 강제 주입된다."""

    return f"""
[TASK] 핵심 요소 추출 — Story Elements Extraction (시리즈)

아래 기획 자료와 시즌 아크를 분석하여 시나리오 집필에 반드시 반영해야 할 핵심 요소를 추출하라.
이 추출 결과는 매 비트 집필 시 강제로 주입되어, 누락을 방지한다.

[기획 자료]
{_format_inputs(inputs)}

[시즌 아크]
{season_arc[:4000]}

[장르]
{_genre_text(genre)}

[추출 항목 — 아래 형식으로 정확히 출력하라]

===맥거핀===
- 맥거핀 1: (이름) — (역할) — (처음 등장 에피소드) — (최종 역할)
(맥거핀 = 플롯을 움직이는 핵심 소도구/정보/장소. 없으면 "없음")

===캐릭터 비밀===
- (인물명)의 비밀: (내용) — 폭로 시점: EP? — 폭로 시 영향: (누구에게 어떤 변화)
(시즌 아크의 Secret Map + 캐릭터 바이블에서 모두 추출)

===캐릭터 전술===
- (인물명): 전술1 / 전술2 / 전술3
(Tactics = Character: 장애물을 넘는 방식. 캐릭터 바이블에서 추출)

===핵심 장소===
- (장소명): (역할) — (감정적 의미) — (반복 등장 규칙)
(톤 문서 + 세계관에서 추출)

===모티프===
- (모티프명): (등장 규칙)
(톤 문서의 motifs에서 추출. 예: "물 — 모든 씬에서 물이 어디에 있는지 확인")

===에피소드별 클라이맥스 설계===
- EP1 클라이맥스: (핵심 행동 + 클리프행어)
- EP2: ...
- ...EP{8 if 'structure' in str(inputs) else 6}: ...

===톤 하드 룰===
- (톤 문서에서 추출한 절대 규칙들)

각 항목은 기획 자료에서 직접 추출. 없는 항목은 "기획 자료에 없음 — 집필 시 설계 필요"로 표기.
""".strip()


# ═══════════════════════════════════════════════════════════
# 2. 에피소드별 씬 플랜
# ═══════════════════════════════════════════════════════════

def build_episode_plan_prompt(
    inputs: dict, season_arc: str,
    ep_num: int, num_episodes: int, duration: int, genre: str,
    prev_episode_plan: str = "", prev_episode_last_scene: str = "",
) -> str:
    gr = _genre_text(genre)
    ep_beats = _format_episode_beats()
    target = EP_SCENE_TARGETS.get(duration, EP_SCENE_TARGETS[50])

    continuity = ""
    if prev_episode_plan:
        continuity += f"══ 직전 에피소드(EP{ep_num - 1}) 씬 플랜 ══\n{prev_episode_plan[-3000:]}\n\n"
    if prev_episode_last_scene:
        continuity += (
            f"══ 직전 에피소드 마지막 씬/클리프행어 ══\n{prev_episode_last_scene}\n"
            f"→ 이 에피소드의 콜드 오프닝은 위의 클리프행어와 연결되어야 한다.\n\n"
        )

    return f"""아래 시즌 아크와 기획 자료를 바탕으로 **EP{ep_num}의 씬 플랜**을 작성하라.

══ 기획 자료 (요약) ══
{_format_inputs(inputs)}

══ 시즌 아크 ══
{season_arc[:4000]}

══ 장르 ══
{gr}

{continuity}

══ 에피소드 내부 비트 구조 ══
{ep_beats}

══ EP{ep_num} 씬 플랜 작성 규칙 ══

분량: {duration}분, 씬 수: {target['scenes']}, 비트당: {target['beat_scenes']}

[씬 다양성 — 에피소드를 지루하지 않게 채우는 핵심]
5종 씬 타입을 반드시 혼합 배치하라:
  [A] 메인 사건 씬 (50~60%) — A-Story. 플롯 전진. 갈등과 전환.
  [B] 서브플롯 씬 (20~25%) — B/C-Story. 관계·감정·테마. 메인과 다른 감정 톤.
  [C] 멀티라인 씬 (10~15%) — C/D-Story. 다른 인물의 시점. 세계 확장.
  [BR] 호흡 씬 (5~8%) — 캐릭터의 인간적 순간. 대사 0~1개.
       예: 커피를 마시며 창밖을 보는 주인공. 무전기를 내려놓는 손.
  [CUT] 컷어웨이 씬 (3~5%) — 동시다발 진행. 리듬 전환.

장소 분산 규칙:
- 같은 장소에서 연속 3씬 이상 금지.
- INT. 5개 연속이면 반드시 EXT. 1개.
- 전체 씬의 최소 15%는 EXT.

씬 길이 변주:
- 긴 대화 씬(3~4분) 뒤에는 짧은 행동/이미지 씬(30초~1분).
- 같은 감정 톤의 씬이 3개 연속이면 안 된다.

[멀티 스토리라인 직조]
- A 씬 2~3개 → B 씬 1개 → A 씬 2개 → C 씬 1개 → BR → 반복
- 스토리라인 간 전환은 감정 대비로 (긴장→이완, 슬픔→유머)

출력 형식:

### EP{ep_num} 씬 플랜 — [에피소드 부제]

**에피소드 질문**: [이 회에서 열리는 질문]
**POV 인물**: [이번 회의 주인공]
**클리프행어 유형**: [유형 + 구체 내용]

[Cold Opening]
S#1. INT./EXT. 장소 — 시간 | [A]/[B]/[C]/[BR]/[CUT] | 인물 | Hook
  요약 (2~3줄)
S#2. ...

[Beat 1 — Act 1 Setup]
S#3. 장소 — 시간 | [A] | 인물 | Hook/Punch
  요약
...

[Beat 7 — Act 3 + Cliffhanger]
S#마지막. 장소 — 시간 | [A] | 인물 | ★Punch=클리프행어
  요약 + 클리프행어 상세

---
마지막에:
- 이 에피소드 씬 수 / 씬 타입별 수: [A] 00 / [B] 00 / [C] 00 / [BR] 00 / [CUT] 00
- INT/EXT 비율
- Water Cooler Moment (화제 장면)
- 에피소드 종료 시 열린 질문
- 시즌 질문 진전
- 비밀 경제 현황: 터진 비밀 / 새로 생긴 비밀 / 유지 중인 비밀

한국어, 간결하고 시각적인 시나리오 작가의 언어로."""


# ═══════════════════════════════════════════════════════════
# 3. 비트별 집필
# ═══════════════════════════════════════════════════════════

def build_write_episode_beat_prompt(
    inputs: dict, season_arc: str, episode_plan: str,
    ep_num: int, beat_num: int,
    num_episodes: int, duration: int, genre: str,
    prev_beat_text: str = "", character_bible: str = "",
    story_elements: str = "",
) -> str:
    gr = _genre_text(genre)
    beat_info = EPISODE_BEATS[beat_num] if beat_num < len(EPISODE_BEATS) else EPISODE_BEATS[-1]
    target = EP_SCENE_TARGETS.get(duration, EP_SCENE_TARGETS[50])

    # 캐릭터 바이블 — 매번 전문 (최대 4000자)
    char_block = character_bible[:4000] if character_bible else "(캐릭터 정보 없음)"
    # 톤 — 매번 포함
    tone_block = inputs.get("tone", "")[:1500]
    # 트리트먼트
    treat_block = inputs.get("treatment", "")[:3000]

    # 직전 비트 연속성
    prev_block = ""
    if prev_beat_text:
        tail = prev_beat_text[-2500:]
        prev_block = f"\n[직전 비트 마지막 부분 — 연속성 유지]\n{tail}\n"

    # Beat 0 = 콜드 오프닝 특별 지시
    cold_open_block = ""
    if beat_num == 0:
        genre_data = GENRE_RULES.get(genre, {})
        opening_strategy = genre_data.get("opening", "")
        cold_open_block = f"""
[⚡ 콜드 오프닝 특별 지시 — Beat 0 전용]
타이틀 전 시퀀스. 2~5분 분량.
관객을 즉시 잡는 훅으로 시작하라.

오프닝 전략: {opening_strategy}

[콜드 오프닝 규칙]
- 첫 씬의 첫 3줄이 관객의 호기심을 잡아야 한다. 설명으로 시작하지 마라.
- EP1: 시리즈 전체의 테마를 깔아라. Drop in the Middle.
- EP2~: 직전 클리프행어 연결 또는 새로운 훅.
- 콜드 오프닝 끝에 미니 클리프행어.
- "--- TITLE ---" 라인으로 콜드 오프닝 종료를 표시하라.
"""

    # Beat 7 = 클리프행어 특별 지시
    cliff_block = ""
    if beat_num == 7:
        cliff_block = """
[⚡ 클리프행어 특별 지시 — Beat 7 전용]
이 비트는 에피소드 마지막 비트다.
- 에피소드 질문을 (부분적으로) 해결하라.
- 반드시 클리프행어로 끝내라. 씬 플랜에 명시된 유형과 내용을 따르라.
- 클리프행어는 마지막 씬의 마지막 줄이어야 한다.
- "다음 에피소드를 안 볼 수 없는" 수준의 긴장으로 끝내라.
- 감정 연쇄: 이 클리프행어의 감정이 다음 에피소드 콜드 오프닝의 전제다.
"""

    # 핵심 요소 블록
    elements_block = ""
    if story_elements:
        elements_block = f"""
[⚡ 핵심 요소 — 반드시 반영. 누락 시 실패.]
{story_elements}

[핵심 요소 강제 규칙]
0. 위 핵심 요소의 맥거핀, 캐릭터 비밀, 핵심 장소, 모티프가 이 비트에 해당되면 반드시 씬에 등장시켜라.
   - 맥거핀: 이 비트에서 어떻게 관여하는가?
   - 캐릭터 비밀: 이 비트에서 폭로되는 비밀? 유지되는 비밀?
   - 핵심 장소: 감정적 의미·규칙을 반영하라.
   - 모티프: 매 씬에서 모티프가 어디에 있는지 확인하라.
   - 캐릭터 전술: 바이블의 전술 목록과 일치하는지 확인.
"""

    return f"""
[TASK] EP{ep_num} Beat {beat_num} 시나리오 집필 — {beat_info['name']}
{beat_info['role']}

이 비트에 해당하는 모든 씬을 한국 표준 시나리오 서식으로 집필하라.

[장르]
{gr}

[로그라인] {inputs.get('logline', '(씬 플랜 참조)')[:300]}
{cold_open_block}
{cliff_block}

[시즌 아크 (요약)]
{season_arc[:2500]}

[EP{ep_num} 씬 플랜 — 이 비트의 씬을 찾아 정확히 따르라]
{episode_plan}

[캐릭터 바이블 — 각 인물의 말투·리듬·태도를 반드시 반영]
{char_block}

[세계관]
{inputs.get('world', '')[:1500] or '(씬 플랜 참조)'}

[트리트먼트 참조]
{treat_block}

{f"[톤 문서]{chr(10)}{tone_block}" if tone_block else ""}
{prev_block}
{elements_block}

[RULES — 분량 기준 ★반드시 준수★]
1. 씬 플랜에서 Beat {beat_num}의 씬들을 찾아 전부 집필.
2. 1씬 = 600~800자(한국어). 200자 미만 씬은 너무 짧다. 반드시 600자 이상 쓸 것.
   단, [BR] 호흡 씬은 200~400자도 허용. 짧지만 이미지가 강해야 한다.
3. 비트당 총 3,500~5,000자 이상. 이 분량에 미달하면 씬이 부족하거나 너무 얇은 것이다.
4. 지문 3~4줄 + 대사 2~4개 교환 + turn + exit hook = 1씬의 최소 구성.
5. 대사 없이 지문만으로 끝나는 씬은 1~2개까지만 허용.

[씬 다양성]
5-1. 씬 플랜의 씬 타입([A]/[B]/[C]/[BR]/[CUT])을 반드시 따르라:
   [A] 메인 사건 씬 — 플롯 전진. 갈등과 전환.
   [B] 서브플롯 씬 — 관계·감정·테마. 메인과 다른 감정 톤.
   [C] 멀티라인 씬 — 다른 인물의 시점. 세계 확장.
   [BR] 호흡 씬 — 짧다(200~400자도 OK). 캐릭터의 인간적 순간. 대사 0~1개.
   [CUT] 컷어웨이 씬 — 동시다발. 리듬 전환.

5-2. 씬 리듬 변주:
   - 긴 대화 씬 뒤에는 짧은 행동/이미지 씬.
   - 긴장 씬 뒤에는 이완 씬. 같은 감정 톤 3개 연속 금지.

5-3. 장소 분산:
   - 같은 장소에서 연속 3씬 금지.

[장르 강제 적용]
6. 이 비트의 모든 씬에서 장르 필수 장치 10개 중 최소 2개 작동.
7. 비트 전체에서 장르 장치 5개 이상 등장.
8. 장르의 Hook으로 시작, Punch로 끝내라.
9. 장르 실패 신호가 느껴지면 그 씬은 다시 써야 한다.

[멀티 스토리라인]
- 씬 플랜의 A/B/C 스토리라인 배치를 따르라.
- 스토리라인 전환은 감정 대비로.

[관객 심리 설계]
- Dramatic Irony: 관객에게 캐릭터가 모르는 정보를 먼저 줘라.
- Information Gap: 최소 1개의 "열린 질문" 유지.
- Zeigarnik: 비트 끝에 미해결 질문 또는 중단된 행동.
- Pattern & Violation: 반복 패턴을 깨뜨릴 타이밍인지 점검.
- Delayed Gratification: 관객이 원하는 정보/만남/대결을 최대한 늦춰라.

[집필 규칙]
10. 캐릭터 바이블의 말투·대사 샘플 참조 → 보이스 구분. 시리즈는 8시간 동안 귀에 남는 시그니처 말투.
11. desire → obstacle → conflict → turn → emotional shift → exit pressure
12. 대사 = 행동. 서브텍스트 필수. 설명성 대사 금지. Too Wet 금지.
13. 직전 비트와의 연속성 유지.
14. 지문(Action Line): 한 단락 3~4줄. "그는~한다" 반복 금지. 핵심 이미지만. pithy.
15. 감정 연쇄 — 3% 법칙. 이 씬의 감정 톤이 다음 씬의 전제.
16. Intention & Obstacle — 매 씬에서 "누가 뭘 원하고, 뭐가 막는가" 명확히.
17. Nonsense Filter — 목적 없는 장면, 시즌 아크 무관 가지치기 금지.

[OUTPUT]
맨 위에 헤더:

═══════════════════════════════════════
EP{ep_num} — Beat {beat_num}. {beat_info['name']}
═══════════════════════════════════════

씬들을 순서대로 집필. 씬 사이 빈 줄 2개.
마지막에 --- 후 내부 메모:
- 비트 요약 1줄
- 작동한 장르 장치 목록
- 핵심 요소 추적: 등장한 맥거핀/비밀/핵심장소/모티프
- 스토리라인 진행: A/B/C 각 상태
- 관객 심리: 현재 유지 중인 열린 질문 / Dramatic Irony
- 비밀 경제: 이 비트에서의 비밀 상태
- 보이스 점검 1줄
""".strip()


# ═══════════════════════════════════════════════════════════
# 4. 비트 다시 쓰기
# ═══════════════════════════════════════════════════════════

def build_rewrite_prompt(
    beat_text: str, instruction: str,
    genre: str = "", character_bible: str = "",
) -> str:
    gr = _genre_text(genre)
    char_block = character_bible[:3000] if character_bible else ""
    user_inst = instruction.strip() if instruction else "극적 힘, 서브텍스트, 캐릭터 보이스, 장르 효능, Hook & Punch, 클리프행어를 강화하라."

    return f"""
[TASK] 비트 다시 쓰기 — {user_inst}

[장르]
{gr}

{f"[캐릭터 바이블 — 말투 반영 필수]{chr(10)}{char_block}" if char_block else ""}

[현재 텍스트]
{beat_text}

[RULES]
1. 강점 유지, 약점 개선.
2. 보이스 분리 강화 — 캐릭터 바이블 말투 규칙 반드시 참조. 시리즈 시그니처 말투.
3. 서브텍스트·장르 효능 강화. Too Wet 금지.
4. 설명성 대사 제거.
5. 지문 압축 — 소설체 금지. 한 단락 3~4줄. 핵심 이미지만. "그는~한다" 반복 금지.
6. Hook(씬 시작)과 Punch(씬 끝) 모든 씬에 점검·보강.
7. 감정 연쇄 점검 — 3% 법칙. 씬 간 감정 톤 일관성.
8. Intention & Obstacle — 매 씬에서 "누가 뭘 원하고, 뭐가 막는가" 명확히.
9. 분량 점검 — 1씬 600~800자. [BR] 씬은 200~400자 허용.
10. 멀티 스토리라인 전환 시 감정 대비 확인.

[OUTPUT]
개선된 시나리오 전문. 마지막에 --- 후 변경 요약 3줄.
""".strip()
