# Claude Code 실전 사용 팁 모음

Claude Code(공식 CLI)의 실전 사용 팁 8편을 하나의 문서로 모은 버전이다. 각 팁은 "상황 → 방법 → 예시 → 주의점" 순서로 구성된다.

## 목차

1. [PostToolUse 훅으로 파일 저장 시 자동 린트 실행](#1-posttooluse-훅으로-파일-저장-시-자동-린트-실행)
2. [PreToolUse 훅으로 위험한 Bash 명령 차단](#2-pretooluse-훅으로-위험한-bash-명령-차단)
3. [settings.json에 $schema 추가로 에디터 자동완성 활성화](#3-settingsjson에-schema-추가로-에디터-자동완성-활성화)
4. [서브에이전트 frontmatter로 모델과 툴 제한](#4-서브에이전트-frontmatter로-모델과-툴-제한)
5. [스킬 disable-model-invocation으로 배포·커밋 명령 보호](#5-스킬-disable-model-invocation으로-배포커밋-명령-보호)
6. [CLAUDE.md를 .claude/rules/로 분리하고 경로 스코핑 적용](#6-claudemd를-claudrules로-분리하고-경로-스코핑-적용)
7. [acceptEdits 모드를 기본값으로 설정](#7-acceptedits-모드를-기본값으로-설정)
8. [에이전트 팀(Agent Teams) 실험 기능 활성화 및 운용](#8-에이전트-팀agent-teams-실험-기능-활성화-및-운용)

---

## 1. PostToolUse 훅으로 파일 저장 시 자동 린트 실행

**태그**: 훅, 자동화 · **출처**: https://code.claude.com/docs/en/hooks

### 상황

Claude가 Edit/Write/MultiEdit 툴로 파일을 수정할 때마다 수동으로 린터를 돌려야 하는 번거로움이 있다. 코드 품질 체크를 자동화하고 싶다.

### 방법

1. `.claude/settings.json`의 `hooks` 항목에 `PostToolUse` 훅을 추가한다.
2. `matcher`를 `"Write|Edit|MultiEdit"`으로 설정해 파일 수정 툴만 걸러낸다.
3. stdin으로 전달되는 JSON에서 `tool_input.file_path`를 읽어 해당 파일에만 린터를 실행하는 스크립트를 작성한다.

### 예시

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

### 주의점

- `PostToolUse` 훅은 툴 실행을 **차단할 수 없다**. 사전 차단이 필요하면 `PreToolUse` 훅을 사용한다.
- 스크립트가 비정상 종료해도 Claude의 작업 흐름은 계속된다. 린트 오류를 Claude에게 알리려면 훅 출력을 활용하거나 별도 피드백 메커니즘을 설계해야 한다.
- `matcher`는 정규식이므로 `"Write|Edit|MultiEdit"` 외에 세밀한 패턴도 지정할 수 있다.

---

## 2. PreToolUse 훅으로 위험한 Bash 명령 차단

**태그**: 훅, 보안 · **출처**: https://code.claude.com/docs/en/hooks

### 상황

Claude가 `rm -rf` 나 `git push --force` 같은 되돌리기 어려운 명령을 자동으로 실행하는 상황을 막고 싶다. 실수로 데이터나 히스토리를 날리기 전에 선제적으로 차단해야 한다.

### 방법

1. `.claude/settings.json`의 `hooks` 항목에 `PreToolUse` 훅을 추가한다.
2. `matcher`를 `"Bash"`로 설정해 Bash 툴 호출만 가로챈다.
3. stdin JSON에서 `tool_input.command`를 파싱해 금지 패턴과 비교한다.
4. 위험 명령 감지 시 **종료코드 2**를 반환하거나 JSON으로 `permissionDecision: "deny"`를 출력해 실행을 차단한다.

### 예시

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
        result = {
            "permissionDecision": "deny",
            "reason": f"위험 명령 감지: '{pattern}' 포함. 수동으로 확인 후 실행하세요."
        }
        print(json.dumps(result))
        sys.exit(0)

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

### 주의점

- 차단 방법은 두 가지: **종료코드 2** 반환 또는 **`permissionDecision: "deny"` JSON 출력**. 둘 다 유효하다.
- 종료코드 1은 오류로 처리되어 Claude에게 에러 메시지가 전달되지만 차단은 아니다.
- 패턴이 지나치게 넓으면 정상 명령도 막힐 수 있다. 명확한 문자열 매칭을 권장한다.
- `PostToolUse`는 이미 실행된 뒤라 차단 불가 — 반드시 `PreToolUse`를 사용해야 한다.

---

## 3. settings.json에 $schema 추가로 에디터 자동완성 활성화

**태그**: 설정, 개발환경 · **출처**: https://code.claude.com/docs/en/settings

### 상황

`.claude/settings.json`을 편집할 때 키 이름을 기억하거나 공식 문서를 번갈아 봐야 한다. VS Code나 Cursor 같은 에디터에서 자동완성과 인라인 검증을 바로 쓰고 싶다.

### 방법

`settings.json` 첫 줄에 `$schema` 키를 추가한다. JSON Schema Store에 공개된 스키마를 참조하면 에디터가 즉시 자동완성과 오류 강조를 제공한다.

### 예시

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

### 주의점

- `$schema` 키는 JSON 파싱에 영향을 주지 않는다. Claude Code는 이 키를 무시하고 나머지 설정만 읽는다.
- 프로젝트 설정 파일(`.claude/settings.json`)과 글로벌 설정 파일(`~/.claude.json`)은 **별개**다. 구조가 다르므로 그대로 복붙하지 않는다.
- 네트워크가 없는 환경에서는 스키마를 로컬에 내려받아 상대 경로로 참조한다.

```json
{
  "$schema": "./.claude/claude-code-settings.schema.json"
}
```

---

## 4. 서브에이전트 frontmatter로 모델과 툴 제한

**태그**: 서브에이전트, 설정 · **출처**: https://code.claude.com/docs/en/sub-agents

### 상황

`.claude/agents/` 아래에 서브에이전트를 정의할 때, 무거운 작업엔 Sonnet, 가벼운 탐색엔 Haiku를 쓰거나, 특정 에이전트에게 위험한 툴(Bash 등)을 아예 주지 않고 싶다.

### 방법

서브에이전트 마크다운 파일의 YAML frontmatter에 `model`과 `tools` 필드를 지정한다.

- `model`: 사용할 모델 ID. 읽기 전용 탐색엔 `claude-haiku-4-5`로 비용 절감.
- `tools`: 허용 툴 배열. 생략하면 부모 에이전트 툴을 상속.
- `description`: Claude가 호출 시기를 판단하는 데 쓰이므로 구체적으로 작성.

### 예시

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

### 주의점

- **서브에이전트는 서브에이전트를 스폰할 수 없다.** 중첩 호출은 금지.
- `tools`를 생략하면 부모 컨텍스트의 툴이 전부 상속된다. 보안이 중요한 에이전트는 명시적으로 나열한다.
- 잘못된 모델 ID는 호출 시 오류가 발생한다. 공식 문서에서 확인.
- frontmatter가 없거나 불완전해도 동작하지만 기본값이 적용된다.

---

## 5. 스킬 disable-model-invocation으로 배포·커밋 명령 보호

**태그**: 스킬, 보안 · **출처**: https://code.claude.com/docs/en/skills

### 상황

`/deploy`나 `/commit` 같은 슬래시 커맨드 스킬을 정의했을 때, Claude가 자동으로 판단해서 실행하는 것을 막고 싶다. 배포나 커밋은 반드시 사람이 명시적으로 입력해야만 실행되어야 한다.

### 방법

스킬의 `SKILL.md` frontmatter에 `disable-model-invocation: true`를 추가한다. 이 플래그가 설정된 스킬은 Claude가 대화 흐름에서 자동으로 호출하지 않는다. 사용자가 직접 `/스킬명`을 입력해야만 실행된다.

### 예시

`.claude/skills/deploy/SKILL.md`:

```yaml
---
name: deploy
description: 프로덕션 환경에 빌드를 배포한다.
disable-model-invocation: true
---
```

```markdown
# deploy

## 실행 조건
이 스킬은 사용자가 `/deploy` 를 직접 입력했을 때만 실행된다.

## 절차
1. `npm run build` 로 빌드 확인
2. `git tag` 로 버전 태그 생성
3. 배포 스크립트 실행: `./scripts/deploy.sh`

## 완료 기준
배포 로그에 "Deploy successful" 문자열 확인.
```

### 주의점

- `disable-model-invocation: true`는 Claude의 **자동 호출을 막는** 것이다. 사용자가 직접 `/deploy`를 입력하면 여전히 실행된다.
- `user-invocable: false`는 **반대 개념**이다. 이 플래그를 쓰면 사용자가 슬래시 커맨드로 직접 호출할 수 없고, 다른 스킬이나 에이전트에서만 호출 가능하다. 혼동 금지.
- 두 플래그를 동시에 설정한 경우의 동작은 공식 문서에 명시되지 않았으므로 테스트 후 적용한다.

---

## 6. CLAUDE.md를 .claude/rules/로 분리하고 경로 스코핑 적용

**태그**: 메모리, 설정 · **출처**: https://code.claude.com/docs/en/memory

### 상황

`CLAUDE.md` 하나에 모든 규칙을 몰아넣으면 파일이 비대해지고, 특정 폴더에만 적용되어야 할 규칙이 항상 컨텍스트에 로드된다. 주제별로 규칙을 분리하고, 관련 파일을 편집할 때만 해당 규칙을 로드하고 싶다.

### 방법

1. `.claude/rules/` 디렉터리 아래에 주제별 `.md` 파일을 만든다.
2. 각 파일의 frontmatter에 `paths` 필드로 glob 패턴을 지정한다. 매칭되는 파일을 다룰 때만 그 규칙이 로드된다.
3. `paths`를 생략하면 항상 로드된다(전역 규칙).

### 예시

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

### 주의점

- `CLAUDE.md` 안의 HTML 주석(`<!-- ... -->`)은 컨텍스트에서 자동으로 제거된다. 숨긴 지시사항이 실제로는 전달되지 않을 수 있다.
- `.claude/rules/`는 `CLAUDE.md`를 **대체**가 아니라 **보완**한다. 프로젝트 루트의 `CLAUDE.md`는 여전히 동작한다.
- `paths` glob이 너무 넓으면 스코핑 효과가 없다. `"**/*"`는 결국 전역 로드와 같다.
- 지원 버전 범위는 공식 문서에서 확인한다.

---

## 7. acceptEdits 모드를 기본값으로 설정

**태그**: 설정, 권한 · **출처**: https://code.claude.com/docs/en/permission-modes

### 상황

Claude가 파일을 수정할 때마다 매번 승인 프롬프트가 뜨는 것이 불편하다. 파일 편집은 자동 승인하되 Bash 실행은 여전히 확인받고 싶다.

### 방법

`settings.json`의 `permissions.defaultMode`를 `"acceptEdits"`로 설정한다. 이 모드에서는 파일 읽기·편집 관련 툴은 자동 승인되고, Bash 실행 등 더 위험한 작업은 여전히 사용자 확인을 요구한다. 세션 중에는 Shift+Tab으로 모드를 순환 전환할 수 있다.

### 예시

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

### 주의점

- `.git/` 및 `.claude/` 디렉터리는 **어떤 모드에서도 자동 승인되지 않는다**. 이 경로는 항상 명시적 확인이 필요하다.
- `"auto"` 모드는 **Team/Enterprise 플랜 + Sonnet 4.6 이상 + Anthropic API 직접 사용** 환경에서만 활성화된다.
- 프로젝트 단위 설정은 `.claude/settings.json`, 글로벌 설정은 `~/.claude.json`에서 관리한다.

---

## 8. 에이전트 팀(Agent Teams) 실험 기능 활성화 및 운용

**태그**: 서브에이전트, 실험기능 · **출처**: https://code.claude.com/docs/en/agent-teams

### 상황

하나의 복잡한 작업을 여러 에이전트가 병렬로 분담해서 처리하고 싶다. 각 에이전트가 독립적인 컨텍스트를 가지면서 서로 메시지를 교환하는 팀 구조가 필요하다.

### 방법

환경 변수 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`를 `"1"`로 설정하고 Claude Code를 시작한다. 활성화되면 여러 teammate 에이전트를 생성해 작업을 분배할 수 있다. teammate는 각자 독립적인 컨텍스트 창을 가지며, 오케스트레이터(주 에이전트)와 메시지를 교환한다. 팀원 수는 3~5명이 적정하다.

### 예시

환경 변수 설정 후 실행:

```bash
# 단일 세션에 적용
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude

# 셸 프로파일에 영구 설정
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

세션 내에서 팀 생성 프롬프트 예시:

```
세 명의 teammate를 구성해줘.
- researcher: 공식 문서에서 관련 API를 조사한다
- coder: researcher 결과를 바탕으로 구현 코드를 작성한다
- reviewer: coder 결과물을 검토하고 개선점을 제안한다
```

작업 완료 후 정리:

```
팀 작업이 끝났으니 team을 clean up해줘.
```

### 주의점

- **실험적 기능**이다. 프로덕션 사용 전 충분히 검증한다.
- 세션을 **재개(resume)할 때 팀 구성이 복원되지 않는다**. 작업 완료 후 반드시 "clean up the team" 요청을 해야 리소스가 정리된다.
- teammate는 독립 컨텍스트이므로 메인 대화 내용을 자동 공유하지 않는다. 필요한 정보는 명시적으로 전달한다.
- 팀원이 너무 많으면 조율 오버헤드가 커진다. 3~5명 권장.
- 지원 플랜 및 최소 버전 요구사항은 공식 문서에서 확인한다.
