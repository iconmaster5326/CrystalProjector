import typing
import json
import io

from gen.database import Database as RawDatabase
from gen.ability import Ability
from gen.actor import Actor
from gen.biome import Biome
from gen.voxel import Voxel


JSONObject = typing.Dict[str, "JSON"]
"""A JSON object."""


JSONArray = typing.List["JSON"]
"""A JSON array."""


JSON = typing.Union[None, bool, float, str, "JSONObject", "JSONArray"]
"""A JSON value."""


class Database(typing.NamedTuple):
    """A parsed Crystal Project database `.dat` file."""

    version: int
    """The version of this database file."""
    database: JSONArray
    """The database."""

    @classmethod
    def load(cls, infile: typing.BinaryIO) -> "Database":
        """Load a database from memory."""

        db = RawDatabase.from_io(infile)

        result = io.BytesIO()
        for b in db.database:
            result.write((255 - b).to_bytes(1, 'little'))
        return Database(db.version, json.loads(str(result.getvalue(), encoding="UTF-8")))


def load_abilities(infile: typing.BinaryIO) -> typing.Dict[int, Ability]:
    return {json["ID"]: Ability.from_dict(json) for json in Database.load(infile).database if json}


def load_actors(infile: typing.BinaryIO) -> typing.Dict[int, Actor]:
    return {json["ID"]: Actor.from_dict(json) for json in Database.load(infile).database if json}


def load_biomes(infile: typing.BinaryIO) -> typing.Dict[int, Biome]:
    return {json["ID"]: Biome.from_dict(json) for json in Database.load(infile).database if json}


def load_voxels(infile: typing.BinaryIO) -> typing.Dict[int, Voxel]:
    return {json["ID"]: Voxel.from_dict(json) for json in Database.load(infile).database if json}


############
# TEMP STUFF
############

if __name__ == "__main__":
    import yaml
    import jsonschema

    root = "C:/Program Files (x86)/Steam/steamapps/common/Crystal Project/Content/Database"

    def test_db(filename: str, load_fn: typing.Callable[[typing.BinaryIO], typing.Any]):
        print(f"=== {filename.upper()} ===")
        schema = yaml.load(open(f"schema/json/{filename}.yaml", encoding="UTF-8"), yaml.FullLoader)
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema)
        dbfile = open(f"{root}/{filename}.dat", "rb")
        raw_json = Database.load(dbfile).database
        for thing in raw_json:
            if thing:
                print(f"\tValidating {thing['ID']} ({thing['Name']})...")
                validator.validate(thing, schema)
        print("\tTesting deserialization...")
        dbfile.seek(0)
        load_fn(dbfile)
        print("\tDone!")
    
    def copy_over_db(filename: str):
        dbfile = open(f"{root}/{filename}.dat", "rb")
        raw_json = Database.load(dbfile).database
        with open(f"temp/{filename}.dat.json", "w", encoding="UTF-8") as outfile:
            json.dump(raw_json, outfile, indent=2)
    
    test_db("ability", load_abilities)
    test_db("actor", load_actors)
    # copy_over_db("animation")
    test_db("biome", load_biomes)
    # copy_over_db("difficulty")
    # copy_over_db("equipment")
    # copy_over_db("gender")
    # copy_over_db("item")
    # copy_over_db("job")
    # # copy_over_db("loading") # TODO: this has its own format!
    # copy_over_db("monster")
    # copy_over_db("passive")
    # copy_over_db("patch")
    # copy_over_db("recipe")
    # copy_over_db("spark")
    # copy_over_db("status")
    # copy_over_db("system")
    # copy_over_db("troop")
    test_db("voxel", load_voxels)
