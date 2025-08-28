from typing import Any, Optional, List, TypeVar, Type, cast, Callable


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


class Color:
    """The color of this flash."""

    a: float
    """The alpha channel."""

    b: float
    """The blue channel."""

    g: float
    """The green channel."""

    r: float
    """The red channel."""

    def __init__(self, a: float, b: float, g: float, r: float) -> None:
        self.a = a
        self.b = b
        self.g = g
        self.r = r

    @staticmethod
    def from_dict(obj: Any) -> 'Color':
        assert isinstance(obj, dict)
        a = from_float(obj.get("A"))
        b = from_float(obj.get("B"))
        g = from_float(obj.get("G"))
        r = from_float(obj.get("R"))
        return Color(a, b, g, r)

    def to_dict(self) -> dict:
        result: dict = {}
        result["A"] = to_float(self.a)
        result["B"] = to_float(self.b)
        result["G"] = to_float(self.g)
        result["R"] = to_float(self.r)
        return result


class Flash:
    """A target flash effect."""

    color: Color
    """The color of this flash."""

    duration: int
    """How long this flash lasts."""

    frame: int
    """The frame at which this flash occurs."""

    scope: int
    """Who the flash applies to."""

    def __init__(self, color: Color, duration: int, frame: int, scope: int) -> None:
        self.color = color
        self.duration = duration
        self.frame = frame
        self.scope = scope

    @staticmethod
    def from_dict(obj: Any) -> 'Flash':
        assert isinstance(obj, dict)
        color = Color.from_dict(obj.get("Color"))
        duration = from_int(obj.get("Duration"))
        frame = from_int(obj.get("Frame"))
        scope = from_int(obj.get("Scope"))
        return Flash(color, duration, frame, scope)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Color"] = to_class(Color, self.color)
        result["Duration"] = from_int(self.duration)
        result["Frame"] = from_int(self.frame)
        result["Scope"] = from_int(self.scope)
        return result


class FrameImage:
    """A frame of the animation.
    
    An image displayed during this frame of the animation.
    """
    blend: int
    """The opacity blending mode for this animation cell."""

    interpolate: bool
    """Interpolate these values between this frame and the next?"""

    mirror: bool
    """Mirror the animation cell along the X axis?"""

    opacity: int
    """The opacity of the animation cell. 0 (default) to 255 (invisible)."""

    pattern: int
    """The animation cell to use."""

    rotation: int
    """The rotation to apply to the animation cell, in degrees."""

    scale: int
    """The scaling factor to apply to the animation cell. 100 is default."""

    texture_index: int
    """The index into `Images` to use. A texture."""

    x: int
    """The X offset from the anchor to display this animation cell."""

    y: int
    """The Y offset from the anchor to display this animation cell."""

    def __init__(self, blend: int, interpolate: bool, mirror: bool, opacity: int, pattern: int, rotation: int, scale: int, texture_index: int, x: int, y: int) -> None:
        self.blend = blend
        self.interpolate = interpolate
        self.mirror = mirror
        self.opacity = opacity
        self.pattern = pattern
        self.rotation = rotation
        self.scale = scale
        self.texture_index = texture_index
        self.x = x
        self.y = y

    @staticmethod
    def from_dict(obj: Any) -> 'FrameImage':
        assert isinstance(obj, dict)
        blend = from_int(obj.get("Blend"))
        interpolate = from_bool(obj.get("Interpolate"))
        mirror = from_bool(obj.get("Mirror"))
        opacity = from_int(obj.get("Opacity"))
        pattern = from_int(obj.get("Pattern"))
        rotation = from_int(obj.get("Rotation"))
        scale = from_int(obj.get("Scale"))
        texture_index = from_int(obj.get("TextureIndex"))
        x = from_int(obj.get("X"))
        y = from_int(obj.get("Y"))
        return FrameImage(blend, interpolate, mirror, opacity, pattern, rotation, scale, texture_index, x, y)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Blend"] = from_int(self.blend)
        result["Interpolate"] = from_bool(self.interpolate)
        result["Mirror"] = from_bool(self.mirror)
        result["Opacity"] = from_int(self.opacity)
        result["Pattern"] = from_int(self.pattern)
        result["Rotation"] = from_int(self.rotation)
        result["Scale"] = from_int(self.scale)
        result["TextureIndex"] = from_int(self.texture_index)
        result["X"] = from_int(self.x)
        result["Y"] = from_int(self.y)
        return result


