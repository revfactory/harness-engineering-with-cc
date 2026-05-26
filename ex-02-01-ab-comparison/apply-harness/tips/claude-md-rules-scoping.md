---
title: CLAUDE.md를 .claude/rules/로 분리하고 경로 스코핑 적용
tags: [메모리, 설정]
updated: 2026-04-09
source: https://code.claude.com/docs/en/memory
---

# CLAUDE.md를 .claude/rules/로 분리하고 경로 스코핑 적용

## 상황

`CLAUDE.md` 하나에 모든 규칙을 몰아넣으면 파일이 비대해지고, 특정 폴더에만 적용되어야 할 규칙이 항상 컨텍스트에 로드된다. 주제별로 규칙을 분리하고, 관련 파일을 편집할 때만 해당 규칙을 로드하고 싶다.

## 방법

1. `.claude/rules/` 디렉터리 아래에 주제별 `.md` 파일을 만든다.
2. 각 파일의 frontmatter에 `paths` 필드로 glob 패턴을 지정한다. 해당 패턴에 매칭되는 파일을 다룰 때만 그 규칙이 로드된다.
3. `paths`를 생략하면 항상 로드된다(전역 규칙으로 동작).

## 예시

디렉터리 구조:

```
.claude/
  rules/
    python-style.md       # Python 파일 편집 시만 로드
    api-contracts.md      # API 디렉터리 작업 시만 로드
    global-safety.md      # paths 없음 → 항상 로드
```

`.claude/rules/python-style.md`:

```yaml
---
paths:
  - "**/*.py"
---
```

```markdown
# Python 스타일 규칙

- 타입 힌트를 항상 추가한다.
- 함수 docstring은 Google 스타일을 따른다.
- `black` 포매터 기준 라인 길이 88자.
```

`.claude/rules/api-contracts.md`:

```yaml
---
paths:
  - "src/api/**"
  - "tests/api/**"
---
```

```markdown
# API 계약 규칙

- 응답 스키마는 변경하지 않는다.
- 새 엔드포인트는 반드시 OpenAPI 스펙을 먼저 작성한다.
```

`.claude/rules/global-safety.md` (paths 없음 — 항상 로드):

```markdown
# 전역 안전 규칙

- 시크릿 키, 비밀번호를 코드에 하드코딩하지 않는다.
- `node_modules/`, `.env` 파일은 수정하지 않는다.
```

## 주의점

- `CLAUDE.md` 안의 HTML 주석(`<!-- ... -->`)은 컨텍스트에서 자동으로 제거된다. 숨겨둔 지시사항이 실제로는 Claude에게 전달되지 않을 수 있다.
- `.claude/rules/` 방식은 `CLAUDE.md`를 **대체**하는 것이 아니라 **보완**한다. 프로젝트 루트의 `CLAUDE.md`는 여전히 동작한다.
- `paths` glob이 너무 넓으면 스코핑 효과가 없다. `"**/*"` 같은 패턴은 결국 전역 로드와 같다.
- 확인 필요: `.claude/rules/` 지원 버전 범위는 공식 문서에서 확인한다.
