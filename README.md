Wavepack
============

*Righ now some result aren't adequate. Be careful!*

Python library for calculating quantum scattering process.


installing
----------

Depends on scipy, numpy and matplotlib. To install type something like this:

	apt-get install python-numpy python-scipy python-matplotlib


usage
-----

For example like this:

	import scatter

    potential = scatter.potential.Gauss(2.236,-41.47)

	solver = scatter.solver.PhaseFunctions(potential,1000.,5.)
	data1 = solver.solve(80)
	
	gr = scatter.Graph()
	gr.push(data1.get_dcs())
	gr.show()


contents
--------

Available potentials:
- Gauss potential

Available solvers:
- PhaseFunc -- phase functions method. Works good at low energies, i.e. tenths MeV for NN-scattering.
- WavePack -- wave packet approximation without partial wave decomposition. Slower, but better on higher energies. Right now results are *not correct*!

todo
----
- Fix WavePack solver!
- Documentate sources.
- Write some tests on accuracy.
