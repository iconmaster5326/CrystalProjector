meta:
  id: texture_pack
  endian: le
doc: A packed bundle of textures, found in top-level `.dat` files in the `Textures` directory.
seq:
  - id: version
    doc: The version of this pack.
    type: u2
  - id: num_textures
    doc: How many textures are in this pack?
    type: u4
  - id: texture_headers
    doc: Headers for each texture.
    type: texture_header
    repeat: expr
    repeat-expr: num_textures
  - id: textures
    doc: The textures in this pack.
    type: texture
    repeat: expr
    repeat-expr: num_textures
types:
  texture_header:
    doc: Metadata found before a texture.
    seq:
      - id: magic1
        doc: Unknown.
        size: 7
  texture:
    doc: A named texture.
    seq:
      - id: len_name
        doc: How long the texture's name is.
        type: u4
      - id: name
        type: str
        encoding: UTF-8
        size: len_name
      - id: len_image
        doc: How long the texture file is.
        type: u4
      - id: image
        doc: The actual texture. A PNG file.
        size: len_image
