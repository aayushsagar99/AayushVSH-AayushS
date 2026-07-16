import unittest
from decimal import Decimal
from Simulators import ProjectileSimulator

class TestProjectileSimulator(unittest.TestCase):

    def test_straight_up_launch(self):
        """Tests that a projectile launched straight up has 0 horizontal movement."""
        # 10 m/s velocity, 90 degrees (straight up)
        sim = ProjectileSimulator(velocity=10, angle_degrees=90)
        
        flight_time = sim.total_flight_time()
        # Halfway through flight time should be peak height
        mid_x, mid_y = sim.calculate_position(float(flight_time / 2))
        
        self.assertEqual(mid_x, Decimal('0.0000')) # No forward movement
        self.assertGreater(mid_y, Decimal('0.0000')) # It went up

    def test_ground_level_stay(self):
        """Tests that a projectile launched at 0 degrees instantly hits the ground."""
        sim = ProjectileSimulator(velocity=15, angle_degrees=0)
        self.assertEqual(sim.total_flight_time(), Decimal('0.0000'))

if __name__ == '__main__':
    unittest.main()
