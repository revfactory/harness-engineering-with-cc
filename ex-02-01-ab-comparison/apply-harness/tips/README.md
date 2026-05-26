# Claude Code 사용 팁 인덱스

마지막 갱신: 2026-04-09

> 이 폴더는 `tip-researcher` → `tip-writer` → `tip-curator` 에이전트 파이프라인으로 채워집니다.
> 포맷은 `.claude/skills/tip-format/SKILL.md`를 참고하세요.

## 훅 (Hooks)

- [PostToolUse 훅으로 파일 저장 시 자동 린트 실행](posttooluse-auto-lint.md) — 파일 수정 툴 실행 후 자동으로 린터를 호출하는 PostToolUse 훅 설정법
- [PreToolUse 훅으로 위험한 Bash 명령 차단](pretooluse-block-dangerous-bash.md) — `rm -rf`, `git push --force` 등 되돌릴 수 없는 명령을 PreToolUse 훅으로 선제 차단하는 방법

## 서브에이전트

- [서브에이전트 frontmatter로 모델과 툴 제한](subagent-frontmatter-model-tools.md) — 에이전트 파일의 YAML frontmatter에서 model과 tools를 지정해 비용 절감 및 권한 최소화
- [에이전트 팀(Agent Teams) 실험 기능 활성화 및 운용](agent-teams-experimental.md) — 환경 변수로 다중 에이전트 팀 기능을 켜고 병렬 작업을 분배하는 방법

## 스킬

- [스킬 disable-model-invocation으로 배포·커밋 명령 보호](skill-disable-model-invocation.md) — `disable-model-invocation: true` 플래그로 배포·커밋 스킬의 Claude 자동 호출 차단

## 설정 / 키바인딩

- [acceptEdits 모드를 기본값으로 설정](accept-edits-default-mode.md) — `permissions.defaultMode: acceptEdits`로 파일 편집은 자동 승인하고 Bash 실행만 확인받는 설정
- [settings.json에 $schema 추가로 에디터 자동완성 활성화](settings-json-schema-autocomplete.md) — JSON Schema Store의 스키마를 참조해 VS Code / Cursor에서 자동완성과 오류 강조 활성화

## 메모리 / 규칙

- [CLAUDE.md를 .claude/rules/로 분리하고 경로 스코핑 적용](claude-md-rules-scoping.md) — 주제별 규칙 파일을 paths glob으로 특정 경로에만 로드해 컨텍스트 낭비 방지

## MCP

_(비어 있음)_
