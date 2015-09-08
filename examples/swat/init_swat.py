"""
SWaT DB initialization

Minimal initialization

Some ideas to improve this script
-add a check_levels, to check if the levels are > 0 and < HH (and correct them)
-add a check_valves, to check if the state is coherent (and correct it)
-add a function to check to DB and correct its state if necessary

-abstract this kind of init: set values, tags, and predicats to check as arguments
-put the values, predicats ... in a conf file, and parse it ?
"""



from constants import update_statedb
from constants import logger
from constants import write_cpppo

import sys

if __name__ == '__main__':

    try:
        # update_statedb(1196, 'AI_LIT_101_LEVEL')
        # update_statedb(796, 'AI_LIT_101_LEVEL')
        # update_statedb(496, 'AI_LIT_101_LEVEL')
        update_statedb(246, 'AI_LIT_101_LEVEL')

        update_statedb(810, 'AI_LIT_301_LEVEL')
        update_statedb(1, 'DO_P_101_START')
        update_statedb(1, 'DO_MV_101_OPEN')
        update_statedb(0, 'DO_MV_201_OPEN')
        update_statedb(0.7, 'AI_FIT_101_FLOW')
        update_statedb(0.5, 'AI_FIT_201_FLOW')
        update_statedb(0, 'DO_MV_101_CLOSE')
        update_statedb(1, 'DO_MV_201_CLOSE')
        logger.debug('DB - initialized')

    except Exception, e:
        print repr(e)
        sys.exit(1)

