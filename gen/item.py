from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Item:
    """A Crystal Project item definition.
    This does NOT cover equipment items, those are a separate category!
    """
    ability_id: Optional[int]
    """The ID of the ability that is used when you use this item."""

    auto_lost_and_found: bool
    """Does this item go to the lost and found store automatically?"""

    comments: Optional[str]
    """A comment for game and mod developers. Not shown in game."""

    cost: int
    """The cost of the item, in copper."""

    description: Optional[str]
    """Appears after the flavor in the item text. Localizable."""

    flavor: Optional[str]
    """Any additional text shown to the player after its effects. Localizable."""

    id: int
    """The ID of this item."""

    increase_max_capacity_by: Optional[int]
    """The amount of that this pouch increases the maxmimum count by."""

    increase_max_capacity_for_item_id: Optional[int]
    """The ID of the the item that this item is a pouch for."""

    is_combat: bool
    """Is this item usable in combat?"""

    is_consumable: bool
    """Is this item consumed when used?"""

    is_sellable: bool
    """Can this item be sold?"""

    location_biome_id: Optional[int]
    """The ID of the biome this item first appears in.
    You can lie about this if you'd like.
    Used for the records view.
    """
    map_for_biome_id: Optional[int]
    """The ID of the biome of the map this item unlocks whil you hold it."""

    max_capacity: int
    """The maximum amount of this item you can hold (without pouches). 0 means unlimited."""

    name: str
    """The English name of this item. Localizable."""

    scaled_order: int
    """The order to sort this in, when the "Approx. Power" sorting option is selected."""

    sort_order: int
    """The order to sort this in, in places like the inventory and the records."""

    special_bonus: int
    """The special property this item has, if any.
    Used for Skeleton Key, Babel Quintar, and Treasure Finder.
    """
    texture_index: int
    """The index into the texture for the icon.
    Item icons are 18x18 pixels,
    and go from left to right and then top to bottom.
    """
    texture_path: str
    """The item icon. The texture pack, followed by a slash, followed by the texture name."""

    def __init__(self, ability_id: Optional[int], auto_lost_and_found: bool, comments: Optional[str], cost: int, description: Optional[str], flavor: Optional[str], id: int, increase_max_capacity_by: Optional[int], increase_max_capacity_for_item_id: Optional[int], is_combat: bool, is_consumable: bool, is_sellable: bool, location_biome_id: Optional[int], map_for_biome_id: Optional[int], max_capacity: int, name: str, scaled_order: int, sort_order: int, special_bonus: int, texture_index: int, texture_path: str) -> None:
        self.ability_id = ability_id
        self.auto_lost_and_found = auto_lost_and_found
        self.comments = comments
        self.cost = cost
        self.description = description
        self.flavor = flavor
        self.id = id
        self.increase_max_capacity_by = increase_max_capacity_by
        self.increase_max_capacity_for_item_id = increase_max_capacity_for_item_id
        self.is_combat = is_combat
        self.is_consumable = is_consumable
        self.is_sellable = is_sellable
        self.location_biome_id = location_biome_id
        self.map_for_biome_id = map_for_biome_id
        self.max_capacity = max_capacity
        self.name = name
        self.scaled_order = scaled_order
        self.sort_order = sort_order
        self.special_bonus = special_bonus
        self.texture_index = texture_index
        self.texture_path = texture_path

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        ability_id = from_union([from_none, from_int], obj.get("AbilityID"))
        auto_lost_and_found = from_bool(obj.get("AutoLostAndFound"))
        comments = from_union([from_none, from_str], obj.get("Comments"))
        cost = from_int(obj.get("Cost"))
        description = from_union([from_none, from_str], obj.get("Description"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        id = from_int(obj.get("ID"))
        increase_max_capacity_by = from_union([from_none, from_int], obj.get("IncreaseMaxCapacityBy"))
        increase_max_capacity_for_item_id = from_union([from_none, from_int], obj.get("IncreaseMaxCapacityForItemID"))
        is_combat = from_bool(obj.get("IsCombat"))
        is_consumable = from_bool(obj.get("IsConsumable"))
        is_sellable = from_bool(obj.get("IsSellable"))
        location_biome_id = from_union([from_none, from_int], obj.get("LocationBiomeID"))
        map_for_biome_id = from_union([from_none, from_int], obj.get("MapForBiomeID"))
        max_capacity = from_int(obj.get("MaxCapacity"))
        name = from_str(obj.get("Name"))
        scaled_order = from_int(obj.get("ScaledOrder"))
        sort_order = from_int(obj.get("SortOrder"))
        special_bonus = from_int(obj.get("SpecialBonus"))
        texture_index = from_int(obj.get("TextureIndex"))
        texture_path = from_str(obj.get("TexturePath"))
        return Item(ability_id, auto_lost_and_found, comments, cost, description, flavor, id, increase_max_capacity_by, increase_max_capacity_for_item_id, is_combat, is_consumable, is_sellable, location_biome_id, map_for_biome_id, max_capacity, name, scaled_order, sort_order, special_bonus, texture_index, texture_path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AbilityID"] = from_union([from_none, from_int], self.ability_id)
        result["AutoLostAndFound"] = from_bool(self.auto_lost_and_found)
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["Cost"] = from_int(self.cost)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["ID"] = from_int(self.id)
        result["IncreaseMaxCapacityBy"] = from_union([from_none, from_int], self.increase_max_capacity_by)
        result["IncreaseMaxCapacityForItemID"] = from_union([from_none, from_int], self.increase_max_capacity_for_item_id)
        result["IsCombat"] = from_bool(self.is_combat)
        result["IsConsumable"] = from_bool(self.is_consumable)
        result["IsSellable"] = from_bool(self.is_sellable)
        result["LocationBiomeID"] = from_union([from_none, from_int], self.location_biome_id)
        result["MapForBiomeID"] = from_union([from_none, from_int], self.map_for_biome_id)
        result["MaxCapacity"] = from_int(self.max_capacity)
        result["Name"] = from_str(self.name)
        result["ScaledOrder"] = from_int(self.scaled_order)
        result["SortOrder"] = from_int(self.sort_order)
        result["SpecialBonus"] = from_int(self.special_bonus)
        result["TextureIndex"] = from_int(self.texture_index)
        result["TexturePath"] = from_str(self.texture_path)
        return result


def item_from_dict(s: Any) -> Item:
    return Item.from_dict(s)


def item_to_dict(x: Item) -> Any:
    return to_class(Item, x)
