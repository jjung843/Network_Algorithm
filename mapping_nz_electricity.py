from fontTools.svgLib.path import arc
from sympy.abc import lamda

from module_lab2_task2 import *

network = NetworkElectricNZ()
network.read_network('nz_network')
network.plot_network()

print(network)