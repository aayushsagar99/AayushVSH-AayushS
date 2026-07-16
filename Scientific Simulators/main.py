import subprocess
from physics_engine import UltimateProjectileSimulator

def main():
    print("=== Step 1: Running Element Regression Tests ===")
    subprocess.run(["python", "-m", "unittest", "test_suite.py"])
    
    print("\n=== Step 2: Running Long-Range Rocket Simulation ===")
    # High-velocity launch (300 m/s) climbing high into the air, facing a 15 m/s headwind
    simulator = UltimateProjectileSimulator(
        velocity=300.0,
        angle_degrees=55.0,
        mass=25.0,
        drag_coefficient=0.25, 
        cross_sectional_area=0.03,
        wind_velocity=-15.0  # 15 m/s headwind pushing backwards
    )
    
    print("Computing vectors with wind currents and air thinning calculations...")
    trajectory_data = simulator.run_simulation(time_step=0.005)
    
    final_record = trajectory_data[-1]
    max_height = max(row[2] for row in trajectory_data)
    
    print(f"\nSimulation complete!")
    print(f"Peak Altitude Achieved: {max_height:.2f} meters")
    print(f"Total Airtime         : {final_record[0]:.3f} seconds")
    print(f"Final Impact Range    : {final_record[1]:.2f} meters")
    
    print("\n=== Step 3: Serializing Telemetry Data ===")
    output_file = "ballistics_trajectory.csv"
    simulator.export_to_csv(trajectory_data, output_file)
    print(f"Data matrices successfully exported to '{output_file}'")

if __name__ == '__main__':
    main()

