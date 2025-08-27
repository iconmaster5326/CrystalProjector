meta:
  id: loading
  endian: le
  imports:
    - vlq_base128_le
doc: |
  The `loading.dat` database is different from the others.
  This contains strings related to the loading screen.
seq:
  - id: num_strings
    doc: How many strings are in the database.
    type: u1
  - id: strings
    doc: The strings present in the database.
    type: string
    repeat: expr
    repeat-expr: num_strings
types:
  string:
    doc: A string.
    seq:
      - id: length
        doc: How long is this string?
        type: vlq_base128_le
      - id: value
        doc: The string.
        type: str
        encoding: UTF-8
        size: length.value
