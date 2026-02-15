import unittest
from random import Random

from fractured_light.content import default_system_state, default_world_state
from fractured_light.mechanics import apply_grounding, attempt_switch, choose_mission_approach


class MechanicsTests(unittest.TestCase):
    def test_grounding_reduces_stress(self):
        system = default_system_state()
        baseline_stress = system.stress

        apply_grounding(system, "safehouse")

        self.assertLess(system.stress, baseline_stress)
        self.assertGreaterEqual(system.regulation, 65)

    def test_switch_success_when_state_stable(self):
        system = default_system_state()
        system.stress = 20
        system.regulation = 80

        result = attempt_switch(system, "Jun", rng=Random(0))

        self.assertTrue(result.switched)
        self.assertEqual(system.fronting, "Jun")
        self.assertTrue(system.continuity_notes)

    def test_objective_alignment_improves_outcomes(self):
        system = default_system_state()
        world = default_world_state()

        # Ari lacks hacking specialty.
        miss = choose_mission_approach(system, world, "Vesper Heights", "infiltrate_archive")

        self.assertFalse(miss.success)

        system.stress = 20
        system.regulation = 85
        switched = attempt_switch(system, "Jun", rng=Random(1))
        self.assertTrue(switched.switched)

        hit = choose_mission_approach(system, world, "Vesper Heights", "infiltrate_archive")
        self.assertTrue(hit.success)


if __name__ == "__main__":
    unittest.main()
