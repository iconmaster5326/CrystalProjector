from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Gender:
    """A Crystal Project gender definition.
    Your gender affects some stat growths as you level.
    By default, there is a gender binary, but with modding, you can gender it up as you
    please.
    """
    appearance: int
    """The index into some variant arrays for player appearance.
    0 for masculine-presenting, 1 for feminine-presenting.
    """
    boost_agi: bool
    """Does this gender boost your Agility?"""

    boost_dex: bool
    """Does this gender boost your Dexterity?"""

    boost_hp: bool
    """Does this gender boost your HP?"""

    boost_lck: bool
    """Does this gender boost your Luck?"""

    boost_mnd: bool
    """Does this gender boost your Mind?"""

    boost_mp: bool
    """Does this gender boost your MP?"""

    boost_spd: bool
    """Does this gender boost your Speed?"""

    boost_spi: bool
    """Does this gender boost your Spirit?"""

    boost_str: bool
    """Does this gender boost your Strength?"""

    boost_vit: bool
    """Does this gender boost your Vitality?"""

    id: int
    """The ID of this gender."""

    name: str
    """The English name of this gender. Localizable."""

    def __init__(self, appearance: int, boost_agi: bool, boost_dex: bool, boost_hp: bool, boost_lck: bool, boost_mnd: bool, boost_mp: bool, boost_spd: bool, boost_spi: bool, boost_str: bool, boost_vit: bool, id: int, name: str) -> None:
        self.appearance = appearance
        self.boost_agi = boost_agi
        self.boost_dex = boost_dex
        self.boost_hp = boost_hp
        self.boost_lck = boost_lck
        self.boost_mnd = boost_mnd
        self.boost_mp = boost_mp
        self.boost_spd = boost_spd
        self.boost_spi = boost_spi
        self.boost_str = boost_str
        self.boost_vit = boost_vit
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'Gender':
        assert isinstance(obj, dict)
        appearance = from_int(obj.get("Appearance"))
        boost_agi = from_bool(obj.get("BoostAgi"))
        boost_dex = from_bool(obj.get("BoostDex"))
        boost_hp = from_bool(obj.get("BoostHP"))
        boost_lck = from_bool(obj.get("BoostLck"))
        boost_mnd = from_bool(obj.get("BoostMnd"))
        boost_mp = from_bool(obj.get("BoostMP"))
        boost_spd = from_bool(obj.get("BoostSpd"))
        boost_spi = from_bool(obj.get("BoostSpi"))
        boost_str = from_bool(obj.get("BoostStr"))
        boost_vit = from_bool(obj.get("BoostVit"))
        id = from_int(obj.get("ID"))
        name = from_str(obj.get("Name"))
        return Gender(appearance, boost_agi, boost_dex, boost_hp, boost_lck, boost_mnd, boost_mp, boost_spd, boost_spi, boost_str, boost_vit, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Appearance"] = from_int(self.appearance)
        result["BoostAgi"] = from_bool(self.boost_agi)
        result["BoostDex"] = from_bool(self.boost_dex)
        result["BoostHP"] = from_bool(self.boost_hp)
        result["BoostLck"] = from_bool(self.boost_lck)
        result["BoostMnd"] = from_bool(self.boost_mnd)
        result["BoostMP"] = from_bool(self.boost_mp)
        result["BoostSpd"] = from_bool(self.boost_spd)
        result["BoostSpi"] = from_bool(self.boost_spi)
        result["BoostStr"] = from_bool(self.boost_str)
        result["BoostVit"] = from_bool(self.boost_vit)
        result["ID"] = from_int(self.id)
        result["Name"] = from_str(self.name)
        return result


def gender_from_dict(s: Any) -> Gender:
    return Gender.from_dict(s)


def gender_to_dict(x: Gender) -> Any:
    return to_class(Gender, x)
