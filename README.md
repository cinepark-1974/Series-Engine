# 👖 BLUE JEANS SERIES ENGINE v2.1.0

**Netflix 미니시리즈/시리즈(시즌 1) 시나리오 집필 엔진**

> BLUE JEANS PICTURES · Series Writing Pipeline
> Creator Engine → **Series Engine** → Writer Engine / Rewrite Engine

---

## 한 줄 정의

시즌 아크 → 시리즈 확장(캐릭터·사건 보강) → 에피소드 씬 플랜 → 비트 단위 집필 구조 위에 **OPENING/MIDSEASON TWIST/LOWEST POINT/FINALE MASTERY 4종, 9장르 GENRE BOOSTER, INSERT 시스템, PROP 연속성 추적, 시즌 표현 누적 차단, 회별 사건/시즌 비중 자동 조정, 한국 시나리오 표준 양식 DOCX 빌더**를 중첩 제어하여 "매 회 끝에 다음 회를 안 볼 수 없는 시리즈 시나리오"를 쓰는 집필 엔진.

---

## 파일 구조

```
series-engine/
├── main.py              (3,583줄) — Streamlit 메인 앱 + DOCX 양식 빌더
├── prompt.py            (3,480줄) — 시리즈 작법 원칙 + 빌더 함수 + v2.0 모듈
├── profession_pack.py   (2,586줄) — 직업 디테일 자동 주입
├── period_pack.py       (1,605줄) — 시대 디테일 자동 주입
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
| 집필 모델 | claude-opus-4-6 (Opus = WRITE) |
| 구조 모델 | claude-sonnet-4-6 (Sonnet = ANALYZE) |
| API KEY | ANTHROPIC_API_KEY (Streamlit Secrets) |

## 배포

1. GitHub `cinepark-1974/series-engine` 레포 main 브랜치에 푸시
2. Streamlit Cloud 자동 재배포 (1~2분)
3. Secrets에 `ANTHROPIC_API_KEY` 설정 (한 번만)

## 파이프라인 (5단계)

```
STEP 1: 자료 입력
  Creator Engine 9칸 붙여넣기 또는 Creator JSON 업로드 자동 채우기
  + 에피소드 수(6/8) + 분량(40/50/60분) + 장르 + LOCKED/OPEN 설정 잠금
     ↓
STEP 2: 시즌 아크 설계 (Sonnet) ← 1회 클릭
  → 시즌 비트 / 시즌 질문 / Secret Map / 클리프행어 / 멀티라인 / 서사동력
  → Plant-Payoff 시리즈 맵 (6쌍 이상)
  → ★ v2.0 — 회별 마스터리 사전 인지 (EP1/EP4/EP6/EP8)
  → ★ v2.0 — 회별 사건/시즌 비중 가이드 자동 주입
     ↓
STEP 2.5: 시리즈 확장 (Sonnet) ← 3회 클릭
  2.5a 캐릭터 확장 / 2.5b 사건 보강 / 2.5c 핵심 요소 + Plant-Payoff 맵
     ↓
STEP 3: 에피소드별 씬 플랜 (Sonnet) ← 에피소드당 1회 클릭
  → Cold Opening + 8비트 + 클리프행어 + 5종 씬 타입
  → ★ v2.0 — EP 단위 씬 번호 연속 채번 강제
  → ★ v2.0 — "(연속)" 표기 금지, CUT TO / CLOSE UP / INSERT 가이드
  → ★ v2.0 — EP1/EP4/EP6/EP8 마스터리 힌트 자동 주입
     ↓
STEP 4: 비트별 집필 (Opus) ← 에피소드당 8비트 = 8회 클릭
  → SCOPE MANDATE + 5단계 서술 구조 + 빌런 추적 + LOCKED 검증
  → Genre Drive 5점 + AI Escape A1~A17 + 비트 구조 변주
  → ★ v2.0 — 같은 EP 안에서 직전 비트 마지막 씬 번호 자동 추출 → S#(N+1)부터 강제
  → ★ v2.0.8 — 새 EP의 첫 비트(Beat 0)는 S#1부터 리셋 (시즌 통산 채번 차단)
  → ★ v2.1.0 — 세계관 전문(inputs.world) 비트 주입 + 스케일 환기 강제 + 다중 빌런 EP당 현존 (글로벌 스케일 축소 차단)
  → ★ v2.1.0 — 씬 플랜: 시즌 아크 A-Story 핵심 사건 장면화 강제 + EP 구간 별도 전달 (피의 밤 같은 도입 사건 누락 차단)
  → ★ v2.0 — INSERT 시스템 + PROP 연속성 + GENRE BOOSTER + HELPER 룰 자동 주입
  → ★ v2.0 — 회별 마스터리 모듈 자동 분기 (EP1·EP4·EP6·EP8)
  → ★ v2.0 — 시즌 표현 누적 DB 자동 추출·차단 (AI Escape A17 해결)
     ↓
