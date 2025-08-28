from typing import List, Optional, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


class Condition:
    """A condition."""

    cond_eval: int
    """The operator to use.
    Only used in certain condition categories.
    Only matters if `CondGroup` is `N/A`.
    """
    cond_group: int
    """The boolean operator to combine sub-conditions with."""

    cond_var: int
    """The category of condition.
    Only matters if `CondGroup` is `N/A`.
    TODO - this is a big enum!
    """
    data1: int
    """The ID to test a property of.
    Only used in certain condition categories.
    Only matters if `CondGroup` is `N/A`.
    """
    condition_not: bool
    """Invert this condition?
    Only used in certain condition categories.
    Only matters if `CondGroup` is `N/A`.
    """
    sub_conds: Optional[List['Condition']]
    """Any sub-conditions.
    `null` if `CondGroup` is `N/A`.
    """
    value: int
    """The constant value to test against.
    Only used in certain condition categories.
    Only matters if `CondGroup` is `N/A`.
    """

    def __init__(self, cond_eval: int, cond_group: int, cond_var: int, data1: int, condition_not: bool, sub_conds: Optional[List['Condition']], value: int) -> None:
        self.cond_eval = cond_eval
        self.cond_group = cond_group
        self.cond_var = cond_var
        self.data1 = data1
        self.condition_not = condition_not
        self.sub_conds = sub_conds
        self.value = value

    @staticmethod
    def from_dict(obj: Any) -> 'Condition':
        assert isinstance(obj, dict)
        cond_eval = from_int(obj.get("CondEval"))
        cond_group = from_int(obj.get("CondGroup"))
        cond_var = from_int(obj.get("CondVar"))
        data1 = from_int(obj.get("Data1"))
        condition_not = from_bool(obj.get("Not"))
        sub_conds = from_union([from_none, lambda x: from_list(Condition.from_dict, x)], obj.get("SubConds"))
        value = from_int(obj.get("Value"))
        return Condition(cond_eval, cond_group, cond_var, data1, condition_not, sub_conds, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CondEval"] = from_int(self.cond_eval)
        result["CondGroup"] = from_int(self.cond_group)
        result["CondVar"] = from_int(self.cond_var)
        result["Data1"] = from_int(self.data1)
        result["Not"] = from_bool(self.condition_not)
        result["SubConds"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Condition, x), x)], self.sub_conds)
        result["Value"] = from_int(self.value)
        return result


class Action:
    """An entry in the AI table of this monster."""

    ability_id: int
    """The ID of the ability to use if the condition is met."""

    ally_monster_id_filter: Optional[int]
    """What allies should we only use this ability on?"""

    apply_monster_id_filter_to_conds: bool
    """Apply `AllyMonsterIDFilter` while calculating the condition?"""

    apply_monster_id_filter_to_targets: bool
    """Apply `AllyMonsterIDFilter` while calculating the targets?"""

    conds: List[Condition]
    """The conditions under which this ability can be used."""

    dialogue: Optional[str]
    """The message that appears when `HasDialogue` is `true`."""

    has_dialogue: bool
    """Does using this ability make a message pop up?"""

    priority: int
    """The priority of this ability.
    Higher means it will be checked first.
    """
    target_type_override: Optional[int]
    """Override the targets of the ability? If so, to what?"""

    weight: int
    """The chance to use this ability,
    for randomly selecting between multiple valid table entries.
    """

    def __init__(self, ability_id: int, ally_monster_id_filter: Optional[int], apply_monster_id_filter_to_conds: bool, apply_monster_id_filter_to_targets: bool, conds: List[Condition], dialogue: Optional[str], has_dialogue: bool, priority: int, target_type_override: Optional[int], weight: int) -> None:
        self.ability_id = ability_id
        self.ally_monster_id_filter = ally_monster_id_filter
        self.apply_monster_id_filter_to_conds = apply_monster_id_filter_to_conds
        self.apply_monster_id_filter_to_targets = apply_monster_id_filter_to_targets
        self.conds = conds
        self.dialogue = dialogue
        self.has_dialogue = has_dialogue
        self.priority = priority
        self.target_type_override = target_type_override
        self.weight = weight

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        assert isinstance(obj, dict)
        ability_id = from_int(obj.get("AbilityID"))
        ally_monster_id_filter = from_union([from_none, from_int], obj.get("AllyMonsterIDFilter"))
        apply_monster_id_filter_to_conds = from_bool(obj.get("ApplyMonsterIDFilterToConds"))
        apply_monster_id_filter_to_targets = from_bool(obj.get("ApplyMonsterIDFilterToTargets"))
        conds = from_list(Condition.from_dict, obj.get("Conds"))
        dialogue = from_union([from_none, from_str], obj.get("Dialogue"))
        has_dialogue = from_bool(obj.get("HasDialogue"))
        priority = from_int(obj.get("Priority"))
        target_type_override = from_union([from_none, from_int], obj.get("TargetTypeOverride"))
        weight = from_int(obj.get("Weight"))
        return Action(ability_id, ally_monster_id_filter, apply_monster_id_filter_to_conds, apply_monster_id_filter_to_targets, conds, dialogue, has_dialogue, priority, target_type_override, weight)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AbilityID"] = from_int(self.ability_id)
        result["AllyMonsterIDFilter"] = from_union([from_none, from_int], self.ally_monster_id_filter)
        result["ApplyMonsterIDFilterToConds"] = from_bool(self.apply_monster_id_filter_to_conds)
        result["ApplyMonsterIDFilterToTargets"] = from_bool(self.apply_monster_id_filter_to_targets)
        result["Conds"] = from_list(lambda x: to_class(Condition, x), self.conds)
        result["Dialogue"] = from_union([from_none, from_str], self.dialogue)
        result["HasDialogue"] = from_bool(self.has_dialogue)
        result["Priority"] = from_int(self.priority)
        result["TargetTypeOverride"] = from_union([from_none, from_int], self.target_type_override)
        result["Weight"] = from_int(self.weight)
        return result


