import sys
import py_modules.CtypesWrappers as cw

argv = sys.argv
if len(argv) == 2:
    print('chi2:  {}'.format(cw.get_min_reference(argv[1])))
    print('rowid: {}'.format(cw.get_min_reference_rowid(argv[1])))
