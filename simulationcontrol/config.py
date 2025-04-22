import os

HERE = os.path.dirname(os.path.abspath(__file__))
SNIPER = os.path.dirname(HERE)

RESULTS_FOLDER = os.path.join(SNIPER, 'results')
NUMBER_CORES = 4
SNIPER_CONFIG = 'biglittle'
ENABLE_HEARTBEATS = True
# SCRIPTS = ['magic_timestamp', 'magic_perforation_rate:0,0,0'] # for running with heartbeats and no perforation active. 
SCRIPTS = ['magic_timestamp']