STEP 5: 다운로드
  → ★ v2.0 — 한국 시나리오 표준 양식 DOCX (Writer Engine 양식 정합)
  → ★ v2.0.3 — 출력 모드 토글
       · 집필 모드: 비트 헤더 포함 + 표지 페이지 (작가 검토용)
       · 최종 모드: 비트 헤더 제거 + 표지 없음 (제작·연출·투자 전달용)
  → ★ v2.0.7 — 최종 모드는 시나리오 본문 1페이지 S#1부터 바로 시작 (엔진 메타 노출 차단)
  → 시즌 표지 + EP 분리 페이지 + 씬번호/대사/지문/INSERT 자동 양식화
  → 에피소드별 TXT/DOCX + 시즌 전체 TXT/DOCX
```

## v2.0 본 작업 — 신규 기능 전체 목록

### prompt.py 신규 (10개)

| # | 기능 | 설명 |
|---|------|------|
| 1 | **INSERT_SYSTEM_MODULE** | 카톡·문자·SNS·뉴스 화면 텍스트 자동 양식화 |
| 2 | **PROP_CONTINUITY_MODULE** | 소품 연속성 추적 + 시즌 누적 추적 |
| 3 | **GENRE_BOOSTER 9장르** | 스릴러/호러/액션/로맨스/코미디/드라마/SF/판타지/미스터리 — 각 10필수장치 |
| 4 | **HELPER_CHARACTER_RULE** | 조력자 5씬 연속 등장 금지 + 4역할 검증 |
| 5 | **EPISODE_FOCUS_RATIO** | 회별 사건/시즌 비중 자동 조정 (EP1=30/70, EP4=40/60, EP6=50/50, EP8=20/80) |
| 6 | **FINALE_MASTERY_MODULE** | EP8 — EP1 수미상관 + Plant 회수 + 시즌 질문 답 강제 |
| 7 | **MIDSEASON_TWIST_MASTERY_MODULE** | EP4(8부작)/EP3(6부작) — 시즌 전제 뒤집기 + EP1~3 단서 재해석 |
| 8 | **LOWEST_POINT_MASTERY_MODULE** | EP6(8부작)/EP4(6부작) — 진짜 상실 + 빌런 시즌 최고 우위 |
| 9 | **get_opening_mastery_v2** | Writer Engine 풀버전 + EP1 분량 2500-4000자 + 빌런 15회 강제 |
| 10 | **SCENE RULES 강화** | 씬 분할 룰 4종 + 씬 번호 연속 채번 + 대사 형식 ❌/✅ 예시 3종 |

### main.py 신규 (6개)

| # | 기능 | 설명 |
|---|------|------|
| 11 | **extract_signature_expressions** | 비트 집필 결과에서 18~80자 시그니처 표현 자동 추출 |
| 12 | **update_season_expression_db** | 시즌 단위 표현 누적 DB 갱신 |
| 13 | **get_overused_expressions** | 3회 이상 누적된 표현 추출 → 다음 비트 집필 시 차단 |
| 14 | **사이드바 v2.0 누적 현황** | 시즌 표현 추적 상태 실시간 표시 |
| 15 | **DOCX 양식 빌더 (v1.9 패치본 유지)** | Writer Engine 양식 정합 — 씬번호/대사/지문/INSERT 자동 분리 |
| 16 | **백업 JSON에 season_expression_db 추가** | 세션 재개 시 표현 누적 유지 |

### v1.x 기능 유지 (v2.0에도 전부 작동)

- Planting & Payoff 시리즈 맵
- AI Escape A1~A17 자가 점검
- Genre Drive 5-point Check
- 비트 구조 변주 6유형 (INV/CON/REV/EMO/ACT/SIL)
- Genre Rule Pack 9장르 × 12필드
- Villain 4 Questions
- 기능적 조연 규칙 4역할
- 서사동력 비트별 추적
- 프로듀서 노트 집필모드
- 컨텍스트 오버플로 대응 (적응형 컨텍스트)
- 비트 간 중복 방지 (에피소드 내)
- Profession Pack (캐릭터 직업 디테일)
- Period Pack (시대 디테일)
- LOCKED/OPEN 시스템
- 리라이트 모드 (독립)
- Creator Engine JSON 자동 로더

## 디자인 시스템

Creator Engine / Writer Engine과 완전 통일:
- CSS 변수: `--navy: #191970`, `--y: #FFCB05`, `--bg: #F7F7F5`
- 폰트: Pretendard + Paperlogy + Playfair Display
- 사이드바 ENGINE INFO 박스 + v2.0 시즌 표현 누적 현황 박스
- 브랜드 헤더: `BLUE JEANS PICTURES → SERIES ENGINE → YOUNG·VINTAGE·FREE·INNOVATIVE`