class DropTableEntry:
    """A possible item drop."""

    equipment_id: int
    """The ID of the item, if `LootType` is `Equipment`. 0 otherwise."""

    item_id: int
    """The ID of the item, if `LootType` is `Item`. 0 otherwise."""

    loot_chance: int
    """The chance, between 0 and 100, of this item dropping,
    or the chance of this item being present to steal.
    """
    loot_type: int
    """The category of item in this table."""

    max_loot_count: int
    """If you have more than this amount of this item, then it won't drop further.
    0 disables this feature. Only applies with drops, not steals!
    """
    steal_chance: int
    """The chance, between 0 and 100, that you successfully steal this item."""

    def __init__(self, equipment_id: int, item_id: int, loot_chance: int, loot_type: int, max_loot_count: int, steal_chance: int) -> None:
        self.equipment_id = equipment_id
        self.item_id = item_id
        self.loot_chance = loot_chance
        self.loot_type = loot_type
        self.max_loot_count = max_loot_count
        self.steal_chance = steal_chance

    @staticmethod
    def from_dict(obj: Any) -> 'DropTableEntry':
        assert isinstance(obj, dict)
        equipment_id = from_int(obj.get("EquipmentID"))
        item_id = from_int(obj.get("ItemID"))
        loot_chance = from_int(obj.get("LootChance"))
        loot_type = from_int(obj.get("LootType"))
        max_loot_count = from_int(obj.get("MaxLootCount"))
        steal_chance = from_int(obj.get("StealChance"))
        return DropTableEntry(equipment_id, item_id, loot_chance, loot_type, max_loot_count, steal_chance)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EquipmentID"] = from_int(self.equipment_id)
        result["ItemID"] = from_int(self.item_id)
        result["LootChance"] = from_int(self.loot_chance)
        result["LootType"] = from_int(self.loot_type)
        result["MaxLootCount"] = from_int(self.max_loot_count)
        result["StealChance"] = from_int(self.steal_chance)
        return result


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


