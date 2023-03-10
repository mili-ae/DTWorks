import matplotlib.pyplot as plt
from swarm import Swarm
from matplotlib.animation import FuncAnimation

iterations_done = 0


def update(frame):
    global iterations_done
    xdata = swarm.xs
    ydata = swarm.ys
    
    swarm.tick()
    ln.set_data(xdata, ydata)
    
    print(swarm)
    print()
    print("Iteration #:", iterations_done)
    print("Global Minimum:", swarm.xgb, swarm.ygb)
    print("Function:", swarm.f(swarm.xgb, swarm.ygb))
    print()
    iterations_done += 1
    
    return ln

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax = plt.axes()
    xdata, ydata = [], []
    ln, = plt.plot([], [], 'ro')
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)

    swarm = Swarm(1000)
    lijst1 = swarm.xs
    lijst2 = swarm.ys

    ani = FuncAnimation(fig, update, frames=100, interval=10, repeat=True)  
    ani.save('swarm_ani.gif', writer='pillow')