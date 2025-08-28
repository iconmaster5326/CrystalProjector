import typing
import json
import io

from gen.database import Database as RawDatabase
from gen.loading import Loading as RawLoading
from gen.ability import Ability
from gen.actor import Actor
from gen.animation import Animation
from gen.biome import Biome
from gen.difficulty import Difficulty
from gen.equipment import Equipment
from gen.gender import Gender
from gen.item import Item
from gen.job import Job
from gen.monster import Monster
from gen.passive import Passive
from gen.recipe import Recipe
from gen.spark import Spark
from gen.status import Status
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


def load_animations(infile: typing.BinaryIO) -> typing.Dict[int, Animation]:
    return {json["ID"]: Animation.from_dict(json) for json in Database.load(infile).database if json}


def load_biomes(infile: typing.BinaryIO) -> typing.Dict[int, Biome]:
    return {json["ID"]: Biome.from_dict(json) for json in Database.load(infile).database if json}


def load_difficulties(infile: typing.BinaryIO) -> typing.Dict[int, Difficulty]:
    return {json["ID"]: Difficulty.from_dict(json) for json in Database.load(infile).database if json}


def load_equipment(infile: typing.BinaryIO) -> typing.Dict[int, Equipment]:
    return {json["ID"]: Equipment.from_dict(json) for json in Database.load(infile).database if json}


def load_genders(infile: typing.BinaryIO) -> typing.Dict[int, Gender]:
    return {json["ID"]: Gender.from_dict(json) for json in Database.load(infile).database if json}


def load_items(infile: typing.BinaryIO) -> typing.Dict[int, Item]:
    return {json["ID"]: Item.from_dict(json) for json in Database.load(infile).database if json}


def load_jobs(infile: typing.BinaryIO) -> typing.Dict[int, Job]:
    return {json["ID"]: Job.from_dict(json) for json in Database.load(infile).database if json}


def load_loading(infile: typing.BinaryIO) -> typing.List[str]:
    return [s.value for s in RawLoading.from_io(infile).strings]


def load_monsters(infile: typing.BinaryIO) -> typing.Dict[int, Monster]:
    return {json["ID"]: Monster.from_dict(json) for json in Database.load(infile).database if json}


def load_passives(infile: typing.BinaryIO) -> typing.Dict[int, Passive]:
    return {json["ID"]: Passive.from_dict(json) for json in Database.load(infile).database if json}


def load_recipes(infile: typing.BinaryIO) -> typing.Dict[int, Recipe]:
    return {json["ID"]: Recipe.from_dict(json) for json in Database.load(infile).database if json}


def load_sparks(infile: typing.BinaryIO) -> typing.Dict[int, Spark]:
    return {json["ID"]: Spark.from_dict(json) for json in Database.load(infile).database if json}


def load_statuses(infile: typing.BinaryIO) -> typing.Dict[int, Status]:
    return {json["ID"]: Status.from_dict(json) for json in Database.load(infile).database if json}


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
    test_db("animation", load_animations)
    test_db("biome", load_biomes)
    test_db("difficulty", load_difficulties)
    test_db("equipment", load_equipment)
    test_db("gender", load_genders)
    test_db("item", load_items)
    test_db("job", load_jobs)

    print(f"=== LOADING ===")
    with open(f"{root}/loading.dat", "rb") as stream:
        loading = load_loading(stream)
        for message in loading:
            print(f"\t{message}")

    test_db("monster", load_monsters)
    test_db("passive", load_passives)
    # copy_over_db("patch")
    test_db("recipe", load_recipes)
    test_db("spark", load_sparks)
    test_db("status", load_statuses)
    # copy_over_db("system")
    # copy_over_db("troop")
    test_db("voxel", load_voxels)
