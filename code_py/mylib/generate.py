"""
Author: Rayla Kurosaki

GitHub: https://github.com/rkp1503
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

COLORS = ["#000000", "#FF0000", "#0000FF", "#00FF00", "#00FFFF", "#FF00FF",
          "#FFFF00", "#7F00FF"]


def save_figure(ic_set: str, filename: str):
    path_to_project_dir: str = os.path.dirname(os.getcwd())
    path_to_figs: str = os.path.join(path_to_project_dir, "report\\figures")
    if os.path.exists(path_to_figs):
        path_to_dir: str = os.path.join(path_to_figs, ic_set)
        if not os.path.exists(path_to_dir):
            os.makedirs(path_to_dir)
            pass
        path_to_fig: str = os.path.join(path_to_dir, f"{filename}.png")
        plt.savefig(path_to_fig, bbox_inches="tight")
        pass
    pass


def save_animation(anim, ic_set: str, filename: str):
    path_to_project_dir: str = os.path.dirname(os.getcwd())
    path_to_figs: str = os.path.join(path_to_project_dir, "report\\figures")
    if os.path.exists(path_to_figs):
        path_to_dir: str = os.path.join(path_to_figs, ic_set)
        if not os.path.exists(path_to_dir):
            os.makedirs(path_to_dir)
            pass
        path_to_animation: str = os.path.join(path_to_dir, f"{filename}.gif")
        anim.save(path_to_animation, dpi=300, fps=60, writer='Pillow')
        pass
    pass


def figure(xs, ys, label, xaxis, yaxis, title, ic_set, filename):
    for i in range(0, len(ys)):
        if ys[i] is not None:
            if label[i] == "f":
                plt.plot(xs, ys[i], color=COLORS[i], label=label[i],
                         linewidth=1, markersize=1, marker="o")
                pass
            else:
                plt.plot(xs, ys[i], color=COLORS[i], label=label[i],
                         linewidth=1)
                pass
            pass
        pass
    if not label == [""]:
        plt.legend(bbox_to_anchor=(1.04, 1), loc='upper left')
        pass
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(title)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='#000000')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='#FF0000')
    save_figure(ic_set, filename)
    plt.show()
    pass


def animation(ic, sol, title, ic_set, filename):
    # Misc variables
    data_skip = 60
    offset = 0.1

    m1, m2, l1, l2, theta1_0, theta2_0, omega1_0, omega2_0 = ic
    x1, y1, x2, y2, ts, theta1, theta2, omega1, omega2, PE, KE, TE = sol

    # Initialize a figure
    fig = plt.figure(figsize=(15, 7))

    # Title for Initial Conditions
    units_str = r'$m_1=$' + str(m1) + 'kg, ' + \
                r'$m_2=$' + str(m2) + 'kg, ' + \
                r'$l_1=$' + str(l1) + 'm, ' + \
                r'$l_2=$' + str(l2) + 'm, ' + \
                r'$\theta_1=$' + str(theta1_0) + r'$^\circ$, ' + \
                r'$\theta_2=$' + str(theta2_0) + r'$^\circ$, ' + \
                r'$\omega_1=$' + str(omega1_0) + r'$^\circ s^{-1}$, ' + \
                r'$\omega_2=$' + str(omega2_0) + r'$^\circ s^{-1}$'

    # Display the Title of the figure
    plt.suptitle('Double Pendulum Simulation\n' +
                 'Rayla Kurosaki\n' +
                 str(units_str), color='#FF00FF')
    plt.suptitle(f"{title}\n{str(units_str)}", color='#FF00FF')

    # Initialize Double Pendulum Animation
    ax1 = fig.add_subplot(2, 3, 1)
    ax1.grid(True)
    s = l1 + l2
    ax1.set_xlim((-s * 1.2, s * 1.2))
    ax1.set_ylim((-s * 1.2, s * 1.2))
    ax1.set_title('Double Pendulum Animation')
    plt.subplots_adjust(top=0.86, bottom=0.07)
    x_data, y_data = [], []
    pendulum1_string, = ax1.plot(x_data, y_data, lw=1, color='black')
    pendulum2_string, = ax1.plot(x_data, y_data, lw=1, color='black')
    x_path_bob1, y_path_bob1 = [], []
    x_path_bob2, y_path_bob2 = [], []
    trace_path_bob1, = ax1.plot(x_path_bob1, y_path_bob1, lw=1, color='black')
    trace_path_bob2, = ax1.plot(x_path_bob2, y_path_bob2, lw=1, color='red')

    # Initialize Phase Plot of bobs' position
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.set_xlabel('$\\theta_1$ in $rad$')
    ax2.set_ylabel('$\\theta_2$ in $rad$')
    ax2.set_title('$\\theta_2$ vs $\\theta_1$')
    ax2.set_xlim((min(theta1) - offset, max(theta1) + offset))
    ax2.set_ylim((min(theta2) - offset, max(theta2) + offset))
    ax2.minorticks_on()
    ax2.grid(which='major', linestyle='-', linewidth='0.5', color='#000000')
    ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='#FF0000')
    curve2_x, curve2_y = [], []
    curve2, = ax2.plot(curve2_x, curve2_y, lw=1, color='black')

    # Initialize Phase Plot of bobs' angular velocity
    ax3 = fig.add_subplot(2, 3, 3)
    ax3.set_xlabel('$\omega_1$ in $rad/s$')
    ax3.set_ylabel('$\omega_2$ in $rad/s$')
    ax3.set_title('$\omega_2$ vs $\omega_1$')
    ax3.set_xlim((min(omega1) - offset, max(omega1) + offset))
    ax3.set_ylim((min(omega2) - offset, max(omega2) + offset))
    ax3.minorticks_on()
    ax3.grid(which='major', linestyle='-', linewidth='0.5', color='#000000')
    ax3.grid(which='minor', linestyle=':', linewidth='0.5', color='#FF0000')
    curve3_x, curve3_y = [], []
    curve3, = ax3.plot(curve3_x, curve3_y, lw=1, color='black')

    # Initialize Time Plot of bobs' position
    ax4 = fig.add_subplot(2, 3, 4)
    ax4.set_xlabel('time in $s$')
    ax4.set_ylabel('Angular position in $rad$')
    ax4.set_title('$\\theta_1$ and $\\theta_2$ vs time')
    ax4.set_xlim((ts[0] - offset, ts[-1] + offset))
    ax4.set_ylim((min(min(theta1), min(theta2)) - offset,
                  max(max(theta1), max(theta2)) + offset))
    ax4.minorticks_on()
    ax4.grid(which='major', linestyle='-', linewidth='0.5', color='#000000')
    ax4.grid(which='minor', linestyle=':', linewidth='0.5', color='#FF0000')
    curve4a_x, curve4a_y = [], []
    curve4a, = ax4.plot(curve4a_x, curve4a_y, lw=1, color='black',
                        label=r'$\theta_1$')
    curve4b_x, curve4b_y = [], []
    curve4b, = ax4.plot(curve4b_x, curve4b_y, lw=1, color='red',
                        label=r'$\theta_2$')
    ax4.legend(loc='best', framealpha=0.5)

    # Initialize Time Plot of bobs' angular velocity
    ax5 = fig.add_subplot(2, 3, 5)
    ax5.set_xlabel('time in $s$')
    ax5.set_ylabel('Angular velocity in $rad/s$')
    ax5.set_title('$\omega_2$ and $\omega_1$ vs time')
    ax5.set_xlim((ts[0] - offset, ts[-1] + offset))
    ax5.set_ylim((min(min(omega1), min(omega2)) - offset,
                  max(max(omega1), max(omega2)) + offset))
    ax5.minorticks_on()
    ax5.grid(which='major', linestyle='-', linewidth='0.5', color='#000000')
    ax5.grid(which='minor', linestyle=':', linewidth='0.5', color='#FF0000')
    curve5a_x, curve5a_y = [], []
    curve5a, = ax5.plot(curve5a_x, curve5a_y, lw=1, color='black',
                        label=r'$\omega_1$')
    curve5b_x, curve5b_y = [], []
    curve5b, = ax5.plot(curve5b_x, curve5b_y, lw=1, color='red',
                        label=r'$\omega_2$')
    ax5.legend(loc='best', framealpha=0.5)

    # Initialize Time Plot of Energies
    ax6 = fig.add_subplot(2, 3, 6)
    ax6.set_xlabel('time in $s$')
    ax6.set_ylabel('Energy in $J$')
    ax6.set_title('Energies vs time')
    ax6.set_xlim((ts[0] - offset, ts[-1] + offset))
    ax6.set_ylim((min(min(PE), min(KE), min(TE)) - offset,
                  max(max(PE), max(KE), max(TE)) + offset))
    ax6.minorticks_on()
    ax6.grid(which='major', linestyle='-', linewidth='0.5', color='#000000')
    ax6.grid(which='minor', linestyle=':', linewidth='0.5', color='#FF0000')
    curve6a_x, curve6a_y = [], []
    curve6a, = ax6.plot(curve6a_x, curve6a_y, lw=1, color='black',
                        label='Potential')
    curve6b_x, curve6b_y = [], []
    curve6b, = ax6.plot(curve6b_x, curve6b_y, lw=1, color='red',
                        label='Kinetic')
    curve6c_x, curve6c_y = [], []
    curve6c, = ax6.plot(curve6c_x, curve6c_y, lw=1, color='blue',
                        label='Total')
    ax6.legend(loc='best', framealpha=0.5)

    def initialize():
        # Initialize Double Pendulum Animation
        pendulum1_string.set_data(x_data, y_data)
        pendulum2_string.set_data(x_data, y_data)
        # trace_bob1 = ax1.scatter(x_data, y_data, marker='o', color='blue')
        # trace_bob2 = ax1.scatter(x_data, y_data, marker='o', color='red')
        trace_path_bob2.set_data(x_path_bob2, y_path_bob2)
        bob1 = ax1.scatter((max(x1) + max(x2)), 0, marker='o', color='black')
        bob2 = ax1.scatter((max(x1) + max(x2)), -0.5, marker='o', color='red')
        bob1_text = ax1.annotate(r'$= m_1$',
                                 xy=((max(x1) + max(x2)) + 0.1, -0.04))
        bob2_text = ax1.annotate(r'$= m_2$',
                                 xy=((max(x1) + max(x2)) + 0.1, -0.55))

        # Initialize Phase Plot of bobs' position
        curve2.set_data(curve2_x, curve2_y)
        # curve2_marker = ax2.scatter(curve2_x, curve2_y, color='black')

        # Initialize Phase Plot of bobs' angular velocity
        curve3.set_data(curve3_x, curve3_y)
        # curve3_marker = ax3.scatter(curve3_x, curve3_y, color='black')

        # Initialize Time Plot of bobs' position
        curve4a.set_data(curve4a_x, curve4a_y)
        # curve4a_marker = ax4.scatter(curve4a_x, curve4a_y, color='black')

        curve4b.set_data(curve4b_x, curve4b_y)
        # curve4b_marker = ax4.scatter(curve4b_x, curve4b_y, color='red')

        # Initialize Time Plot of bobs' angular velocity
        curve5a.set_data(curve5a_x, curve5a_y)
        # curve5a_marker = ax5.scatter(curve5a_x, curve5a_y, color='black')

        curve5b.set_data(curve5b_x, curve5b_y)
        # curve5b_marker = ax5.scatter(curve5b_x, curve5b_y, color='red')

        # Initialize Time Plot of Energies
        curve6a.set_data(curve6a_x, curve6a_y)
        # curve6a_marker = ax6.scatter(curve6a_x, curve6a_y, color='black')

        curve6b.set_data(curve6b_x, curve6b_y)
        # curve6b_marker = ax6.scatter(curve6b_x, curve6b_y, color='red')

        curve6c.set_data(curve6c_x, curve6c_y)
        # curve6c_marker = ax6.scatter(curve6c_x, curve6c_y, color='blue')

        return [bob1, bob2, bob1_text, bob2_text,
                pendulum1_string, pendulum2_string,
                # trace_bob1, trace_bob2,
                trace_path_bob1, trace_path_bob2,
                curve2, 
                # curve2_marker,
                curve3, 
                # curve3_marker,
                curve4a, curve4b,
                # curve4a_marker, # curve4b_marker,
                curve5a, curve5b,
                # curve5a_marker,  # curve5b_marker,
                curve6a, curve6b, curve6c,
                # curve6a_marker,  # curve6b_marker,  # curve6c_marker,
                ]

    def update(i):
        # Updating Double Pendulum Animation
        bob1 = ax1.scatter((max(x1) + max(x2)), 0, color='black')
        bob2 = ax1.scatter((max(x1) + max(x2)), -0.5, color='red')
        bob1_text = ax1.annotate(r'$= m_1$',
                                 xy=((max(x1) + max(x2)) + 0.1, -0.04))
        bob2_text = ax1.annotate(r'$= m_2$',
                                 xy=((max(x1) + max(x2)) + 0.1, -0.55))
        pendulum1_string.set_data([0, x1[i]], [0, y1[i]])
        pendulum2_string.set_data([x1[i], x2[i]], [y1[i], y2[i]])
        # trace_bob1 = ax1.scatter(x1[i], y1[i], color='black')
        # trace_bob2 = ax1.scatter(x2[i], y2[i], color='red')
        x_path_bob1.append(x1[i])
        y_path_bob1.append(y1[i])
        x_path_bob2.append(x2[i])
        y_path_bob2.append(y2[i])
        trace_path_bob1.set_data(x_path_bob1, y_path_bob1)
        trace_path_bob2.set_data(x_path_bob2, y_path_bob2)

        # Updating Phase Plot of bobs' position
        curve2_x.append(theta1[i])
        curve2_y.append(theta2[i])
        curve2.set_data(curve2_x, curve2_y)
        # curve2_marker = ax2.scatter(curve2_x[-1], curve2_y[-1], color='black')

        # Updating Phase Plot of bobs' angular velocity
        curve3_x.append(omega1[i])
        curve3_y.append(omega2[i])
        curve3.set_data(curve3_x, curve3_y)
        # curve3_marker = ax3.scatter(curve3_x[-1], curve3_y[-1], color='black')

        # Updating Time Plot of bobs' position
        curve4a_x.append(ts[i])
        curve4a_y.append(theta1[i])
        curve4a.set_data(curve4a_x, curve4a_y)
        # curve4a_marker = ax4.scatter(curve4a_x[-1], curve4a_y[-1], color='black')

        curve4b_x.append(ts[i])
        curve4b_y.append(theta2[i])
        curve4b.set_data(curve4b_x, curve4b_y)
        # curve4b_marker = ax4.scatter(curve4b_x[-1], curve4b_y[-1], color='red')

        # Updating Time Plot of bobs' angular velocity
        curve5a_x.append(ts[i])
        curve5a_y.append(omega1[i])
        curve5a.set_data(curve5a_x, curve5a_y)
        # curve5a_marker = ax5.scatter(curve5a_x[-1], curve5a_y[-1], color='black')

        curve5b_x.append(ts[i])
        curve5b_y.append(omega2[i])
        curve5b.set_data(curve5b_x, curve5b_y)
        # curve5b_marker = ax5.scatter(curve5b_x[-1], curve5b_y[-1], color='red')

        # Updating Time Plot of Energies
        curve6a_x.append(ts[i])
        curve6a_y.append(PE[i])
        curve6a.set_data(curve6a_x, curve6a_y)
        # curve6a_marker = ax6.scatter(curve6a_x[-1], curve6a_y[-1], color='black')

        curve6b_x.append(ts[i])
        curve6b_y.append(KE[i])
        curve6b.set_data(curve6b_x, curve6b_y)
        # curve6b_marker = ax6.scatter(curve6b_x[-1], curve6b_y[-1], color='red')

        curve6c_x.append(ts[i])
        curve6c_y.append(TE[i])
        curve6c.set_data(curve6c_x, curve6c_y)
        # curve6c_marker = ax6.scatter(curve6c_x[-1], curve6c_y[-1], color='blue')

        return [bob1, bob2, bob1_text, bob2_text,
                pendulum1_string, pendulum2_string,
                # trace_bob1, trace_bob2,
                trace_path_bob1, trace_path_bob2,
                curve2, 
                # curve2_marker,
                curve3, 
                # curve3_marker,
                curve4a, curve4b,
                # curve4a_marker, # curve4b_marker,
                curve5a, curve5b,
                # curve5a_marker,  # curve5b_marker,
                curve6a, curve6b, curve6c,
                # curve6a_marker,  # curve6b_marker,  # curve6c_marker,
                ]

    plt.tight_layout()
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(ts), data_skip),
                         init_func=initialize, interval=20, repeat=False,
                         blit=True)
    save_animation(anim, ic_set, filename)
    plt.show()
    return
