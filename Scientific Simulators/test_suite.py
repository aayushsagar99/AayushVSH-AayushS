import unittest
from physics_engine import UltimateProjectileSimulator

class TestAdvancedElements(unittest.TestCase):
    
    def test_headwind_reduces_range(self):
        """Checks that firing into a severe headwind reduces total horizontal range."""
        # No wind profile
        calm_sim = UltimateProjectileSimulator(
            velocity=150, angle_degrees=45, mass=10, drag_coefficient=0.4, cross_sectional_area=0.02, wind_velocity=0
        )
        # Heavy 30 m/s (~67 mph) headwind hitting object upfront
        headwind_sim = UltimateProjectileSimulator(
            velocity=150, angle_degrees=45, mass=10, drag_coefficient=0.4, cross_sectional_area=0.02, wind_velocity=-30
        )
        
        log_calm = calm_sim.run_simulation()
        log_wind = headwind_sim.run_simulation()
        
        # Last index array value [1] contains final X coordinate data
        self.assertGreater(log_calm[-1][1], log_wind[-1][1])

if __name__ == '__main__':
    unittest.main()
