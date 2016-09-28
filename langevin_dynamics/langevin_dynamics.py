def langevin_dynamics(x0,v0,t,m,filename,lam,T):
    '''This function is a one dimensional Langevin Dynamics Simulator.

    Parameters
    ----------
        x0 : int
            initial position
        v0 : float
            initial velocity
        t : float
            time per step
        m : float
            mass
        filename : string
            name of file containing potential information, must have 4 columns, index, position, potential energy at that positoin, and force at that position, position must have a stepsize of .001
        lam : float
            the lambda for brownian motion
        T : float
            the amount of time the simulation will be run for

    Returns
    -------
    pos, vel, time : lists
        lists indicating position, velocity, and time for each step
    also writes to a file named "output.txt" in the directory
    '''
    import random
    x = x0
    v = v0
    crs = open(filename, "r")
    fps = []
    for columns in (raw.strip().split() for raw in crs):
        fps.append(columns[3])
    pos=[]
    vel=[]
    time=[]
    i_s = []
    for i in range(0,int(T/t)):
        fd = -lam*v
        fs = random.gauss(0,1)
        #fs = np.random.normal(0,1)
        xp = int(x * 10)
        fp = float(fps[xp])
        a = fd + fs+ fp
        v = v + t * a
        x = x + t * v
        i_s.append(i)
        pos.append(x)
        vel.append(v)
        time.append(i*t)
    f = open("output.txt",'w')
    for i in i_s:
        f.write("%s\n" % str(i))
    for i in pos:
        f.write("%s\n" % str(i))
    for i in vel:
        f.write("%s\n" % str(i))
    for i in time:
        f.write("%s\n" % str(i))
    return pos,vel,time
