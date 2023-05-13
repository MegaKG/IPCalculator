#!/usr/bin/env python3
import tkinter as tk
import time
import re

def checkint(INSTR):
    if len(INSTR) == 0:
        return False
    
    ch = set('1234567890')
    for i in INSTR:
        if i not in ch:
            return False
    return True

def checkIP(INSTR):
    SP = INSTR.split('.')
    if len(SP) == 4:
        for i in SP:
            if not checkint(i):
                return False
            else:
                if (int(i) > 255):
                    return False
        return True

    return False

def checkShortNM(IN):
    if len(IN) > 0:
        if IN[0] == '/':
            if checkint(IN[1:]):
                if int(IN[1:]) <= 32:
                    return True

    return False

def shortToBits(NM):
    Value = int(NM[1:])

    Out = ''
    for i in range(Value):
        Out += '1'
    
    for i in range(32-Value):
        Out += '0'

    #print(Out)

    IntArray = []
    for i in range(0,(4*8)-7,8):
        IntArray.append(int(Out[i:i+8],2))
    return IntArray



def longToBits(NM):
    Out = []

    for i in NM.split('.'):
        Out.append(int(i))
    return Out


def extendBinary(IN):
    while len(IN) != 8:
        IN = '0' + IN
    return IN

def arrToBinary(ARRIN):
    Out = ''

    for i in ARRIN:
        Out += extendBinary(bin(i)[2:10])
        Out += '.'

    Out = Out[:-1]
    
    return Out

def arrToIP(ARRIN):
    Out = ''

    for i in ARRIN:
        Out += str(i)
        Out += '.'

    Out = Out[:-1]
    
    return Out


def countInstances(IN,I='1'):
    count = 0
    for i in IN:
        if i == I:
            count += 1
    return count
    


