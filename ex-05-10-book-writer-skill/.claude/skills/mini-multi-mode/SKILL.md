---
name: mini-multi-mode
description: "다중 모드 오케스트레이터 — README 작성/변경로그 생성/PR 본문 작성. 사용자가 '리드미', 'README', '체인지로그', 'changelog', 'PR 본문', 'pull request body'를 요청하면 호출. 본 sub-harness 데모용. 단순 1줄 수정은 직접 처리."
allowed-tools: Read, Write
---

# mini-multi-mode (Layer 2 — 3모드 라우터)

7모드(book-writer)는 시작하기에 부담이라, 3모드로 축소한 미니 템플릿.
본문은 라우터만, 모드별 상세는 workflows로 위임 (Progressive Disclosure).

## 라우팅
- README 작성 요청이면 → `workflows/01-readme.md`
- 변경로그(changelog) 요청이면 → `workflows/02-changelog.md`
- PR 본문 요청이면 → `workflows/03-pr-body.md`

조건이 맞는 workflow만 로드된다 — 나머지는 컨텍스트에 올라오지 않음.
