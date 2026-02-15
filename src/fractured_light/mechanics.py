from __future__ import annotations

from dataclasses import dataclass
from random import Random
from typing import Optional

from fractured_light.content import default_identities
from fractured_light.models import MissionResult, SystemState, WorldState


@dataclass
class SwitchResult:
    switched: bool
    message: str


IDENTITIES = default_identities()


def attempt_switch(system: SystemState, target: str, *, rng: Optional[Random] = None) -> SwitchResult:
    if target not in IDENTITIES:
        return SwitchResult(False, f"Unknown identity: {target}")
    if target in system.consent_locks:
        return SwitchResult(False, f"{target} is unavailable without explicit consent right now.")

    if system.fronting == target:
        return SwitchResult(True, f"{target} is already fronting.")

    rng = rng or Random()
    trust = system.trust_matrix.get(target, 50)
    stress_penalty = max(0, system.stress - 40)
    regulation_bonus = max(0, system.regulation - 50)
    switch_score = trust + regulation_bonus - stress_penalty + rng.randint(-10, 10)

    if switch_score >= 50:
        previous = system.fronting
        system.fronting = target
        system.continuity_notes.append(f"Switch {previous} -> {target} succeeded at stress {system.stress}.")
        return SwitchResult(True, f"Switch succeeded. {target} is now fronting.")

    system.stress = min(100, system.stress + 8)
    return SwitchResult(False, f"Switch failed due to overload. Stress increased to {system.stress}.")


def apply_grounding(system: SystemState, technique: str) -> str:
    gains = {
        "breathing": (10, -8),
        "cold_water": (12, -10),
        "safehouse": (20, -15),
        "trusted_call": (15, -12),
    }
    regulation_gain, stress_drop = gains.get(technique, (8, -5))

    system.regulation = min(100, system.regulation + regulation_gain)
    system.stress = max(0, system.stress + stress_drop)
    return (
        f"Grounding via {technique}: regulation {system.regulation}, "
        f"stress {system.stress}."
    )


def choose_mission_approach(
    system: SystemState,
    world: WorldState,
    district_name: str,
    objective: str,
) -> MissionResult:
    district = world.districts[district_name]
    front = IDENTITIES[system.fronting]

    objective_map = {
        "infiltrate_archive": "hacking",
        "public_hearing": "dialogue",
        "rescue_source": "escape",
        "community_clinic": "medicine",
        "memory_trace": "pattern_finding",
    }

    needed = objective_map.get(objective, "dialogue")
    has_fit = needed in front.strengths

    difficulty = district.civic_pressure - (district.support_network // 2)
    skill_bonus = 25 if has_fit else 5
    regulation_bonus = max(0, (system.regulation - 50) // 2)
    stress_penalty = max(0, (system.stress - front.stress_tolerance) // 2)

    score = 50 + skill_bonus + regulation_bonus - difficulty - stress_penalty
    success = score >= 35

    if success:
        system.stress = min(100, system.stress + 6)
        narrative = (
            f"{front.name} completed {objective} in {district_name}. "
            f"Approach aligned with {front.name}'s strengths."
        )
        world.continuity_log.append(f"SUCCESS:{front.name}:{objective}:{district_name}")
        return MissionResult(True, front.name, narrative, stress_delta=6, regulation_delta=0)

    system.stress = min(100, system.stress + 12)
    system.regulation = max(0, system.regulation - 8)
    narrative = (
        f"{front.name} struggled with {objective} in {district_name}. "
        "The team needs grounding and a better-aligned fronting plan."
    )
    world.continuity_log.append(f"FAIL:{front.name}:{objective}:{district_name}")
    return MissionResult(False, front.name, narrative, stress_delta=12, regulation_delta=-8)