class Monster:
    """A Crystal Project job definition."""

    actions: List[Action]
    """The AI of this monster."""

    agi: int
    """The base Agility of this monster."""

    attack_animation_id: Optional[int]
    """The ID of this monster's basic attack, if it has any.
    Only matters when `IsPVP` is `false`.
    """
    avg_pop: int
    """Unknown."""

    category: int
    """Unknown."""

    comments: Optional[str]
    """A comment for game and mod developers. Not shown in game."""

    description: Optional[str]
    """Seemingly unused."""

    dex: int
    """The base Dexterity of this monster."""

    exp: int
    """The XP this monster gives at the end of a battle."""

    flavor: Optional[str]
    """Seemingly unused."""

    has_breathing: bool
    """Does this monster use the "breathing" animation?
    Only matters when `IsPVP` is `false`.
    """
    has_shadow: bool
    """Does this monster cast a shadow?
    Only matters when `IsPVP` is `false`.
    """
    hp: int
    """The base HP of this monster."""

    id: int
    """The ID of this monster."""

    is_boss: bool
    """Is this considered a boss?"""

    is_pvp: bool
    """Is this a "fake PC" monster?"""

    item_drops: List[DropTableEntry]
    """The items this monster can drop."""

    item_steals: List[DropTableEntry]
    """The items this monster can have on them to steal."""

    jp: int
    """The JP this monster gives at the end of a battle."""

    lck: int
    """The base Luck of this monster."""

    level: int
    """The level of the monster.
    Does not affect stats directly, but is shown to players,
    and is used in the randomizer to scale stats.
    """
    location_biome_id: Optional[int]
    """The ID of the biome this mosnter first appears in.
    You can lie about this if you'd like.
    """
    m_def: int
    """The base magical defence of this monster."""

    mnd: int
    """The base Mind of this monster."""

    money: int
    """The amount of currency this monster drops, in copper."""

    mp: int
    """The base MP of this monster."""

    m_pen: int
    """The base magical defence penetration of this monster."""

    name: str
    """The English name of this monster. Localizable."""

    no_auto: bool
    """Unknown."""

    p_acc_rating: int
    """The base physical accuracy rating of this monster."""

    p_atk: int
    """The base physical attack of this monster."""

    p_crit_chance: int
    """The base physical critical hit chance of this monster."""

    p_crit_dmg: int
    """The base pyhsical critical hit damage bonus of this monster."""

    p_def: int
    """The base physical defence of this monster."""

    p_eva_rating: int
    """The base physical evasion rating of this monster."""

    p_pen: int
    """The base physical defence penetration of this monster."""

    p_variance: int
    """The base physical damage variance of this monster."""

    pvp_gender_id: int
    """The ID of this "fake PC's" gender.
    Only matters when `IsPVP` is `true`.
    """
    pvp_job_id: int
    """The ID of this "fake PC's" job.
    Only matters when `IsPVP` is `true`.
    """
    pvp_texture_type: int
    """Whether or not to use the `Alt` texture of the "fake PC".
    Only matters when `IsPVP` is `true`.
    """
    pvp_weapon_id: Optional[int]
    """The ID of this "fake PC's" held weapon, if any.
    Only matters when `IsPVP` is `true`.
    """
    sort_order: int
    """The order to sort this in, in places like the records."""

    spd: int
    """The base Speed of this monster."""

    spi: int
    """The base Spirit of this monster."""

    stat_mods: List[StatMod]
    """The stat modifiers this monster has."""

    monster_str: int
    """The base Strength of this monster."""

    texture_bubble_x: int
    """The X coordinate in the sprite of where the cursor should point to when selected.
    Only matters when `IsPVP` is `false`.
    """
    texture_bubble_y: int
    """The Y coordinate in the sprite of where the cursor should point to when selected.
    Only matters when `IsPVP` is `false`.
    """
    texture_focus_x: int
    """The X coordinate in the sprite of the zoomed-in portrait of the enemy.
    Used in the bottom turn tracker in combat.
    Only matters when `IsPVP` is `false`.
    """
    texture_focus_y: int
    """The Y coordinate in the sprite of the zoomed-in portrait of the enemy.
    Used in the bottom turn tracker in combat.
    Only matters when `IsPVP` is `false`.
    """
    texture_path: Optional[str]
    """The monster's sprite.
    The texture pack, followed by a slash, followed by the texture name.
    Only matters when `IsPVP` is `false`.
    """
    texture_path_alt: Optional[str]
    """The monster's sprite if the profanity filter is on.
    The texture pack, followed by a slash, followed by the texture name.
    Only matters when `IsPVP` is `false`.
    """
    vit: int
    """The base Vitality of this monster."""

    def __init__(self, actions: List[Action], agi: int, attack_animation_id: Optional[int], avg_pop: int, category: int, comments: Optional[str], description: Optional[str], dex: int, exp: int, flavor: Optional[str], has_breathing: bool, has_shadow: bool, hp: int, id: int, is_boss: bool, is_pvp: bool, item_drops: List[DropTableEntry], item_steals: List[DropTableEntry], jp: int, lck: int, level: int, location_biome_id: Optional[int], m_def: int, mnd: int, money: int, mp: int, m_pen: int, name: str, no_auto: bool, p_acc_rating: int, p_atk: int, p_crit_chance: int, p_crit_dmg: int, p_def: int, p_eva_rating: int, p_pen: int, p_variance: int, pvp_gender_id: int, pvp_job_id: int, pvp_texture_type: int, pvp_weapon_id: Optional[int], sort_order: int, spd: int, spi: int, stat_mods: List[StatMod], monster_str: int, texture_bubble_x: int, texture_bubble_y: int, texture_focus_x: int, texture_focus_y: int, texture_path: Optional[str], texture_path_alt: Optional[str], vit: int) -> None:
        self.actions = actions
        self.agi = agi
        self.attack_animation_id = attack_animation_id
        self.avg_pop = avg_pop
        self.category = category
        self.comments = comments
        self.description = description
        self.dex = dex
        self.exp = exp
        self.flavor = flavor
        self.has_breathing = has_breathing
        self.has_shadow = has_shadow
        self.hp = hp
        self.id = id
        self.is_boss = is_boss
        self.is_pvp = is_pvp
        self.item_drops = item_drops
        self.item_steals = item_steals
        self.jp = jp
        self.lck = lck
        self.level = level
        self.location_biome_id = location_biome_id
        self.m_def = m_def
        self.mnd = mnd
        self.money = money
        self.mp = mp
        self.m_pen = m_pen
        self.name = name
        self.no_auto = no_auto
        self.p_acc_rating = p_acc_rating
        self.p_atk = p_atk
        self.p_crit_chance = p_crit_chance
        self.p_crit_dmg = p_crit_dmg
        self.p_def = p_def
        self.p_eva_rating = p_eva_rating
        self.p_pen = p_pen
        self.p_variance = p_variance
        self.pvp_gender_id = pvp_gender_id
        self.pvp_job_id = pvp_job_id
        self.pvp_texture_type = pvp_texture_type
        self.pvp_weapon_id = pvp_weapon_id
        self.sort_order = sort_order
        self.spd = spd
        self.spi = spi
        self.stat_mods = stat_mods
        self.monster_str = monster_str
        self.texture_bubble_x = texture_bubble_x
        self.texture_bubble_y = texture_bubble_y
        self.texture_focus_x = texture_focus_x
        self.texture_focus_y = texture_focus_y
        self.texture_path = texture_path
        self.texture_path_alt = texture_path_alt
        self.vit = vit

    @staticmethod
    def from_dict(obj: Any) -> 'Monster':
        assert isinstance(obj, dict)
        actions = from_list(Action.from_dict, obj.get("Actions"))
        agi = from_int(obj.get("Agi"))
        attack_animation_id = from_union([from_none, from_int], obj.get("AttackAnimationID"))
        avg_pop = from_int(obj.get("AvgPop"))
        category = from_int(obj.get("Category"))
        comments = from_union([from_none, from_str], obj.get("Comments"))
        description = from_union([from_none, from_str], obj.get("Description"))
        dex = from_int(obj.get("Dex"))
        exp = from_int(obj.get("Exp"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        has_breathing = from_bool(obj.get("HasBreathing"))
        has_shadow = from_bool(obj.get("HasShadow"))
        hp = from_int(obj.get("HP"))
        id = from_int(obj.get("ID"))
        is_boss = from_bool(obj.get("IsBoss"))
        is_pvp = from_bool(obj.get("IsPvp"))
        item_drops = from_list(DropTableEntry.from_dict, obj.get("ItemDrops"))
        item_steals = from_list(DropTableEntry.from_dict, obj.get("ItemSteals"))
        jp = from_int(obj.get("JP"))
        lck = from_int(obj.get("Lck"))
        level = from_int(obj.get("Level"))
        location_biome_id = from_union([from_none, from_int], obj.get("LocationBiomeID"))
        m_def = from_int(obj.get("MDef"))
        mnd = from_int(obj.get("Mnd"))
        money = from_int(obj.get("Money"))
        mp = from_int(obj.get("MP"))
        m_pen = from_int(obj.get("MPen"))
        name = from_str(obj.get("Name"))
        no_auto = from_bool(obj.get("NoAuto"))
        p_acc_rating = from_int(obj.get("PAccRating"))
        p_atk = from_int(obj.get("PAtk"))
        p_crit_chance = from_int(obj.get("PCritChance"))
        p_crit_dmg = from_int(obj.get("PCritDmg"))
        p_def = from_int(obj.get("PDef"))
        p_eva_rating = from_int(obj.get("PEvaRating"))
        p_pen = from_int(obj.get("PPen"))
        p_variance = from_int(obj.get("PVariance"))
        pvp_gender_id = from_int(obj.get("PvpGenderID"))
        pvp_job_id = from_int(obj.get("PvpJobID"))
        pvp_texture_type = from_int(obj.get("PvpTextureType"))
        pvp_weapon_id = from_union([from_none, from_int], obj.get("PvpWeaponID"))
        sort_order = from_int(obj.get("SortOrder"))
        spd = from_int(obj.get("Spd"))
        spi = from_int(obj.get("Spi"))
        stat_mods = from_list(StatMod.from_dict, obj.get("StatMods"))
        monster_str = from_int(obj.get("Str"))
        texture_bubble_x = from_int(obj.get("TextureBubbleX"))
        texture_bubble_y = from_int(obj.get("TextureBubbleY"))
        texture_focus_x = from_int(obj.get("TextureFocusX"))
        texture_focus_y = from_int(obj.get("TextureFocusY"))
        texture_path = from_union([from_none, from_str], obj.get("TexturePath"))
        texture_path_alt = from_union([from_none, from_str], obj.get("TexturePathAlt"))
        vit = from_int(obj.get("Vit"))
        return Monster(actions, agi, attack_animation_id, avg_pop, category, comments, description, dex, exp, flavor, has_breathing, has_shadow, hp, id, is_boss, is_pvp, item_drops, item_steals, jp, lck, level, location_biome_id, m_def, mnd, money, mp, m_pen, name, no_auto, p_acc_rating, p_atk, p_crit_chance, p_crit_dmg, p_def, p_eva_rating, p_pen, p_variance, pvp_gender_id, pvp_job_id, pvp_texture_type, pvp_weapon_id, sort_order, spd, spi, stat_mods, monster_str, texture_bubble_x, texture_bubble_y, texture_focus_x, texture_focus_y, texture_path, texture_path_alt, vit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Actions"] = from_list(lambda x: to_class(Action, x), self.actions)
        result["Agi"] = from_int(self.agi)
        result["AttackAnimationID"] = from_union([from_none, from_int], self.attack_animation_id)
        result["AvgPop"] = from_int(self.avg_pop)
        result["Category"] = from_int(self.category)
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["Dex"] = from_int(self.dex)
        result["Exp"] = from_int(self.exp)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["HasBreathing"] = from_bool(self.has_breathing)
        result["HasShadow"] = from_bool(self.has_shadow)
        result["HP"] = from_int(self.hp)
        result["ID"] = from_int(self.id)
        result["IsBoss"] = from_bool(self.is_boss)
        result["IsPvp"] = from_bool(self.is_pvp)
        result["ItemDrops"] = from_list(lambda x: to_class(DropTableEntry, x), self.item_drops)
        result["ItemSteals"] = from_list(lambda x: to_class(DropTableEntry, x), self.item_steals)
        result["JP"] = from_int(self.jp)
        result["Lck"] = from_int(self.lck)
        result["Level"] = from_int(self.level)
        result["LocationBiomeID"] = from_union([from_none, from_int], self.location_biome_id)
        result["MDef"] = from_int(self.m_def)
        result["Mnd"] = from_int(self.mnd)
        result["Money"] = from_int(self.money)
        result["MP"] = from_int(self.mp)
        result["MPen"] = from_int(self.m_pen)
        result["Name"] = from_str(self.name)
        result["NoAuto"] = from_bool(self.no_auto)
        result["PAccRating"] = from_int(self.p_acc_rating)
        result["PAtk"] = from_int(self.p_atk)
        result["PCritChance"] = from_int(self.p_crit_chance)
        result["PCritDmg"] = from_int(self.p_crit_dmg)
        result["PDef"] = from_int(self.p_def)
        result["PEvaRating"] = from_int(self.p_eva_rating)
        result["PPen"] = from_int(self.p_pen)
        result["PVariance"] = from_int(self.p_variance)
        result["PvpGenderID"] = from_int(self.pvp_gender_id)
        result["PvpJobID"] = from_int(self.pvp_job_id)
        result["PvpTextureType"] = from_int(self.pvp_texture_type)
        result["PvpWeaponID"] = from_union([from_none, from_int], self.pvp_weapon_id)
        result["SortOrder"] = from_int(self.sort_order)
        result["Spd"] = from_int(self.spd)
        result["Spi"] = from_int(self.spi)
        result["StatMods"] = from_list(lambda x: to_class(StatMod, x), self.stat_mods)
        result["Str"] = from_int(self.monster_str)
        result["TextureBubbleX"] = from_int(self.texture_bubble_x)
        result["TextureBubbleY"] = from_int(self.texture_bubble_y)
        result["TextureFocusX"] = from_int(self.texture_focus_x)
        result["TextureFocusY"] = from_int(self.texture_focus_y)
        result["TexturePath"] = from_union([from_none, from_str], self.texture_path)
        result["TexturePathAlt"] = from_union([from_none, from_str], self.texture_path_alt)
        result["Vit"] = from_int(self.vit)
        return result


def monster_from_dict(s: Any) -> Monster:
    return Monster.from_dict(s)


def monster_to_dict(x: Monster) -> Any:
    return to_class(Monster, x)
