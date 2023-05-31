"""
Author: Ramsey (Rayla) Phuc

Alias: Rayla Kurosaki

GitHub: https://github.com/rkp1503

Terminal cmd: python code_py/main.py
"""

# 3rd party libraries to install
import matplotlib, numpy

# Custom libraries
from mylib import generate
from mylib import ode

if __name__ == '__main__':
    # ------------------------------------------------------------------------
    # Mass in kilograms (kg)
    m_1: float = 1
    m_2: float = 1

    # Length of each string in meters (m)
    l_1: float = 1
    l_2: float = 1

    # Acceleration due to gravity (m/s^2)
    g: float = 9.81

    # Initial Angle relative to the y-axis in degrees
    theta_i_1: float = 45
    theta_i_2: float = 1

    # Initial angular velocity [rad/s]
    omega_i_1: float = 0
    omega_i_2: float = 0

    # Time span in seconds (s)
    t_1: float = 0
    t_2: float = 10

    # Sets of initial initial conditions
    ic_set: str = "initial-conditions-b"
    # ------------------------------------------------------------------------
    # Solving the governing system of differential equations                
    sol = ode.solve(m_1, m_2, l_1, l_2, g, theta_i_1, theta_i_2, omega_i_1, 
                    omega_i_2, t_1, t_2)

    # x and y coordiantes of bob 1
    x_1: float = sol[0]
    y_1: float = sol[1]

    # x and y coordiantes of bob 2
    x_2: float = sol[2]
    y_2: float = sol[3]

    # Time span
    ts = sol[4]

    # Angle positions relative to the y-axis
    theta_1: float = sol[5]
    theta_2: float = sol[6]

    # Angular velocities
    omega_1: float = sol[7]
    omega_2: float = sol[8]

    # Energies
    potential_energy: float = sol[9]
    kinetic_energy: float = sol[10]
    total_energy: float = sol[11]
    # ------------------------------------------------------------------------
    xs = theta_1
    ys = [theta_2]
    labels = [""]
    xaxis: str = '$\\theta_1$ in $rad$'
    yaxis: str = '$\\theta_2$ in $rad$'
    title: str = '$\\theta_2$ vs $\\theta_1$'
    filename: str = "theta_2 vs theta_1"
    generate.figure(xs, ys, labels, xaxis, yaxis, title, ic_set, filename)
    # ------------------------------------------------------------------------
    xs = omega_1
    ys = [omega_2]
    labels = [""]
    xaxis: str = '$\\omega_1$ in $rad/s$'
    yaxis: str = '$\\omega_2$ in $rad/s$'
    title: str = '$\\omega_2$ vs $\\omega_1$'
    filename: str = f"omega_2 vs omega_1"
    generate.figure(xs, ys, labels, xaxis, yaxis, title, ic_set, filename)
    # ------------------------------------------------------------------------
    xs = ts
    ys = [theta_1, theta_2]
    labels = ["$\\theta_1$", "$\\theta_2$"]
    xaxis: str = 'time in $s$'
    yaxis: str = 'Angular position in $rad$'
    title: str = '$\\theta_1$ and $\\theta_2$ vs time'
    filename: str = "Angular Positions vs Time"
    generate.figure(xs, ys, labels, xaxis, yaxis, title, ic_set, filename)
    # ------------------------------------------------------------------------
    xs = ts
    ys = [omega_1, omega_2]
    labels = ["$\\omega_1$", "$\\omega_2$"]
    xaxis: str = 'time in $s$'
    yaxis: str = 'Angular velocity in $rad/s$'
    title: str = '$\\omega_1$ and $\\omega_2$ vs time'
    filename: str = "Angular Velocities vs Time"
    generate.figure(xs, ys, labels, xaxis, yaxis, title, ic_set, filename)
    # ------------------------------------------------------------------------
    xs = ts
    ys = [potential_energy, kinetic_energy, total_energy]
    labels = ["Potential", "Kinetic", "Total"]
    xaxis: str = 'time in $s$'
    yaxis: str = "Energy in $J$"
    title: str = "Energies vs time"
    filename: str = "Energies vs Time"
    generate.figure(xs, ys, labels, xaxis, yaxis, title, ic_set, filename)
    # ------------------------------------------------------------------------
    initial_conditions = (m_1, m_2, l_1, l_2, theta_i_1, theta_i_2, omega_i_1, 
                        omega_i_2)
    title: str = f"Double Pendulum Simulation\nRayla Kurosaki"
    filename: str = "Double Pendulum Simulation"
    # generate.animation(initial_conditions, sol, title, ic_set, filename)
    pass
