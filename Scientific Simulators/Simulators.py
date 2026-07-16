from decimal import Decimal, getcontext
import math

# Set precision high enough for physical simulation tracking
getcontext().prec = 28

class ProjectileSimulator:
    def __init__(self, velocity: float, angle_degrees: float, gravity: float = 9.81):
        # Convert inputs to Decimals for high-precision calculations
        self.v0 = Decimal(str(velocity))
        self.gravity = Decimal(str(gravity))
        
        # Math functions require standard floats, convert to Decimal after calculation
        angle_rad = math.radians(angle_degrees)
        self.vx = self.v0 * Decimal(str(math.cos(angle_rad)))
        self.vy = self.v0 * Decimal(str(math.sin(angle_rad)))

    def calculate_position(self, time: float) -> tuple:
        """Calculates the (x, y) coordinates at a given time step."""
        t = Decimal(str(time))
        
        # x = v0 * cos(theta) * t
        x = self.vx * t
        
        # y = v0 * sin(theta) * t - 0.5 * g * t^2
        y = (self.vy * t) - (Decimal('0.5') * self.gravity * (t ** 2))
        
        # If the projectile hits the ground, clamp y to 0
        if y < 0:
            y = Decimal('0')
            
        return (x.quantize(Decimal('0.0001')), y.quantize(Decimal('0.0001')))

    def total_flight_time(self) -> Decimal:
        """Calculates total time in the air before hitting the ground."""
        if self.vy <= 0:
            return Decimal('0')
        # t = (2 * vy) / g
        return ((Decimal('2') * self.vy) / self.gravity).quantize(Decimal('0.0001'))
