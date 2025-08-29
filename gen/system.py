from typing import Any, Optional, List, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


class Achievement:
    """An achievement."""

    description: str
    """The description of the achievement. Localizable."""

    is_hidden: bool
    """Is this achievment initially hidden from the list, until you unlock it?"""

    name: str
    """The name of the achievement. Localizable."""

    def __init__(self, description: str, is_hidden: bool, name: str) -> None:
        self.description = description
        self.is_hidden = is_hidden
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'Achievement':
        assert isinstance(obj, dict)
        description = from_str(obj.get("Description"))
        is_hidden = from_bool(obj.get("IsHidden"))
        name = from_str(obj.get("Name"))
        return Achievement(description, is_hidden, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Description"] = from_str(self.description)
        result["IsHidden"] = from_bool(self.is_hidden)
        result["Name"] = from_str(self.name)
        return result


class BattleConfig:
    """Settings to tweak the combat system."""

    damage_bonus_from_ap_cost_rate: int
    """The rate at which physical damage increases AP cost."""

    dual_wield_p_atk_rate: int
    """The percent extra physical attack when dual-wielding."""

    heal_multi_with_penalty_rate: int
    """The healing multiplier when there are penalties."""

    learn_all_job_zero_jp_abilities: bool
    """Can we learn all abilities for zero JP?"""

    p_dmg_increases_max_hp_absorb_rate: int
    """The rate at which physical damage increases max HP absorb."""

    p_dmg_increases_max_hp_decay_rate: int
    """The rate at which physical damage increases max HP decay."""

    perfect_dodge_at_chance_or_lower: int
    """The cutoff to land a "perfect dodge"."""

    perfect_hit_at_chance_or_higher: int
    """The cutoff to land a "perfect hit"."""

    str_while_unarmed_bonus_flat: int
    """The default bonus to Strength when unarmed."""

    target_single_with_bonus_rate: int
    """The rate at which a single-target attack is multipled when it hits multiple targets."""

    two_handed_p_atk_flat: int
    """The base physical attack damage when using a two-handed weapon."""

    two_handed_p_atk_rate: int
    """The percent extra physical attack when using a two-handed weapon."""

    def __init__(self, damage_bonus_from_ap_cost_rate: int, dual_wield_p_atk_rate: int, heal_multi_with_penalty_rate: int, learn_all_job_zero_jp_abilities: bool, p_dmg_increases_max_hp_absorb_rate: int, p_dmg_increases_max_hp_decay_rate: int, perfect_dodge_at_chance_or_lower: int, perfect_hit_at_chance_or_higher: int, str_while_unarmed_bonus_flat: int, target_single_with_bonus_rate: int, two_handed_p_atk_flat: int, two_handed_p_atk_rate: int) -> None:
        self.damage_bonus_from_ap_cost_rate = damage_bonus_from_ap_cost_rate
        self.dual_wield_p_atk_rate = dual_wield_p_atk_rate
        self.heal_multi_with_penalty_rate = heal_multi_with_penalty_rate
        self.learn_all_job_zero_jp_abilities = learn_all_job_zero_jp_abilities
        self.p_dmg_increases_max_hp_absorb_rate = p_dmg_increases_max_hp_absorb_rate
        self.p_dmg_increases_max_hp_decay_rate = p_dmg_increases_max_hp_decay_rate
        self.perfect_dodge_at_chance_or_lower = perfect_dodge_at_chance_or_lower
        self.perfect_hit_at_chance_or_higher = perfect_hit_at_chance_or_higher
        self.str_while_unarmed_bonus_flat = str_while_unarmed_bonus_flat
        self.target_single_with_bonus_rate = target_single_with_bonus_rate
        self.two_handed_p_atk_flat = two_handed_p_atk_flat
        self.two_handed_p_atk_rate = two_handed_p_atk_rate

    @staticmethod
    def from_dict(obj: Any) -> 'BattleConfig':
        assert isinstance(obj, dict)
        damage_bonus_from_ap_cost_rate = from_int(obj.get("DamageBonusFromAPCostRate"))
        dual_wield_p_atk_rate = from_int(obj.get("DualWieldPAtkRate"))
        heal_multi_with_penalty_rate = from_int(obj.get("HealMultiWithPenaltyRate"))
        learn_all_job_zero_jp_abilities = from_bool(obj.get("LearnAllJobZeroJPAbilities"))
        p_dmg_increases_max_hp_absorb_rate = from_int(obj.get("PDmgIncreasesMaxHPAbsorbRate"))
        p_dmg_increases_max_hp_decay_rate = from_int(obj.get("PDmgIncreasesMaxHPDecayRate"))
        perfect_dodge_at_chance_or_lower = from_int(obj.get("PerfectDodgeAtChanceOrLower"))
        perfect_hit_at_chance_or_higher = from_int(obj.get("PerfectHitAtChanceOrHigher"))
        str_while_unarmed_bonus_flat = from_int(obj.get("StrWhileUnarmedBonusFlat"))
        target_single_with_bonus_rate = from_int(obj.get("TargetSingleWithBonusRate"))
        two_handed_p_atk_flat = from_int(obj.get("TwoHandedPAtkFlat"))
        two_handed_p_atk_rate = from_int(obj.get("TwoHandedPAtkRate"))
        return BattleConfig(damage_bonus_from_ap_cost_rate, dual_wield_p_atk_rate, heal_multi_with_penalty_rate, learn_all_job_zero_jp_abilities, p_dmg_increases_max_hp_absorb_rate, p_dmg_increases_max_hp_decay_rate, perfect_dodge_at_chance_or_lower, perfect_hit_at_chance_or_higher, str_while_unarmed_bonus_flat, target_single_with_bonus_rate, two_handed_p_atk_flat, two_handed_p_atk_rate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DamageBonusFromAPCostRate"] = from_int(self.damage_bonus_from_ap_cost_rate)
        result["DualWieldPAtkRate"] = from_int(self.dual_wield_p_atk_rate)
        result["HealMultiWithPenaltyRate"] = from_int(self.heal_multi_with_penalty_rate)
        result["LearnAllJobZeroJPAbilities"] = from_bool(self.learn_all_job_zero_jp_abilities)
        result["PDmgIncreasesMaxHPAbsorbRate"] = from_int(self.p_dmg_increases_max_hp_absorb_rate)
        result["PDmgIncreasesMaxHPDecayRate"] = from_int(self.p_dmg_increases_max_hp_decay_rate)
        result["PerfectDodgeAtChanceOrLower"] = from_int(self.perfect_dodge_at_chance_or_lower)
        result["PerfectHitAtChanceOrHigher"] = from_int(self.perfect_hit_at_chance_or_higher)
        result["StrWhileUnarmedBonusFlat"] = from_int(self.str_while_unarmed_bonus_flat)
        result["TargetSingleWithBonusRate"] = from_int(self.target_single_with_bonus_rate)
        result["TwoHandedPAtkFlat"] = from_int(self.two_handed_p_atk_flat)
        result["TwoHandedPAtkRate"] = from_int(self.two_handed_p_atk_rate)
        return result


class Bulletin:
    """A piece of Castle Seqouia bulletin dialogue."""

    contents: str
    """The message of this bulletin. Localizable."""

    header: str
    """The title of this bulletin. Localizable."""

    id: int
    """The unique ID of this bulletin."""

    is_number_greater_equal: bool
    """If `true`, `VariableKey` is a numeric variable. Otherwise, it's a flag."""

    rhs: int
    """If `IsNumberGreaterEqual` is `true`, how high does the variable need to be for this
    bulletin to appear?
    """
    variable_key: str
    """The variable to test to see if we should display this bulletin."""

    def __init__(self, contents: str, header: str, id: int, is_number_greater_equal: bool, rhs: int, variable_key: str) -> None:
        self.contents = contents
        self.header = header
        self.id = id
        self.is_number_greater_equal = is_number_greater_equal
        self.rhs = rhs
        self.variable_key = variable_key

    @staticmethod
    def from_dict(obj: Any) -> 'Bulletin':
        assert isinstance(obj, dict)
        contents = from_str(obj.get("Contents"))
        header = from_str(obj.get("Header"))
        id = from_int(obj.get("ID"))
        is_number_greater_equal = from_bool(obj.get("IsNumberGreaterEqual"))
        rhs = from_int(obj.get("RHS"))
        variable_key = from_str(obj.get("VariableKey"))
        return Bulletin(contents, header, id, is_number_greater_equal, rhs, variable_key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Contents"] = from_str(self.contents)
        result["Header"] = from_str(self.header)
        result["ID"] = from_int(self.id)
        result["IsNumberGreaterEqual"] = from_bool(self.is_number_greater_equal)
        result["RHS"] = from_int(self.rhs)
        result["VariableKey"] = from_str(self.variable_key)
        return result


class FieldConfig:
    """Settings to tweak out of combat systems."""

    golden_quintar_jump3: bool
    """Can golden quintars jump 3 blocks?"""

    def __init__(self, golden_quintar_jump3: bool) -> None:
        self.golden_quintar_jump3 = golden_quintar_jump3

    @staticmethod
    def from_dict(obj: Any) -> 'FieldConfig':
        assert isinstance(obj, dict)
        golden_quintar_jump3 = from_bool(obj.get("GoldenQuintarJump3"))
        return FieldConfig(golden_quintar_jump3)

    def to_dict(self) -> dict:
        result: dict = {}
        result["GoldenQuintarJump3"] = from_bool(self.golden_quintar_jump3)
        return result


class MainNpc:
    """A reusable NPC definition."""

    key: str
    """The unique handle for this NPC."""

    name: str
    """The name of this NPC. Localizable."""

    texture_key: str
    """The texture of this NPC.
    First the pack name, then a slash, then the texture name.
    """

    def __init__(self, key: str, name: str, texture_key: str) -> None:
        self.key = key
        self.name = name
        self.texture_key = texture_key

    @staticmethod
    def from_dict(obj: Any) -> 'MainNpc':
        assert isinstance(obj, dict)
        key = from_str(obj.get("Key"))
        name = from_str(obj.get("Name"))
        texture_key = from_str(obj.get("TextureKey"))
        return MainNpc(key, name, texture_key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Key"] = from_str(self.key)
        result["Name"] = from_str(self.name)
        result["TextureKey"] = from_str(self.texture_key)
        return result


class MemberDefault:
    """A starting party member."""

    gender_id: int
    """The ID of the starting gender."""

    job_id: int
    """The ID of the starting job."""

    level: int
    """The starting level."""

    name: Optional[str]
    """The name of the party member."""

    sub_job_id: Optional[int]
    """The ID of the starting sub-job, if any."""

    def __init__(self, gender_id: int, job_id: int, level: int, name: Optional[str], sub_job_id: Optional[int]) -> None:
        self.gender_id = gender_id
        self.job_id = job_id
        self.level = level
        self.name = name
        self.sub_job_id = sub_job_id

    @staticmethod
    def from_dict(obj: Any) -> 'MemberDefault':
        assert isinstance(obj, dict)
        gender_id = from_int(obj.get("GenderID"))
        job_id = from_int(obj.get("JobID"))
        level = from_int(obj.get("Level"))
        name = from_union([from_none, from_str], obj.get("Name"))
        sub_job_id = from_union([from_none, from_int], obj.get("SubJobID"))
        return MemberDefault(gender_id, job_id, level, name, sub_job_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["GenderID"] = from_int(self.gender_id)
        result["JobID"] = from_int(self.job_id)
        result["Level"] = from_int(self.level)
        result["Name"] = from_union([from_none, from_str], self.name)
        result["SubJobID"] = from_union([from_none, from_int], self.sub_job_id)
        return result


class Narration:
    """A piece of narration."""

    contents: str
    """The text of this narration. Localizable."""

    id: int
    """The unique ID of this narration."""

    music_cue: int
    """The ID of a music track ti play during this cutscene."""

    def __init__(self, contents: str, id: int, music_cue: int) -> None:
        self.contents = contents
        self.id = id
        self.music_cue = music_cue

    @staticmethod
    def from_dict(obj: Any) -> 'Narration':
        assert isinstance(obj, dict)
        contents = from_str(obj.get("Contents"))
        id = from_int(obj.get("ID"))
        music_cue = from_int(obj.get("MusicCue"))
        return Narration(contents, id, music_cue)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Contents"] = from_str(self.contents)
        result["ID"] = from_int(self.id)
        result["MusicCue"] = from_int(self.music_cue)
        return result


class RandomizerTree:
    """A prerequisite tree for the randomizer."""

    children: List['RandomizerTree']
    """The items that this item unlocks."""

    id: int
    """The ID of the item/equipment."""

    def __init__(self, children: List['RandomizerTree'], id: int) -> None:
        self.children = children
        self.id = id

    @staticmethod
    def from_dict(obj: Any) -> 'RandomizerTree':
        assert isinstance(obj, dict)
        children = from_list(RandomizerTree.from_dict, obj.get("Children"))
        id = from_int(obj.get("ID"))
        return RandomizerTree(children, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Children"] = from_list(lambda x: to_class(RandomizerTree, x), self.children)
        result["ID"] = from_int(self.id)
        return result


class ItemCount:
    id: int
    """The ID of the item."""

    min: int
    """The minimum amount of the item that must be obtainable."""

    tot: int
    """The total amount of the item that is in the vanilla game."""

    def __init__(self, id: int, min: int, tot: int) -> None:
        self.id = id
        self.min = min
        self.tot = tot

    @staticmethod
    def from_dict(obj: Any) -> 'ItemCount':
        assert isinstance(obj, dict)
        id = from_int(obj.get("ID"))
        min = from_int(obj.get("Min"))
        tot = from_int(obj.get("Tot"))
        return ItemCount(id, min, tot)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ID"] = from_int(self.id)
        result["Min"] = from_int(self.min)
        result["Tot"] = from_int(self.tot)
        return result


class Randomizer:
    """Randomizer information."""

    common_teleport_points: List[int]
    """What teleport point IDs are early-game?"""

    consumable_item_i_ds: List[int]
    """Item IDs to be treated as consumables."""

    equipment_prerequisite_tree: List[RandomizerTree]
    """What equipment IDs, in the vanilla game, are gated behind other items?"""

    exclude_ability_i_ds: List[int]
    """The ability IDs to exclude from randomization."""

    exclude_equipment_i_ds: List[int]
    """The eqipment IDs to exclude from randomization."""

    exclude_item_i_ds: List[int]
    """The item IDs to exclude from randomization."""

    exclude_job_i_ds: List[int]
    """The job IDs to exclude from randomization."""

    exclude_passive_i_ds: List[int]
    """The passive IDs to exclude from randomization."""

    exclude_troop_i_ds: List[int]
    """The troop IDs to exclude from randomization."""

    item_counts: List[ItemCount]
    """How much of certain item IDs needs to generate."""

    item_prerequisite_tree: List[RandomizerTree]
    """What item IDs, in the vanilla game, are gated behind other items?"""

    progression_gate_item_i_ds: List[int]
    """Item IDs that are needed in some amount to get progression items."""

    progression_gate_teleport_points: List[int]
    """What teleport point IDs represent the end of the game?"""

    progression_item_i_ds: List[int]
    """Item IDs that are necesary for progression."""

    progression_troop_i_ds: List[int]
    """The troop IDs that must be beaten to obtain progression items."""

    quest_item_i_ds: List[int]
    """Item IDs that are necesary for quests."""

    recovery_item_i_ds: List[int]
    """Item IDs that are necesary for classes to use in-battle."""

    restricted_teleport_points: List[int]
    """What teleport point IDs are late-game?"""

    valid_teleport_points: List[int]
    """What teleport point IDs should be randomized?"""

    def __init__(self, common_teleport_points: List[int], consumable_item_i_ds: List[int], equipment_prerequisite_tree: List[RandomizerTree], exclude_ability_i_ds: List[int], exclude_equipment_i_ds: List[int], exclude_item_i_ds: List[int], exclude_job_i_ds: List[int], exclude_passive_i_ds: List[int], exclude_troop_i_ds: List[int], item_counts: List[ItemCount], item_prerequisite_tree: List[RandomizerTree], progression_gate_item_i_ds: List[int], progression_gate_teleport_points: List[int], progression_item_i_ds: List[int], progression_troop_i_ds: List[int], quest_item_i_ds: List[int], recovery_item_i_ds: List[int], restricted_teleport_points: List[int], valid_teleport_points: List[int]) -> None:
        self.common_teleport_points = common_teleport_points
        self.consumable_item_i_ds = consumable_item_i_ds
        self.equipment_prerequisite_tree = equipment_prerequisite_tree
        self.exclude_ability_i_ds = exclude_ability_i_ds
        self.exclude_equipment_i_ds = exclude_equipment_i_ds
        self.exclude_item_i_ds = exclude_item_i_ds
        self.exclude_job_i_ds = exclude_job_i_ds
        self.exclude_passive_i_ds = exclude_passive_i_ds
        self.exclude_troop_i_ds = exclude_troop_i_ds
        self.item_counts = item_counts
        self.item_prerequisite_tree = item_prerequisite_tree
        self.progression_gate_item_i_ds = progression_gate_item_i_ds
        self.progression_gate_teleport_points = progression_gate_teleport_points
        self.progression_item_i_ds = progression_item_i_ds
        self.progression_troop_i_ds = progression_troop_i_ds
        self.quest_item_i_ds = quest_item_i_ds
        self.recovery_item_i_ds = recovery_item_i_ds
        self.restricted_teleport_points = restricted_teleport_points
        self.valid_teleport_points = valid_teleport_points

    @staticmethod
    def from_dict(obj: Any) -> 'Randomizer':
        assert isinstance(obj, dict)
        common_teleport_points = from_list(from_int, obj.get("CommonTeleportPoints"))
        consumable_item_i_ds = from_list(from_int, obj.get("ConsumableItemIDs"))
        equipment_prerequisite_tree = from_list(RandomizerTree.from_dict, obj.get("EquipmentPrerequisiteTree"))
        exclude_ability_i_ds = from_list(from_int, obj.get("ExcludeAbilityIDs"))
        exclude_equipment_i_ds = from_list(from_int, obj.get("ExcludeEquipmentIDs"))
        exclude_item_i_ds = from_list(from_int, obj.get("ExcludeItemIDs"))
        exclude_job_i_ds = from_list(from_int, obj.get("ExcludeJobIDs"))
        exclude_passive_i_ds = from_list(from_int, obj.get("ExcludePassiveIDs"))
        exclude_troop_i_ds = from_list(from_int, obj.get("ExcludeTroopIDs"))
        item_counts = from_list(ItemCount.from_dict, obj.get("ItemCounts"))
        item_prerequisite_tree = from_list(RandomizerTree.from_dict, obj.get("ItemPrerequisiteTree"))
        progression_gate_item_i_ds = from_list(from_int, obj.get("ProgressionGateItemIDs"))
        progression_gate_teleport_points = from_list(from_int, obj.get("ProgressionGateTeleportPoints"))
        progression_item_i_ds = from_list(from_int, obj.get("ProgressionItemIDs"))
        progression_troop_i_ds = from_list(from_int, obj.get("ProgressionTroopIDs"))
        quest_item_i_ds = from_list(from_int, obj.get("QuestItemIDs"))
        recovery_item_i_ds = from_list(from_int, obj.get("RecoveryItemIDs"))
        restricted_teleport_points = from_list(from_int, obj.get("RestrictedTeleportPoints"))
        valid_teleport_points = from_list(from_int, obj.get("ValidTeleportPoints"))
        return Randomizer(common_teleport_points, consumable_item_i_ds, equipment_prerequisite_tree, exclude_ability_i_ds, exclude_equipment_i_ds, exclude_item_i_ds, exclude_job_i_ds, exclude_passive_i_ds, exclude_troop_i_ds, item_counts, item_prerequisite_tree, progression_gate_item_i_ds, progression_gate_teleport_points, progression_item_i_ds, progression_troop_i_ds, quest_item_i_ds, recovery_item_i_ds, restricted_teleport_points, valid_teleport_points)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CommonTeleportPoints"] = from_list(from_int, self.common_teleport_points)
        result["ConsumableItemIDs"] = from_list(from_int, self.consumable_item_i_ds)
        result["EquipmentPrerequisiteTree"] = from_list(lambda x: to_class(RandomizerTree, x), self.equipment_prerequisite_tree)
        result["ExcludeAbilityIDs"] = from_list(from_int, self.exclude_ability_i_ds)
        result["ExcludeEquipmentIDs"] = from_list(from_int, self.exclude_equipment_i_ds)
        result["ExcludeItemIDs"] = from_list(from_int, self.exclude_item_i_ds)
        result["ExcludeJobIDs"] = from_list(from_int, self.exclude_job_i_ds)
        result["ExcludePassiveIDs"] = from_list(from_int, self.exclude_passive_i_ds)
        result["ExcludeTroopIDs"] = from_list(from_int, self.exclude_troop_i_ds)
        result["ItemCounts"] = from_list(lambda x: to_class(ItemCount, x), self.item_counts)
        result["ItemPrerequisiteTree"] = from_list(lambda x: to_class(RandomizerTree, x), self.item_prerequisite_tree)
        result["ProgressionGateItemIDs"] = from_list(from_int, self.progression_gate_item_i_ds)
        result["ProgressionGateTeleportPoints"] = from_list(from_int, self.progression_gate_teleport_points)
        result["ProgressionItemIDs"] = from_list(from_int, self.progression_item_i_ds)
        result["ProgressionTroopIDs"] = from_list(from_int, self.progression_troop_i_ds)
        result["QuestItemIDs"] = from_list(from_int, self.quest_item_i_ds)
        result["RecoveryItemIDs"] = from_list(from_int, self.recovery_item_i_ds)
        result["RestrictedTeleportPoints"] = from_list(from_int, self.restricted_teleport_points)
        result["ValidTeleportPoints"] = from_list(from_int, self.valid_teleport_points)
        return result


class StartingLoot:
    """An item given at the start of the game."""

    loot_id: int
    """The item to give. Depends on `LootType`:
    
    - `Nothing`: Invalid.
    - `Item`: The ID of the item.
    - `Equipment`: The ID of the equipment.
    - `Currency`: Always 0.
    """
    loot_quantity: int
    """The amount of this item/currency to give."""

    loot_type: int
    """The type of item given."""

    def __init__(self, loot_id: int, loot_quantity: int, loot_type: int) -> None:
        self.loot_id = loot_id
        self.loot_quantity = loot_quantity
        self.loot_type = loot_type

    @staticmethod
    def from_dict(obj: Any) -> 'StartingLoot':
        assert isinstance(obj, dict)
        loot_id = from_int(obj.get("LootID"))
        loot_quantity = from_int(obj.get("LootQuantity"))
        loot_type = from_int(obj.get("LootType"))
        return StartingLoot(loot_id, loot_quantity, loot_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["LootID"] = from_int(self.loot_id)
        result["LootQuantity"] = from_int(self.loot_quantity)
        result["LootType"] = from_int(self.loot_type)
        return result


class Coord:
    """The location of the teleport point."""

    x: int
    """The X coordinate."""

    y: int
    """The Y coordinate."""

    z: int
    """The Z coordinate."""

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def from_dict(obj: Any) -> 'Coord':
        assert isinstance(obj, dict)
        x = from_int(obj.get("X"))
        y = from_int(obj.get("Y"))
        z = from_int(obj.get("Z"))
        return Coord(x, y, z)

    def to_dict(self) -> dict:
        result: dict = {}
        result["X"] = from_int(self.x)
        result["Y"] = from_int(self.y)
        result["Z"] = from_int(self.z)
        return result


class TeleportPoint:
    """A teleport point."""

    coord: Coord
    """The location of the teleport point."""

    name: str
    """The name of the point. Not shown to players."""

    def __init__(self, coord: Coord, name: str) -> None:
        self.coord = coord
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'TeleportPoint':
        assert isinstance(obj, dict)
        coord = Coord.from_dict(obj.get("Coord"))
        name = from_str(obj.get("Name"))
        return TeleportPoint(coord, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Coord"] = to_class(Coord, self.coord)
        result["Name"] = from_str(self.name)
        return result


class Vocab:
    """Reusable, localizable strings."""

    ability_mod_text: List[str]
    """Descriptions for each ability modifier."""

    allow_new_line_at_any_char: bool
    """Allow automatic newlines anywhere, not just at word boundaries?"""

    element_names: List[str]
    """Descriptions for each element."""

    equipment_names: List[str]
    """Descriptions for each equipment category."""

    equipment_slot_names: List[str]
    """Descriptions for each equipment slot."""

    general: Dict[str, Any]
    """The localization key-value pairs."""

    input_char_field: str
    """The name input grid."""

    new_line_end_list: None
    """Unknown."""

    new_line_start_range_list: None
    """Unknown."""

    rand_names_f: List[str]
    """Random feminine names. For the random name button in new games."""

    rand_names_m: List[str]
    """Random masculine names. For the random name button in new games."""

    stat_mod_text: List[str]
    """Descriptions for each stat modifier."""

    text_replacements: None
    """Unknown."""

    def __init__(self, ability_mod_text: List[str], allow_new_line_at_any_char: bool, element_names: List[str], equipment_names: List[str], equipment_slot_names: List[str], general: Dict[str, Any], input_char_field: str, new_line_end_list: None, new_line_start_range_list: None, rand_names_f: List[str], rand_names_m: List[str], stat_mod_text: List[str], text_replacements: None) -> None:
        self.ability_mod_text = ability_mod_text
        self.allow_new_line_at_any_char = allow_new_line_at_any_char
        self.element_names = element_names
        self.equipment_names = equipment_names
        self.equipment_slot_names = equipment_slot_names
        self.general = general
        self.input_char_field = input_char_field
        self.new_line_end_list = new_line_end_list
        self.new_line_start_range_list = new_line_start_range_list
        self.rand_names_f = rand_names_f
        self.rand_names_m = rand_names_m
        self.stat_mod_text = stat_mod_text
        self.text_replacements = text_replacements

    @staticmethod
    def from_dict(obj: Any) -> 'Vocab':
        assert isinstance(obj, dict)
        ability_mod_text = from_list(from_str, obj.get("AbilityModText"))
        allow_new_line_at_any_char = from_bool(obj.get("AllowNewLineAtAnyChar"))
        element_names = from_list(from_str, obj.get("ElementNames"))
        equipment_names = from_list(from_str, obj.get("EquipmentNames"))
        equipment_slot_names = from_list(from_str, obj.get("EquipmentSlotNames"))
        general = from_dict(lambda x: x, obj.get("General"))
        input_char_field = from_str(obj.get("InputCharField"))
        new_line_end_list = from_none(obj.get("NewLineEndList"))
        new_line_start_range_list = from_none(obj.get("NewLineStartRangeList"))
        rand_names_f = from_list(from_str, obj.get("RandNamesF"))
        rand_names_m = from_list(from_str, obj.get("RandNamesM"))
        stat_mod_text = from_list(from_str, obj.get("StatModText"))
        text_replacements = from_none(obj.get("TextReplacements"))
        return Vocab(ability_mod_text, allow_new_line_at_any_char, element_names, equipment_names, equipment_slot_names, general, input_char_field, new_line_end_list, new_line_start_range_list, rand_names_f, rand_names_m, stat_mod_text, text_replacements)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AbilityModText"] = from_list(from_str, self.ability_mod_text)
        result["AllowNewLineAtAnyChar"] = from_bool(self.allow_new_line_at_any_char)
        result["ElementNames"] = from_list(from_str, self.element_names)
        result["EquipmentNames"] = from_list(from_str, self.equipment_names)
        result["EquipmentSlotNames"] = from_list(from_str, self.equipment_slot_names)
        result["General"] = from_dict(lambda x: x, self.general)
        result["InputCharField"] = from_str(self.input_char_field)
        result["NewLineEndList"] = from_none(self.new_line_end_list)
        result["NewLineStartRangeList"] = from_none(self.new_line_start_range_list)
        result["RandNamesF"] = from_list(from_str, self.rand_names_f)
        result["RandNamesM"] = from_list(from_str, self.rand_names_m)
        result["StatModText"] = from_list(from_str, self.stat_mod_text)
        result["TextReplacements"] = from_none(self.text_replacements)
        return result


class System:
    """Crystal Project top-level system information."""

    achievements: List[Achievement]
    """The achievments for this game."""

    battle_config: BattleConfig
    """Settings to tweak the combat system."""

    bulletin_items: List[Bulletin]
    """The Castle Seqouia bulletin dialogue."""

    comments: str
    """Any comments the developer has left for us. Not seen in-game."""

    credits: str
    """The game's credits. Localizable."""

    field_config: FieldConfig
    """Settings to tweak out of combat systems."""

    main_npcs: List[MainNpc]
    """Reusable NPC definitions."""

    member_defaults: List[MemberDefault]
    """Default information for the starting party."""

    narration_items: List[Narration]
    """The cutscene dialogue."""

    randomizer: Randomizer
    """Randomizer information."""

    starting_loot: List[StartingLoot]
    """The items, equipment, and currency you start with."""

    teleport_points: List[Optional[TeleportPoint]]
    """The game's teleport points.
    More information about these regions can be found in the world data.
    """
    vocab: Vocab
    """Reusable, localizable strings."""

    def __init__(self, achievements: List[Achievement], battle_config: BattleConfig, bulletin_items: List[Bulletin], comments: str, credits: str, field_config: FieldConfig, main_npcs: List[MainNpc], member_defaults: List[MemberDefault], narration_items: List[Narration], randomizer: Randomizer, starting_loot: List[StartingLoot], teleport_points: List[Optional[TeleportPoint]], vocab: Vocab) -> None:
        self.achievements = achievements
        self.battle_config = battle_config
        self.bulletin_items = bulletin_items
        self.comments = comments
        self.credits = credits
        self.field_config = field_config
        self.main_npcs = main_npcs
        self.member_defaults = member_defaults
        self.narration_items = narration_items
        self.randomizer = randomizer
        self.starting_loot = starting_loot
        self.teleport_points = teleport_points
        self.vocab = vocab

    @staticmethod
    def from_dict(obj: Any) -> 'System':
        assert isinstance(obj, dict)
        achievements = from_list(Achievement.from_dict, obj.get("Achievements"))
        battle_config = BattleConfig.from_dict(obj.get("BattleConfig"))
        bulletin_items = from_list(Bulletin.from_dict, obj.get("BulletinItems"))
        comments = from_str(obj.get("Comments"))
        credits = from_str(obj.get("Credits"))
        field_config = FieldConfig.from_dict(obj.get("FieldConfig"))
        main_npcs = from_list(MainNpc.from_dict, obj.get("MainNpcs"))
        member_defaults = from_list(MemberDefault.from_dict, obj.get("MemberDefaults"))
        narration_items = from_list(Narration.from_dict, obj.get("NarrationItems"))
        randomizer = Randomizer.from_dict(obj.get("Randomizer"))
        starting_loot = from_list(StartingLoot.from_dict, obj.get("StartingLoot"))
        teleport_points = from_list(lambda x: from_union([from_none, TeleportPoint.from_dict], x), obj.get("TeleportPoints"))
        vocab = Vocab.from_dict(obj.get("Vocab"))
        return System(achievements, battle_config, bulletin_items, comments, credits, field_config, main_npcs, member_defaults, narration_items, randomizer, starting_loot, teleport_points, vocab)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Achievements"] = from_list(lambda x: to_class(Achievement, x), self.achievements)
        result["BattleConfig"] = to_class(BattleConfig, self.battle_config)
        result["BulletinItems"] = from_list(lambda x: to_class(Bulletin, x), self.bulletin_items)
        result["Comments"] = from_str(self.comments)
        result["Credits"] = from_str(self.credits)
        result["FieldConfig"] = to_class(FieldConfig, self.field_config)
        result["MainNpcs"] = from_list(lambda x: to_class(MainNpc, x), self.main_npcs)
        result["MemberDefaults"] = from_list(lambda x: to_class(MemberDefault, x), self.member_defaults)
        result["NarrationItems"] = from_list(lambda x: to_class(Narration, x), self.narration_items)
        result["Randomizer"] = to_class(Randomizer, self.randomizer)
        result["StartingLoot"] = from_list(lambda x: to_class(StartingLoot, x), self.starting_loot)
        result["TeleportPoints"] = from_list(lambda x: from_union([from_none, lambda x: to_class(TeleportPoint, x)], x), self.teleport_points)
        result["Vocab"] = to_class(Vocab, self.vocab)
        return result


def system_from_dict(s: Any) -> System:
    return System.from_dict(s)


def system_to_dict(x: System) -> Any:
    return to_class(System, x)
