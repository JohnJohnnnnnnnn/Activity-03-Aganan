class evcalc():
    def Evs(ev_stats,target,D,mods):
        evneed = (ev_stats/mods)
        evneed = (evneed - D)*400
        evneed = ((evneed/target)/4)
        evneed = evneed * 4
        return evneed