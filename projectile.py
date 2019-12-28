# program developed to plot the trajectory of a particle by Fasil Tesema
# Longyearbyen, Norway, Jan. 29 2019
from math import sin, cos, pi
import numpy as np
import matplotlib.pyplot as plt


def projectile_angle(v0, g, theta):
    """Projectile motion used to calculate the projectile trajectory of a
    particle given initial velocity v0 gravity g and angle theta in radians"""
    theta = pi * theta / 180.  # theta in radians
    t = 2 * v0 * sin(theta) / g
    td = np.linspace(0, t, 50)
    x = v0 * td * cos(theta)
    y = v0 * sin(theta) * td - 0.5 * g * td ** 2
    # h = v0**2*(sin(theta))**2/g
    return x, y


def projectile_angles(v0, g, theta):
    """
    this is a projectile
    """
    try:
        for i in theta:
            x, y = projectile_angle(v0, g, i)
            plt.plot(x, y)
            plt.text(np.max(x) / 2, np.max(y), str(i) + '$^0$')
        axes = plt.gca()
        _, ymax = axes.get_ylim()
        _, xmax = axes.get_xlim()
        plt.xlim(0, xmax)
        plt.ylim(0, ymax)
        plt.xlabel('Range (m)')
        plt.ylabel('Height (m)')
        plt.title(
            'Projectile motion at a given initial velocity of '+str(v0)+' m/s' + ' on Earth')
        # plt.show()
        plt.savefig('projectile.eps', dpi=100, bbox_inches='tight')
    except TypeError:
        print("You have only one projectile angle use 'projectile_angle' instead")


def graphics_projectile(x, y):
    plt.figure(2)
    plt.plot(x, y)
    plt.xlabel('Horizontal distance')
    plt.ylabel('Vertical distance')
    plt.xlim(0, np.max(x))
    axes = plt.gca()
    _, ymax = axes.get_ylim()
    _, xmax = axes.get_xlim()
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.show()


#x2,y2=projectile_angle(20, 10, 30)
#graphics_projectile(x2, y2)
# plt.show()
projectile_angles(10, 10, [15, 30, 45, 60, 75])
#x, y = projectile_angle(40, 10, 25)
#graphics_projectile(x, y)
#plt.savefig('projectile.eps', dpi=100, bbox_inches='tight')