class application:
    def calculate(self):
        IP_IN = self.IPVar.get()
        NM_IN = self.NetVar.get()

        if checkIP(IP_IN) and (checkIP(NM_IN) or checkShortNM(NM_IN)):
            IP = longToBits(IP_IN)

            if checkIP(NM_IN):
                NETMASK = longToBits(NM_IN)
            else:
                NETMASK = shortToBits(NM_IN)

            self.AddrDVar.set(arrToIP(IP));self.AddrDVarB.set(arrToBinary(IP))
            self.NetmDVar.set(arrToIP(NETMASK) + " = /" + str(countInstances(arrToBinary(NETMASK),'1')));self.NetmDVarB.set(arrToBinary(NETMASK))

            WildCard = []
            for i in NETMASK:
                WildCard.append(255-i)
            self.WildDVar.set(arrToIP(WildCard));self.WildDVarB.set(arrToBinary(WildCard))

            Network = []
            for i in range(4):
                Network.append(IP[i]&NETMASK[i])
            self.NetwDVar.set(arrToIP(Network));self.NetwDVarB.set(arrToBinary(Network))

            Broadcast = []
            for i in range(4):
                Broadcast.append(IP[i]|WildCard[i])
            #print(Broadcast)
            self.BroaDVar.set(arrToIP(Broadcast));self.BroaDVarB.set(arrToBinary(Broadcast))

            MinH = []
            for i in Network:
                MinH.append(i)
            MinH[-1] += 1
            self.HMinDVar.set(arrToIP(MinH));self.HMinDVarB.set(arrToBinary(MinH))

            MaxH = []
            for i in Broadcast:
                MaxH.append(i)
            MaxH[-1] -= 1
            self.HMaxDVar.set(arrToIP(MaxH));self.HMaxDVarB.set(arrToBinary(MaxH))

            HCount = (2 ** (32 - countInstances(arrToBinary(NETMASK)))) - 2
            self.HNumDVar.set(str(HCount))









    def quit(self):
        self.Run = False

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("IP Calc V1.0")

        self.Run = True

        self.EntryFrame = tk.Frame(self.root)

        tk.Label(self.EntryFrame,text="IP Address:").grid(row=0,column=0,sticky=tk.W)
        tk.Label(self.EntryFrame,text="Netmask (Full or Abbreviated):").grid(row=0,column=2,sticky=tk.W)

        self.IPVar = tk.StringVar()
        self.NetVar = tk.StringVar()

        tk.Entry(self.EntryFrame,textvariable=self.IPVar).grid(row=0,column=1)
        tk.Entry(self.EntryFrame,textvariable=self.NetVar).grid(row=0,column=3)

        self.EntryFrame.grid(row=0,column=0)

        tk.Button(self.root,text="Calculate",command=self.calculate).grid(row=1,column=0)


        self.ResultFrame = tk.Frame(self.root)

        tk.Label(self.ResultFrame,text="Address:").grid(row=1,column=0,sticky=tk.W)
        tk.Label(self.ResultFrame,text="Netmask:").grid(row=2,column=0,sticky=tk.W)
        tk.Label(self.ResultFrame,text="Wildcard:").grid(row=3,column=0,sticky=tk.W)
        tk.Label(self.ResultFrame,text="Network:").grid(row=4,column=0,sticky=tk.W)
        tk.Label(self.ResultFrame,text="Broadcast:").grid(row=5,column=0,sticky=tk.W)
        tk.Label(self.ResultFrame,text="Host Min:").grid(row=6,column=0,sticky=tk.W)
        tk.Label(self.ResultFrame,text="Host Max:").grid(row=7,column=0,sticky=tk.W)
        tk.Label(self.ResultFrame,text="Number of Hosts:").grid(row=8,column=0,sticky=tk.W)


        self.AddrDVar = tk.StringVar();self.AddrDVar.set('-')
        self.NetmDVar = tk.StringVar();self.NetmDVar.set('-')
        self.WildDVar = tk.StringVar();self.WildDVar.set('-')
        self.NetwDVar = tk.StringVar();self.NetwDVar.set('-')
        self.BroaDVar = tk.StringVar();self.BroaDVar.set('-')
        self.HMinDVar = tk.StringVar();self.HMinDVar.set('-')
        self.HMaxDVar = tk.StringVar();self.HMaxDVar.set('-')
        self.HNumDVar = tk.StringVar();self.HNumDVar.set('-')


        self.AddrDVarB = tk.StringVar();self.AddrDVarB.set('-')
        self.NetmDVarB = tk.StringVar();self.NetmDVarB.set('-')
        self.WildDVarB = tk.StringVar();self.WildDVarB.set('-')
        self.NetwDVarB = tk.StringVar();self.NetwDVarB.set('-')
        self.BroaDVarB = tk.StringVar();self.BroaDVarB.set('-')
        self.HMinDVarB = tk.StringVar();self.HMinDVarB.set('-')
        self.HMaxDVarB = tk.StringVar();self.HMaxDVarB.set('-')
        self.HNumDVarB = tk.StringVar();self.HNumDVarB.set('-')


        tk.Label(self.ResultFrame,textvariable=self.AddrDVar,width=20).grid(row=1,column=1,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.NetmDVar,width=20).grid(row=2,column=1,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.WildDVar,width=20).grid(row=3,column=1,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.NetwDVar,width=20).grid(row=4,column=1,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.BroaDVar,width=20).grid(row=5,column=1,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.HMinDVar,width=20).grid(row=6,column=1,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.HMaxDVar,width=20).grid(row=7,column=1,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.HNumDVar,width=20).grid(row=8,column=1,sticky=tk.E)


        tk.Label(self.ResultFrame,textvariable=self.AddrDVarB,width=(8*4) + 3).grid(row=1,column=2,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.NetmDVarB,width=(8*4) + 3).grid(row=2,column=2,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.WildDVarB,width=(8*4) + 3).grid(row=3,column=2,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.NetwDVarB,width=(8*4) + 3).grid(row=4,column=2,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.BroaDVarB,width=(8*4) + 3).grid(row=5,column=2,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.HMinDVarB,width=(8*4) + 3).grid(row=6,column=2,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.HMaxDVarB,width=(8*4) + 3).grid(row=7,column=2,sticky=tk.E)
        tk.Label(self.ResultFrame,textvariable=self.HNumDVarB,width=(8*4) + 3).grid(row=8,column=2,sticky=tk.E)

        self.ResultFrame.grid(row=2,column=0)

        tk.Button(self.root,text="Quit",command=self.quit).grid(row=3,column=0)

    def run(self):
        while self.Run:
            time.sleep(0.1)
            self.root.update()
        self.root.destroy()


if __name__ == '__main__':
    app = application()
    app.run()