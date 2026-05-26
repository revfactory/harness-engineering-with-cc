---
title: PreToolUse 훅으로 위험한 Bash 명령 차단
tags: [훅, 보안]
updated: 2026-04-09
source: https://code.claude.com/docs/en/hooks
---

# PreToolUse 훅으로 위험한 Bash 명령 차단

## 상황

Claude가 `rm -rf` 나 `git push --force` 같은 되돌리기 어려운 명령을 자동으로 실행하는 상황을 막고 싶다. 실수로 데이터나 히스토리를 날리기 전에 선제적으로 차단해야 한다.

## 방법

1. `.claude/settings.json`의 `hooks` 항목에 `PreToolUse` 훅을 추가한다.
2. `matcher`를 `"Bash"`로 설정해 Bash 툴 호출만 가로챈다.
3. stdin JSON에서 `tool_input.command`를 파싱해 금지 패턴과 비교한다.
4. 위험 명령 감지 시 **종료코드 2**를 반환하거나 JSON으로 `permissionDecision: "deny"`를 출력해 실행을 차단한다.

## 예시

`.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/scripts/block-dangerous.py"
          }
        ]
      }
    ]
  }
}
```

`.claude/scripts/block-dangerous.py`:

```python
#!/usr/bin/env python3
import sys
import json

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

BLOCKED_PATTERNS = [
    "rm -rf",
    "git push --force",
    "git push -f",
    "> /dev/sda",
    "mkfs",
]

for pattern in BLOCKED_PATTERNS:
    if pattern in command:
        # JSON 방식으로 차단 — 이유를 메시지에 포함
        result = {
            "permissionDecision": "deny",
            "reason": f"위험 명령 감지: '{pattern}' 포함. 수동으로 확인 후 실행하세요."
        }
        print(json.dumps(result))
        sys.exit(0)

# 차단 없음 — 정상 종료
sys.exit(0)
```

종료코드 2를 사용하는 단순 bash 방식:

```bash
#!/usr/bin/env bash
COMMAND=$(cat - | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))")

if echo "$COMMAND" | grep -qE '(rm -rf|git push --force|git push -f)'; then
  echo "위험 명령이 차단되었습니다: $COMMAND" >&2
  exit 2
fi
```

## 주의점

- `PreToolUse` 훅에서 차단하는 방법은 두 가지다. **종료코드 2** 반환 또는 **`permissionDecision: "deny"` JSON 출력**. 둘 다 유효하다.
- 종료코드 1은 오류로 처리되어 Claude에게 에러 메시지가 전달되지만 차단은 아니다. 차단은 반드시 코드 2 또는 JSON deny를 사용한다.
- 패턴이 지나치게 넓으면 정상 명령도 막힐 수 있다. 정규식보다 명확한 문자열 매칭을 권장한다.
- `PostToolUse`는 이미 실행된 뒤라 차단 불가 — 반드시 `PreToolUse`를 사용해야 한다.
