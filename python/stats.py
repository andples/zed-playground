"""A few statistics helpers. Try: hover `mean`, or break a type on purpose."""

from collections.abc import Sequence
import math


def mean(xs: Sequence[float]) -> float:
    if not xs:
        raise ValueError("mean of empty sequence")
    return sum(xs) / len(xs)


def stdev(xs: Sequence[float]) -> float:
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / len(xs))


if __name__ == "__main__":
    data = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    print(f"mean={mean(data)} stdev={stdev(data)}")
