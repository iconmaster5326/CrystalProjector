# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MapRegion(KaitaiStruct):
    """Metadata for a particular map. This file is at `maps/MAPNAME/region_X_Z.dat`, where `MAPNAME` is either `biomeX` or `world`, in the world ZIP. `X` and `Z` start from 0."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.version = self._io.read_u1()
        self.map_pixels = []
        i = 0
        while not self._io.is_eof():
            self.map_pixels.append(MapRegion.MapPixel(self._io, self, self._root))
            i += 1


    class MapPixel(KaitaiStruct):
        """A single pixel of a map."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.voxel_id = self._io.read_u1()
            self.height = self._io.read_u1()
            self.water_depth = self._io.read_u1()
            if not self.water_depth <= 7:
                raise kaitaistruct.ValidationGreaterThanError(7, self.water_depth, self._io, u"/types/map_pixel/seq/2")



