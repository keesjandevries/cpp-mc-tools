# distutils: language = c++
# distutils: include_dirs = SLHALib-2.2/x86_64-linux/include/ 
# distutils: libraries = SLHA gfortran
# distutils: library_dirs = SLHALib-2.2/x86_64-linux/lib/
import os
from uuid import uuid1

cdef extern from "CSLHA.h":
    cdef int nslhadata
    cdef int invalid
    cdef int OffsetSPInfo
    cdef void SLHAWrite(int *, const double complex *, const char *)
    cdef void SLHARead(int *, double complex *, const char *, const int )

cdef class SlhaFile:
    #FIXME: had to hard wire the number (nslhadata in SLHADefs.h)
    cdef double complex _slhadata[5558]
    cdef str _tmp_dir
    cdef dict _lookup
    def __cinit__(self, filename=None, tmp_dir='./', lookup=None):
        self._tmp_dir = tmp_dir
        #First create the lookup
        if lookup:
            self._lookup = lookup
        else:
            self._lookup = self.create_lookup()
        #Then read in file
        if filename :
            self.read(filename)
        else:
            for i in range(nslhadata):
                self._slhadata[i] = invalid
    def __dealloc__(self):
        pass
    def __setitem__(self, key, value):
        self._slhadata[self._lookup[key]] = value
    def __getitem__(self, key):
        return self._slhadata[self._lookup[key]]
    def write(self, filename):
        cdef int error
        b_filename = filename.encode('UTF-8')
        SLHAWrite(&error, self._slhadata, b_filename)
    def read(self, filename):
        cdef int error
        b_filename = filename.encode('UTF-8')
        SLHARead(&error, self._slhadata, b_filename, 0)
    def __str__(self):
        tmp_name = os.path.join(self._tmp_dir, str(uuid1()))
        self.write(tmp_name)
        with open(tmp_name, 'r') as f:
            txt = f.read()
        os.remove(tmp_name)
        return txt
    def get_lookup(self):
        return self._lookup
    def create_lookup(self):
        """
         This function returns a dictionary
         { slhalib_nr: ('block','comment'), ... , 
           ('block','comment'): slhalib_nr, ... }
        """
        cdef int i
        for i in range(OffsetSPInfo):
            self._slhadata[i] = i
        for i in range(OffsetSPInfo, nslhadata):
            self._slhadata[i] = invalid
        block_comment_nr_list = self.get_blocks_comments_values()
        lookup = {}
        for block, comment, nr in block_comment_nr_list:
            nr = int(nr)
            lookup[nr] = (block, comment)
        tmp_dict = {}
        for nr, oid in lookup.items():
            tmp_dict[oid] = nr
        lookup.update(tmp_dict)
        return lookup
    def get_blocks_comments_values(self):
        """
        This function contains knowledge about what an slhafile from slhalib looks like
        It returns a list: [(block, comment, value)]
        NB: atm ignoring BLOCK SPINFO  and  DECAY's
        """
        s = str(self)
        data = []
        block_name = None
        for line in s.split('\n'):
            if line.startswith('B'):
                # is a block
                block_name = line.split()[1]
                if 'Q=' in line:
                    q_value = float(line.split('=')[1].split()[0])
                    data.append((block_name, 'Qscale', q_value))
            elif line.startswith('D'):
                #FIXME: we may want to change this
                print("WARNING: DECAY's are ignored in "
                        "SLHA.get_blocks_indices_comments_values() ")
                block_name = None
            elif block_name and (not block_name == 'SPINFO') :
                #FIXME: possibly want to have the SPINFO as well at some point
                items = line.split()
                if len(items):
                    first_non_index = next(x for x in items if not isinstance(x, int))
                    indices_end = items.index(first_non_index)
                    comment_pos = items.index('#') if '#' in items else 0
                    if comment_pos >0: 
                        indices_end=comment_pos-1
#                    indices = tuple([int(x) for x in items[:indices_end]])
                    values = tuple([float(x) for x in
                            items[indices_end:comment_pos]])
                    if len(values) == 1:
                        values = values[0]
                    comment = ' '.join(items[comment_pos:]).lstrip('#').lstrip()
                    data.append((block_name, comment, values))
        return data
