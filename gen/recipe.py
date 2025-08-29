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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Ingredient:
    """An ingredient that is consumed."""

    loot_id: int
    """The input to the craft. Depends on `LootType`:
    
    - `Nothing`: Invalid.
    - `Item`: The ID of the item.
    - `Equipment`: The ID of the equipment.
    - `Currency`: Always 0.
    """
    loot_quantity: int
    """The amount of this item/currency to consume."""

    loot_type: int
    """The type of item that this recipe uses."""

    def __init__(self, loot_id: int, loot_quantity: int, loot_type: int) -> None:
        self.loot_id = loot_id
        self.loot_quantity = loot_quantity
        self.loot_type = loot_type

    @staticmethod
    def from_dict(obj: Any) -> 'Ingredient':
        assert isinstance(obj, dict)
        loot_id = from_int(obj.get("LootID"))
        loot_quantity = from_int(obj.get("LootQuantity"))
        loot_type = from_int(obj.get("LootType"))
        return Ingredient(loot_id, loot_quantity, loot_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["LootID"] = from_int(self.loot_id)
        result["LootQuantity"] = from_int(self.loot_quantity)
        result["LootType"] = from_int(self.loot_type)
        return result


class Recipe:
    """A Crystal Project recipe definition.
    Recipes represent crafting entries done at shops.
    """
    comments: Optional[str]
    """Any comments for developers. Does not appear in game."""

    cost: int
    """The cost of the recipe to make, in copper."""

    description: Optional[str]
    """Unused."""

    flavor: Optional[str]
    """Unused."""

    icon_path: None
    """Unused."""

    id: int
    """The unique ID of this recipe."""

    ingredients: List[Ingredient]
    """The input ingredients to consume."""

    loot_id: int
    """The result of the craft. Depends on `LootType`:
    
    - `Nothing`: Invalid.
    - `Item`: The ID of the item.
    - `Equipment`: The ID of the equipment.
    - `Currency`: Invalid.
    """
    loot_type: int
    """The category of item this produces."""

    name: str
    """The name of this recipe. Not displayed to users."""

    sort_order: int
    """Likely unused."""

    def __init__(self, comments: Optional[str], cost: int, description: Optional[str], flavor: Optional[str], icon_path: None, id: int, ingredients: List[Ingredient], loot_id: int, loot_type: int, name: str, sort_order: int) -> None:
        self.comments = comments
        self.cost = cost
        self.description = description
        self.flavor = flavor
        self.icon_path = icon_path
        self.id = id
        self.ingredients = ingredients
        self.loot_id = loot_id
        self.loot_type = loot_type
        self.name = name
        self.sort_order = sort_order

    @staticmethod
    def from_dict(obj: Any) -> 'Recipe':
        assert isinstance(obj, dict)
        comments = from_union([from_none, from_str], obj.get("Comments"))
        cost = from_int(obj.get("Cost"))
        description = from_union([from_none, from_str], obj.get("Description"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        icon_path = from_none(obj.get("IconPath"))
        id = from_int(obj.get("ID"))
        ingredients = from_list(Ingredient.from_dict, obj.get("Ingredients"))
        loot_id = from_int(obj.get("LootID"))
        loot_type = from_int(obj.get("LootType"))
        name = from_str(obj.get("Name"))
        sort_order = from_int(obj.get("SortOrder"))
        return Recipe(comments, cost, description, flavor, icon_path, id, ingredients, loot_id, loot_type, name, sort_order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["Cost"] = from_int(self.cost)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["IconPath"] = from_none(self.icon_path)
        result["ID"] = from_int(self.id)
        result["Ingredients"] = from_list(lambda x: to_class(Ingredient, x), self.ingredients)
        result["LootID"] = from_int(self.loot_id)
        result["LootType"] = from_int(self.loot_type)
        result["Name"] = from_str(self.name)
        result["SortOrder"] = from_int(self.sort_order)
        return result


def recipe_from_dict(s: Any) -> Recipe:
    return Recipe.from_dict(s)


def recipe_to_dict(x: Recipe) -> Any:
    return to_class(Recipe, x)
