from typing import Any, List, Optional, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AbilityMod:
    """An ability modifier."""

    tag: int
    """The type of ability modifier this is. TODO - there's a lot in this enum"""

    value1: int
    """The first parameter to the ability mod, if the type of ability mod accepts such a
    parameter, and 0 otherwise.
    """
    value2: int
    """The secpnd parameter to the ability mod, if the type of ability mod accepts such a
    parameter, and 0 otherwise.
    """

    def __init__(self, tag: int, value1: int, value2: int) -> None:
        self.tag = tag
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def from_dict(obj: Any) -> 'AbilityMod':
        assert isinstance(obj, dict)
        tag = from_int(obj.get("Tag"))
        value1 = from_int(obj.get("Value1"))
        value2 = from_int(obj.get("Value2"))
        return AbilityMod(tag, value1, value2)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Tag"] = from_int(self.tag)
        result["Value1"] = from_int(self.value1)
        result["Value2"] = from_int(self.value2)
        return result


class TargetStatusElement:
    """A status effect applied/removed to/from someone."""

    chance: Any
    """The percent chance to apply/remove the status effect."""

    count: int
    """The number of stacks of the effect to apply, or if negative, remove."""

    status_id: int
    """The ID of the status effect."""

    def __init__(self, chance: Any, count: int, status_id: int) -> None:
        self.chance = chance
        self.count = count
        self.status_id = status_id

    @staticmethod
    def from_dict(obj: Any) -> 'TargetStatusElement':
        assert isinstance(obj, dict)
        chance = obj.get("Chance")
        count = from_int(obj.get("Count"))
        status_id = from_int(obj.get("StatusID"))
        return TargetStatusElement(chance, count, status_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Chance"] = self.chance
        result["Count"] = from_int(self.count)
        result["StatusID"] = from_int(self.status_id)
        return result


class Ability:
    """A Crystal Project ability definition.
    Abilities are both attacks and skills in battle,
    and the result of using items in the field.
    """
    ability_mods: List[AbilityMod]
    """Any ability modifiers and other effects this might have."""

    agi_rate: int
    """The Agility % to use for the damage/healing calculation."""

    animation_id: Optional[int]
    """The ID of an animation to use when activating the ability."""

    ap_cost: int
    """How much AP this ability costs."""

    attribute: int
    """What type of damage this ability deals/heals."""

    base_acc: int
    """The ability's flat increase to hit."""

    base_crit_chance: int
    """The ability's flat increase to crit."""

    base_crit_dmg: int
    """The ability's percentage increase to crit damage."""

    base_p_atk_rate: int
    """The ability's hit rate."""

    base_power: int
    """The ability's base strength of its healing/damaging effect."""

    base_var: int
    """The ability's percent variance for the damage roll."""

    battle_disabled: bool
    """Is this ability always disabled in battle?"""

    cd_cost: int
    """How long before you can use this ability again."""

    comments: Optional[str]
    """Any comments for developers. Does not appear in game."""

    ct_cost: int
    """How much this ability delays you by."""

    description: Optional[str]
    """Appears after the flavor in the ability text. Localizable."""

    dex_rate: int
    """The Dexterity % to use for the damage/healing calculation."""

    element: Optional[int]
    """The element of this ability, if any."""

    enabled_unarmed: bool
    """Can you only use this while unarmed (or have the weapon types above?)"""

    enabled_weapon_types: List[int]
    """What weapon types do you have to have to activate this ability?
    An empty array means this can be used with any weapon.
    """
    field_enabled: bool
    """Is this ability always enabled in the field?"""

    flavor: Optional[str]
    """Appears after the statistical information in the ability text. Localizable."""

    hide_damage_from_description: bool
    """Do we hide the damage calculation from the players when previewing?"""

    hide_mods_from_description: bool
    """Do we hide the modifiers from the players when previewing?"""

    hide_scope_from_description: bool
    """Do we hide the targets from the players when previewing?"""

    hide_statuses_from_description: bool
    """Do we hide the statuses inflicted from the players when previewing?"""

    hp_cost: int
    """How much HP this ability costs, in % of maximum HP."""

    id: int
    """The unique ID of this ability."""

    invert_enabled_types_display: bool
    """If true, display what you CAN'T use this ability with, rather than what you must use it
    with.
    """
    is_basic: bool
    """Is this ability a basic action?"""

    is_default_locked: bool
    """Is this ability unavailable at the start of battles?"""

    is_m_abil: bool
    """Is this ability magical in nature?"""

    is_p_abil: bool
    """Is this ability physical in nature?"""

    is_sight_learned: bool
    """Is this ability learnable via the Scholar job?"""

    jp: int
    """The JP cost to unlock this ability."""

    lck_rate: int
    """The Luck % to use for the damage/healing calculation."""

    m_def_rate: int
    """The amount of magical defence penetration."""

    mnd_rate: int
    """The Mind % to use for the damage/healing calculation."""

    mp_cost: int
    """How much MP this ability costs."""

    name: str
    """The English name of this ability. Displayed to users.Localizable."""

    p_def_as_p_atk: bool
    """TODO - seemingly unused."""

    p_def_rate: int
    """The amount of physical defence penetration."""

    scaling_p_atk_rate: Optional[int]
    """The % your hit rate is affected by your level."""

    scaling_power: Optional[int]
    """The % your power is affected by your level."""

    scope: int
    """The number of targets of the ability."""

    scope_locked: bool
    """Are the targets of the ability unselectable by the user?"""

    sort_order: int
    """The order this is displayed in records."""

    spd_rate: int
    """The Speed % to use for the damage/healing calculation."""

    spi_rate: int
    """The Spirit % to use for the damage/healing calculation."""

    str_rate: int
    """The Strength % to use for the damage/healing calculation."""

    target: int
    """The allowable targets of the ability."""

    target_statuses: List[TargetStatusElement]
    """What status effects to apply/remove to/from the targets."""

    texture_index: Optional[int]
    """The index of the texture in `Icon.dat` to use. Textures are TODOxTODO pixels, and there
    are TODOxTODO per sheet.
    """
    texture_path: Optional[str]
    """The name of the texture in `Icon.dat` to use."""

    usage_animation_id: Optional[int]
    """The ID of an animation.
    Only used with Doublecast, and it leads to a no-op animation.
    TODO - What does this do?
    """
    user_statuses: List[TargetStatusElement]
    """What status effects to apply/remove to/from the user."""

    vit_rate: int
    """The Vitality % to use for the damage/healing calculation."""

    def __init__(self, ability_mods: List[AbilityMod], agi_rate: int, animation_id: Optional[int], ap_cost: int, attribute: int, base_acc: int, base_crit_chance: int, base_crit_dmg: int, base_p_atk_rate: int, base_power: int, base_var: int, battle_disabled: bool, cd_cost: int, comments: Optional[str], ct_cost: int, description: Optional[str], dex_rate: int, element: Optional[int], enabled_unarmed: bool, enabled_weapon_types: List[int], field_enabled: bool, flavor: Optional[str], hide_damage_from_description: bool, hide_mods_from_description: bool, hide_scope_from_description: bool, hide_statuses_from_description: bool, hp_cost: int, id: int, invert_enabled_types_display: bool, is_basic: bool, is_default_locked: bool, is_m_abil: bool, is_p_abil: bool, is_sight_learned: bool, jp: int, lck_rate: int, m_def_rate: int, mnd_rate: int, mp_cost: int, name: str, p_def_as_p_atk: bool, p_def_rate: int, scaling_p_atk_rate: Optional[int], scaling_power: Optional[int], scope: int, scope_locked: bool, sort_order: int, spd_rate: int, spi_rate: int, str_rate: int, target: int, target_statuses: List[TargetStatusElement], texture_index: Optional[int], texture_path: Optional[str], usage_animation_id: Optional[int], user_statuses: List[TargetStatusElement], vit_rate: int) -> None:
        self.ability_mods = ability_mods
        self.agi_rate = agi_rate
        self.animation_id = animation_id
        self.ap_cost = ap_cost
        self.attribute = attribute
        self.base_acc = base_acc
        self.base_crit_chance = base_crit_chance
        self.base_crit_dmg = base_crit_dmg
        self.base_p_atk_rate = base_p_atk_rate
        self.base_power = base_power
        self.base_var = base_var
        self.battle_disabled = battle_disabled
        self.cd_cost = cd_cost
        self.comments = comments
        self.ct_cost = ct_cost
        self.description = description
        self.dex_rate = dex_rate
        self.element = element
        self.enabled_unarmed = enabled_unarmed
        self.enabled_weapon_types = enabled_weapon_types
        self.field_enabled = field_enabled
        self.flavor = flavor
        self.hide_damage_from_description = hide_damage_from_description
        self.hide_mods_from_description = hide_mods_from_description
        self.hide_scope_from_description = hide_scope_from_description
        self.hide_statuses_from_description = hide_statuses_from_description
        self.hp_cost = hp_cost
        self.id = id
        self.invert_enabled_types_display = invert_enabled_types_display
        self.is_basic = is_basic
        self.is_default_locked = is_default_locked
        self.is_m_abil = is_m_abil
        self.is_p_abil = is_p_abil
        self.is_sight_learned = is_sight_learned
        self.jp = jp
        self.lck_rate = lck_rate
        self.m_def_rate = m_def_rate
        self.mnd_rate = mnd_rate
        self.mp_cost = mp_cost
        self.name = name
        self.p_def_as_p_atk = p_def_as_p_atk
        self.p_def_rate = p_def_rate
        self.scaling_p_atk_rate = scaling_p_atk_rate
        self.scaling_power = scaling_power
        self.scope = scope
        self.scope_locked = scope_locked
        self.sort_order = sort_order
        self.spd_rate = spd_rate
        self.spi_rate = spi_rate
        self.str_rate = str_rate
        self.target = target
        self.target_statuses = target_statuses
        self.texture_index = texture_index
        self.texture_path = texture_path
        self.usage_animation_id = usage_animation_id
        self.user_statuses = user_statuses
        self.vit_rate = vit_rate

    @staticmethod
    def from_dict(obj: Any) -> 'Ability':
        assert isinstance(obj, dict)
        ability_mods = from_list(AbilityMod.from_dict, obj.get("AbilityMods"))
        agi_rate = from_int(obj.get("AgiRate"))
        animation_id = from_union([from_none, from_int], obj.get("AnimationID"))
        ap_cost = from_int(obj.get("APCost"))
        attribute = from_int(obj.get("Attribute"))
        base_acc = from_int(obj.get("BaseAcc"))
        base_crit_chance = from_int(obj.get("BaseCritChance"))
        base_crit_dmg = from_int(obj.get("BaseCritDmg"))
        base_p_atk_rate = from_int(obj.get("BasePAtkRate"))
        base_power = from_int(obj.get("BasePower"))
        base_var = from_int(obj.get("BaseVar"))
        battle_disabled = from_bool(obj.get("BattleDisabled"))
        cd_cost = from_int(obj.get("CDCost"))
        comments = from_union([from_none, from_str], obj.get("Comments"))
        ct_cost = from_int(obj.get("CTCost"))
        description = from_union([from_none, from_str], obj.get("Description"))
        dex_rate = from_int(obj.get("DexRate"))
        element = from_union([from_none, from_int], obj.get("Element"))
        enabled_unarmed = from_bool(obj.get("EnabledUnarmed"))
        enabled_weapon_types = from_list(from_int, obj.get("EnabledWeaponTypes"))
        field_enabled = from_bool(obj.get("FieldEnabled"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        hide_damage_from_description = from_bool(obj.get("HideDamageFromDescription"))
        hide_mods_from_description = from_bool(obj.get("HideModsFromDescription"))
        hide_scope_from_description = from_bool(obj.get("HideScopeFromDescription"))
        hide_statuses_from_description = from_bool(obj.get("HideStatusesFromDescription"))
        hp_cost = from_int(obj.get("HPCost"))
        id = from_int(obj.get("ID"))
        invert_enabled_types_display = from_bool(obj.get("InvertEnabledTypesDisplay"))
        is_basic = from_bool(obj.get("IsBasic"))
        is_default_locked = from_bool(obj.get("IsDefaultLocked"))
        is_m_abil = from_bool(obj.get("IsMAbil"))
        is_p_abil = from_bool(obj.get("IsPAbil"))
        is_sight_learned = from_bool(obj.get("IsSightLearned"))
        jp = from_int(obj.get("JP"))
        lck_rate = from_int(obj.get("LckRate"))
        m_def_rate = from_int(obj.get("MDefRate"))
        mnd_rate = from_int(obj.get("MndRate"))
        mp_cost = from_int(obj.get("MPCost"))
        name = from_str(obj.get("Name"))
        p_def_as_p_atk = from_bool(obj.get("PDefAsPAtk"))
        p_def_rate = from_int(obj.get("PDefRate"))
        scaling_p_atk_rate = from_union([from_none, from_int], obj.get("ScalingPAtkRate"))
        scaling_power = from_union([from_none, from_int], obj.get("ScalingPower"))
        scope = from_int(obj.get("Scope"))
        scope_locked = from_bool(obj.get("ScopeLocked"))
        sort_order = from_int(obj.get("SortOrder"))
        spd_rate = from_int(obj.get("SpdRate"))
        spi_rate = from_int(obj.get("SpiRate"))
        str_rate = from_int(obj.get("StrRate"))
        target = from_int(obj.get("Target"))
        target_statuses = from_list(TargetStatusElement.from_dict, obj.get("TargetStatuses"))
        texture_index = from_union([from_none, from_int], obj.get("TextureIndex"))
        texture_path = from_union([from_none, from_str], obj.get("TexturePath"))
        usage_animation_id = from_union([from_none, from_int], obj.get("UsageAnimationID"))
        user_statuses = from_list(TargetStatusElement.from_dict, obj.get("UserStatuses"))
        vit_rate = from_int(obj.get("VitRate"))
        return Ability(ability_mods, agi_rate, animation_id, ap_cost, attribute, base_acc, base_crit_chance, base_crit_dmg, base_p_atk_rate, base_power, base_var, battle_disabled, cd_cost, comments, ct_cost, description, dex_rate, element, enabled_unarmed, enabled_weapon_types, field_enabled, flavor, hide_damage_from_description, hide_mods_from_description, hide_scope_from_description, hide_statuses_from_description, hp_cost, id, invert_enabled_types_display, is_basic, is_default_locked, is_m_abil, is_p_abil, is_sight_learned, jp, lck_rate, m_def_rate, mnd_rate, mp_cost, name, p_def_as_p_atk, p_def_rate, scaling_p_atk_rate, scaling_power, scope, scope_locked, sort_order, spd_rate, spi_rate, str_rate, target, target_statuses, texture_index, texture_path, usage_animation_id, user_statuses, vit_rate)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AbilityMods"] = from_list(lambda x: to_class(AbilityMod, x), self.ability_mods)
        result["AgiRate"] = from_int(self.agi_rate)
        result["AnimationID"] = from_union([from_none, from_int], self.animation_id)
        result["APCost"] = from_int(self.ap_cost)
        result["Attribute"] = from_int(self.attribute)
        result["BaseAcc"] = from_int(self.base_acc)
        result["BaseCritChance"] = from_int(self.base_crit_chance)
        result["BaseCritDmg"] = from_int(self.base_crit_dmg)
        result["BasePAtkRate"] = from_int(self.base_p_atk_rate)
        result["BasePower"] = from_int(self.base_power)
        result["BaseVar"] = from_int(self.base_var)
        result["BattleDisabled"] = from_bool(self.battle_disabled)
        result["CDCost"] = from_int(self.cd_cost)
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["CTCost"] = from_int(self.ct_cost)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["DexRate"] = from_int(self.dex_rate)
        result["Element"] = from_union([from_none, from_int], self.element)
        result["EnabledUnarmed"] = from_bool(self.enabled_unarmed)
        result["EnabledWeaponTypes"] = from_list(from_int, self.enabled_weapon_types)
        result["FieldEnabled"] = from_bool(self.field_enabled)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["HideDamageFromDescription"] = from_bool(self.hide_damage_from_description)
        result["HideModsFromDescription"] = from_bool(self.hide_mods_from_description)
        result["HideScopeFromDescription"] = from_bool(self.hide_scope_from_description)
        result["HideStatusesFromDescription"] = from_bool(self.hide_statuses_from_description)
        result["HPCost"] = from_int(self.hp_cost)
        result["ID"] = from_int(self.id)
        result["InvertEnabledTypesDisplay"] = from_bool(self.invert_enabled_types_display)
        result["IsBasic"] = from_bool(self.is_basic)
        result["IsDefaultLocked"] = from_bool(self.is_default_locked)
        result["IsMAbil"] = from_bool(self.is_m_abil)
        result["IsPAbil"] = from_bool(self.is_p_abil)
        result["IsSightLearned"] = from_bool(self.is_sight_learned)
        result["JP"] = from_int(self.jp)
        result["LckRate"] = from_int(self.lck_rate)
        result["MDefRate"] = from_int(self.m_def_rate)
        result["MndRate"] = from_int(self.mnd_rate)
        result["MPCost"] = from_int(self.mp_cost)
        result["Name"] = from_str(self.name)
        result["PDefAsPAtk"] = from_bool(self.p_def_as_p_atk)
        result["PDefRate"] = from_int(self.p_def_rate)
        result["ScalingPAtkRate"] = from_union([from_none, from_int], self.scaling_p_atk_rate)
        result["ScalingPower"] = from_union([from_none, from_int], self.scaling_power)
        result["Scope"] = from_int(self.scope)
        result["ScopeLocked"] = from_bool(self.scope_locked)
        result["SortOrder"] = from_int(self.sort_order)
        result["SpdRate"] = from_int(self.spd_rate)
        result["SpiRate"] = from_int(self.spi_rate)
        result["StrRate"] = from_int(self.str_rate)
        result["Target"] = from_int(self.target)
        result["TargetStatuses"] = from_list(lambda x: to_class(TargetStatusElement, x), self.target_statuses)
        result["TextureIndex"] = from_union([from_none, from_int], self.texture_index)
        result["TexturePath"] = from_union([from_none, from_str], self.texture_path)
        result["UsageAnimationID"] = from_union([from_none, from_int], self.usage_animation_id)
        result["UserStatuses"] = from_list(lambda x: to_class(TargetStatusElement, x), self.user_statuses)
        result["VitRate"] = from_int(self.vit_rate)
        return result


def ability_from_dict(s: Any) -> Ability:
    return Ability.from_dict(s)


def ability_to_dict(x: Ability) -> Any:
    return to_class(Ability, x)
