---
title: 스킬 disable-model-invocation으로 배포·커밋 명령 보호
tags: [스킬, 보안]
updated: 2026-04-09
source: https://code.claude.com/docs/en/skills
---

# 스킬 disable-model-invocation으로 배포·커밋 명령 보호

## 상황

`/deploy`나 `/commit` 같은 슬래시 커맨드 스킬을 정의했을 때, Claude가 자동으로 판단해서 실행하는 것을 막고 싶다. 배포나 커밋은 반드시 사람이 명시적으로 입력해야만 실행되어야 한다.

## 방법

스킬의 `SKILL.md` frontmatter에 `disable-model-invocation: true`를 추가한다. 이 플래그가 설정된 스킬은 Claude가 대화 흐름에서 자동으로 호출하지 않는다. 사용자가 직접 `/스킬명`을 입력해야만 실행된다.

## 예시

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

## 주의점

- `disable-model-invocation: true`는 Claude의 **자동 호출을 막는** 것이다. 사용자가 직접 `/deploy`를 입력하면 여전히 실행된다.
- `user-invocable: false`는 반대 개념이다. 이 플래그를 쓰면 사용자도 슬래시 커맨드로 직접 호출할 수 없고, 오직 다른 스킬이나 에이전트에서만 호출 가능하다. 두 플래그를 혼동하지 않는다.
- 확인 필요: 두 플래그를 동시에 설정한 경우의 동작은 공식 문서에서 명시적으로 설명되지 않으므로 테스트 후 적용한다.
