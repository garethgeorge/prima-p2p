import pulse2percept as p2p
import numpy as np
import matplotlib as plt
from prima import Prima
from pulse2percept.viz import plot_implant_on_axon_map

# Array Shape plotting
implant = Prima(x=-50, y=50, rot=np.deg2rad(0))
plt, _ = plot_implant_on_axon_map(
    implant, annotate_implant=False, marker_style='hw')
# plt, _ = plot_implant_on_axon_map(
#     implant, annotate_implant=False)
plt.savefig("array_shape.svg")

# Plot a pulse train on one electrode
# argus = Prima()
# stim = p2p.stimuli.PulseTrain(0.005/1000.0)
# sim = p2p.Simulation(argus, engine='serial')
# sim.set_ganglion_cell_layer('Nanduri2012')
# sim.set_optic_fiber_layer(sampling=250, decay_const=2)
# percept = sim.pulse2percept({"A1": stim, "B2": stim}, layers=["OFL", "GCL"])

# plt.pcolor(percept.data[:, :, 50000])
# plt.savefig("blargh.png")
