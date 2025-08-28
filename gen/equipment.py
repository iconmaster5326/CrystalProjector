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


class Equipment:
    """A Crystal Project equipment definition."""

    comments: Optional[str]
    """A comment for game and mod developers. Not shown in game."""

    cost: int
    """The cost of the item, in copper."""

    description: Optional[str]
    """Appears after the flavor in the item text. Localizable."""

    equipment_type: int
    """The equip slot this equipment goes into, the type of weapon, and the category of the
    armor.
    """
    flavor: Optional[str]
    """Any additional text shown to the player after its effects. Localizable."""

    hide_stat_mods_from_description: bool
    """Do we hide the exact mechanical effects from the players?"""

    id: int
    """The ID of this equipment."""

    is_one_only: bool
    """Can you only have one of this equipped?"""

    is_two_handed: bool
    """Does this weapon take up both hand slots? Has no meaning for non-weapons, probably."""

    level: int
    """The expected level at which you aquire this item.
    Used in things like the randomizer, to scale stats.
    """
    max_capacity: int
    """The maximum amount of this item you can hold (without pouches). 0 means unlimited."""

    name: str
    """The English name of this equipment. Localizable."""

    no_auto_cost: bool
    """Skip scaling the cost when changing the level of the item in the randomizer?"""

    no_auto_stats: bool
    """Skip scaling the stats when changing the level of the item in the randomizer?"""

    prevent_auto_equip: bool
    """Is this item unsuitable for auto-equip?"""

    scaled_order: int
    """The order to sort this in, when the "Approx. Power" sorting option is selected. Also
    affects auto-equip.
    """
    sort_order: int
    """The order to sort this in, in places like the inventory and the records."""

    stat_mods: List[StatMod]
    """What stat modifiers this item grants on equip."""

    texture_index: int
    """The index into the texture for the icon.
    Item icons are 18x18 pixels,
    and go from left to right and then top to bottom.
    """
    texture_path: str
    """The item icon. The texture pack, followed by a slash, followed by the texture name."""

    def __init__(self, comments: Optional[str], cost: int, description: Optional[str], equipment_type: int, flavor: Optional[str], hide_stat_mods_from_description: bool, id: int, is_one_only: bool, is_two_handed: bool, level: int, max_capacity: int, name: str, no_auto_cost: bool, no_auto_stats: bool, prevent_auto_equip: bool, scaled_order: int, sort_order: int, stat_mods: List[StatMod], texture_index: int, texture_path: str) -> None:
        self.comments = comments
        self.cost = cost
        self.description = description
        self.equipment_type = equipment_type
        self.flavor = flavor
        self.hide_stat_mods_from_description = hide_stat_mods_from_description
        self.id = id
        self.is_one_only = is_one_only
        self.is_two_handed = is_two_handed
        self.level = level
        self.max_capacity = max_capacity
        self.name = name
        self.no_auto_cost = no_auto_cost
        self.no_auto_stats = no_auto_stats
        self.prevent_auto_equip = prevent_auto_equip
        self.scaled_order = scaled_order
        self.sort_order = sort_order
        self.stat_mods = stat_mods
        self.texture_index = texture_index
        self.texture_path = texture_path

    @staticmethod
    def from_dict(obj: Any) -> 'Equipment':
        assert isinstance(obj, dict)
        comments = from_union([from_none, from_str], obj.get("Comments"))
        cost = from_int(obj.get("Cost"))
        description = from_union([from_none, from_str], obj.get("Description"))
        equipment_type = from_int(obj.get("EquipmentType"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        hide_stat_mods_from_description = from_bool(obj.get("HideStatModsFromDescription"))
        id = from_int(obj.get("ID"))
        is_one_only = from_bool(obj.get("IsOneOnly"))
        is_two_handed = from_bool(obj.get("IsTwoHanded"))
        level = from_int(obj.get("Level"))
        max_capacity = from_int(obj.get("MaxCapacity"))
        name = from_str(obj.get("Name"))
        no_auto_cost = from_bool(obj.get("NoAutoCost"))
        no_auto_stats = from_bool(obj.get("NoAutoStats"))
        prevent_auto_equip = from_bool(obj.get("PreventAutoEquip"))
        scaled_order = from_int(obj.get("ScaledOrder"))
        sort_order = from_int(obj.get("SortOrder"))
        stat_mods = from_list(StatMod.from_dict, obj.get("StatMods"))
        texture_index = from_int(obj.get("TextureIndex"))
        texture_path = from_str(obj.get("TexturePath"))
        return Equipment(comments, cost, description, equipment_type, flavor, hide_stat_mods_from_description, id, is_one_only, is_two_handed, level, max_capacity, name, no_auto_cost, no_auto_stats, prevent_auto_equip, scaled_order, sort_order, stat_mods, texture_index, texture_path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["Cost"] = from_int(self.cost)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["EquipmentType"] = from_int(self.equipment_type)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["HideStatModsFromDescription"] = from_bool(self.hide_stat_mods_from_description)
        result["ID"] = from_int(self.id)
        result["IsOneOnly"] = from_bool(self.is_one_only)
        result["IsTwoHanded"] = from_bool(self.is_two_handed)
        result["Level"] = from_int(self.level)
        result["MaxCapacity"] = from_int(self.max_capacity)
        result["Name"] = from_str(self.name)
        result["NoAutoCost"] = from_bool(self.no_auto_cost)
        result["NoAutoStats"] = from_bool(self.no_auto_stats)
        result["PreventAutoEquip"] = from_bool(self.prevent_auto_equip)
        result["ScaledOrder"] = from_int(self.scaled_order)
        result["SortOrder"] = from_int(self.sort_order)
        result["StatMods"] = from_list(lambda x: to_class(StatMod, x), self.stat_mods)
        result["TextureIndex"] = from_int(self.texture_index)
        result["TexturePath"] = from_str(self.texture_path)
        return result


def equipment_from_dict(s: Any) -> Equipment:
    return Equipment.from_dict(s)


def equipment_to_dict(x: Equipment) -> Any:
    return to_class(Equipment, x)
