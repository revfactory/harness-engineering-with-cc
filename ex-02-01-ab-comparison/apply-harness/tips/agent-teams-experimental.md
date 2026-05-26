---
title: 에이전트 팀(Agent Teams) 실험 기능 활성화 및 운용
tags: [서브에이전트, 실험기능]
updated: 2026-04-09
source: https://code.claude.com/docs/en/agent-teams
---

# 에이전트 팀(Agent Teams) 실험 기능 활성화 및 운용

## 상황

하나의 복잡한 작업을 여러 에이전트가 병렬로 분담해서 처리하고 싶다. 각 에이전트가 독립적인 컨텍스트를 가지면서 서로 메시지를 교환하는 팀 구조가 필요하다.

## 방법

환경 변수 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`를 `"1"`로 설정하고 Claude Code를 시작한다. 활성화되면 여러 teammate 에이전트를 생성해 작업을 분배할 수 있다.

teammate는 각자 독립적인 컨텍스트 창을 가지며, 오케스트레이터(주 에이전트)와 메시지를 교환하며 작업한다. 팀원 수는 3~5명이 적정하다.

## 예시

환경 변수 설정 후 실행:

```bash
# 단일 세션에 적용
CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 claude

# 셸 프로파일에 영구 설정
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

세션 내에서 팀 생성 예시 (프롬프트):

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

## 주의점

- **실험적 기능**이다. 프로덕션 환경에서 사용하기 전에 충분히 검증한다.
- 세션을 **재개(resume)할 때 팀 구성이 복원되지 않는다**. 팀 작업 완료 후 반드시 "clean up the team" 요청을 해야 리소스가 정리된다.
- teammate는 독립 컨텍스트를 사용하므로 메인 컨텍스트의 대화 내용을 자동으로 공유하지 않는다. 필요한 정보는 명시적으로 전달해야 한다.
- 팀원이 너무 많으면 조율 오버헤드가 커진다. 3~5명을 권장하며, 역할을 명확하게 분리할 수 있는 경우에만 팀을 구성한다.
- 확인 필요: 지원 플랜 및 최소 버전 요구사항은 공식 문서에서 확인한다.
