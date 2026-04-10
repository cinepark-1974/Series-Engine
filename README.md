# 👖 BLUE JEANS SERIES ENGINE v1.7

**Netflix 미니시리즈/시리즈(시즌 1) 시나리오 집필 엔진**

> BLUE JEANS PICTURES · Series Writing Pipeline  
> Creator Engine → **Series Engine** → Rewrite Engine

---

## 한 줄 정의

시즌 아크 → **시리즈 확장(캐릭터·사건 보강)** → 에피소드 씬 플랜 → 비트 단위 집필 구조 위에 **Planting & Payoff 시리즈 맵, AI Escape A1~A10, Genre Drive 5-point Check, 비트 구조 변주 6유형, Villain 4 Questions**, 클리프행어 시스템, 비밀 경제, 앙상블 캐릭터, 멀티 스토리라인 직조, 서사동력 프레임워크, LOCKED 설정 보호를 중첩 제어하여 **"매 회 끝에 다음 회를 안 볼 수 없는 시리즈 시나리오"**를 쓰는 집필 엔진.

---

## 파일 구조

```
series-engine/
├── main.py              (1,384줄) — Streamlit 메인 앱
├── prompt.py            (1,657줄) — 시리즈 작법 원칙 + 빌더 함수
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

## 파이프라인 (6단계 — v1.7 확장)

```
STEP 1: 자료 입력
  Creator Engine 9칸 붙여넣기 + 에피소드 수(6/8) + 분량(40/50/60분) + 장르
  + LOCKED/OPEN 설정 잠금
     ↓
STEP 2: 시즌 아크 설계 (Sonnet) ← 1회 클릭
  → 시즌 비트 / 시즌 질문 / Secret Map / 클리프행어 / 멀티라인 / 서사동력
  → ★ Plant-Payoff 시리즈 맵 (6쌍 이상)
  → ★ 캐릭터 부족 진단
     ↓
STEP 2.5: 시리즈 확장 (Sonnet) ← 3회 클릭 ★v1.7 신규★
  2.5a 캐릭터 확장 → 부족한 인물 생성 (간이 바이블 + 기능적 조연)
  2.5b 사건 보강 → 빈 구간 분석 + 에스컬레이션 구체화
  2.5c 핵심 요소 + Plant-Payoff 맵 추출 → 매 비트 강제 주입
     ↓
STEP 3: 에피소드별 씬 플랜 (Sonnet) ← 에피소드당 1회 클릭
  → 콜드 오프닝 + 8비트 + 클리프행어 + [A]/[B]/[C]/[BR]/[CUT] 씬 타입
  → ★ 비트 구조 변주 6유형 배정
  → ★ Plant-Payoff 배치
  → ★ 기능적 조연 배치
     ↓
STEP 4: 비트별 집필 (Opus) ← 에피소드당 8비트 = 8회 클릭
  → SCOPE MANDATE + 5단계 서술 구조 + 빌런 추적 + LOCKED 검증
  → ★ Genre Drive 5-point Check
  → ★ AI Escape A1~A10 자가 점검
  → ★ 비트 구조 변주 연속 방지
  → ★ 프로듀서 노트 주입
  → ★ 컨텍스트 오버플로 대응 (에피소드 요약 캐시)
  + 마지막 비트 다시 쓰기 (Opus)
     ↓
STEP 5: 다운로드
  → 에피소드별 TXT/DOCX + 시즌 전체 TXT/DOCX
```

**총 클릭 수 (8부작 기준):** 시즌 아크 1 + 시리즈 확장 3 + 씬 플랜 8 + 집필 64 = **76회**

## v1.7 업그레이드 상세 (18개 기능)

### prompt.py 신규 기능 (12개)

| # | 기능 | 설명 |
|---|------|------|
| 1 | **Planting & Payoff 시리즈 맵** | 시즌 전체 6쌍 이상. 캐릭터/관계/세계관 각 2개. EP1~2 심기, EP5~8 회수 |
| 2 | **AI Escape A1~A10** | 감정설명지문, 같은말투, 본것반복, 무대연출, 편의적정보, 침묵부재, 대사대칭, 처음시작, 같은씬해소, 총칭감각 |
| 3 | **Genre Drive 5-point Check** | 정보비대칭, 에스컬레이션, 적대자승패, 타이머, 장르쾌감 |
| 4 | **비트 구조 변주 6유형** | INV/CON/REV/EMO/ACT/SIL — 2막 반복 패턴 방지 |
| 5 | **Action Idea 검증** | 매 비트가 핵심 행동을 향해 전진하는지 체크 |
| 6 | **Genre Rule Pack 9장르×12필드** | 미스터리 추가, must_have/hook_rule/punch_rule/setpiece 필드 |
| 7 | **Villain 4 Questions** | 흥미/다크미러/계획파괴/승률 — Creator Engine v1.9 통합 |
| 8 | **기능적 조연 규칙** | 정보전달자, 관점제공자, 대가체감자, 이완감초 |
| 9 | **em dash / 볼드 금지** | 시나리오 plain text 품질 |
| 10 | **대사 형식 규칙** | 같은 캐릭터 연속 대사 금지 |
| 11 | **서사동력 비트별 추적** | Goal↔Need 간극 EP별 진행 |
| 12 | **프로듀서 노트 집필모드** | 모든 비트 집필에 프로듀서 노트 자동 주입 |

### main.py 신규 기능 (6개)

| # | 기능 | 설명 |
|---|------|------|
| 13 | **STEP 2.5a 캐릭터 확장** | 시즌 아크 분석 → 부족한 인물 간이 바이블 생성 |
| 14 | **STEP 2.5b 사건 보강** | 빈 구간 분석 + B-Story 보강 + 에스컬레이션 구체화 |
| 15 | **STEP 2.5c Plant-Payoff 맵** | 핵심 요소 추출과 통합 |
| 16 | **프로듀서 노트 UI** | STEP 4에 프로듀서 노트 입력 → 전 비트 주입 |
| 17 | **컨텍스트 오버플로 대응** | 완료 에피소드 자동 요약 → 토큰 관리 |
| 18 | **비트 구조 유형 추적** | 출력에서 자동 추출 → 연속 방지 |

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
| v1.1 | Writer Engine v2.2 통합 (씬 문법, 지문, 대사, 감정 연쇄) |
| v1.2 | Creator Engine v1.4 통합 (B-Story 강화, 5단계 서술 구조) |
| v1.3 | SCOPE MANDATE, B-Story 시간축 시각화 |
| v1.4 | Creator Engine 캐릭터 구조 통합 (characters + extended_characters) |
| v1.5 | 모델 분리 (Opus=집필, Sonnet=구조) |
| v1.6 | LOCKED/OPEN 시스템, 빌런 추적, 서사동력, 리라이트 모드 |
| **v1.7** | **18개 기능 업그레이드: P&P 시리즈맵, AI Escape A1~A10, Genre Drive 5점, 비트변주 6유형, 9장르×12필드, Villain 4Q, 시리즈 확장(캐릭터·사건 생성), 프로듀서 노트 집필모드, 컨텍스트 관리** |

---

© 2026 BLUE JEANS PICTURES · Series Engine v1.7
