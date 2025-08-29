from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class TroopMember:
    """A monster in this troop."""

    begin_battle_dead: bool
    """Does this monster start the battle dead?"""

    monster_id: int
    """The ID of a monster."""

    pos_x: float
    """The X offset on the screen where this monster appears."""

    pos_y: float
    """The Y offset on the screen where this monster appears."""

    pos_z: float
    """The Z offset on the screen where this monster appears."""

    def __init__(self, begin_battle_dead: bool, monster_id: int, pos_x: float, pos_y: float, pos_z: float) -> None:
        self.begin_battle_dead = begin_battle_dead
        self.monster_id = monster_id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z

    @staticmethod
    def from_dict(obj: Any) -> 'TroopMember':
        assert isinstance(obj, dict)
        begin_battle_dead = from_bool(obj.get("BeginBattleDead"))
        monster_id = from_int(obj.get("MonsterID"))
        pos_x = from_float(obj.get("PosX"))
        pos_y = from_float(obj.get("PosY"))
        pos_z = from_float(obj.get("PosZ"))
        return TroopMember(begin_battle_dead, monster_id, pos_x, pos_y, pos_z)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BeginBattleDead"] = from_bool(self.begin_battle_dead)
        result["MonsterID"] = from_int(self.monster_id)
        result["PosX"] = to_float(self.pos_x)
        result["PosY"] = to_float(self.pos_y)
        result["PosZ"] = to_float(self.pos_z)
        return result


class Troop:
    """A Crystal Project troop definition.
    A troop is a set of enemies to battle.
    """
    id: int
    """The unique ID of this troop."""

    members: List[TroopMember]
    """The monsters in this troop."""

    name: str
    """The name of this troop. Not seen in gameplay."""

    scaled_order: int
    """The order to sort this in, when the "Approx. Power" sorting option is selected.
    Likely unused. Might be used in the randomizer?
    """
    sort_order: int
    """The order to sort this in. Likely unused."""

    def __init__(self, id: int, members: List[TroopMember], name: str, scaled_order: int, sort_order: int) -> None:
        self.id = id
        self.members = members
        self.name = name
        self.scaled_order = scaled_order
        self.sort_order = sort_order

    @staticmethod
    def from_dict(obj: Any) -> 'Troop':
        assert isinstance(obj, dict)
        id = from_int(obj.get("ID"))
        members = from_list(TroopMember.from_dict, obj.get("Members"))
        name = from_str(obj.get("Name"))
        scaled_order = from_int(obj.get("ScaledOrder"))
        sort_order = from_int(obj.get("SortOrder"))
        return Troop(id, members, name, scaled_order, sort_order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ID"] = from_int(self.id)
        result["Members"] = from_list(lambda x: to_class(TroopMember, x), self.members)
        result["Name"] = from_str(self.name)
        result["ScaledOrder"] = from_int(self.scaled_order)
        result["SortOrder"] = from_int(self.sort_order)
        return result


def troop_from_dict(s: Any) -> Troop:
    return Troop.from_dict(s)


def troop_to_dict(x: Troop) -> Any:
    return to_class(Troop, x)
