#!/usr/bin/env python3
"""Small arithmetic helpers for forecasting workflows.

Examples
--------
Normalize provisional percentages:
    python scripts/forecast_math.py normalize 45 32 8 7 2 6

Expected value from bucket probabilities and midpoints:
    python scripts/forecast_math.py ev --probs 5,18,36,28,10,3 --midpoints 337.5,362.5,387.5,412.5,437.5,462.5

Historical growth summary from q1:q2 pairs, optionally applied to a new base:
    python scripts/forecast_math.py growth --pairs 184800:201250 310048:254695 422875:466140 386810:443956 336681:384122 --apply 358023
"""

from __future__ import annotations

import argparse
import statistics as st
from typing import List, Sequence, Tuple


def fmt(value: float) -> str:
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.6f}".rstrip("0").rstrip(".")


def normalize(values: Sequence[float]) -> List[float]:
    total = sum(values)
    if total <= 0:
        raise ValueError("sum of values must be positive")
    normalized = [100.0 * v / total for v in values]
    rounded = [round(v, 2) for v in normalized]
    residual = round(100.0 - sum(rounded), 2)
    if abs(residual) > 1e-9:
        idx = max(range(len(rounded)), key=lambda i: rounded[i])
        rounded[idx] = round(rounded[idx] + residual, 2)
    return rounded


def expected_value(probs: Sequence[float], midpoints: Sequence[float]) -> float:
    if len(probs) != len(midpoints):
        raise ValueError("probs and midpoints must have the same length")
    total_prob = sum(probs)
    if total_prob <= 0:
        raise ValueError("sum of probabilities must be positive")
    normalized = [p / total_prob for p in probs]
    return sum(p * x for p, x in zip(normalized, midpoints))


def parse_float_list(text: str) -> List[float]:
    return [float(x.strip()) for x in text.split(",") if x.strip()]


def parse_pairs(items: Sequence[str]) -> List[Tuple[float, float]]:
    pairs: List[Tuple[float, float]] = []
    for item in items:
        left, right = item.split(":", 1)
        pairs.append((float(left), float(right)))
    return pairs


def growth_summary(pairs: Sequence[Tuple[float, float]]) -> dict:
    rates = [(b / a) - 1.0 for a, b in pairs]
    diffs = [b - a for a, b in pairs]
    out = {
        "count": len(pairs),
        "rates": rates,
        "diffs": diffs,
        "mean_rate": st.mean(rates),
        "median_rate": st.median(rates),
        "mean_diff": st.mean(diffs),
        "median_diff": st.median(diffs),
    }
    if len(rates) >= 3:
        sorted_rates = sorted(rates)
        trimmed = sorted_rates[1:-1]
        out["trimmed_mean_rate"] = st.mean(trimmed)
    return out


def cmd_normalize(args: argparse.Namespace) -> None:
    values = [float(x) for x in args.values]
    result = normalize(values)
    print("normalized:", ", ".join(fmt(v) for v in result))
    print("sum:", fmt(sum(result)))


def cmd_ev(args: argparse.Namespace) -> None:
    probs = parse_float_list(args.probs)
    midpoints = parse_float_list(args.midpoints)
    ev = expected_value(probs, midpoints)
    print("expected_value:", fmt(ev))


def cmd_growth(args: argparse.Namespace) -> None:
    pairs = parse_pairs(args.pairs)
    summary = growth_summary(pairs)
    print("count:", summary["count"])
    print("rates_pct:", ", ".join(fmt(100 * r) for r in summary["rates"]))
    print("mean_rate_pct:", fmt(100 * summary["mean_rate"]))
    print("median_rate_pct:", fmt(100 * summary["median_rate"]))
    if "trimmed_mean_rate" in summary:
        print("trimmed_mean_rate_pct:", fmt(100 * summary["trimmed_mean_rate"]))
    print("mean_diff:", fmt(summary["mean_diff"]))
    print("median_diff:", fmt(summary["median_diff"]))
    if args.apply is not None:
        base = float(args.apply)
        print("apply_mean:", fmt(base * (1.0 + summary["mean_rate"])))
        print("apply_median:", fmt(base * (1.0 + summary["median_rate"])))
        if "trimmed_mean_rate" in summary:
            print("apply_trimmed_mean:", fmt(base * (1.0 + summary["trimmed_mean_rate"])))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Arithmetic helpers for forecasting workflows")
    sub = parser.add_subparsers(dest="command", required=True)

    p_norm = sub.add_parser("normalize", help="normalize provisional percentages to 100")
    p_norm.add_argument("values", nargs="+", help="provisional percentages or weights")
    p_norm.set_defaults(func=cmd_normalize)

    p_ev = sub.add_parser("ev", help="compute expected value from probabilities and midpoints")
    p_ev.add_argument("--probs", required=True, help="comma-separated probabilities or weights")
    p_ev.add_argument("--midpoints", required=True, help="comma-separated bucket midpoints")
    p_ev.set_defaults(func=cmd_ev)

    p_growth = sub.add_parser("growth", help="summarize historical growth rates from a:b pairs")
    p_growth.add_argument("--pairs", nargs="+", required=True, help="space-separated a:b pairs")
    p_growth.add_argument("--apply", help="optional base to apply rates to")
    p_growth.set_defaults(func=cmd_growth)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
