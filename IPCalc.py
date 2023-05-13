#!/usr/bin/env python3
import tkinter as tk
import time

class application:
    def calculate(self):
        pass

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