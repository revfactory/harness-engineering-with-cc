---
title: acceptEdits 모드를 기본값으로 설정
tags: [설정, 권한]
updated: 2026-04-09
source: https://code.claude.com/docs/en/permission-modes
---

# acceptEdits 모드를 기본값으로 설정

## 상황

Claude가 파일을 수정할 때마다 매번 승인 프롬프트가 뜨는 것이 불편하다. 파일 편집은 자동 승인하되 Bash 실행은 여전히 확인받고 싶다.

## 방법

`settings.json`의 `permissions.defaultMode`를 `"acceptEdits"`로 설정한다. 이 모드에서는 파일 읽기·편집 관련 툴은 자동 승인되고, Bash 실행 등 더 위험한 작업은 여전히 사용자 확인을 요구한다.

Shift+Tab 키로 세션 중에 모드를 순환 전환할 수도 있다.

## 예시

`.claude/settings.json`:

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "defaultMode": "acceptEdits"
  }
}
```

사용 가능한 `defaultMode` 값:

| 값 | 설명 |
|---|---|
| `"default"` | 모든 작업에 확인 요청 (기본값) |
| `"acceptEdits"` | 파일 편집 자동 승인, Bash는 확인 |
| `"auto"` | 모든 작업 자동 승인 (제한 조건 있음) |

세션 중 단축키 전환:

```
Shift+Tab  →  default → acceptEdits → auto → default (순환)
```

## 주의점

- `.git/` 및 `.claude/` 디렉터리는 **어떤 모드에서도 자동 승인되지 않는다**. 이 경로는 항상 명시적 확인이 필요하다.
- `"auto"` 모드는 **Team/Enterprise 플랜 + Sonnet 4.6 이상 + Anthropic API 직접 사용** 환경에서만 활성화된다. 그 외 환경에서 `"auto"`를 설정해도 동작하지 않을 수 있다.
- 프로젝트 단위로 `.claude/settings.json`에 설정하면 해당 프로젝트에만 적용되고, 글로벌 설정은 `~/.claude.json`에서 관리한다.
