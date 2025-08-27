meta:
  id: map_region
  endian: le
doc: Metadata for a particular map. This file is at `maps/map_MAPNAME/region_X_Z.dat`, where `MAPNAME` is either `biomeX` or `world`, in the world ZIP. `X` and `Z` start from 0.
seq:
  - id: version
    doc: The version number of this map region.
    type: u1
  - id: map_pixels
    doc: The pixels in this map. This may be up to 64x64 pixels, but may be less, if this region is at the end of the map's X or Z bounds.
    type: map_pixel
    repeat: eos
types:
  map_pixel:
    doc: A single pixel of a map.
    seq:
      - id: voxel_id
        doc: The ID of the voxel's top texture to display in the map.
        type: u1
      - id: height
        doc: The height to display this pixel at.
        type: u1
      - id: water_depth
        doc: How deep is the water at this pixel? 0-7.
        type: u1
        valid:
          max: 7
