from typing import List, Optional

class Estimate:
    def __init__(self, developer: str, estimate: int) -> None:
        self._developer: str = developer
        self._estimate: int = estimate

    def getDeveloper(self) -> str:
        return self._developer

    def getEstimate(self) -> int:
        return self._estimate


class PlanningPoker:
    def identify_extremes(self, estimates: List[Estimate]) -> List[str]:
        lowest_estimate: Optional[Estimate] = None
        highest_estimate: Optional[Estimate] = None

        for estimate in estimates:
            if highest_estimate is None or \
               estimate.getEstimate() > highest_estimate.getEstimate():
                highest_estimate = estimate
            elif lowest_estimate is None or \
                 estimate.getEstimate() < lowest_estimate.getEstimate():
                lowest_estimate = estimate

        return [
            lowest_estimate.getDeveloper(),
            highest_estimate.getDeveloper()
        ]