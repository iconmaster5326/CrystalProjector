meta:
  id: world
  endian: le
doc: A world file is a `.dat` file that contains top-level information about a game world.
seq:
  - id: version
    doc: The version number of the world.
    type: u2
  - id: data_and_maps
    doc: The world archive file. ZIP format. Contains a `world_data` file as well as map information.
    size-eos: true
