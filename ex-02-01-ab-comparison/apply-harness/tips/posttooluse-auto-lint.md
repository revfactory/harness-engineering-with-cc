---
title: PostToolUse 훅으로 파일 저장 시 자동 린트 실행
tags: [훅, 자동화]
updated: 2026-04-09
source: https://code.claude.com/docs/en/hooks
---

# PostToolUse 훅으로 파일 저장 시 자동 린트 실행

## 상황

Claude가 Edit/Write/MultiEdit 툴로 파일을 수정할 때마다 수동으로 린터를 돌려야 하는 번거로움이 있다. 코드 품질 체크를 자동화하고 싶다.

## 방법

1. `.claude/settings.json`의 `hooks` 항목에 `PostToolUse` 훅을 추가한다.
2. `matcher`를 `"Write|Edit|MultiEdit"`으로 설정해 파일 수정 툴만 걸러낸다.
3. stdin으로 전달되는 JSON에서 `tool_input.file_path`를 읽어 해당 파일에만 린터를 실행하는 스크립트를 작성한다.

## 예시

`.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/scripts/lint-on-save.sh"
          }
        ]
      }
    ]
  }
}
```

`.claude/scripts/lint-on-save.sh`:

```bash
#!/usr/bin/env bash
# stdin에서 tool_input.file_path 추출
FILE_PATH=$(cat - | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))")

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# 확장자에 따라 린터 선택
case "$FILE_PATH" in
  *.py) python3 -m ruff check "$FILE_PATH" ;;
  *.ts|*.tsx|*.js|*.jsx) npx eslint "$FILE_PATH" ;;
  *.go) golint "$FILE_PATH" ;;
esac
```

## 주의점

- `PostToolUse` 훅은 툴 실행을 **차단할 수 없다**. 사전 차단이 필요하면 `PreToolUse` 훅을 사용한다.
- 스크립트가 비정상 종료해도 Claude의 작업 흐름은 계속된다. 린트 오류를 Claude에게 알리려면 훅 출력을 활용하거나 별도 피드백 메커니즘을 설계해야 한다.
- `matcher`는 정규식이므로 `"Write|Edit|MultiEdit"` 외에 세밀한 패턴도 지정할 수 있다.
