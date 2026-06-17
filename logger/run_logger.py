import json
from pathlib import Path
from datetime import datetime

class RunLogger:

    LOG_DIR = Path("logs")

    @classmethod
    def save(cls, data):

        cls.LOG_DIR.mkdir(
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filepath = (
            cls.LOG_DIR
            /
            f"run_{timestamp}.json"
        )

        with open(filepath, "w") as f:

            json.dump(
                data,
                f,
                indent=2,
                default=str
            )

        return filepath