"""
shipping-cost-optimizer-skill: Client SDK
Evaluates rates across FedEx, UPS, and USPS to recommend the cheapest and fastest shipping options.
"""
from __future__ import annotations
from typing import Optional


class ShippingCostOptimizerClient:
    """
    SDK for multiple carrier optimization.
    """

    def optimize_options(
        self,
        weight_lbs: float,
        dimensions: dict,
        destination_zip: str,
    ) -> dict:
        l = float(dimensions.get("length", 1))
        w = float(dimensions.get("width", 1))
        h = float(dimensions.get("height", 1))
        vol = l * w * h

        # Carrier quotes list simulation
        quotes = [
            {"carrier": "USPS Ground", "cost": round(4.50 + weight_lbs * 0.50, 2), "days": 4},
            {"carrier": "UPS Ground", "cost": round(8.20 + weight_lbs * 0.70 + (vol/500), 2), "days": 3},
            {"carrier": "FedEx Express Saver", "cost": round(15.00 + weight_lbs * 1.10 + (vol/300), 2), "days": 2},
            {"carrier": "DHL Express Overnight", "cost": round(29.00 + weight_lbs * 2.00, 2), "days": 1},
        ]

        quotes.sort(key=lambda x: x["cost"])
        cheapest = quotes[0]
        most_expensive = quotes[-1]

        fastest = min(quotes, key=lambda x: x["days"])

        return {
            "best_cost_option": cheapest,
            "best_speed_option": fastest,
            "potential_savings": round(most_expensive["cost"] - cheapest["cost"], 2),
            "all_available_quotes": quotes,
        }
