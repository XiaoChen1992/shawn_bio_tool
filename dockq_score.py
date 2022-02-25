"""
@ Description: Generate DockQ score by Fnat, LRMS, iRMS
@ Author: Shawn Chen
@ Date: 2022-02-25
"""


def calculate_dockq(fnat: float, lrms: float, irms: float) -> float:
	def scaled(rms: float, d: float) -> float:
		return 1 / (1 + (rms / d)**2)
	scaled_lrms = scaled(lrms, d1)
	scaled_irms = scaled(irms, d2)

	return (fnat, scaled_lrms + scaled_irms) / 3