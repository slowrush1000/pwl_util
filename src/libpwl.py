
class XY:
    def __init__(self, x = 0.0, y = 0.0):
        self.m_x    = x
        self.m_y    = y
    def SetX(self, x):
        self.m_x    = x
    def GetX(self):
        return self.m_x
    def SetY(self, y):
        self.m_y    = y
    def GetY(self):
        return self.m_y

class PWL:
    def __init__(self):
        self.m_name         = ''
        self.m_nodenames    = []
        self.m_xys          = []
    def SetName(self, name):
        self.m_name         = name
    def GetName(self):
        return self.m_name
    def SetPosNodename(self, pos_nodename):
        self.m_nodenames[0] = pos_nodename
    def GetPosNodename(self):
        return self.m_nodenames[0]
    def SetNegNodename(self, neg_nodename):
        self.m_nodenames[1] = neg_nodename
    def GetNegNodename(self):
        return self.m_nodenames[1]
    def AddXY(self, xy):
        self.m_xys.append(xy)
    def GetXs(self):
        xs  = []
        for xy in self.m_xys:
            xs.append(xy.GetX())
        return xs
    def GetYs(self):
        ys  = []
        for xy in self.m_xys:
            ys.append(xy.GetY())
        return ys