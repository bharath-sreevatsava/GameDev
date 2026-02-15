from fractured_light.content import default_system_state, default_world_state
from fractured_light.mechanics import apply_grounding, attempt_switch, choose_mission_approach


def run_vertical_slice() -> None:
    system = default_system_state()
    world = default_world_state()

    print("=== Fractured Light :: Vertical Slice Prototype ===")
    print(f"Initial fronting: {system.fronting} | stress={system.stress} regulation={system.regulation}")

    print("\nMission 1: Infiltrate archive in Vesper Heights")
    result_1 = choose_mission_approach(system, world, "Vesper Heights", "infiltrate_archive")
    print(result_1.narrative)

    print("\nRequest switch to Jun for technical objective...")
    switch = attempt_switch(system, "Jun")
    print(switch.message)

    print("\nGrounding routine: trusted_call")
    print(apply_grounding(system, "trusted_call"))

    print("\nMission 2: Infiltrate archive in Vesper Heights")
    result_2 = choose_mission_approach(system, world, "Vesper Heights", "infiltrate_archive")
    print(result_2.narrative)

    print("\nContinuity log:")
    for entry in world.continuity_log:
        print(f"- {entry}")


if __name__ == "__main__":
    run_vertical_slice()
