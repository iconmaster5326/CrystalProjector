from typing import Any, Optional, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class StatMod:
    """A stat modifier."""

    tag: int
    """The stat modifier type. TODO - this is an enum with a lot of values!"""

    value1: int
    """A value whose semantics are determined by the tag."""

    value2: int
    """A value whose semantics are determined by the tag."""

    value3: int
    """A value whose semantics are determined by the tag."""

    def __init__(self, tag: int, value1: int, value2: int, value3: int) -> None:
        self.tag = tag
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    @staticmethod
    def from_dict(obj: Any) -> 'StatMod':
        assert isinstance(obj, dict)
        tag = from_int(obj.get("Tag"))
        value1 = from_int(obj.get("Value1"))
        value2 = from_int(obj.get("Value2"))
        value3 = from_int(obj.get("Value3"))
        return StatMod(tag, value1, value2, value3)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Tag"] = from_int(self.tag)
        result["Value1"] = from_int(self.value1)
        result["Value2"] = from_int(self.value2)
        result["Value3"] = from_int(self.value3)
        return result


class Passive:
    """A Crystal Project passive ability definition."""

    comments: Optional[str]
    """Any comments for developers. Does not appear in game."""

    description: Optional[str]
    """Appears after the flavor in the ability text. Localizable."""

    flavor: Optional[str]
    """Appears after the statistical information in the ability text. Localizable."""

    hide_stat_mods_from_description: bool
    """Do we hide the mechanical changes of this ability from the player?"""

    id: int
    """The unique ID of this ability."""

    is_default_locked: bool
    """Is this ability locked by default, needing unlocked by code?"""

    is_innate: bool
    """Is this ability the innate ability of a job?"""

    is_learnable: bool
    """Is this ability learnable by the player?"""

    jp: int
    """The JP cost to unlock this ability."""

    name: str
    """The English name of this ability. Displayed to users. Localizable."""

    pp: int
    """The number of passive points you need to equip this passive."""

    sort_order: int
    """The order this is displayed in the records."""

    stat_mods: List[StatMod]
    """Any stat modifiers this passive ability grants."""

    def __init__(self, comments: Optional[str], description: Optional[str], flavor: Optional[str], hide_stat_mods_from_description: bool, id: int, is_default_locked: bool, is_innate: bool, is_learnable: bool, jp: int, name: str, pp: int, sort_order: int, stat_mods: List[StatMod]) -> None:
        self.comments = comments
        self.description = description
        self.flavor = flavor
        self.hide_stat_mods_from_description = hide_stat_mods_from_description
        self.id = id
        self.is_default_locked = is_default_locked
        self.is_innate = is_innate
        self.is_learnable = is_learnable
        self.jp = jp
        self.name = name
        self.pp = pp
        self.sort_order = sort_order
        self.stat_mods = stat_mods

    @staticmethod
    def from_dict(obj: Any) -> 'Passive':
        assert isinstance(obj, dict)
        comments = from_union([from_none, from_str], obj.get("Comments"))
        description = from_union([from_none, from_str], obj.get("Description"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        hide_stat_mods_from_description = from_bool(obj.get("HideStatModsFromDescription"))
        id = from_int(obj.get("ID"))
        is_default_locked = from_bool(obj.get("IsDefaultLocked"))
        is_innate = from_bool(obj.get("IsInnate"))
        is_learnable = from_bool(obj.get("IsLearnable"))
        jp = from_int(obj.get("JP"))
        name = from_str(obj.get("Name"))
        pp = from_int(obj.get("PP"))
        sort_order = from_int(obj.get("SortOrder"))
        stat_mods = from_list(StatMod.from_dict, obj.get("StatMods"))
        return Passive(comments, description, flavor, hide_stat_mods_from_description, id, is_default_locked, is_innate, is_learnable, jp, name, pp, sort_order, stat_mods)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["HideStatModsFromDescription"] = from_bool(self.hide_stat_mods_from_description)
        result["ID"] = from_int(self.id)
        result["IsDefaultLocked"] = from_bool(self.is_default_locked)
        result["IsInnate"] = from_bool(self.is_innate)
        result["IsLearnable"] = from_bool(self.is_learnable)
        result["JP"] = from_int(self.jp)
        result["Name"] = from_str(self.name)
        result["PP"] = from_int(self.pp)
        result["SortOrder"] = from_int(self.sort_order)
        result["StatMods"] = from_list(lambda x: to_class(StatMod, x), self.stat_mods)
        return result


def passive_from_dict(s: Any) -> Passive:
    return Passive.from_dict(s)


def passive_to_dict(x: Passive) -> Any:
    return to_class(Passive, x)
