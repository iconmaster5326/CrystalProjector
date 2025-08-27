meta:
  id: voxels
  endian: le
doc: A file of the form `yX.dat`,  that lists all voxels in a 16x16x16 cube chunk, for the chunk at y level X.
seq:
  - id: version
    doc: A version byte.
    type: u1
  - id: magic1
    doc: Unknown.
    size: 12
  - id: voxels
    doc: The voxels in this chunk. A 16x16x16 array.
    type: voxel
    repeat: expr
    repeat-expr: 4096
types:
  voxel:
    doc: A single voxel definition.
    seq:
      - id: id
        doc: The voxel ID used in this spot.
        type: u1
      - id: magic1
        doc: Unknown.
        size: 3
