class basic_physics:
    import math
    def __init__(self, explain=False):
        self.C = 300000000

    def Help(self):
        print("Returns missing variable's value.")
        print("\tForces:")
        print("\t\t.Force: \t\tVariables: F,M,A")
        print("\t\t.Kinet_Energy: \t\tVariables: Ek,M,V")
        print("\t\t.Pot_Energy: \t\tVariables: Ep,M,G,H")
        print("\t\t.Power: \t\tVariables: P,W,T")
        print("\t\t.Work: \t\t\tVariables: W,F,D,Rad")
        print("\t\t.Spring_Force: \t\tVariables: F,K,X")
        print("\t\t.Pressure: \t\tVariables: P,F,A")
        print()
        print("\tMovement:")
        print("\t\t.Angu_Accel: \t\tVariables: Vf,Vs,A,T")
        print("\t\t.Cent_Accel: \t\tVariables: Ac,V,R")
        print("\t\t.Momentum: \t\tVariables: Mass,Moment,V")
        print()
        print("\tEnergy:")
        print("\t\t.Energy: \t\tVariables: E,M")
        print("\t\t.Cons_Of_Energy: \tVariables: Et,Ek,Ep")
        print()
        print("\tElectricity:")
        print("\t\t.Elec_Current: \t\tVariables: I,Q,T")
        print("\t\t.Elec_Work: \t\tVariables: W,C,V""")
        print()
        print("\tMISC:")
        print("\t\t.Density: \t\tVariables: M,V,D")


    def MultipleNone(self):
        raise("Multiple variables were not listed.")

    
    def NoNone(self):
        raise("No variables were listed as None.")


    def Force(self,F=None, M=None, A=None):
        if (F == None and M == None) or (F == None and A == None) or (A == None and M == None):
            self.MultipleNone()
        elif F == None:
            return M*A
        elif M == None:
            return F/A
        elif A == None:
            return F/M
        else:
            self.NoNone()


    def Kinet_Energy(self, Ek = None, M = None, V = None):
        if (Ek == None and M == None) or (Ek == None and V == None) or (M == None and V == None):
            self.MultipleNone()
        elif Ek == None:
            return .5 * M * V * V
        elif M == None:
            return 2 * Ek / (V * V)
        elif V == None:
            return pow((2 * Ek / M),.5)
        else:
            self.NoNone()


    def Pot_Energy(self, Ep = None, M = None, G = None, H = None):
        if ((Ep == None and M == None) or (Ep == None and G == None) or
           (Ep == None or H == None) or (M == None and G == None) or
           (M == None and H == None) or (G == None and H == None)):
            self.MultipleNone()
        elif Ep == None:
            return M * G * H
        elif M == None:
            return Ep / (G * H)
        elif G == None:
            return Ep / (M * H)
        elif H == None:
            return Ep / (G * M)
        else:
            self.NoNone()


    def Power(self, P = None, W = None, T = None):
        if (P == None and W == None) or (P == None and T == None) or (W == None and T == None):
            self.MultipleNone()
        elif P == None:
            return W * T
        elif W == None:
            return P/T
        elif T == None:
            return P/W
        else:
            self.NoNone()


    def Work(self, W = None, F = None, D = None, Rad = 0):
        if (W == None and F == None) or (W == None and D == None) or (F == None and D == None):
            self.MultipleNone()
        elif W == None:
            return F*D*cos(Rad)
        elif F == None:
            return W/(D*cos(Rad))
        elif D == None:
            return W/(F*cos(Rad))
        elif Rad == None:
            self.NoNone()
        else:
            raise("Not completed yet.")


    def Spring_Force(self,F = None,K = None,X = None):
        if (F == None and K == None) or (F == None and X == None) or (K == None and X == None):
            self.MultipleNone()
        elif F == None:
            return -1 * K * X
        elif K == None:
            return -1 * F / X
        elif X == None:
            return -1 * F / K
        else:
            self.NoNone()


    def Pressure(self, P = None, F = None, A = None):
        if (P == None and F == None) or (P == None and A == None) or (F == None and A == None):
            self.MultipleNone()
        elif P == None:
            return F/A
        elif F == None:
            return P * A
        elif A == None:
            return F/P
        else:
            self.NoNone()


    def Angu_Accel(self, Vf = None, Vs = None, A = None, T = None):
        if ((Vf == None and Vs == None) or (Vf == None and A == None) or (Vf == None and T == None) or
            (Vs == None and A == None) or (Vs == None and T == None) or (A == None and T == None)):
            self.MultipleNone()
        elif Vf == None:
            return Vs + A * T
        elif Vs == None:
            return Vf - A * T
        elif A == None:
            return (Vf - Vs)/T
        elif T == None:
            return (Vf - Vs)/A
        else:
            self.NoNone()


    def Cent_Accel(self, Ac = None, V = None, R = None):
        if (Ac == None and V == None) or (Ac == None and R == None) or (V == None and R == None):
            self.MultipleNone()
        elif Ac == None:
            return V * V * R
        elif V == None:
            return pow(Ac * R, .5)
        elif R == None:
            return (V * V) / Ac
        else:
            return self.NoNone()


    def Momentum(self, Mass = None, Moment = None, V = None):
        if (Mass == None and Moment == None) or (Moment == None and V == None) or (Mass == None and V == None):
            self.MultipleNone()
        elif Mass == None:
            return Moment/V
        elif Moment == None:
            return Mass * V
        elif V == None:
            return Moment/Mass
        else:
            self.NoNone()


    def Energy(self, E = None, M = None):
        if E == None and M == None:
            self.MultipleNone()
        elif E == None:
            return M * self.C * self.C
        elif M == None:
            return E / (self.C * self.C)
        else:
            self.NoNone()


    def Cons_Of_Energy(self, Et = None, Ek = None, Ep = None):
        if (Et == None and Ek == None) or (Et == None and Ep == None) or (Ek == None and Ep == None):
            self.MultipleNone()
        elif Et == None:
            return Ek + Ep
        elif Ek == None:
            return Et - Ep
        elif Ep == None:
            return Et - Ek
        else:
            self.NoNone()


    def Elec_Current(self, I = None, Q = None, T = None):
        if (I == None and Q == None) or (I == None and T == None) or (Q == None and T == None):
            self.MultipleNone()
        elif I == None:
            return Q/T
        elif Q == None:
            return I * T
        elif T == None:
            return Q/I
        else:
            self.NoNone()


    def Elec_Work(self, W = None, C = None, V = None):
        if (W == None and C == None) or (W == None and V == None) or (C == None and V == None):
            self.MultipleNone()
        elif W == None:
            return .5 * C * V * V
        elif C == None:
            return 2 * W / (V * V)
        elif V == None:
            return pow(2 * W / C, .5)
        else:
            self.NoNone()


    def Density(self, M = None, V = None, D = None):
        if (M == None and V == None) or (M == None and D == None) or (V == None and D == None):
            self.MultipleNone()
        elif M == None:
            return D * V
        elif D == None:
            return M / V
        elif V == None:
            return M / D
        else:
            self.NoNone()
