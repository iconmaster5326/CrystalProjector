from typing import Any, Optional, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Color:
    """The color that the target is recolored to, should `HasBattlerColor` be `true`.
    
    An RGB color.
    
    The color that the target is outlined in, should `HasOutlineColor` be `true`.
    """
    b: float
    """The blue channel."""

    g: float
    """The green channel."""

    r: float
    """The red channel."""

    def __init__(self, b: float, g: float, r: float) -> None:
        self.b = b
        self.g = g
        self.r = r

    @staticmethod
    def from_dict(obj: Any) -> 'Color':
        assert isinstance(obj, dict)
        b = from_float(obj.get("B"))
        g = from_float(obj.get("G"))
        r = from_float(obj.get("R"))
        return Color(b, g, r)

    def to_dict(self) -> dict:
        result: dict = {}
        result["B"] = to_float(self.b)
        result["G"] = to_float(self.g)
        result["R"] = to_float(self.r)
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


class Status:
    """A Crystal Project status effect definition."""

    animation_id: Optional[int]
    """The ID of the animation this effect uses when it activates."""

    battler_color: Color
    """The color that the target is recolored to, should `HasBattlerColor` be `true`."""

    battler_color_opacity: float
    """The intensity of the recoloring, should `HasBattlerColor` be `true`."""

    category: int
    """The category of status effect is. Is it good, bad, etc?"""

    comments: Optional[str]
    """A comment for game and mod developers. Not shown in game."""

    decrement_on_crit_given: bool
    """Does this effect remove a stack when you crit?"""

    decrement_on_dmg_taken: bool
    """Does this effect remove a stack when damage is taken?"""

    decrement_on_each_user_turn: bool
    """Does this effect remove a stack at the beginning of each of the affected's turns?"""

    decrement_on_effect: bool
    """Does this effect remove a stack by some other method?"""

    decrement_on_fixed_interval: bool
    """Does this effect remove a stack on a time interval?"""

    decrement_on_heal_given: bool
    """Does this effect remove a stack when you heal?"""

    decrement_on_heal_taken: bool
    """Does this effect remove a stack when you're healed?"""

    decrement_on_m_dmg_evaded: bool
    """Does this effect remove a stack when magical damage is evaded?"""

    decrement_on_m_dmg_given: bool
    """Does this effect remove a stack when magical damage is dealt?"""

    decrement_on_m_dmg_taken: bool
    """Does this effect remove a stack when magical damage is taken?"""

    decrement_on_p_dmg_evaded: bool
    """Does this effect remove a stack when physical damage is evaded?"""

    decrement_on_p_dmg_given: bool
    """Does this effect remove a stack when physical damage is dealt?"""

    decrement_on_p_dmg_taken: bool
    """Does this effect remove a stack when physical damage is taken?"""

    description: Optional[str]
    """Appears after the flavor in the item text. Localizable."""

    flavor: Optional[str]
    """Any additional text shown to the player after its effects. Localizable."""

    force_motion: Optional[int]
    """Force the idle player sprite into a particular pose?"""

    has_battler_color: bool
    """Does this effect recolor the target it's applied to?"""

    has_outline_color: bool
    """Does this effect give a colored outline to the target it's applied to?"""

    hide_duration_from_description: bool
    """Do we hide how long this status effect lasts?"""

    hide_stat_mods_from_description: bool
    """Do we hide the exact mechanical effects from the players?"""

    id: int
    """The unique ID of this status effect."""

    is_hidden: bool
    """Is this effect hidden from the player?"""

    name: str
    """The English name of this status effect. Localizable."""

    outline_color: Color
    """The color that the target is outlined in, should `HasOutlineColor` be `true`."""

    outline_color_opacity: float
    """The intensity of the outline, should `HasOutlineColor` be `true`."""

    persists_through_death: bool
    """Does this effect persist through death?"""

    prevent_removal: bool
    """Can this effect not be removed by any means?"""

    re_apply_resistance: bool
    """Does this effect change resistances?"""

    remove_on_dmg_taken: bool
    """Do all stacks of this effect go away when damage is taken?"""

    sort_order: int
    """The order to sort this in, in places like the records."""

    stat_mods: List[StatMod]
    """The stat mods applied while this effect is active."""

    texture_index: int
    """The index into the texture for the icon.
    Item icons are 18x18 pixels,
    and go from left to right and then top to bottom.
    """
    texture_path: str
    """The icon. The texture pack, followed by a slash, followed by the texture name."""

    visual_priority: int
    """The priority this status effect should take when applying visual effects."""

    def __init__(self, animation_id: Optional[int], battler_color: Color, battler_color_opacity: float, category: int, comments: Optional[str], decrement_on_crit_given: bool, decrement_on_dmg_taken: bool, decrement_on_each_user_turn: bool, decrement_on_effect: bool, decrement_on_fixed_interval: bool, decrement_on_heal_given: bool, decrement_on_heal_taken: bool, decrement_on_m_dmg_evaded: bool, decrement_on_m_dmg_given: bool, decrement_on_m_dmg_taken: bool, decrement_on_p_dmg_evaded: bool, decrement_on_p_dmg_given: bool, decrement_on_p_dmg_taken: bool, description: Optional[str], flavor: Optional[str], force_motion: Optional[int], has_battler_color: bool, has_outline_color: bool, hide_duration_from_description: bool, hide_stat_mods_from_description: bool, id: int, is_hidden: bool, name: str, outline_color: Color, outline_color_opacity: float, persists_through_death: bool, prevent_removal: bool, re_apply_resistance: bool, remove_on_dmg_taken: bool, sort_order: int, stat_mods: List[StatMod], texture_index: int, texture_path: str, visual_priority: int) -> None:
        self.animation_id = animation_id
        self.battler_color = battler_color
        self.battler_color_opacity = battler_color_opacity
        self.category = category
        self.comments = comments
        self.decrement_on_crit_given = decrement_on_crit_given
        self.decrement_on_dmg_taken = decrement_on_dmg_taken
        self.decrement_on_each_user_turn = decrement_on_each_user_turn
        self.decrement_on_effect = decrement_on_effect
        self.decrement_on_fixed_interval = decrement_on_fixed_interval
        self.decrement_on_heal_given = decrement_on_heal_given
        self.decrement_on_heal_taken = decrement_on_heal_taken
        self.decrement_on_m_dmg_evaded = decrement_on_m_dmg_evaded
        self.decrement_on_m_dmg_given = decrement_on_m_dmg_given
        self.decrement_on_m_dmg_taken = decrement_on_m_dmg_taken
        self.decrement_on_p_dmg_evaded = decrement_on_p_dmg_evaded
        self.decrement_on_p_dmg_given = decrement_on_p_dmg_given
        self.decrement_on_p_dmg_taken = decrement_on_p_dmg_taken
        self.description = description
        self.flavor = flavor
        self.force_motion = force_motion
        self.has_battler_color = has_battler_color
        self.has_outline_color = has_outline_color
        self.hide_duration_from_description = hide_duration_from_description
        self.hide_stat_mods_from_description = hide_stat_mods_from_description
        self.id = id
        self.is_hidden = is_hidden
        self.name = name
        self.outline_color = outline_color
        self.outline_color_opacity = outline_color_opacity
        self.persists_through_death = persists_through_death
        self.prevent_removal = prevent_removal
        self.re_apply_resistance = re_apply_resistance
        self.remove_on_dmg_taken = remove_on_dmg_taken
        self.sort_order = sort_order
        self.stat_mods = stat_mods
        self.texture_index = texture_index
        self.texture_path = texture_path
        self.visual_priority = visual_priority

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        assert isinstance(obj, dict)
        animation_id = from_union([from_none, from_int], obj.get("AnimationID"))
        battler_color = Color.from_dict(obj.get("BattlerColor"))
        battler_color_opacity = from_float(obj.get("BattlerColorOpacity"))
        category = from_int(obj.get("Category"))
        comments = from_union([from_none, from_str], obj.get("Comments"))
        decrement_on_crit_given = from_bool(obj.get("DecrementOnCritGiven"))
        decrement_on_dmg_taken = from_bool(obj.get("DecrementOnDmgTaken"))
        decrement_on_each_user_turn = from_bool(obj.get("DecrementOnEachUserTurn"))
        decrement_on_effect = from_bool(obj.get("DecrementOnEffect"))
        decrement_on_fixed_interval = from_bool(obj.get("DecrementOnFixedInterval"))
        decrement_on_heal_given = from_bool(obj.get("DecrementOnHealGiven"))
        decrement_on_heal_taken = from_bool(obj.get("DecrementOnHealTaken"))
        decrement_on_m_dmg_evaded = from_bool(obj.get("DecrementOnMDmgEvaded"))
        decrement_on_m_dmg_given = from_bool(obj.get("DecrementOnMDmgGiven"))
        decrement_on_m_dmg_taken = from_bool(obj.get("DecrementOnMDmgTaken"))
        decrement_on_p_dmg_evaded = from_bool(obj.get("DecrementOnPDmgEvaded"))
        decrement_on_p_dmg_given = from_bool(obj.get("DecrementOnPDmgGiven"))
        decrement_on_p_dmg_taken = from_bool(obj.get("DecrementOnPDmgTaken"))
        description = from_union([from_none, from_str], obj.get("Description"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        force_motion = from_union([from_none, from_int], obj.get("ForceMotion"))
        has_battler_color = from_bool(obj.get("HasBattlerColor"))
        has_outline_color = from_bool(obj.get("HasOutlineColor"))
        hide_duration_from_description = from_bool(obj.get("HideDurationFromDescription"))
        hide_stat_mods_from_description = from_bool(obj.get("HideStatModsFromDescription"))
        id = from_int(obj.get("ID"))
        is_hidden = from_bool(obj.get("IsHidden"))
        name = from_str(obj.get("Name"))
        outline_color = Color.from_dict(obj.get("OutlineColor"))
        outline_color_opacity = from_float(obj.get("OutlineColorOpacity"))
        persists_through_death = from_bool(obj.get("PersistsThroughDeath"))
        prevent_removal = from_bool(obj.get("PreventRemoval"))
        re_apply_resistance = from_bool(obj.get("ReApplyResistance"))
        remove_on_dmg_taken = from_bool(obj.get("RemoveOnDmgTaken"))
        sort_order = from_int(obj.get("SortOrder"))
        stat_mods = from_list(StatMod.from_dict, obj.get("StatMods"))
        texture_index = from_int(obj.get("TextureIndex"))
        texture_path = from_str(obj.get("TexturePath"))
        visual_priority = from_int(obj.get("VisualPriority"))
        return Status(animation_id, battler_color, battler_color_opacity, category, comments, decrement_on_crit_given, decrement_on_dmg_taken, decrement_on_each_user_turn, decrement_on_effect, decrement_on_fixed_interval, decrement_on_heal_given, decrement_on_heal_taken, decrement_on_m_dmg_evaded, decrement_on_m_dmg_given, decrement_on_m_dmg_taken, decrement_on_p_dmg_evaded, decrement_on_p_dmg_given, decrement_on_p_dmg_taken, description, flavor, force_motion, has_battler_color, has_outline_color, hide_duration_from_description, hide_stat_mods_from_description, id, is_hidden, name, outline_color, outline_color_opacity, persists_through_death, prevent_removal, re_apply_resistance, remove_on_dmg_taken, sort_order, stat_mods, texture_index, texture_path, visual_priority)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AnimationID"] = from_union([from_none, from_int], self.animation_id)
        result["BattlerColor"] = to_class(Color, self.battler_color)
        result["BattlerColorOpacity"] = to_float(self.battler_color_opacity)
        result["Category"] = from_int(self.category)
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["DecrementOnCritGiven"] = from_bool(self.decrement_on_crit_given)
        result["DecrementOnDmgTaken"] = from_bool(self.decrement_on_dmg_taken)
        result["DecrementOnEachUserTurn"] = from_bool(self.decrement_on_each_user_turn)
        result["DecrementOnEffect"] = from_bool(self.decrement_on_effect)
        result["DecrementOnFixedInterval"] = from_bool(self.decrement_on_fixed_interval)
        result["DecrementOnHealGiven"] = from_bool(self.decrement_on_heal_given)
        result["DecrementOnHealTaken"] = from_bool(self.decrement_on_heal_taken)
        result["DecrementOnMDmgEvaded"] = from_bool(self.decrement_on_m_dmg_evaded)
        result["DecrementOnMDmgGiven"] = from_bool(self.decrement_on_m_dmg_given)
        result["DecrementOnMDmgTaken"] = from_bool(self.decrement_on_m_dmg_taken)
        result["DecrementOnPDmgEvaded"] = from_bool(self.decrement_on_p_dmg_evaded)
        result["DecrementOnPDmgGiven"] = from_bool(self.decrement_on_p_dmg_given)
        result["DecrementOnPDmgTaken"] = from_bool(self.decrement_on_p_dmg_taken)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["ForceMotion"] = from_union([from_none, from_int], self.force_motion)
        result["HasBattlerColor"] = from_bool(self.has_battler_color)
        result["HasOutlineColor"] = from_bool(self.has_outline_color)
        result["HideDurationFromDescription"] = from_bool(self.hide_duration_from_description)
        result["HideStatModsFromDescription"] = from_bool(self.hide_stat_mods_from_description)
        result["ID"] = from_int(self.id)
        result["IsHidden"] = from_bool(self.is_hidden)
        result["Name"] = from_str(self.name)
        result["OutlineColor"] = to_class(Color, self.outline_color)
        result["OutlineColorOpacity"] = to_float(self.outline_color_opacity)
        result["PersistsThroughDeath"] = from_bool(self.persists_through_death)
        result["PreventRemoval"] = from_bool(self.prevent_removal)
        result["ReApplyResistance"] = from_bool(self.re_apply_resistance)
        result["RemoveOnDmgTaken"] = from_bool(self.remove_on_dmg_taken)
        result["SortOrder"] = from_int(self.sort_order)
        result["StatMods"] = from_list(lambda x: to_class(StatMod, x), self.stat_mods)
        result["TextureIndex"] = from_int(self.texture_index)
        result["TexturePath"] = from_str(self.texture_path)
        result["VisualPriority"] = from_int(self.visual_priority)
        return result


def status_from_dict(s: Any) -> Status:
    return Status.from_dict(s)


def status_to_dict(x: Status) -> Any:
    return to_class(Status, x)
