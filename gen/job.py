from typing import Any, List, Optional, TypeVar, Callable, Type, cast


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Color:
    """The color associated with this job. Used for recoloring crystals."""

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


class LearnTreeNode:
    """A column in the learn tree.
    
    A node in the learn tree.
    """
    data_id: int
    """The ID of the ability (if `NodeType` is `Ability`) or passive (if `NodeType` is
    `Passive`).
    """
    node_type: int
    """The type of this node."""

    prereq_left: bool
    """Is the node to the upper-left a prerequisite to this node?"""

    prereq_middle: bool
    """Is the node above a prerequisite to this node?"""

    prereq_right: bool
    """Is the node to the upper-right a prerequisite to this node?"""

    def __init__(self, data_id: int, node_type: int, prereq_left: bool, prereq_middle: bool, prereq_right: bool) -> None:
        self.data_id = data_id
        self.node_type = node_type
        self.prereq_left = prereq_left
        self.prereq_middle = prereq_middle
        self.prereq_right = prereq_right

    @staticmethod
    def from_dict(obj: Any) -> 'LearnTreeNode':
        assert isinstance(obj, dict)
        data_id = from_int(obj.get("DataID"))
        node_type = from_int(obj.get("NodeType"))
        prereq_left = from_bool(obj.get("PrereqLeft"))
        prereq_middle = from_bool(obj.get("PrereqMiddle"))
        prereq_right = from_bool(obj.get("PrereqRight"))
        return LearnTreeNode(data_id, node_type, prereq_left, prereq_middle, prereq_right)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DataID"] = from_int(self.data_id)
        result["NodeType"] = from_int(self.node_type)
        result["PrereqLeft"] = from_bool(self.prereq_left)
        result["PrereqMiddle"] = from_bool(self.prereq_middle)
        result["PrereqRight"] = from_bool(self.prereq_right)
        return result


