from typing import Any, Optional, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
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


class GlobalIndexOrigin:
    """The position in the world `arena.dat` where the battle takes place."""

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
    def from_dict(obj: Any) -> 'GlobalIndexOrigin':
        assert isinstance(obj, dict)
        x = from_int(obj.get("X"))
        y = from_int(obj.get("Y"))
        z = from_int(obj.get("Z"))
        return GlobalIndexOrigin(x, y, z)

    def to_dict(self) -> dict:
        result: dict = {}
        result["X"] = from_int(self.x)
        result["Y"] = from_int(self.y)
        result["Z"] = from_int(self.z)
        return result


class ArenaClass:
    global_index_origin: GlobalIndexOrigin
    """The position in the world `arena.dat` where the battle takes place."""

    is_indoor: bool
    """Should indoor effects apply while fighting in this arena?"""

    is_underwater: bool
    """Should underwater effects apply while fighting in this arena?"""

    def __init__(self, global_index_origin: GlobalIndexOrigin, is_indoor: bool, is_underwater: bool) -> None:
        self.global_index_origin = global_index_origin
        self.is_indoor = is_indoor
        self.is_underwater = is_underwater

    @staticmethod
    def from_dict(obj: Any) -> 'ArenaClass':
        assert isinstance(obj, dict)
        global_index_origin = GlobalIndexOrigin.from_dict(obj.get("GlobalIndexOrigin"))
        is_indoor = from_bool(obj.get("IsIndoor"))
        is_underwater = from_bool(obj.get("IsUnderwater"))
        return ArenaClass(global_index_origin, is_indoor, is_underwater)

    def to_dict(self) -> dict:
        result: dict = {}
        result["GlobalIndexOrigin"] = to_class(GlobalIndexOrigin, self.global_index_origin)
        result["IsIndoor"] = from_bool(self.is_indoor)
        result["IsUnderwater"] = from_bool(self.is_underwater)
        return result


class IndColor:
    """A representative color of this map."""

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
    def from_dict(obj: Any) -> 'IndColor':
        assert isinstance(obj, dict)
        b = from_float(obj.get("B"))
        g = from_float(obj.get("G"))
        r = from_float(obj.get("R"))
        return IndColor(b, g, r)

    def to_dict(self) -> dict:
        result: dict = {}
        result["B"] = to_float(self.b)
        result["G"] = to_float(self.g)
        result["R"] = to_float(self.r)
        return result


