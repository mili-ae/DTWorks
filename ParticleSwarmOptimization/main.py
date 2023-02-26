import matplotlib.pyplot as plt
from swarm import Swarm
from matplotlib.animation import FuncAnimation


def update(frame):
    xdata = swarm.xs
    ydata = swarm.ys
    
    swarm.tick()
    ln.set_data(xdata, ydata)
    
    print(swarm)
    print()
    print("Global Minimum:", swarm.xgb, swarm.ygb)
    print("Function:", swarm.f(swarm.xgb, swarm.ygb))
    print()
    
    return ln

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax = plt.axes()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'ro')
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)

    swarm = Swarm(100)
    lijst1 = swarm.xs
    lijst2 = swarm.ys

    ani = FuncAnimation(fig, update, frames=50, interval=10, repeat=True)  
    ani.save('swarm_ani.gif', writer='pillow')
