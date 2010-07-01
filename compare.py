#!/usr/bin/env python
import scatter

potential = scatter.potential.Gauss(2.2,-5.5)

solver = scatter.solver.PhaseFunctions(potential,1000.,100.)
data1 = solver.solve(80)
data1.print_dcs()

solver = scatter.solver.WavePack(potential,1000.,100.)
data2 = solver.solve(12,15,4.)
data2.print_dcs()

s = scatter.ScatterData(data2.theta)
s.init_phase( solver.Born )

gr = scatter.Graph()
gr.push(data1.get_dcs())
gr.push(data2.get_dcs())
gr.push(s.get_dcs() )
gr.show()


