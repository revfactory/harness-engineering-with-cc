# Claude Code 사용 팁 정리 프로젝트

이 저장소는 Claude Code(공식 CLI)의 실전 사용 팁을 수집·정리·발행하기 위한 작업 공간입니다.

## 목적
- Claude Code의 기능(훅, 슬래시 커맨드, MCP, 서브에이전트, 스킬, 설정 등)에 대한 팁을 한국어로 정리한다.
- 팁은 `tips/` 폴더 아래에 주제별 Markdown 파일로 축적한다.
- 정리 작업은 전용 서브에이전트와 스킬이 분담한다.

## 폴더 구조
- `tips/` — 정리된 팁 문서(주제별 `.md`)
- `.claude/agents/` — 팁 작업 전용 서브에이전트
  - `tip-researcher` — 공식 문서/릴리즈노트/코드베이스에서 팁 소재 리서치
  - `tip-writer` — 리서치 결과를 사용자 친화적 한국어 팁 문서로 작성
  - `tip-curator` — 기존 `tips/` 중복·품질 점검 및 인덱스(README) 갱신
- `.claude/skills/` — 위 에이전트들이 공통으로 쓰는 스킬
  - `tip-collect` — 소스에서 팁 소재를 모으는 절차
  - `tip-format` — 팁 문서 표준 포맷/프론트매터 규약
  - `tip-publish` — `tips/`에 저장하고 인덱스 갱신하는 절차

## 작업 흐름
1. 사용자가 주제를 제시하거나 "팁 정리" 요청을 한다.
2. `tip-researcher` 에이전트가 `tip-collect` 스킬을 사용해 소재를 수집한다.
3. `tip-writer` 에이전트가 `tip-format` 스킬 규약에 맞춰 초안을 작성한다.
4. `tip-curator` 에이전트가 `tip-publish` 스킬로 `tips/`에 저장하고 `tips/README.md` 인덱스를 갱신한다.

## 원칙
- 한국어로 작성, 커밋 메시지도 한국어.
- 팁 하나 = 한 파일. 파일명은 `kebab-case.md`.
- 추측 금지, 검증 가능한 공식 소스 또는 직접 실험 결과만 수록.
- 각 팁은 "상황 → 방법 → 예시 → 주의점" 순서를 권장.
