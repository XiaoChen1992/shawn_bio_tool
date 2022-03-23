"""
@ Description: Generate DockQ score by Fnat, LRMS, iRMS, map dockq to CAPRI standard
@ Author: Shawn Chen
@ Date: 2022-02-25
"""


def calculate_dockq(fnat: float, lrms: float, irms: float) -> float:
	def scaled(rms: float, d: float) -> float:
		return 1 / (1 + (rms / d)**2)
	scaled_lrms = scaled(lrms, d=8.5)
	scaled_irms = scaled(irms, d=1.5)

	return (fnat, scaled_lrms + scaled_irms) / 3


def classification(dockq_score: float) -> float:
    """0: incorrect, 1: acceptable, 2: medium, 3: high"""
    if 0 <= dockq_score < 0.23:
        return 0.0
    elif 0.23 <= dockq_score < 0.49:
        return 1.0
    elif 0.49 <= dockq_score < 0.8:
        return 2.0
    elif dockq_score >= 0.8:
        return 3.0
    else:
        raise ValueError(f'The dockq score shout between 0 and 1. The current value is {dockq_score}')