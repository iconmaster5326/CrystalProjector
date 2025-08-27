# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class WorldData(KaitaiStruct):
    """A world data file contains information about the `WORLDNAME.dat` file nested in a world file called WORLDNAME in the world ZIP."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.len_metadata = self._io.read_u4le()
        self.metadata = (self._io.read_bytes(self.len_metadata)).decode(u"UTF-8")
        self.len_warp_points = self._io.read_u4le()
        self.warp_points = (self._io.read_bytes(self.len_warp_points)).decode(u"UTF-8")
        self.num_layer_infos = self._io.read_u4le()
        self.layer_infos = []
        for i in range(self.num_layer_infos):
            self.layer_infos.append(WorldData.LayerInfo(self._io, self, self._root))

        self.magic1 = self._io.read_bytes(4)
        self.len_layers = self._io.read_u4le()
        self.layers = self._io.read_bytes(self.len_layers)

    class LayerInfo(KaitaiStruct):
        """Basic chunk layer information used to find a chunk layer archive."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.x = self._io.read_s4le()
            self.z = self._io.read_s4le()
            self.offset = self._io.read_u4le()
            self.length = self._io.read_u4le()

        @property
        def layer(self):
            """The layer archive. A ZIP file."""
            if hasattr(self, '_m_layer'):
                return self._m_layer

            io = self._parent._io
            _pos = io.pos()
            io.seek(self._parent.start_of_layers + self.offset)
            self._m_layer = io.read_bytes(self.length)
            io.seek(_pos)
            return getattr(self, '_m_layer', None)


    @property
    def start_of_layers(self):
        """The address of the start of `layers`."""
        if hasattr(self, '_m_start_of_layers'):
            return self._m_start_of_layers

        self._m_start_of_layers = ((((((4 + self.len_metadata) + 4) + self.len_warp_points) + 4) + self.num_layer_infos * 16) + 4) + 4
        return getattr(self, '_m_start_of_layers', None)


