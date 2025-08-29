from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class BoundingBox:
    """A bounding box."""

    x_neg: float
    """The lower X bound."""

    x_pos: float
    """The upper X bound."""

    y_neg: float
    """The lower Y bound."""

    y_pos: float
    """The upper Y bound."""

    z_neg: float
    """The lower Z bound."""

    z_pos: float
    """The upper Z bound."""

    def __init__(self, x_neg: float, x_pos: float, y_neg: float, y_pos: float, z_neg: float, z_pos: float) -> None:
        self.x_neg = x_neg
        self.x_pos = x_pos
        self.y_neg = y_neg
        self.y_pos = y_pos
        self.z_neg = z_neg
        self.z_pos = z_pos

    @staticmethod
    def from_dict(obj: Any) -> 'BoundingBox':
        assert isinstance(obj, dict)
        x_neg = from_float(obj.get("XNeg"))
        x_pos = from_float(obj.get("XPos"))
        y_neg = from_float(obj.get("YNeg"))
        y_pos = from_float(obj.get("YPos"))
        z_neg = from_float(obj.get("ZNeg"))
        z_pos = from_float(obj.get("ZPos"))
        return BoundingBox(x_neg, x_pos, y_neg, y_pos, z_neg, z_pos)

    def to_dict(self) -> dict:
        result: dict = {}
        result["XNeg"] = to_float(self.x_neg)
        result["XPos"] = to_float(self.x_pos)
        result["YNeg"] = to_float(self.y_neg)
        result["YPos"] = to_float(self.y_pos)
        result["ZNeg"] = to_float(self.z_neg)
        result["ZPos"] = to_float(self.z_pos)
        return result


