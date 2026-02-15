from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Set


@dataclass
class Identity:
    name: str
    role: str
    strengths: Set[str]
    stress_tolerance: int
    trust_with_system: int = 50


@dataclass
class SystemState:
    fronting: str
    stress: int = 35
    regulation: int = 65
    trust_matrix: Dict[str, int] = field(default_factory=dict)
    consent_locks: Set[str] = field(default_factory=set)
    continuity_notes: List[str] = field(default_factory=list)


@dataclass
class District:
    name: str
    civic_pressure: int
    support_network: int


@dataclass
class WorldState:
    districts: Dict[str, District]
    identity_reputation: Dict[str, Dict[str, int]] = field(default_factory=dict)
    continuity_log: List[str] = field(default_factory=list)


@dataclass
class MissionResult:
    success: bool
    fronting: str
    narrative: str
    stress_delta: int
    regulation_delta: int
