# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import vlq_base128_le


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Loading(KaitaiStruct):
    """The `loading.dat` database is different from the others.
    This contains strings related to the loading screen.
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.num_strings = self._io.read_u1()
        self.strings = []
        for i in range(self.num_strings):
            self.strings.append(Loading.String(self._io, self, self._root))


    class String(KaitaiStruct):
        """A string."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.length = vlq_base128_le.VlqBase128Le(self._io)
            self.value = (self._io.read_bytes(self.length.value)).decode(u"UTF-8")



