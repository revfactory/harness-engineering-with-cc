"""ex-08-15 — MAX_RETRIES 안전장치 (책 p140 의사코드 + 실행 가능 스텁).

책 의사코드 시그니처는 그대로 보존하고, 더미 generator/verifier로
성공·실패 두 시나리오를 시연한다. 표준 라이브러리만 사용한다.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

MAX_RETRIES = 3


@dataclass
class VerifyResult:
    passed: bool
    reason: str = ""


class CodeGenerator:
    """더미 생성자 — attempt가 진행될수록 품질이 올라가는 스텁."""

    def __init__(self, scenario: str) -> None:
        self.scenario = scenario  # "success" or "fail"
        self.attempt = 0

    def run(self, spec: str) -> str:
        self.attempt += 1
        # 성공 시나리오: 2회차에서 "good" 산출. 실패 시나리오: 항상 "bad".
        if self.scenario == "success" and self.attempt >= 2:
            return f"artifact_v{self.attempt}_good"
        return f"artifact_v{self.attempt}_bad"


class TestRunner:
    """더미 검증자 — 산출물 이름에 'good' 포함 여부로 PASS/FAIL."""

    def run(self, artifact: str) -> VerifyResult:
        if "good" in artifact:
            return VerifyResult(passed=True)
        return VerifyResult(passed=False, reason=f"{artifact} 검증 실패: 'good' 마커 누락")


def generate_with_retries(spec: str, generator: CodeGenerator, verifier: TestRunner) -> str:
    """책 p140 의사코드 시그니처를 그대로 보존한 안전장치 루프."""
    for attempt in range(MAX_RETRIES):
        artifact = generator.run(spec)
        result = verifier.run(artifact)
        print(f"  [attempt {attempt + 1}/{MAX_RETRIES}] artifact={artifact} passed={result.passed} reason={result.reason}")
        if result.passed:
            return artifact

    return f"escalated: {MAX_RETRIES}회 실패, 수동 개입 필요"


def main() -> int:
    scenario = sys.argv[1] if len(sys.argv) > 1 else "success"
    if scenario not in {"success", "fail"}:
        print(f"unknown scenario: {scenario}. expected 'success' or 'fail'")
        return 2

    print(f"=== scenario: {scenario} ===")
    generator = CodeGenerator(scenario)
    verifier = TestRunner()
    result = generate_with_retries("dummy spec", generator, verifier)
    print(f"result: {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
