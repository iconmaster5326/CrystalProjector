# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Voxels(KaitaiStruct):
    """A file of the form `yX.dat`,  that lists all voxels in a 16x16x16 cube chunk, for the chunk at y level X."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.version = self._io.read_u1()
        self.magic1 = self._io.read_bytes(12)
        self.voxels = []
        for i in range(4096):
            self.voxels.append(Voxels.Voxel(self._io, self, self._root))


    class Voxel(KaitaiStruct):
        """A single voxel definition."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.id = self._io.read_u1()
            self.magic1 = self._io.read_bytes(3)



