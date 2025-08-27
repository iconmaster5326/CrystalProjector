meta:
  id: map_meta
  endian: le
doc: Metadata for a particular map. This file is at `maps/map_MAPNAME/meta.dat`, where `MAPNAME` is either `biomeX` or `world`, in the world ZIP.
seq:
  - id: version
    doc: The version number of this map.
    type: u1
  - id: pos_y
    doc: The Y level this map should be rendered at in the world map.
    type: s4
  - id: pos_x
    doc: The X coordinate the map starts at, in voxel coordinates.
    type: s4
  - id: pos_z
    doc: The Z coordinate the map starts at, in voxel coordinates.
    type: s4
  - id: size_x
    doc: The size of this map along the X axis.
    type: u4
  - id: size_z
    doc: The size of this map along the Z axis.
    type: u4
  - id: region_size_x
    doc: The maximum size a map region can cover along the X axis. Always 64.
    type: u4
    valid: 64
  - id: region_size_z
    doc: The maximum size a map region can cover along the Z axis. Always 64.
    type: u4
    valid: 64
  - id: num_regions_x
    doc: The number of regions this map contains along the X axis.
    type: u4
  - id: num_regions_z
    doc: The number of regions this map contains along the Z axis.
    type: u4
