meta:
  id: world_data
  endian: le
doc: A world data file contains information about the `WORLDNAME.dat` file nested in a world file called WORLDNAME in the world ZIP.
seq:
  - id: len_metadata
    doc: How long is the metadata field?
    type: u4
  - id: metadata
    doc: A string containing /r/n separated key=value pairs, representing global map information.
    type: str
    encoding: UTF-8
    size: len_metadata
  - id: len_warp_points
    doc: How long is the warp-points field?
    type: u4
  - id: warp_points
    doc: "A string containing /r/n separated I:X1,Y1,Z1:X2,Y2,Z2; pairs, representing teleport points on the map."
    type: str
    encoding: UTF-8
    size: len_warp_points
  - id: num_layer_infos
    doc: How many chunk layers are there in this map?
    type: u4
  - id: layer_infos
    doc: Basic chunk layer information used to find the chunk layer archives.
    type: layer_info
    repeat: expr
    repeat-expr: num_layer_infos
  - id: magic1
    doc: Unknown.
    size: 4
  - id: len_layers
    doc: The total size of all the layer archives in bytes.
    type: u4
  - id: layers
    doc: The chunk layer archive files. ZIP format. Use the `offset` and `length` fields in `layer_info`s to read these.
    size: len_layers
types:
  layer_info:
    doc: Basic chunk layer information used to find a chunk layer archive.
    seq:
      - id: x
        doc: The X coordinate of the chunk layer.
        type: s4
      - id: z
        doc: The Z coordinate of the chunk layer.
        type: s4
      - id: offset
        doc: The relative offset from the beginning of `layers` into which you can find this archive.
        type: u4
        # valid:
        #   max: _parent.len_layers
      - id: length
        doc: The size of the archive.
        type: u4
        # valid:
        #   max: _parent.len_layers
    instances:
      layer:
        doc: The layer archive. A ZIP file.
        io: _parent._io
        pos: _parent.start_of_layers + offset
        size: length
instances:
  start_of_layers:
    doc: The address of the start of `layers`.
    value: 4 + len_metadata + 4 + len_warp_points + 4 + num_layer_infos*16 + 4 + 4
