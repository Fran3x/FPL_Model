from getters import *
from understat import *
from mergers import *
from cleaners import *

import pprint as pp

epl_data = get_epl_data()
pp.pprint(epl_data[0]['71'])