class Biome:
    """A Crystal Project biome, which is a region of the map."""

    arena: Optional[ArenaClass]
    """Information about the outdoor arena."""

    arena_indoor: Optional[ArenaClass]
    """Information about the indoor arena."""

    base_id: int
    """The ID of a map that this map is contained as a part of, or 0 if not applicable.
    (Yes, this does imply that N/A can't ever be a base of any maps.)
    """
    battle_music_cue: Optional[int]
    """The battle music ID played in this biome."""

    boss_music_cue: Optional[int]
    """The boss music ID played in this biome."""

    camera_angle_offset: Optional[float]
    """The offset to the camera's angle in this biome."""

    camera_indoor_far_clip_is_black: Optional[bool]
    """Should the camera clip color be black?"""

    camera_indoor_far_clip_override: Optional[float]
    """The far clip value for the camera while in this biome."""

    camera_indoor_zoom_offset: Optional[float]
    """The offset to the camera's zoom level while indoors in this biome."""

    camera_zoom_offset: Optional[float]
    """The offset to the camera's zoom level in this biome."""

    disable_sunlight: Optional[bool]
    """Do we disable sunlight effects here?"""

    enable_camera_peeking: Optional[bool]
    """Can you press the bumpers to tilt the camera here?"""

    fog_b: Optional[int]
    """The fog color. Blue channel."""

    fog_far: Optional[float]
    """The distance the fog reaches full inensity."""

    fog_g: Optional[int]
    """The fog color. Green channel."""

    fog_near: Optional[float]
    """The distance the fog starts."""

    fog_r: Optional[int]
    """The fog color. Red channel."""

    force_is_indoor: Optional[bool]
    """Is this area entirely indoors?"""

    id: int
    """The ID of the biome.
    Has to fit within a single byte, or else maps won't load.
    """
    ind_color: IndColor
    """A representative color of this map."""

    indoor_height: Optional[int]
    """How tall the ceiling is to be considered indoors here."""

    inherent_status_id: Optional[int]
    """The ID of the status effect applied to everyone in this biome during battles."""

    inherent_status_message: Optional[str]
    """A message that appears when a battle starts in this biome."""

    is_in_demo: bool
    """Is this map part of the demo?"""

    is_map_alt: bool
    """Is this map an alternate version of another map?"""

    is_map_only: bool
    """Is this biome only for showing a single gestalt map to the player?"""

    map_center_x_override: Optional[int]
    """Is the center of this map different from the center of its bounding box? X coordinate."""

    map_center_y_override: Optional[int]
    """Is the center of this map different from the center of its bounding box? Z coordinate."""

    map_layer: int
    """The Z index for maps to draw with."""

    music_cue: Optional[int]
    """The music ID played in this biome."""

    name: str
    """The localizable name of the biome, as displayed to users."""

    sort_order: int
    """The order in which this biome appears in the biome selector in the map screen."""

    underwater_camera: Optional[bool]
    """Do we use the underwater camera effects here?"""

    weather_type: Optional[int]
    """The weather effect playing in this biome, if any."""

    world_b: Optional[int]
    """The background color. Blue channel."""

    world_bloom_intensity: Optional[float]
    """The intensity of the bloom effect in this biome."""

    world_bloom_threshold: Optional[float]
    """The threshold for the bloom effect in this biome."""

    world_g: Optional[int]
    """The background color. Green channel."""

    world_hdr_multiplier: Optional[float]
    """The multiplier to HDR while in this biome."""

    world_r: Optional[int]
    """The background color. Red channel."""

    def __init__(self, arena: Optional[ArenaClass], arena_indoor: Optional[ArenaClass], base_id: int, battle_music_cue: Optional[int], boss_music_cue: Optional[int], camera_angle_offset: Optional[float], camera_indoor_far_clip_is_black: Optional[bool], camera_indoor_far_clip_override: Optional[float], camera_indoor_zoom_offset: Optional[float], camera_zoom_offset: Optional[float], disable_sunlight: Optional[bool], enable_camera_peeking: Optional[bool], fog_b: Optional[int], fog_far: Optional[float], fog_g: Optional[int], fog_near: Optional[float], fog_r: Optional[int], force_is_indoor: Optional[bool], id: int, ind_color: IndColor, indoor_height: Optional[int], inherent_status_id: Optional[int], inherent_status_message: Optional[str], is_in_demo: bool, is_map_alt: bool, is_map_only: bool, map_center_x_override: Optional[int], map_center_y_override: Optional[int], map_layer: int, music_cue: Optional[int], name: str, sort_order: int, underwater_camera: Optional[bool], weather_type: Optional[int], world_b: Optional[int], world_bloom_intensity: Optional[float], world_bloom_threshold: Optional[float], world_g: Optional[int], world_hdr_multiplier: Optional[float], world_r: Optional[int]) -> None:
        self.arena = arena
        self.arena_indoor = arena_indoor
        self.base_id = base_id
        self.battle_music_cue = battle_music_cue
        self.boss_music_cue = boss_music_cue
        self.camera_angle_offset = camera_angle_offset
        self.camera_indoor_far_clip_is_black = camera_indoor_far_clip_is_black
        self.camera_indoor_far_clip_override = camera_indoor_far_clip_override
        self.camera_indoor_zoom_offset = camera_indoor_zoom_offset
        self.camera_zoom_offset = camera_zoom_offset
        self.disable_sunlight = disable_sunlight
        self.enable_camera_peeking = enable_camera_peeking
        self.fog_b = fog_b
        self.fog_far = fog_far
        self.fog_g = fog_g
        self.fog_near = fog_near
        self.fog_r = fog_r
        self.force_is_indoor = force_is_indoor
        self.id = id
        self.ind_color = ind_color
        self.indoor_height = indoor_height
        self.inherent_status_id = inherent_status_id
        self.inherent_status_message = inherent_status_message
        self.is_in_demo = is_in_demo
        self.is_map_alt = is_map_alt
        self.is_map_only = is_map_only
        self.map_center_x_override = map_center_x_override
        self.map_center_y_override = map_center_y_override
        self.map_layer = map_layer
        self.music_cue = music_cue
        self.name = name
        self.sort_order = sort_order
        self.underwater_camera = underwater_camera
        self.weather_type = weather_type
        self.world_b = world_b
        self.world_bloom_intensity = world_bloom_intensity
        self.world_bloom_threshold = world_bloom_threshold
        self.world_g = world_g
        self.world_hdr_multiplier = world_hdr_multiplier
        self.world_r = world_r

    @staticmethod
    def from_dict(obj: Any) -> 'Biome':
        assert isinstance(obj, dict)
        arena = from_union([from_none, ArenaClass.from_dict], obj.get("Arena"))
        arena_indoor = from_union([from_none, ArenaClass.from_dict], obj.get("ArenaIndoor"))
        base_id = from_int(obj.get("BaseID"))
        battle_music_cue = from_union([from_none, from_int], obj.get("BattleMusicCue"))
        boss_music_cue = from_union([from_none, from_int], obj.get("BossMusicCue"))
        camera_angle_offset = from_union([from_none, from_float], obj.get("CameraAngleOffset"))
        camera_indoor_far_clip_is_black = from_union([from_none, from_bool], obj.get("CameraIndoorFarClipIsBlack"))
        camera_indoor_far_clip_override = from_union([from_none, from_float], obj.get("CameraIndoorFarClipOverride"))
        camera_indoor_zoom_offset = from_union([from_none, from_float], obj.get("CameraIndoorZoomOffset"))
        camera_zoom_offset = from_union([from_none, from_float], obj.get("CameraZoomOffset"))
        disable_sunlight = from_union([from_none, from_bool], obj.get("DisableSunlight"))
        enable_camera_peeking = from_union([from_none, from_bool], obj.get("EnableCameraPeeking"))
        fog_b = from_union([from_none, from_int], obj.get("FogB"))
        fog_far = from_union([from_none, from_float], obj.get("FogFar"))
        fog_g = from_union([from_none, from_int], obj.get("FogG"))
        fog_near = from_union([from_none, from_float], obj.get("FogNear"))
        fog_r = from_union([from_none, from_int], obj.get("FogR"))
        force_is_indoor = from_union([from_none, from_bool], obj.get("ForceIsIndoor"))
        id = from_int(obj.get("ID"))
        ind_color = IndColor.from_dict(obj.get("IndColor"))
        indoor_height = from_union([from_none, from_int], obj.get("IndoorHeight"))
        inherent_status_id = from_union([from_none, from_int], obj.get("InherentStatusID"))
        inherent_status_message = from_union([from_none, from_str], obj.get("InherentStatusMessage"))
        is_in_demo = from_bool(obj.get("IsInDemo"))
        is_map_alt = from_bool(obj.get("IsMapAlt"))
        is_map_only = from_bool(obj.get("IsMapOnly"))
        map_center_x_override = from_union([from_none, from_int], obj.get("MapCenterXOverride"))
        map_center_y_override = from_union([from_none, from_int], obj.get("MapCenterYOverride"))
        map_layer = from_int(obj.get("MapLayer"))
        music_cue = from_union([from_none, from_int], obj.get("MusicCue"))
        name = from_str(obj.get("Name"))
        sort_order = from_int(obj.get("SortOrder"))
        underwater_camera = from_union([from_none, from_bool], obj.get("UnderwaterCamera"))
        weather_type = from_union([from_none, from_int], obj.get("WeatherType"))
        world_b = from_union([from_none, from_int], obj.get("WorldB"))
        world_bloom_intensity = from_union([from_none, from_float], obj.get("WorldBloomIntensity"))
        world_bloom_threshold = from_union([from_none, from_float], obj.get("WorldBloomThreshold"))
        world_g = from_union([from_none, from_int], obj.get("WorldG"))
        world_hdr_multiplier = from_union([from_none, from_float], obj.get("WorldHdrMultiplier"))
        world_r = from_union([from_none, from_int], obj.get("WorldR"))
        return Biome(arena, arena_indoor, base_id, battle_music_cue, boss_music_cue, camera_angle_offset, camera_indoor_far_clip_is_black, camera_indoor_far_clip_override, camera_indoor_zoom_offset, camera_zoom_offset, disable_sunlight, enable_camera_peeking, fog_b, fog_far, fog_g, fog_near, fog_r, force_is_indoor, id, ind_color, indoor_height, inherent_status_id, inherent_status_message, is_in_demo, is_map_alt, is_map_only, map_center_x_override, map_center_y_override, map_layer, music_cue, name, sort_order, underwater_camera, weather_type, world_b, world_bloom_intensity, world_bloom_threshold, world_g, world_hdr_multiplier, world_r)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Arena"] = from_union([from_none, lambda x: to_class(ArenaClass, x)], self.arena)
        result["ArenaIndoor"] = from_union([from_none, lambda x: to_class(ArenaClass, x)], self.arena_indoor)
        result["BaseID"] = from_int(self.base_id)
        result["BattleMusicCue"] = from_union([from_none, from_int], self.battle_music_cue)
        result["BossMusicCue"] = from_union([from_none, from_int], self.boss_music_cue)
        result["CameraAngleOffset"] = from_union([from_none, to_float], self.camera_angle_offset)
        result["CameraIndoorFarClipIsBlack"] = from_union([from_none, from_bool], self.camera_indoor_far_clip_is_black)
        result["CameraIndoorFarClipOverride"] = from_union([from_none, to_float], self.camera_indoor_far_clip_override)
        result["CameraIndoorZoomOffset"] = from_union([from_none, to_float], self.camera_indoor_zoom_offset)
        result["CameraZoomOffset"] = from_union([from_none, to_float], self.camera_zoom_offset)
        result["DisableSunlight"] = from_union([from_none, from_bool], self.disable_sunlight)
        result["EnableCameraPeeking"] = from_union([from_none, from_bool], self.enable_camera_peeking)
        result["FogB"] = from_union([from_none, from_int], self.fog_b)
        result["FogFar"] = from_union([from_none, to_float], self.fog_far)
        result["FogG"] = from_union([from_none, from_int], self.fog_g)
        result["FogNear"] = from_union([from_none, to_float], self.fog_near)
        result["FogR"] = from_union([from_none, from_int], self.fog_r)
        result["ForceIsIndoor"] = from_union([from_none, from_bool], self.force_is_indoor)
        result["ID"] = from_int(self.id)
        result["IndColor"] = to_class(IndColor, self.ind_color)
        result["IndoorHeight"] = from_union([from_none, from_int], self.indoor_height)
        result["InherentStatusID"] = from_union([from_none, from_int], self.inherent_status_id)
        result["InherentStatusMessage"] = from_union([from_none, from_str], self.inherent_status_message)
        result["IsInDemo"] = from_bool(self.is_in_demo)
        result["IsMapAlt"] = from_bool(self.is_map_alt)
        result["IsMapOnly"] = from_bool(self.is_map_only)
        result["MapCenterXOverride"] = from_union([from_none, from_int], self.map_center_x_override)
        result["MapCenterYOverride"] = from_union([from_none, from_int], self.map_center_y_override)
        result["MapLayer"] = from_int(self.map_layer)
        result["MusicCue"] = from_union([from_none, from_int], self.music_cue)
        result["Name"] = from_str(self.name)
        result["SortOrder"] = from_int(self.sort_order)
        result["UnderwaterCamera"] = from_union([from_none, from_bool], self.underwater_camera)
        result["WeatherType"] = from_union([from_none, from_int], self.weather_type)
        result["WorldB"] = from_union([from_none, from_int], self.world_b)
        result["WorldBloomIntensity"] = from_union([from_none, to_float], self.world_bloom_intensity)
        result["WorldBloomThreshold"] = from_union([from_none, to_float], self.world_bloom_threshold)
        result["WorldG"] = from_union([from_none, from_int], self.world_g)
        result["WorldHdrMultiplier"] = from_union([from_none, to_float], self.world_hdr_multiplier)
        result["WorldR"] = from_union([from_none, from_int], self.world_r)
        return result


def biome_from_dict(s: Any) -> Biome:
    return Biome.from_dict(s)


def biome_to_dict(x: Biome) -> Any:
    return to_class(Biome, x)
