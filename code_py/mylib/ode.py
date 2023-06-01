"""
Author: Ramsey (Rayla) Phuc

Alias: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import numpy as np


def df(F, t, params) -> np.array:
    # Unpack variables
    theta_1: float = F[0]
    theta_2: float = F[1]
    omega_1: float = F[2]
    omega_2: float = F[3]

    # Unpack parameters
    m_1: float = params[0]
    m_2: float = params[1]
    l_1: float = params[2]
    l_2: float = params[3]
    g: float = params[4]

    # System of differential equations
    theta_1_t: float = omega_1
    theta_2_t: float = omega_2

    # Breaking down each component since the expression is too big
    A1: float = -g * (2 * m_1 + m_2) * np.sin(theta_1)
    A2: float = - m_2 * g * np.sin(theta_1 - 2 * theta_2)
    A3: float = - 2 * m_2 * np.sin(theta_1 - theta_2)
    A4: float = (omega_2 ** 2) * l_2 + (omega_1 ** 2) * l_1 * np.cos(
        theta_1 - theta_2)
    B: float = l_1 * (2 * m_1 + m_2 - m_2 * np.cos(2 * (theta_1 - theta_2)))
    omega_1_t: float = (A1 + A2 + A3 * A4) / B

    # Breaking down each component since the expression is too big
    C1: float = 2 * np.sin(theta_1 - theta_2)
    C2: float = (omega_1 ** 2) * l_1 * (m_1 + m_2)
    C3: float = g * (m_1 + m_2) * np.cos(theta_1)
    C4: float = (omega_2 ** 2) * l_2 * m_2 * np.cos(theta_1 - theta_2)
    D: float = l_2 * (2 * m_1 + m_2 - m_2 * np.cos(2 * (theta_1 - theta_2)))
    omega_2_t: float = C1 * (C2 + C3 + C4) / D
    return np.array([theta_1_t, theta_2_t, omega_1_t, omega_2_t], dtype=float)


def solve(m_1, m_2, l_1, l_2, g, theta_i_1, theta_2_i, omega_1_i, omega_2_i, 
          t_1, t_2):
    # Step size
    h: float = 0.0005

    # Initial Condition
    ic_vec: np.array = np.array([np.radians(theta_i_1), np.radians(theta_2_i),
                                 np.radians(omega_1_i), np.radians(omega_2_i)],
                                dtype=float)

    # Time span in seconds
    ts: np.arange = np.arange(t_1, t_2, h)

    # Solve the model
    params = m_1, m_2, l_1, l_2, g
    ode_sol: np.array = rk4(df, ic_vec, ts, h, params)
    theta_1: float = ode_sol[0]
    theta_2: float = ode_sol[1]
    omega_1: float = ode_sol[2]
    omega_2: float = ode_sol[3]

    # Compute bob1's coordinates and velocity in Cartesian
    x_1: float = l_1 * np.sin(theta_1)
    y_1: float = - l_1 * np.cos(theta_1)
    v_x_1: float = l_1 * omega_1 * np.cos(theta_1)
    v_y_1: float = l_1 * omega_1 * np.sin(theta_1)
    v_1: float = v_x_1 ** 2 + v_y_1 ** 2

    # Compute bob2's coordinates and velocity in Cartesian
    x_2: float = x_1 + l_2 * np.sin(theta_2)
    y_2: float = y_1 - l_2 * np.cos(theta_2)
    v_x_2: float = v_x_1 + l_2 * omega_2 * np.cos(theta_2)
    v_y_2: float = v_y_1 + l_2 * omega_2 * np.sin(theta_2)
    v_2: float = v_x_2 ** 2 + v_y_2 ** 2

    # Compute the Potential Energy
    PE: float = g * ((m_1 * y_1) + (m_2 * y_2))
    # Compute the Kinetic Energy
    KE: float = (1 / 2) * ((m_1 * v_1) + (m_2 * v_2))

    # Compute the Total Energy
    TE: float = PE + KE

    return (x_1, y_1, x_2, y_2, ts, theta_1, theta_2, omega_1, omega_2, PE, 
            KE, TE)


def rk4(df, r, ts, h, params):
    rs = [r]
    for i in range(1, len(ts)):
        f1 = df(rs[i - 1], ts[i - 1], params)
        f2 = df(rs[i - 1] + (h / 2) * f1, ts[i - 1] + (h / 2), params)
        f3 = df(rs[i - 1] + (h / 2) * f2, ts[i - 1] + (h / 2), params)
        f4 = df(rs[i - 1] + h * f3, ts[i - 1] + h, params)
        r = rs[i - 1] + (h / 6) * (f1 + 2 * f2 + 2 * f3 + f4)
        rs.append(r)
        pass
    return get_data(rs)


def get_data(data):
    rs, cs = len(data), len(data[0])
    temp = np.empty((cs, rs), dtype=float)
    for r in range(0, rs):
        for c in range(0, cs):
            temp[c][r] = data[r][c]
            pass
        pass
    if len(temp) == 1:
        return temp[0]
    return temp
