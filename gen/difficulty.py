from typing import Optional, Any, TypeVar, Type, cast


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Difficulty:
    """A Crystal Project difficulty mode definition.
    This affects enemy stats, mostly.
    By default, it's just Easy, Medium, and Hard.
    """
    boss_hp_rate: int
    """A percentage to multiply all bosses' HP by. Default is 100."""

    boss_mp_rate: int
    """A percentage to multiply all bosses' MP by. Default is 100."""

    comments: Optional[str]
    """A comment for game and mod developers. Not shown in game."""

    description: Optional[str]
    """The English description for this difficulty. Localizable."""

    flavor: Optional[str]
    """Unknown. Seemingly unused?"""

    id: int
    """The ID of this difficulty."""

    is_default: bool
    """Is this the default difficulty?
    Only a single difficulty among all of them should have this be `true`.
    """
    member_hit_chance_mod: int
    """A flat number to add to all players' hit chances. Default is 0."""

    monster_agi_rate: int
    """A percentage to multiply all monster' Agility by. Default is 100."""

    monster_dex_rate: int
    """A percentage to multiply all monster' Dexterity by. Default is 100."""

    monster_hit_chance_mod: int
    """A flat number to add to all monsters' hit chances. Default is 0."""

    monster_hp_rate: int
    """A percentage to multiply all non-bosses' HP by. Default is 100."""

    monster_lck_rate: int
    """A percentage to multiply all monster' Luck by. Default is 100."""

    monster_m_def_rate: int
    """A percentage to multiply all monster' magic defence rate by. Default is 100."""

    monster_mnd_rate: int
    """A percentage to multiply all monster' Mind by. Default is 100."""

    monster_mp_rate: int
    """A percentage to multiply all non-bosses' MP by. Default is 100."""

    monster_p_atk_rate: int
    """A percentage to multiply all monster' physical attack rate by. Default is 100."""

    monster_p_def_rate: int
    """A percentage to multiply all monster' physical defence rate by. Default is 100."""

    monster_spd_rate: int
    """A percentage to multiply all monster' Speed by. Default is 100."""

    monster_spi_rate: int
    """A percentage to multiply all monster' Spirit by. Default is 100."""

    monster_str_rate: int
    """A percentage to multiply all monster' Stregth by. Default is 100."""

    monster_vit_rate: int
    """A percentage to multiply all monster' Vitality by. Default is 100."""

    name: str
    """The English name of this difficulty. Localizable."""

    rating: int
    """A "rating" to use to compare difficulties. (TODO - does this do anything?)"""

    sort_order: int
    """The order this difficulty shows up in the list."""

    def __init__(self, boss_hp_rate: int, boss_mp_rate: int, comments: Optional[str], description: Optional[str], flavor: Optional[str], id: int, is_default: bool, member_hit_chance_mod: int, monster_agi_rate: int, monster_dex_rate: int, monster_hit_chance_mod: int, monster_hp_rate: int, monster_lck_rate: int, monster_m_def_rate: int, monster_mnd_rate: int, monster_mp_rate: int, monster_p_atk_rate: int, monster_p_def_rate: int, monster_spd_rate: int, monster_spi_rate: int, monster_str_rate: int, monster_vit_rate: int, name: str, rating: int, sort_order: int) -> None:
        self.boss_hp_rate = boss_hp_rate
        self.boss_mp_rate = boss_mp_rate
        self.comments = comments
        self.description = description
        self.flavor = flavor
        self.id = id
        self.is_default = is_default
        self.member_hit_chance_mod = member_hit_chance_mod
        self.monster_agi_rate = monster_agi_rate
        self.monster_dex_rate = monster_dex_rate
        self.monster_hit_chance_mod = monster_hit_chance_mod
        self.monster_hp_rate = monster_hp_rate
        self.monster_lck_rate = monster_lck_rate
        self.monster_m_def_rate = monster_m_def_rate
        self.monster_mnd_rate = monster_mnd_rate
        self.monster_mp_rate = monster_mp_rate
        self.monster_p_atk_rate = monster_p_atk_rate
        self.monster_p_def_rate = monster_p_def_rate
        self.monster_spd_rate = monster_spd_rate
        self.monster_spi_rate = monster_spi_rate
        self.monster_str_rate = monster_str_rate
        self.monster_vit_rate = monster_vit_rate
        self.name = name
        self.rating = rating
        self.sort_order = sort_order

    @staticmethod
    def from_dict(obj: Any) -> 'Difficulty':
        assert isinstance(obj, dict)
        boss_hp_rate = from_int(obj.get("BossHPRate"))
        boss_mp_rate = from_int(obj.get("BossMPRate"))
        comments = from_union([from_none, from_str], obj.get("Comments"))
        description = from_union([from_none, from_str], obj.get("Description"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        id = from_int(obj.get("ID"))
        is_default = from_bool(obj.get("IsDefault"))
        member_hit_chance_mod = from_int(obj.get("MemberHitChanceMod"))
        monster_agi_rate = from_int(obj.get("MonsterAgiRate"))
        monster_dex_rate = from_int(obj.get("MonsterDexRate"))
        monster_hit_chance_mod = from_int(obj.get("MonsterHitChanceMod"))
        monster_hp_rate = from_int(obj.get("MonsterHPRate"))
        monster_lck_rate = from_int(obj.get("MonsterLckRate"))
        monster_m_def_rate = from_int(obj.get("MonsterMDefRate"))
        monster_mnd_rate = from_int(obj.get("MonsterMndRate"))
        monster_mp_rate = from_int(obj.get("MonsterMPRate"))
        monster_p_atk_rate = from_int(obj.get("MonsterPAtkRate"))
        monster_p_def_rate = from_int(obj.get("MonsterPDefRate"))
        monster_spd_rate = from_int(obj.get("MonsterSpdRate"))
        monster_spi_rate = from_int(obj.get("MonsterSpiRate"))
        monster_str_rate = from_int(obj.get("MonsterStrRate"))
        monster_vit_rate = from_int(obj.get("MonsterVitRate"))
        name = from_str(obj.get("Name"))
        rating = from_int(obj.get("Rating"))
        sort_order = from_int(obj.get("SortOrder"))
        return Difficulty(boss_hp_rate, boss_mp_rate, comments, description, flavor, id, is_default, member_hit_chance_mod, monster_agi_rate, monster_dex_rate, monster_hit_chance_mod, monster_hp_rate, monster_lck_rate, monster_m_def_rate, monster_mnd_rate, monster_mp_rate, monster_p_atk_rate, monster_p_def_rate, monster_spd_rate, monster_spi_rate, monster_str_rate, monster_vit_rate, name, rating, sort_order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BossHPRate"] = from_int(self.boss_hp_rate)
        result["BossMPRate"] = from_int(self.boss_mp_rate)
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["ID"] = from_int(self.id)
        result["IsDefault"] = from_bool(self.is_default)
        result["MemberHitChanceMod"] = from_int(self.member_hit_chance_mod)
        result["MonsterAgiRate"] = from_int(self.monster_agi_rate)
        result["MonsterDexRate"] = from_int(self.monster_dex_rate)
        result["MonsterHitChanceMod"] = from_int(self.monster_hit_chance_mod)
        result["MonsterHPRate"] = from_int(self.monster_hp_rate)
        result["MonsterLckRate"] = from_int(self.monster_lck_rate)
        result["MonsterMDefRate"] = from_int(self.monster_m_def_rate)
        result["MonsterMndRate"] = from_int(self.monster_mnd_rate)
        result["MonsterMPRate"] = from_int(self.monster_mp_rate)
        result["MonsterPAtkRate"] = from_int(self.monster_p_atk_rate)
        result["MonsterPDefRate"] = from_int(self.monster_p_def_rate)
        result["MonsterSpdRate"] = from_int(self.monster_spd_rate)
        result["MonsterSpiRate"] = from_int(self.monster_spi_rate)
        result["MonsterStrRate"] = from_int(self.monster_str_rate)
        result["MonsterVitRate"] = from_int(self.monster_vit_rate)
        result["Name"] = from_str(self.name)
        result["Rating"] = from_int(self.rating)
        result["SortOrder"] = from_int(self.sort_order)
        return result


def difficulty_from_dict(s: Any) -> Difficulty:
    return Difficulty.from_dict(s)


def difficulty_to_dict(x: Difficulty) -> Any:
    return to_class(Difficulty, x)
