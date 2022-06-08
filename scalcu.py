class scalc():
    def health(base,Iv,Ev,level):
        Hp = ((((2*base+Iv+(Ev/4))*level)/100)+level+10)
        return Hp
    
    def attackb(base_os,Iv_os,Ev_os,level1):
        atckb = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1.1)
        return atckb
    
    def attackh(base_os,Iv_os,Ev_os,level1):
        atckh = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 0.9)
        return atckh
    
    def attackn(base_os,Iv_os,Ev_os,level1):
        atckn = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return atckn
    
    def defenseb(base_os,Iv_os,Ev_os,level1):
        defb = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1.1)
        return defb
    
    def defenseh(base_os,Iv_os,Ev_os,level1):
        defh = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 0.9)
        return defh
    
    def defensen(base_os,Iv_os,Ev_os,level1):
        defn = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return defn
    
    def speedb(base_os,Iv_os,Ev_os,level1):
        spedb = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spedb
    def speedh(base_os,Iv_os,Ev_os,level1):
        spedh = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spedh
    def speedn(base_os,Iv_os,Ev_os,level1):
        spedn = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spedn
    
    def sptkb(base_os,Iv_os,Ev_os,level1):
        spatb = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spatb
    def sptkh(base_os,Iv_os,Ev_os,level1):
        spath = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spath
    def sptkn(base_os,Iv_os,Ev_os,level1):
        spddeb = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spddeb
    
    def spdeb(base_os,Iv_os,Ev_os,level1):
        spddeb = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spddeb
    def spdeh(base_os,Iv_os,Ev_os,level1):
        spddeh = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spddeh
    def spden(base_os,Iv_os,Ev_os,level1):
        spdden = (((((2*base_os+Iv_os+(Ev_os/4))*level1)/100)+5) * 1)
        return spdden
