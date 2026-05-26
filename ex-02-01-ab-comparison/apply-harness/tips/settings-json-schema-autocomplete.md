---
title: settings.json에 $schema 추가로 에디터 자동완성 활성화
tags: [설정, 개발환경]
updated: 2026-04-09
source: https://code.claude.com/docs/en/settings
---

# settings.json에 $schema 추가로 에디터 자동완성 활성화

## 상황

`.claude/settings.json`을 편집할 때 키 이름을 기억하거나 공식 문서를 번갈아 봐야 한다. VS Code나 Cursor 같은 에디터에서 자동완성과 인라인 검증을 바로 쓰고 싶다.

## 방법

`settings.json` 첫 줄에 `$schema` 키를 추가한다. JSON Schema Store에 공개된 스키마를 참조하면 에디터가 즉시 자동완성과 오류 강조를 제공한다.

## 예시

`.claude/settings.json`:

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "defaultMode": "acceptEdits"
  },
  "hooks": {
    "PostToolUse": []
  }
}
```

스키마를 추가하면 VS Code / Cursor에서:
- 키 이름 입력 시 자동완성 목록 표시
- 잘못된 값 타입에 빨간 밑줄 표시
- 마우스 오버 시 각 키 설명 툴팁 제공

## 주의점

- `$schema` 키는 JSON 파싱에 영향을 주지 않는다. Claude Code는 이 키를 무시하고 나머지 설정만 읽는다.
- 프로젝트 설정 파일(`.claude/settings.json`)과 글로벌 설정 파일(`~/.claude.json`)은 **별개**다. `~/.claude.json`에는 다른 스키마 또는 키 구조가 적용될 수 있으므로 동일 스키마를 그대로 복붙하지 않는다.
- 네트워크가 없는 환경에서는 스키마를 로컬에 내려받아 상대 경로로 참조한다.

```json
{
  "$schema": "./.claude/claude-code-settings.schema.json"
}
```
