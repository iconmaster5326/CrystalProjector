meta:
  id: database
  endian: le
doc: A database file is a `.dat` file that contains a encrypted JSON file.
seq:
  - id: version
    doc: The version number of the world.
    type: u2
  - id: database
    doc: The database. An encrypted JSON string. Each byte may be decrypted by subtracting 255 from it.
    size-eos: true
