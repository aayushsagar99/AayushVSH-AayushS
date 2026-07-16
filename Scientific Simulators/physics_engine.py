from decimal import Decimal, getcontext
import math
import csv

getcontext().prec = 28

class UltimateProjectileSimulator:
    def __init__(self, velocity: float, angle_degrees: float, mass: float, 
                 drag_coefficient: float, cross_sectional_area: float, 
                 wind_velocity: float = 0.0, gravity: float = 9.81):
        
        self.v0 = Decimal(str(velocity))
        self.mass = Decimal(str(mass))
        self.c_d = Decimal(str(drag_coefficient))
        self.area = Decimal(str(cross_sectional_area))
        self.g = Decimal(str(gravity))
        
        # Wind velocity: positive = tailwind (pushes forward), negative = headwind
        self.v_wind = Decimal(str(wind_velocity))
        
        # Resolve initial launch vectors
        angle_rad = math.radians(angle_degrees)
        self.vx = self.v0 * Decimal(str(math.cos(angle_rad)))
        self.vy = self.v0 * Decimal(str(math.sin(angle_rad)))

    def get_air_density(self, altitude: Decimal) -> Decimal:
        """
        Approximates tropospheric air density (up to ~11km) using standard physics models:
        rho = rho0 * (1 - L*z / T0) ^ ((g * M / R * L) - 1)
        """
        # Sea level constants
        rho0 = Decimal('1.225')  # kg/m^3
        t0 = Decimal('288.15')   # Kelvin (15°C)
        l = Decimal('0.0065')    # Temperature lapse rate (K/m)
        exponent = Decimal('4.256') # (g * M) / (R * L) - 1 for Earth's troposphere
        
        if altitude <= 0:
            return rho0
        if altitude > 11000:
            return Decimal('0.3639') # Lower bound baseline cap for troposphere limit
            
        temperature_ratio = Decimal('1') - (l * altitude / t0)
        return rho0 * (temperature_ratio ** exponent)

    def run_simulation(self, time_step: float = 0.001) -> list:
        """Runs the simulation factoring in moving wind vectors and dynamic altitudes."""
        dt = Decimal(str(time_step))
        x, y, t = Decimal('0'), Decimal('0'), Decimal('0')
        
        trajectory_log = [(float(t), float(x), float(y), float(self.vx), float(self.vy))]
        vx, vy = self.vx, self.vy
        
        while y >= 0:
            # Calculate object's velocity relative to the moving wind stream
            v_rel_x = vx - self.v_wind
            v_rel_y = vy
            
            v_rel_float = math.sqrt(float(v_rel_x**2 + v_rel_y**2))
            v_rel = Decimal(str(v_rel_float))
            
            # Fetch real-time air density for current height position
            rho = self.get_air_density(y)
            drag_factor = Decimal('0.5') * rho * self.c_d * self.area
            
            if v_rel == 0:
                ax, ay = Decimal('0'), -self.g
            else:
                # Drag force calculation using relative airspeed
                f_drag = drag_factor * (v_rel ** 2)
                
                # Apply vector forces opposing relative motion
                ax = -(f_drag * (v_rel_x / v_rel)) / self.mass
                ay = -self.g - ((f_drag * (v_rel_y / v_rel)) / self.mass)
            
            # Perform numerical integration steps
            x += vx * dt
            y += vy * dt
            vx += ax * dt
            vy += ay * dt
            t += dt
            
            if y < 0:
                trajectory_log.append((float(t), float(x), 0.0, float(vx), float(vy)))
                break
                
            trajectory_log.append((float(t), float(x), float(y), float(vx), float(vy)))
            
        return trajectory_log

    @staticmethod
    def export_to_csv(data: list, filename: str = "simulation_output.csv"):
        headers = ["Time (s)", "X Position (m)", "Y Position (m)", "Velocity X (m/s)", "Velocity Y (m/s)"]
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
