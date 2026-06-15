import json
from datetime import datetime
from pathlib import Path

class ResultWriter:

    RESULTS_DIR = Path(
        "evaluation/results"
    )

    @classmethod
    def save(
        cls,
        result
    ):

        cls.RESULTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        file_path = (
            cls.RESULTS_DIR
            /
            f"{timestamp}.json"
        )

        payload = {
            "total": result.total,
            "passed": result.passed,
            "failed": result.failed,
            "accuracy": result.accuracy,
            "details": result.details
        }

        with open(
            file_path,
            "w"
        ) as f:

            json.dump(
                payload,
                f,
                indent=4
            )

        return file_path