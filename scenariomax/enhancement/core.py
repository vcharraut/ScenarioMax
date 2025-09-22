from typing import Any

from scenariomax.enhancement.traffic_lights import add_traffic_lights_to_scenario


def enhance_scenarios(unified_scenario: dict[str, Any]) -> dict[str, Any]:
    """
    Apply enhancements to a unified scenario.

    Args:
        unified_scenario: The unified scenario to enhance

    Returns:
        Enhanced unified scenario
    """
    unified_scenario = add_traffic_lights_to_scenario(unified_scenario)
    return unified_scenario
