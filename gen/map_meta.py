# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MapMeta(KaitaiStruct):
    """Metadata for a particular map. This file is at `maps/MAPNAME/meta.dat`, where `MAPNAME` is either `biomeX` or `world`, in the world ZIP."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.version = self._io.read_u1()
        self.pos_y = self._io.read_s4le()
        self.pos_x = self._io.read_s4le()
        self.pos_z = self._io.read_s4le()
        self.size_x = self._io.read_u4le()
        self.size_z = self._io.read_u4le()
        self.region_size_x = self._io.read_u4le()
        if not self.region_size_x == 64:
            raise kaitaistruct.ValidationNotEqualError(64, self.region_size_x, self._io, u"/seq/6")
        self.region_size_z = self._io.read_u4le()
        if not self.region_size_z == 64:
            raise kaitaistruct.ValidationNotEqualError(64, self.region_size_z, self._io, u"/seq/7")
        self.num_regions_x = self._io.read_u4le()
        self.num_regions_z = self._io.read_u4le()