class Job:
    """A Crystal Project job definition."""

    abilities_name: str
    """The name of the abilities menu for this job. Localizable."""

    ability_i_ds: List[int]
    """The IDs of the abilities this job can learn."""

    actor_texture_path_f: str
    """The texture to use for the feminine-presenting player with this job, when outside of
    battle.
    The format is as follows: The pack's name, a slash, then the texture's name.
    """
    actor_texture_path_m: str
    """The texture to use for the masculine-presenting player with this job, when outside of
    battle.
    The format is as follows: The pack's name, a slash, then the texture's name.
    """
    agi_rating: int
    """This job's Agility growth rate. A percentage from 0 to 100. 10 points is half a star."""

    color: Color
    """The color associated with this job. Used for recoloring crystals."""

    comments: Optional[str]
    """A comment for game and mod developers. Not shown in game."""

    crystal_name: str
    """The name of the color of this job's crystal. Localizable."""

    description: Optional[str]
    """Text to help the user select an initial job at the start of the game. Localizable."""

    dex_rating: int
    """This job's Dexterity growth rate. A percentage from 0 to 100. 10 points is half a star."""

    equipment_types: List[int]
    """The types of weapons and armor this job can equip."""

    flavor: Optional[str]
    """Seemingly unused."""

    hp_rating: int
    """This job's HP growth rate. A percentage from 0 to 100. 10 points is half a star."""

    icon_texture_index: int
    """The index into the texture for the icon.
    Item icons are 18x18 pixels,
    and go from left to right and then top to bottom.
    """
    icon_texture_path: str
    """The texture to use for the job's ability menu icon.
    The format is as follows: The pack's name, a slash, then the texture's name.
    """
    id: int
    """The ID of this job."""

    is_starting_job: bool
    """Is this job one you unlock at the start of the game, without a crystal?"""

    is_unselectable_job: bool
    """Can you not select this job in the job menu?"""

    is_unselectable_sub_job: bool
    """Can you not select this job in the subjob menu?"""

    lck_rating: int
    """This job's Luck growth rate. A percentage from 0 to 100. 10 points is half a star."""

    learn_tree: List[List[LearnTreeNode]]
    """The job's ability/passive tree. 4x6 in size."""

    location_biome_id: Optional[int]
    """The ID of the biome this job's crystal appears in.
    You can lie about this if you'd like.
    """
    member_texture_path_f: str
    """The texture to use for the feminine-presenting player with this job, when in battle.
    The format is as follows: The pack's name, a slash, then the texture's name.
    """
    member_texture_path_f_alt: str
    """Like `MemberTexturePathF`, but sometimes different.
    Used for "fake PC" fights (Astley, etc).
    """
    member_texture_path_m: str
    """The texture to use for the masculine-presenting player with this job, when in battle.
    The format is as follows: The pack's name, a slash, then the texture's name.
    """
    member_texture_path_m_alt: str
    """Like `MemberTexturePathM`, but sometimes different.
    Used for "fake PC" fights (Astley, etc).
    """
    mnd_rating: int
    """This job's Mind growth rate. A percentage from 0 to 100. 10 points is half a star."""

    mp_rating: int
    """This job's MP growth rate. A percentage from 0 to 100. 10 points is half a star."""

    name: str
    """The English name of this job. Localizable."""

    passive_i_ds: List[int]
    """The IDs of the innate passives and the learned passives of this job.
    Exactly one passive here should be innate, and it should be the first one.
    """
    preferred_body_type: int
    """The prefered category of body armor, among the types it can equip."""

    preferred_hand_a_type: int
    """The prefered category of weapons, among the types it can equip."""

    preferred_head_type: int
    """The prefered category of head armor, among the types it can equip."""

    sort_order: int
    """The order to sort this in, in places like the job select screen."""

    spd_rating: int
    """This job's Speed growth rate. A percentage from 0 to 100. 10 points is half a star."""

    spi_rating: int
    """This job's Spirit growth rate. A percentage from 0 to 100. 10 points is half a star."""

    str_rating: int
    """This job's Strength growth rate. A percentage from 0 to 100. 10 points is half a star."""

    vit_rating: int
    """This job's Vitality growth rate. A percentage from 0 to 100. 10 points is half a star."""

    weapon_hold_type_f: int
    """The hold type for feminine-presenting players."""

    weapon_hold_type_m: int
    """The hold type for masculine-presenting players."""

    def __init__(self, abilities_name: str, ability_i_ds: List[int], actor_texture_path_f: str, actor_texture_path_m: str, agi_rating: int, color: Color, comments: Optional[str], crystal_name: str, description: Optional[str], dex_rating: int, equipment_types: List[int], flavor: Optional[str], hp_rating: int, icon_texture_index: int, icon_texture_path: str, id: int, is_starting_job: bool, is_unselectable_job: bool, is_unselectable_sub_job: bool, lck_rating: int, learn_tree: List[List[LearnTreeNode]], location_biome_id: Optional[int], member_texture_path_f: str, member_texture_path_f_alt: str, member_texture_path_m: str, member_texture_path_m_alt: str, mnd_rating: int, mp_rating: int, name: str, passive_i_ds: List[int], preferred_body_type: int, preferred_hand_a_type: int, preferred_head_type: int, sort_order: int, spd_rating: int, spi_rating: int, str_rating: int, vit_rating: int, weapon_hold_type_f: int, weapon_hold_type_m: int) -> None:
        self.abilities_name = abilities_name
        self.ability_i_ds = ability_i_ds
        self.actor_texture_path_f = actor_texture_path_f
        self.actor_texture_path_m = actor_texture_path_m
        self.agi_rating = agi_rating
        self.color = color
        self.comments = comments
        self.crystal_name = crystal_name
        self.description = description
        self.dex_rating = dex_rating
        self.equipment_types = equipment_types
        self.flavor = flavor
        self.hp_rating = hp_rating
        self.icon_texture_index = icon_texture_index
        self.icon_texture_path = icon_texture_path
        self.id = id
        self.is_starting_job = is_starting_job
        self.is_unselectable_job = is_unselectable_job
        self.is_unselectable_sub_job = is_unselectable_sub_job
        self.lck_rating = lck_rating
        self.learn_tree = learn_tree
        self.location_biome_id = location_biome_id
        self.member_texture_path_f = member_texture_path_f
        self.member_texture_path_f_alt = member_texture_path_f_alt
        self.member_texture_path_m = member_texture_path_m
        self.member_texture_path_m_alt = member_texture_path_m_alt
        self.mnd_rating = mnd_rating
        self.mp_rating = mp_rating
        self.name = name
        self.passive_i_ds = passive_i_ds
        self.preferred_body_type = preferred_body_type
        self.preferred_hand_a_type = preferred_hand_a_type
        self.preferred_head_type = preferred_head_type
        self.sort_order = sort_order
        self.spd_rating = spd_rating
        self.spi_rating = spi_rating
        self.str_rating = str_rating
        self.vit_rating = vit_rating
        self.weapon_hold_type_f = weapon_hold_type_f
        self.weapon_hold_type_m = weapon_hold_type_m

    @staticmethod
    def from_dict(obj: Any) -> 'Job':
        assert isinstance(obj, dict)
        abilities_name = from_str(obj.get("AbilitiesName"))
        ability_i_ds = from_list(from_int, obj.get("AbilityIDs"))
        actor_texture_path_f = from_str(obj.get("ActorTexturePathF"))
        actor_texture_path_m = from_str(obj.get("ActorTexturePathM"))
        agi_rating = from_int(obj.get("AgiRating"))
        color = Color.from_dict(obj.get("Color"))
        comments = from_union([from_none, from_str], obj.get("Comments"))
        crystal_name = from_str(obj.get("CrystalName"))
        description = from_union([from_none, from_str], obj.get("Description"))
        dex_rating = from_int(obj.get("DexRating"))
        equipment_types = from_list(from_int, obj.get("EquipmentTypes"))
        flavor = from_union([from_none, from_str], obj.get("Flavor"))
        hp_rating = from_int(obj.get("HPRating"))
        icon_texture_index = from_int(obj.get("IconTextureIndex"))
        icon_texture_path = from_str(obj.get("IconTexturePath"))
        id = from_int(obj.get("ID"))
        is_starting_job = from_bool(obj.get("IsStartingJob"))
        is_unselectable_job = from_bool(obj.get("IsUnselectableJob"))
        is_unselectable_sub_job = from_bool(obj.get("IsUnselectableSubJob"))
        lck_rating = from_int(obj.get("LckRating"))
        learn_tree = from_list(lambda x: from_list(LearnTreeNode.from_dict, x), obj.get("LearnTree"))
        location_biome_id = from_union([from_none, from_int], obj.get("LocationBiomeID"))
        member_texture_path_f = from_str(obj.get("MemberTexturePathF"))
        member_texture_path_f_alt = from_str(obj.get("MemberTexturePathFAlt"))
        member_texture_path_m = from_str(obj.get("MemberTexturePathM"))
        member_texture_path_m_alt = from_str(obj.get("MemberTexturePathMAlt"))
        mnd_rating = from_int(obj.get("MndRating"))
        mp_rating = from_int(obj.get("MPRating"))
        name = from_str(obj.get("Name"))
        passive_i_ds = from_list(from_int, obj.get("PassiveIDs"))
        preferred_body_type = from_int(obj.get("PreferredBodyType"))
        preferred_hand_a_type = from_int(obj.get("PreferredHandAType"))
        preferred_head_type = from_int(obj.get("PreferredHeadType"))
        sort_order = from_int(obj.get("SortOrder"))
        spd_rating = from_int(obj.get("SpdRating"))
        spi_rating = from_int(obj.get("SpiRating"))
        str_rating = from_int(obj.get("StrRating"))
        vit_rating = from_int(obj.get("VitRating"))
        weapon_hold_type_f = from_int(obj.get("WeaponHoldTypeF"))
        weapon_hold_type_m = from_int(obj.get("WeaponHoldTypeM"))
        return Job(abilities_name, ability_i_ds, actor_texture_path_f, actor_texture_path_m, agi_rating, color, comments, crystal_name, description, dex_rating, equipment_types, flavor, hp_rating, icon_texture_index, icon_texture_path, id, is_starting_job, is_unselectable_job, is_unselectable_sub_job, lck_rating, learn_tree, location_biome_id, member_texture_path_f, member_texture_path_f_alt, member_texture_path_m, member_texture_path_m_alt, mnd_rating, mp_rating, name, passive_i_ds, preferred_body_type, preferred_hand_a_type, preferred_head_type, sort_order, spd_rating, spi_rating, str_rating, vit_rating, weapon_hold_type_f, weapon_hold_type_m)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AbilitiesName"] = from_str(self.abilities_name)
        result["AbilityIDs"] = from_list(from_int, self.ability_i_ds)
        result["ActorTexturePathF"] = from_str(self.actor_texture_path_f)
        result["ActorTexturePathM"] = from_str(self.actor_texture_path_m)
        result["AgiRating"] = from_int(self.agi_rating)
        result["Color"] = to_class(Color, self.color)
        result["Comments"] = from_union([from_none, from_str], self.comments)
        result["CrystalName"] = from_str(self.crystal_name)
        result["Description"] = from_union([from_none, from_str], self.description)
        result["DexRating"] = from_int(self.dex_rating)
        result["EquipmentTypes"] = from_list(from_int, self.equipment_types)
        result["Flavor"] = from_union([from_none, from_str], self.flavor)
        result["HPRating"] = from_int(self.hp_rating)
        result["IconTextureIndex"] = from_int(self.icon_texture_index)
        result["IconTexturePath"] = from_str(self.icon_texture_path)
        result["ID"] = from_int(self.id)
        result["IsStartingJob"] = from_bool(self.is_starting_job)
        result["IsUnselectableJob"] = from_bool(self.is_unselectable_job)
        result["IsUnselectableSubJob"] = from_bool(self.is_unselectable_sub_job)
        result["LckRating"] = from_int(self.lck_rating)
        result["LearnTree"] = from_list(lambda x: from_list(lambda x: to_class(LearnTreeNode, x), x), self.learn_tree)
        result["LocationBiomeID"] = from_union([from_none, from_int], self.location_biome_id)
        result["MemberTexturePathF"] = from_str(self.member_texture_path_f)
        result["MemberTexturePathFAlt"] = from_str(self.member_texture_path_f_alt)
        result["MemberTexturePathM"] = from_str(self.member_texture_path_m)
        result["MemberTexturePathMAlt"] = from_str(self.member_texture_path_m_alt)
        result["MndRating"] = from_int(self.mnd_rating)
        result["MPRating"] = from_int(self.mp_rating)
        result["Name"] = from_str(self.name)
        result["PassiveIDs"] = from_list(from_int, self.passive_i_ds)
        result["PreferredBodyType"] = from_int(self.preferred_body_type)
        result["PreferredHandAType"] = from_int(self.preferred_hand_a_type)
        result["PreferredHeadType"] = from_int(self.preferred_head_type)
        result["SortOrder"] = from_int(self.sort_order)
        result["SpdRating"] = from_int(self.spd_rating)
        result["SpiRating"] = from_int(self.spi_rating)
        result["StrRating"] = from_int(self.str_rating)
        result["VitRating"] = from_int(self.vit_rating)
        result["WeaponHoldTypeF"] = from_int(self.weapon_hold_type_f)
        result["WeaponHoldTypeM"] = from_int(self.weapon_hold_type_m)
        return result


def job_from_dict(s: Any) -> Job:
    return Job.from_dict(s)


def job_to_dict(x: Job) -> Any:
    return to_class(Job, x)
