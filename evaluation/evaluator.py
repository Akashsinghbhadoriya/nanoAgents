from evaluation.evaluation_result import EvaluationResult

class Evaluator:

    def __init__(
        self,
        agent_system
    ):
        self.agent_system = agent_system

    def evaluate(self, benchmark):

        details = []
        passed = 0
        total = len(benchmark.samples)

        for sample in benchmark.samples:

            context = self.agent_system.run(
                sample["query"]
            )

            prediction = str(
                context.final_result
            ).strip()

            expected = str(
                sample["expected"]
            ).strip()

            success = prediction == expected
            if success:
                passed += 1
            details.append(
                {
                    "query": sample["query"],
                    "prediction": prediction,
                    "expected": expected,
                    "success": success
                }
            )

            
        
        accuracy = (passed / total) * 100

        return EvaluationResult(
            total=total,
            passed=passed,
            failed=total - passed,
            accuracy=accuracy,
            details=details
        )