# 👖 BLUE JEANS SERIES ENGINE v1.6

**Netflix 미니시리즈/시리즈(시즌 1) 시나리오 집필 엔진**

> BLUE JEANS PICTURES · Series Writing Pipeline  
> Creator Engine → **Series Engine** → Rewrite Engine

---

## 한 줄 정의

시즌 아크 → 에피소드 씬 플랜 → 비트 단위 집필 구조 위에 클리프행어 시스템, 비밀 경제, 앙상블 캐릭터, 멀티 스토리라인 직조, 서사동력 프레임워크, LOCKED 설정 보호를 중첩 제어하여 **"매 회 끝에 다음 회를 안 볼 수 없는 시리즈 시나리오"**를 쓰는 집필 엔진.

---

## 파일 구조

```
series-engine/
├── main.py              (1,096줄) — Streamlit 메인 앱
├── prompt.py            (1,262줄) — 시리즈 작법 원칙 + 빌더 함수
├── requirements.txt     — streamlit, anthropic, python-docx
└── .streamlit/
    └── config.toml      — 라이트모드 (Creator Engine 통일)
```

## 실행 환경

| 항목 | 값 |
|------|------|
| Python | 3.9+ |
| streamlit | ≥1.30 |
| anthropic | ≥0.40 |
| python-docx | ≥1.0 |
| 집필 모델 | claude-opus-4-6 |
| 구조 모델 | claude-sonnet-4-6 |
| API KEY | ANTHROPIC_API_KEY (Streamlit Secrets) |

## 배포

1. GitHub에 `cinepark-1974/series-engine` 레포 생성
2. 4개 파일 push (main.py, prompt.py, requirements.txt, .streamlit/config.toml)
3. Streamlit Cloud에서 New app → 레포 연결 → main branch → main.py
4. Secrets에 `ANTHROPIC_API_KEY` 설정
5. Deploy

## 파이프라인 (5단계)

```
STEP 1: 자료 입력
  Creator Engine 9칸 붙여넣기 + 에피소드 수(6/8) + 분량(40/50/60분) + 장르
  + LOCKED/OPEN 설정 잠금
     ↓
STEP 2: 시즌 아크 설계 (Sonnet) ← 1회 클릭
  → 시즌 비트 / 시즌 질문 / Secret Map / 클리프행어 / 멀티라인 / 서사동력
     ↓
STEP 2.5: 핵심 요소 추출 (Sonnet) ← 1회 클릭
  → 맥거핀 / 캐릭터 비밀·전술·말투 / 핵심 장소 / 모티프 / 서사동력 / 톤 하드 룰
     ↓
STEP 3: 에피소드별 씬 플랜 (Sonnet) ← 에피소드당 1회 클릭
  → 콜드 오프닝 + 8비트 + 클리프행어 + [A]/[B]/[C]/[BR]/[CUT] 씬 타입
     ↓
STEP 4: 비트별 집필 (Opus) ← 에피소드당 8비트 = 8회 클릭
  → SCOPE MANDATE + 5단계 서술 구조 + 빌런 추적 + LOCKED 검증
  + 마지막 비트 다시 쓰기 (Opus)
     ↓
STEP 5: 다운로드
  → 에피소드별 TXT/DOCX + 시즌 전체 TXT/DOCX
```

**총 클릭 수 (8부작 기준):** 시즌 아크 1 + 요소 추출 1 + 씬 플랜 8 + 집필 64 = **74회**

## 디자인 시스템

Creator Engine과 완전 통일:
- CSS 변수: `--navy: #191970`, `--y: #FFCB05`, `--bg: #F7F7F5`
- 폰트: Pretendard + Paperlogy + Playfair Display
- 컴포넌트: 노란 섹션 헤더, 콜아웃, 카드, 5단계 Stepper
- 브랜드 헤더: `BLUE JEANS PICTURES → SERIES ENGINE → YOUNG·VINTAGE·FREE·INNOVATIVE`

## 버전 히스토리

| 버전 | 주요 변경 |
|------|----------|
| v1.0 | 초기 빌드. 5단계 파이프라인, 시리즈 작법 5대 원칙 |
| v1.1 | Writer Engine v2.2 통합 (씬 문법, 지문, 대사, 감정 연쇄, Nonsense Filter, 씬 다양성, Story Elements, Genre Pack, Safety) |
| v1.2 | Creator Engine v1.4 통합 (B-Story 강화, 5단계 서술 구조, 클리프행어 강화, 느와르·액션·코미디 추가) |
| v1.3 | SCOPE MANDATE (비트 = 복수 씬 커버 강제), B-Story 시간축 시각화 |
| v1.4 | Creator Engine 캐릭터 구조 통합 (characters + extended_characters, 바이블 필드 활용 규칙) |
| v1.5 | 모델 분리 (Opus=집필, Sonnet=구조) |
| v1.6 | LOCKED/OPEN 시스템, 빌런 추적, 서사동력 프레임워크, 느와르→범죄/스릴러 통합 |

---

© 2026 BLUE JEANS PICTURES · Series Engine v1.6