class Image:
    """A image used in the animation. Textures are split up into one or more _cells_.
    Animation cells are packed back to back horizontally, and then vertically.
    
    For example, an image with `CellCountX` of 5, a `CellWidth` of 100,
    and a `CellHeight` of 100, and is a 500x300 file,
    will have 15 animation cells.
    """
    cell_count_x: int
    """The number of animation cells in one row of this texture.
    The image's total height determines how many total cells there are.
    """
    cell_height: int
    """The height of each cell in the texture, in pixels."""

    cell_width: int
    """The width of each cell in the texture, in pixels."""

    hue: int
    """Any hue shifting that occurs with this texture."""

    path: Optional[str]
    """The texture's pack, followed by a slash, followed by the texture's name."""

    def __init__(self, cell_count_x: int, cell_height: int, cell_width: int, hue: int, path: Optional[str]) -> None:
        self.cell_count_x = cell_count_x
        self.cell_height = cell_height
        self.cell_width = cell_width
        self.hue = hue
        self.path = path

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        cell_count_x = from_int(obj.get("CellCountX"))
        cell_height = from_int(obj.get("CellHeight"))
        cell_width = from_int(obj.get("CellWidth"))
        hue = from_int(obj.get("Hue"))
        path = from_union([from_none, from_str], obj.get("Path"))
        return Image(cell_count_x, cell_height, cell_width, hue, path)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CellCountX"] = from_int(self.cell_count_x)
        result["CellHeight"] = from_int(self.cell_height)
        result["CellWidth"] = from_int(self.cell_width)
        result["Hue"] = from_int(self.hue)
        result["Path"] = from_union([from_none, from_str], self.path)
        return result


class Sound:
    """A sound effect."""

    frame: int
    """The frame at which this sound starts playing."""

    name: str
    """The name of this sound effect, as appearing in `se.dat`."""

    pan: int
    """The pan shifting of the sound effect."""

    pitch: int
    """The pitch shifting of the sound effect."""

    volume: int
    """The volume of the sound effect. A percentage, default 100."""

    def __init__(self, frame: int, name: str, pan: int, pitch: int, volume: int) -> None:
        self.frame = frame
        self.name = name
        self.pan = pan
        self.pitch = pitch
        self.volume = volume

    @staticmethod
    def from_dict(obj: Any) -> 'Sound':
        assert isinstance(obj, dict)
        frame = from_int(obj.get("Frame"))
        name = from_str(obj.get("Name"))
        pan = from_int(obj.get("Pan"))
        pitch = from_int(obj.get("Pitch"))
        volume = from_int(obj.get("Volume"))
        return Sound(frame, name, pan, pitch, volume)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Frame"] = from_int(self.frame)
        result["Name"] = from_str(self.name)
        result["Pan"] = from_int(self.pan)
        result["Pitch"] = from_int(self.pitch)
        result["Volume"] = from_int(self.volume)
        return result


class Animation:
    """A Crystal Project animation definition.
    These play in combat when you execute actions.
    Consists of a series of frames that play in sequence,
    along with flash and sound information.
    """
    flashes: List[Flash]
    """Sometimes the target flashes a color. These control how and when."""

    fps: int
    """The frames per second the animation plays at."""

    frames: List[List[FrameImage]]
    """The frames of this animation."""

    id: int
    """The ID of this animation."""

    images: List[Image]
    """The images that are used in this animation."""

    mirror_for_monster_use: bool
    """Should this animation play flipped along the X axis if used on an enemy as opposed to a
    player?
    """
    name: str
    """The name of this animation. Does not appear in-game, so does not need localized."""

    position: int
    """The alignment of this animation relative to the target."""

    sounds: List[Sound]
    """Sometimes sounds play during an animation. These control how and when."""

    def __init__(self, flashes: List[Flash], fps: int, frames: List[List[FrameImage]], id: int, images: List[Image], mirror_for_monster_use: bool, name: str, position: int, sounds: List[Sound]) -> None:
        self.flashes = flashes
        self.fps = fps
        self.frames = frames
        self.id = id
        self.images = images
        self.mirror_for_monster_use = mirror_for_monster_use
        self.name = name
        self.position = position
        self.sounds = sounds

    @staticmethod
    def from_dict(obj: Any) -> 'Animation':
        assert isinstance(obj, dict)
        flashes = from_list(Flash.from_dict, obj.get("Flashes"))
        fps = from_int(obj.get("FPS"))
        frames = from_list(lambda x: from_list(FrameImage.from_dict, x), obj.get("Frames"))
        id = from_int(obj.get("ID"))
        images = from_list(Image.from_dict, obj.get("Images"))
        mirror_for_monster_use = from_bool(obj.get("MirrorForMonsterUse"))
        name = from_str(obj.get("Name"))
        position = from_int(obj.get("Position"))
        sounds = from_list(Sound.from_dict, obj.get("Sounds"))
        return Animation(flashes, fps, frames, id, images, mirror_for_monster_use, name, position, sounds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Flashes"] = from_list(lambda x: to_class(Flash, x), self.flashes)
        result["FPS"] = from_int(self.fps)
        result["Frames"] = from_list(lambda x: from_list(lambda x: to_class(FrameImage, x), x), self.frames)
        result["ID"] = from_int(self.id)
        result["Images"] = from_list(lambda x: to_class(Image, x), self.images)
        result["MirrorForMonsterUse"] = from_bool(self.mirror_for_monster_use)
        result["Name"] = from_str(self.name)
        result["Position"] = from_int(self.position)
        result["Sounds"] = from_list(lambda x: to_class(Sound, x), self.sounds)
        return result


def animation_from_dict(s: Any) -> Animation:
    return Animation.from_dict(s)


def animation_to_dict(x: Animation) -> Any:
    return to_class(Animation, x)
