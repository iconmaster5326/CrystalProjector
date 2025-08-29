# Compiling KSY schemas

You need KSC and Python bindings, latest nightly. Do NOT pull from PyPI. Do this instead:

```bash
python3 -m pip install --upgrade --pre git+https://github.com/kaitai-io/kaitai_struct_python_runtime.git
```

From there:

```bash
kaitai-struct-compiler schema/ksy/*.ksy -t python -d gen/
```

Then KSC has some issues:

* No type annotations.
* It imports sub-KSY file dependencies incorrectly; `import X` should be `from . import X`.
* It does not stop keywords from being used as names.

These need fixed manually for now.

# Compiling JSON schemas

For each schema (OTHER THAN `patch.yaml`):

```bash
quicktype --lang python --src-lang schema --out gen/X.py schema/json/X.yaml
```

Quicktype *also* has issues:

* No support for integer enums; if you omit `type: integer` from such enums, Quicktype crashes.
* Does not support multi-file `$ref`s in a smart manner.

# Python dependencies

* `kaitai-struct`: USE THE DEVEL VERSION, see above.
* `Pillow`: For `PIL`.

For testing:

* `pyyaml`: For `yaml`.
* `jsonschema`.
