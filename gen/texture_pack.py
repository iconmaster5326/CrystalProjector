# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class TexturePack(KaitaiStruct):
    """A packed bundle of textures, found in top-level `.dat` files in the `Textures` directory."""
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.version = self._io.read_u2le()
        self.num_textures = self._io.read_u4le()
        self.texture_headers = []
        for i in range(self.num_textures):
            self.texture_headers.append(TexturePack.TextureHeader(self._io, self, self._root))

        self.textures = []
        for i in range(self.num_textures):
            self.textures.append(TexturePack.Texture(self._io, self, self._root))


    class Texture(KaitaiStruct):
        """A named texture."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.len_name = self._io.read_u4le()
            self.name = (self._io.read_bytes(self.len_name)).decode(u"UTF-8")
            self.len_image = self._io.read_u4le()
            self.image = self._io.read_bytes(self.len_image)


    class TextureHeader(KaitaiStruct):
        """Metadata found before a texture."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.magic1 = self._io.read_bytes(7)



