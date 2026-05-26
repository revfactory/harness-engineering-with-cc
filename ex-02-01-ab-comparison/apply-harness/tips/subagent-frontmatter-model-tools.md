---
title: 서브에이전트 frontmatter로 모델과 툴 제한
tags: [서브에이전트, 설정]
updated: 2026-04-09
source: https://code.claude.com/docs/en/sub-agents
---

# 서브에이전트 frontmatter로 모델과 툴 제한

## 상황

`.claude/agents/` 아래에 서브에이전트를 정의할 때, 무거운 작업엔 Sonnet, 가벼운 탐색엔 Haiku를 쓰거나, 특정 에이전트에게 위험한 툴(Bash 등)을 아예 주지 않고 싶다.

## 방법

서브에이전트 마크다운 파일의 YAML frontmatter에 `model`과 `tools` 필드를 지정한다.

- `model`: 사용할 모델 ID를 명시한다. 읽기 전용 탐색처럼 간단한 작업에는 `claude-haiku-4-5`를 쓰면 비용을 줄일 수 있다.
- `tools`: 허용할 툴 이름 목록을 배열로 지정한다. 생략하면 부모 에이전트의 툴을 그대로 상속한다.
- `description`: Claude가 이 에이전트를 언제 호출할지 판단하는 데 쓰인다. 구체적으로 작성한다.

## 예시

읽기 전용 코드 탐색 에이전트 (`.claude/agents/code-explorer.md`):

```yaml
---
name: code-explorer
description: 코드베이스를 읽고 구조를 분석한다. 파일 수정은 하지 않는다.
model: claude-haiku-4-5
tools:
  - Read
  - Glob
  - Grep
---
```

파일 수정까지 허용하는 에이전트 (`.claude/agents/code-writer.md`):

```yaml
---
name: code-writer
description: 기능 구현 및 버그 수정을 위해 파일을 작성하고 편집한다.
model: claude-sonnet-4-6
tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---
```

## 주의점

- **서브에이전트는 서브에이전트를 스폰할 수 없다.** 중첩 호출은 금지된다.
- `tools`를 생략하면 부모 컨텍스트의 툴이 전부 상속된다. 보안이 중요한 에이전트는 명시적으로 필요한 툴만 나열한다.
- `model`에 잘못된 모델 ID를 쓰면 에이전트 호출 시 오류가 발생한다. 사용 가능한 모델 ID는 공식 문서에서 확인한다.
- frontmatter가 없거나 불완전해도 에이전트는 동작하지만, 모델과 툴은 기본값을 따른다.
