from fractured_light.models import District, Identity, SystemState, WorldState


def default_identities() -> dict[str, Identity]:
    return {
        "Ari": Identity(
            name="Ari",
            role="Investigative anchor",
            strengths={"dialogue", "journalism", "credibility"},
            stress_tolerance=70,
        ),
        "Mara": Identity(
            name="Mara",
            role="Protector and tactician",
            strengths={"combat", "escape", "threat_analysis"},
            stress_tolerance=85,
        ),
        "Jun": Identity(
            name="Jun",
            role="Systems engineer",
            strengths={"hacking", "electronics", "surveillance"},
            stress_tolerance=60,
        ),
        "Noor": Identity(
            name="Noor",
            role="Advocate and medic",
            strengths={"deescalation", "medicine", "diplomacy"},
            stress_tolerance=75,
        ),
        "Kite": Identity(
            name="Kite",
            role="Memory scout",
            strengths={"pattern_finding", "hidden_routes", "intuition"},
            stress_tolerance=45,
        ),
    }


def default_system_state() -> SystemState:
    trust = {
        "Ari": 65,
        "Mara": 55,
        "Jun": 60,
        "Noor": 70,
        "Kite": 45,
    }
    return SystemState(fronting="Ari", stress=35, regulation=65, trust_matrix=trust)


def default_world_state() -> WorldState:
    districts = {
        "Glass Harbor": District("Glass Harbor", civic_pressure=75, support_network=30),
        "Old Meridian": District("Old Meridian", civic_pressure=40, support_network=70),
        "Sprawlline": District("Sprawlline", civic_pressure=55, support_network=60),
        "Vesper Heights": District("Vesper Heights", civic_pressure=65, support_network=45),
        "Undertide": District("Undertide", civic_pressure=50, support_network=55),
    }

    rep = {
        "Mutual Aid Coalition": {"Noor": 75, "Ari": 60, "Mara": 40, "Jun": 50, "Kite": 55},
        "Independent Press": {"Ari": 80, "Jun": 65, "Noor": 60, "Mara": 45, "Kite": 35},
        "Transit Union": {"Mara": 70, "Noor": 65, "Ari": 55, "Jun": 50, "Kite": 40},
    }

    return WorldState(districts=districts, identity_reputation=rep)