class Voxel:
    """A Crystal Project voxel type classification. Has rendering and physics information for
    each voxel type.
    """
    bounce_velocity: float
    """If `IsBouncy`, how far do you bounce?"""

    bounding_boxes: List[BoundingBox]
    """If `CollidesSubUnit` is `true`, list the bounding boxes here."""

    collides: bool
    """Does this block collide with entities?"""

    collides_sub_unit: bool
    """If this block collides, does it have a precise hitbox?"""

    extends_action: bool
    """Does this extend actions?"""

    friction: float
    """The friction you experience walking on this block."""

    grows_on: int
    """The block this block 'grows on', or 0 if no such block.
    (this does imply that no blocks can grow on air.)
    """
    has_alpha_pixels: bool
    """Does this voxel render with opacity? Can you see through some pixels?"""

    has_facing: bool
    """Is the facing of this voxel important?"""

    id: int
    """The voxel ID. This is a 1-byte unsigned integer in world files."""

    is_bouncy: bool
    """Do you bounce when you step on this?"""

    is_burning: bool
    """Does this reset the player's position? `true` means the reset uses the fire animation."""

    is_invalid: bool
    """Should this voxel never be used in play?"""

    is_liquid: bool
    """Is this a liquid?"""

    is_prickly: bool
    """Do you get pushed off when you step on this?"""

    is_slide: bool
    """Do you slide off of this block when you step on it?"""

    is_spikes: bool
    """Does this reset the player's position? `true` means the reset uses the spikes animation."""

    is_water: bool
    """Is this water?"""

    is_window: bool
    """Is this considered a window?"""

    light_b: int
    """If `LightSource`, the color of the light. Blue channel."""

    light_g: int
    """If `LightSource`, the color of the light. Green channel."""

    light_r: int
    """If `LightSource`, the color of the light. Red channel."""

    light_source: bool
    """Does this voxel emit light?"""

    material: int
    """The material of this voxel. Determines things like noises. TODO - this is an enum, what
    are its values?
    """
    max_variant: int
    """How many variants exist for this voxel."""

    name: str
    """A human-readable name for this voxel. Not localized."""

    npc_floor: bool
    """Is this considered floor when this voxel is an NPC?"""

    occludes_geometry: bool
    """Does this voxel fully occlude geometry behind it?"""

    occludes_light: bool
    """Does this voxel fully block light behind it?"""

    partial_light_reduction: int
    """Does this voxel partially block light behind it? If so, how much?"""

    prickly_velocity: float
    """If `IsPrickly`, how far do you get pushed off?"""

    primitive_builder: int
    """The ID of the renderer used to render this voxel. TODO - this is an enum, what are its
    values?
    """
    sort_order: int
    """The order this is displayed in in the world editor (not that we have access to the world
    editor).
    """
    tex_bot_u: float
    """The U of the UV of the start point of the bottom face texture.
    The other UVs are determined by the primitive builder.
    """
    tex_bot_v: float
    """The V of the UV of the start point of the bottom face texture.
    The other UVs are determined by the primitive builder.
    """
    tex_side_u: float
    """The U of the UV of the start point of the side face texture.
    The other UVs are determined by the primitive builder.
    """
    tex_side_v: float
    """The V of the UV of the start point of the side face texture.
    The other UVs are determined by the primitive builder.
    """
    tex_top_u: float
    """The U of the UV of the start point of the top face texture.
    The other UVs are determined by the primitive builder.
    """
    tex_top_v: float
    """The V of the UV of the start point of the top face texture.
    The other UVs are determined by the primitive builder.
    """
    triggers_indoor: bool
    """Can this block count as "ceiling" for indoor camera calculation?"""

    visible: bool
    """Does this voxel render anything?"""

    walk_particle: int
    """The particles that appear when you walk on this voxel. 0 for no particles. TODO - this is
    an enum, what are its values?
    """

    def __init__(self, bounce_velocity: float, bounding_boxes: List[BoundingBox], collides: bool, collides_sub_unit: bool, extends_action: bool, friction: float, grows_on: int, has_alpha_pixels: bool, has_facing: bool, id: int, is_bouncy: bool, is_burning: bool, is_invalid: bool, is_liquid: bool, is_prickly: bool, is_slide: bool, is_spikes: bool, is_water: bool, is_window: bool, light_b: int, light_g: int, light_r: int, light_source: bool, material: int, max_variant: int, name: str, npc_floor: bool, occludes_geometry: bool, occludes_light: bool, partial_light_reduction: int, prickly_velocity: float, primitive_builder: int, sort_order: int, tex_bot_u: float, tex_bot_v: float, tex_side_u: float, tex_side_v: float, tex_top_u: float, tex_top_v: float, triggers_indoor: bool, visible: bool, walk_particle: int) -> None:
        self.bounce_velocity = bounce_velocity
        self.bounding_boxes = bounding_boxes
        self.collides = collides
        self.collides_sub_unit = collides_sub_unit
        self.extends_action = extends_action
        self.friction = friction
        self.grows_on = grows_on
        self.has_alpha_pixels = has_alpha_pixels
        self.has_facing = has_facing
        self.id = id
        self.is_bouncy = is_bouncy
        self.is_burning = is_burning
        self.is_invalid = is_invalid
        self.is_liquid = is_liquid
        self.is_prickly = is_prickly
        self.is_slide = is_slide
        self.is_spikes = is_spikes
        self.is_water = is_water
        self.is_window = is_window
        self.light_b = light_b
        self.light_g = light_g
        self.light_r = light_r
        self.light_source = light_source
        self.material = material
        self.max_variant = max_variant
        self.name = name
        self.npc_floor = npc_floor
        self.occludes_geometry = occludes_geometry
        self.occludes_light = occludes_light
        self.partial_light_reduction = partial_light_reduction
        self.prickly_velocity = prickly_velocity
        self.primitive_builder = primitive_builder
        self.sort_order = sort_order
        self.tex_bot_u = tex_bot_u
        self.tex_bot_v = tex_bot_v
        self.tex_side_u = tex_side_u
        self.tex_side_v = tex_side_v
        self.tex_top_u = tex_top_u
        self.tex_top_v = tex_top_v
        self.triggers_indoor = triggers_indoor
        self.visible = visible
        self.walk_particle = walk_particle

    @staticmethod
    def from_dict(obj: Any) -> 'Voxel':
        assert isinstance(obj, dict)
        bounce_velocity = from_float(obj.get("BounceVelocity"))
        bounding_boxes = from_list(BoundingBox.from_dict, obj.get("BoundingBoxes"))
        collides = from_bool(obj.get("Collides"))
        collides_sub_unit = from_bool(obj.get("CollidesSubUnit"))
        extends_action = from_bool(obj.get("ExtendsAction"))
        friction = from_float(obj.get("Friction"))
        grows_on = from_int(obj.get("GrowsOn"))
        has_alpha_pixels = from_bool(obj.get("HasAlphaPixels"))
        has_facing = from_bool(obj.get("HasFacing"))
        id = from_int(obj.get("ID"))
        is_bouncy = from_bool(obj.get("IsBouncy"))
        is_burning = from_bool(obj.get("IsBurning"))
        is_invalid = from_bool(obj.get("IsInvalid"))
        is_liquid = from_bool(obj.get("IsLiquid"))
        is_prickly = from_bool(obj.get("IsPrickly"))
        is_slide = from_bool(obj.get("IsSlide"))
        is_spikes = from_bool(obj.get("IsSpikes"))
        is_water = from_bool(obj.get("IsWater"))
        is_window = from_bool(obj.get("IsWindow"))
        light_b = from_int(obj.get("LightB"))
        light_g = from_int(obj.get("LightG"))
        light_r = from_int(obj.get("LightR"))
        light_source = from_bool(obj.get("LightSource"))
        material = from_int(obj.get("Material"))
        max_variant = from_int(obj.get("MaxVariant"))
        name = from_str(obj.get("Name"))
        npc_floor = from_bool(obj.get("NpcFloor"))
        occludes_geometry = from_bool(obj.get("OccludesGeometry"))
        occludes_light = from_bool(obj.get("OccludesLight"))
        partial_light_reduction = from_int(obj.get("PartialLightReduction"))
        prickly_velocity = from_float(obj.get("PricklyVelocity"))
        primitive_builder = from_int(obj.get("PrimitiveBuilder"))
        sort_order = from_int(obj.get("SortOrder"))
        tex_bot_u = from_float(obj.get("TexBotU"))
        tex_bot_v = from_float(obj.get("TexBotV"))
        tex_side_u = from_float(obj.get("TexSideU"))
        tex_side_v = from_float(obj.get("TexSideV"))
        tex_top_u = from_float(obj.get("TexTopU"))
        tex_top_v = from_float(obj.get("TexTopV"))
        triggers_indoor = from_bool(obj.get("TriggersIndoor"))
        visible = from_bool(obj.get("Visible"))
        walk_particle = from_int(obj.get("WalkParticle"))
        return Voxel(bounce_velocity, bounding_boxes, collides, collides_sub_unit, extends_action, friction, grows_on, has_alpha_pixels, has_facing, id, is_bouncy, is_burning, is_invalid, is_liquid, is_prickly, is_slide, is_spikes, is_water, is_window, light_b, light_g, light_r, light_source, material, max_variant, name, npc_floor, occludes_geometry, occludes_light, partial_light_reduction, prickly_velocity, primitive_builder, sort_order, tex_bot_u, tex_bot_v, tex_side_u, tex_side_v, tex_top_u, tex_top_v, triggers_indoor, visible, walk_particle)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BounceVelocity"] = to_float(self.bounce_velocity)
        result["BoundingBoxes"] = from_list(lambda x: to_class(BoundingBox, x), self.bounding_boxes)
        result["Collides"] = from_bool(self.collides)
        result["CollidesSubUnit"] = from_bool(self.collides_sub_unit)
        result["ExtendsAction"] = from_bool(self.extends_action)
        result["Friction"] = to_float(self.friction)
        result["GrowsOn"] = from_int(self.grows_on)
        result["HasAlphaPixels"] = from_bool(self.has_alpha_pixels)
        result["HasFacing"] = from_bool(self.has_facing)
        result["ID"] = from_int(self.id)
        result["IsBouncy"] = from_bool(self.is_bouncy)
        result["IsBurning"] = from_bool(self.is_burning)
        result["IsInvalid"] = from_bool(self.is_invalid)
        result["IsLiquid"] = from_bool(self.is_liquid)
        result["IsPrickly"] = from_bool(self.is_prickly)
        result["IsSlide"] = from_bool(self.is_slide)
        result["IsSpikes"] = from_bool(self.is_spikes)
        result["IsWater"] = from_bool(self.is_water)
        result["IsWindow"] = from_bool(self.is_window)
        result["LightB"] = from_int(self.light_b)
        result["LightG"] = from_int(self.light_g)
        result["LightR"] = from_int(self.light_r)
        result["LightSource"] = from_bool(self.light_source)
        result["Material"] = from_int(self.material)
        result["MaxVariant"] = from_int(self.max_variant)
        result["Name"] = from_str(self.name)
        result["NpcFloor"] = from_bool(self.npc_floor)
        result["OccludesGeometry"] = from_bool(self.occludes_geometry)
        result["OccludesLight"] = from_bool(self.occludes_light)
        result["PartialLightReduction"] = from_int(self.partial_light_reduction)
        result["PricklyVelocity"] = to_float(self.prickly_velocity)
        result["PrimitiveBuilder"] = from_int(self.primitive_builder)
        result["SortOrder"] = from_int(self.sort_order)
        result["TexBotU"] = to_float(self.tex_bot_u)
        result["TexBotV"] = to_float(self.tex_bot_v)
        result["TexSideU"] = to_float(self.tex_side_u)
        result["TexSideV"] = to_float(self.tex_side_v)
        result["TexTopU"] = to_float(self.tex_top_u)
        result["TexTopV"] = to_float(self.tex_top_v)
        result["TriggersIndoor"] = from_bool(self.triggers_indoor)
        result["Visible"] = from_bool(self.visible)
        result["WalkParticle"] = from_int(self.walk_particle)
        return result


def voxel_from_dict(s: Any) -> Voxel:
    return Voxel.from_dict(s)


def voxel_to_dict(x: Voxel) -> Any:
    return to_class(Voxel, x)