## 버전 히스토리

| 버전 | 주요 변경 |
|------|----------|
| v1.0 | 초기 빌드 — 5단계 파이프라인 |
| v1.1 | Writer Engine v2.2 통합 |
| v1.2 | Creator Engine v1.4 통합 |
| v1.3 | SCOPE MANDATE, B-Story 시간축 |
| v1.4 | Creator Engine 캐릭터 구조 통합 |
| v1.5 | 모델 분리 (Opus=집필, Sonnet=구조) |
| v1.6 | LOCKED/OPEN, 빌런 추적, 서사동력, 리라이트 모드 |
| v1.7 | 18개 기능 업그레이드 — P&P 시리즈맵, AI Escape, Genre Drive, 비트변주, 9장르×12필드, Villain 4Q |
| v1.8 | Profession/Period Pack, 적응형 컨텍스트, 비트 간 중복 방지, Streamlit 안티패턴 안정화 |
| v1.9 | 한국 시나리오 표준 양식 DOCX 빌더 이식 (Writer Engine 양식 정합) |
| v2.0 | 완전한 엔진 — 회별 마스터리 4종, GENRE BOOSTER 9장르, INSERT/PROP 시스템, 시즌 표현 누적 차단, 회별 비중 자동 조정, SCENE RULES 강화 |
| v2.0.1 | [패치 E] 캐릭터+대사 분리 복구 강화 · [패치 F] DOCX/TXT 파일명 규칙 갱신 (각본_제목_v1.0_날짜_시간) |
| v2.0.2 | [패치 G] 씬 헤딩 시간 표기 5단계 표준 강제 (새벽/오전/오후/저녁/밤) |
| v2.0.3 | [패치 H] DOCX 출력 모드 토글 — 최종 모드(기본): 비트 헤더 제거 / 집필 모드: 비트 헤더 포함 |
| v2.0.4 | [패치 I] 외부 모니터링 / 쇼러너 노트 입력 (STEP 2 시즌 아크 영역 + 백업 JSON 스키마 확장) · [Hotfix 1] build_locked_block NameError 수정 |
| v2.0.5 | [패치 J] 작품 제목 입력 + 백업 파일명/사이드바/PDF 푸터 자동 주입 · [패치 K] 리라이트 모드 자동 로더 (Creator JSON + Series JSON) |
| v2.0.6 | [Hotfix 2] 백업 복원 시 monitoring_feedback / showrunner_notes 위젯 instantiate 후 직접 수정 오류 해소 (_pending_widget_sync 경로 통과) |
| v2.0.7 | [패치 L] 최종 모드 DOCX 표지 메타정보 제거 — 시나리오/EPISODE N/장르/기획·제작/엔진버전 5줄 + 끝 © 페이지 + 푸터 자동 스킵 (제작·연출·투자 전달용) |
| v2.0.8 | [패치 M] 씬 번호 회별 리셋 — 새 EP의 첫 비트(Beat 0)는 S#1부터 시작. 시즌 통산 채번 차단. build_write_episode_beat_prompt에 is_first_beat_of_episode 인자 추가 |
| **v2.1.0** | **[패치 N] 세계관/스케일 비트 주입 — build_write_episode_beat_prompt에 world_setting 인자 추가. inputs.world 전문을 [🌐 세계관] 블록으로 주입 + 스케일 환기 강제 + 다중 빌런 EP당 현존 강제 · [패치 O] 씬 플랜 A-Story 핵심 사건 장면화 강제 — build_episode_plan_prompt에 EP 구간 별도 추출 + 핵심 사건→S#번호 대응 점검. 피의 밤 같은 도입 사건이 전사로 요약 처리되어 누락되는 패턴 차단** |

---

© 2026 BLUE JEANS PICTURES · Series Engine v2.1.0
