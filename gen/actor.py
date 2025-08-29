from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Actor:
    """A Crystal Project actor definition. This is... Probably unused?
    This isn't about fake PCs you fight, because Dr. Cool Aids and friends aren't here.
    This isn't about reusable NPCs; that's in `System.dat`.
    """
    agi_rating: int
    comments: str
    description: None
    dex_rating: int
    flavor: None
    hp_rating: int
    id: int
    lck_rating: int
    mnd_rating: int
    mp_rating: int
    name: str
    spd_rating: int
    spi_rating: int
    str_rating: int
    vit_rating: int

    def __init__(self, agi_rating: int, comments: str, description: None, dex_rating: int, flavor: None, hp_rating: int, id: int, lck_rating: int, mnd_rating: int, mp_rating: int, name: str, spd_rating: int, spi_rating: int, str_rating: int, vit_rating: int) -> None:
        self.agi_rating = agi_rating
        self.comments = comments
        self.description = description
        self.dex_rating = dex_rating
        self.flavor = flavor
        self.hp_rating = hp_rating
        self.id = id
        self.lck_rating = lck_rating
        self.mnd_rating = mnd_rating
        self.mp_rating = mp_rating
        self.name = name
        self.spd_rating = spd_rating
        self.spi_rating = spi_rating
        self.str_rating = str_rating
        self.vit_rating = vit_rating

    @staticmethod
    def from_dict(obj: Any) -> 'Actor':
        assert isinstance(obj, dict)
        agi_rating = from_int(obj.get("AgiRating"))
        comments = from_str(obj.get("Comments"))
        description = from_none(obj.get("Description"))
        dex_rating = from_int(obj.get("DexRating"))
        flavor = from_none(obj.get("Flavor"))
        hp_rating = from_int(obj.get("HPRating"))
        id = from_int(obj.get("ID"))
        lck_rating = from_int(obj.get("LckRating"))
        mnd_rating = from_int(obj.get("MndRating"))
        mp_rating = from_int(obj.get("MPRating"))
        name = from_str(obj.get("Name"))
        spd_rating = from_int(obj.get("SpdRating"))
        spi_rating = from_int(obj.get("SpiRating"))
        str_rating = from_int(obj.get("StrRating"))
        vit_rating = from_int(obj.get("VitRating"))
        return Actor(agi_rating, comments, description, dex_rating, flavor, hp_rating, id, lck_rating, mnd_rating, mp_rating, name, spd_rating, spi_rating, str_rating, vit_rating)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AgiRating"] = from_int(self.agi_rating)
        result["Comments"] = from_str(self.comments)
        result["Description"] = from_none(self.description)
        result["DexRating"] = from_int(self.dex_rating)
        result["Flavor"] = from_none(self.flavor)
        result["HPRating"] = from_int(self.hp_rating)
        result["ID"] = from_int(self.id)
        result["LckRating"] = from_int(self.lck_rating)
        result["MndRating"] = from_int(self.mnd_rating)
        result["MPRating"] = from_int(self.mp_rating)
        result["Name"] = from_str(self.name)
        result["SpdRating"] = from_int(self.spd_rating)
        result["SpiRating"] = from_int(self.spi_rating)
        result["StrRating"] = from_int(self.str_rating)
        result["VitRating"] = from_int(self.vit_rating)
        return result


def actor_from_dict(s: Any) -> Actor:
    return Actor.from_dict(s)


def actor_to_dict(x: Actor) -> Any:
    return to_class(Actor, x)
