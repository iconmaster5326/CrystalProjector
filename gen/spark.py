from typing import Any, List, Optional, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class WanderRoutePoint:
    """A point on the wander route."""

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
    def from_dict(obj: Any) -> 'WanderRoutePoint':
        assert isinstance(obj, dict)
        x = from_int(obj.get("X"))
        y = from_int(obj.get("Y"))
        z = from_int(obj.get("Z"))
        return WanderRoutePoint(x, y, z)

    def to_dict(self) -> dict:
        result: dict = {}
        result["X"] = from_int(self.x)
        result["Y"] = from_int(self.y)
        result["Z"] = from_int(self.z)
        return result


class Spark:
    """A Crystal Project spark behaviour definition.
    This ONLY indicates spark movement patterns and physics.
    This does NOT indicate what sparks are where in the world, or what troops you fight!
    That information is contained in the world entities files.
    """
    aggro_accel: float
    """The acceleration of the spark while it's in the aggro phase."""

    aggro_dist: float
    """The distance the spark can become aggro in."""

    aggro_max_time: int
    """The time it takes for the spark to go back to the alert phase."""

    aggro_speed: float
    """The speed of the spark while it's in the aggro phase."""

    alert_accel: float
    """The acceleration of the spark while it's in the alert phase."""

    alert_dist: float
    """The distance the spark can become alerted in."""

    alert_speed: float
    """The speed of the spark while it's in the alert phase."""

    alert_to_aggro_time: int
    """The time it takes for the spark to aggro."""

    area_shape: int
    """The shape of this spark's active area."""

    hazard_immune: bool
    """Does this spark not die when it touches fire/spikes?"""

    id: int
    """The unique ID of this spark."""

    is_flying: bool
    """Can this spark fly?"""

    jump_height: int
    """How high can this spark jump?"""

    name: str
    """The name of this spark. Not displayed to users."""

    requires_los: bool
    """Does this spark need line of sight to aggro?"""

    requires_movement: bool
    """Does this spark only aggro if the player moves in range?"""

    runs_away: bool
    """Does this spark flee the player?"""

    swim_type: int
    """How this spark handles water."""

    unaggro_dist: float
    """The distance the spark loses aggro from."""

    unaggro_time: int
    """The time it takes for the spark to exit the aggro phase."""

    unalert_dist: float
    """The distance the spark loses alert from."""

    unalert_time: int
    """The time it takes for the spark to exit the alert phase."""

    wander_accel: float
    """The acceleration of the wandering."""

    wander_interval: int
    """The wait time between wander points."""

    wander_radius: float
    """The radius of the wander area."""

    wander_route: Optional[List[WanderRoutePoint]]
    """The fixed route this spark moves on."""

    wander_route_is_line: bool
    """Is the route a straight line?"""

    wander_speed: float
    """How quickly the spark wanders."""

    wander_type: int
    """How does this spark wander around, if at all?"""

    withdraw_accel: float
    """The acceleration of the spark while it's in the withdraw phase."""

    withdraw_min_time: int
    """The time it takes for the spark to exit the withdraw phase."""

    withdraw_speed: float
    """The speed of the spark while it's in the withdraw phase."""

    def __init__(self, aggro_accel: float, aggro_dist: float, aggro_max_time: int, aggro_speed: float, alert_accel: float, alert_dist: float, alert_speed: float, alert_to_aggro_time: int, area_shape: int, hazard_immune: bool, id: int, is_flying: bool, jump_height: int, name: str, requires_los: bool, requires_movement: bool, runs_away: bool, swim_type: int, unaggro_dist: float, unaggro_time: int, unalert_dist: float, unalert_time: int, wander_accel: float, wander_interval: int, wander_radius: float, wander_route: Optional[List[WanderRoutePoint]], wander_route_is_line: bool, wander_speed: float, wander_type: int, withdraw_accel: float, withdraw_min_time: int, withdraw_speed: float) -> None:
        self.aggro_accel = aggro_accel
        self.aggro_dist = aggro_dist
        self.aggro_max_time = aggro_max_time
        self.aggro_speed = aggro_speed
        self.alert_accel = alert_accel
        self.alert_dist = alert_dist
        self.alert_speed = alert_speed
        self.alert_to_aggro_time = alert_to_aggro_time
        self.area_shape = area_shape
        self.hazard_immune = hazard_immune
        self.id = id
        self.is_flying = is_flying
        self.jump_height = jump_height
        self.name = name
        self.requires_los = requires_los
        self.requires_movement = requires_movement
        self.runs_away = runs_away
        self.swim_type = swim_type
        self.unaggro_dist = unaggro_dist
        self.unaggro_time = unaggro_time
        self.unalert_dist = unalert_dist
        self.unalert_time = unalert_time
        self.wander_accel = wander_accel
        self.wander_interval = wander_interval
        self.wander_radius = wander_radius
        self.wander_route = wander_route
        self.wander_route_is_line = wander_route_is_line
        self.wander_speed = wander_speed
        self.wander_type = wander_type
        self.withdraw_accel = withdraw_accel
        self.withdraw_min_time = withdraw_min_time
        self.withdraw_speed = withdraw_speed

    @staticmethod
    def from_dict(obj: Any) -> 'Spark':
        assert isinstance(obj, dict)
        aggro_accel = from_float(obj.get("AggroAccel"))
        aggro_dist = from_float(obj.get("AggroDist"))
        aggro_max_time = from_int(obj.get("AggroMaxTime"))
        aggro_speed = from_float(obj.get("AggroSpeed"))
        alert_accel = from_float(obj.get("AlertAccel"))
        alert_dist = from_float(obj.get("AlertDist"))
        alert_speed = from_float(obj.get("AlertSpeed"))
        alert_to_aggro_time = from_int(obj.get("AlertToAggroTime"))
        area_shape = from_int(obj.get("AreaShape"))
        hazard_immune = from_bool(obj.get("HazardImmune"))
        id = from_int(obj.get("ID"))
        is_flying = from_bool(obj.get("IsFlying"))
        jump_height = from_int(obj.get("JumpHeight"))
        name = from_str(obj.get("Name"))
        requires_los = from_bool(obj.get("RequiresLos"))
        requires_movement = from_bool(obj.get("RequiresMovement"))
        runs_away = from_bool(obj.get("RunsAway"))
        swim_type = from_int(obj.get("SwimType"))
        unaggro_dist = from_float(obj.get("UnaggroDist"))
        unaggro_time = from_int(obj.get("UnaggroTime"))
        unalert_dist = from_float(obj.get("UnalertDist"))
        unalert_time = from_int(obj.get("UnalertTime"))
        wander_accel = from_float(obj.get("WanderAccel"))
        wander_interval = from_int(obj.get("WanderInterval"))
        wander_radius = from_float(obj.get("WanderRadius"))
        wander_route = from_union([from_none, lambda x: from_list(WanderRoutePoint.from_dict, x)], obj.get("WanderRoute"))
        wander_route_is_line = from_bool(obj.get("WanderRouteIsLine"))
        wander_speed = from_float(obj.get("WanderSpeed"))
        wander_type = from_int(obj.get("WanderType"))
        withdraw_accel = from_float(obj.get("WithdrawAccel"))
        withdraw_min_time = from_int(obj.get("WithdrawMinTime"))
        withdraw_speed = from_float(obj.get("WithdrawSpeed"))
        return Spark(aggro_accel, aggro_dist, aggro_max_time, aggro_speed, alert_accel, alert_dist, alert_speed, alert_to_aggro_time, area_shape, hazard_immune, id, is_flying, jump_height, name, requires_los, requires_movement, runs_away, swim_type, unaggro_dist, unaggro_time, unalert_dist, unalert_time, wander_accel, wander_interval, wander_radius, wander_route, wander_route_is_line, wander_speed, wander_type, withdraw_accel, withdraw_min_time, withdraw_speed)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AggroAccel"] = to_float(self.aggro_accel)
        result["AggroDist"] = to_float(self.aggro_dist)
        result["AggroMaxTime"] = from_int(self.aggro_max_time)
        result["AggroSpeed"] = to_float(self.aggro_speed)
        result["AlertAccel"] = to_float(self.alert_accel)
        result["AlertDist"] = to_float(self.alert_dist)
        result["AlertSpeed"] = to_float(self.alert_speed)
        result["AlertToAggroTime"] = from_int(self.alert_to_aggro_time)
        result["AreaShape"] = from_int(self.area_shape)
        result["HazardImmune"] = from_bool(self.hazard_immune)
        result["ID"] = from_int(self.id)
        result["IsFlying"] = from_bool(self.is_flying)
        result["JumpHeight"] = from_int(self.jump_height)
        result["Name"] = from_str(self.name)
        result["RequiresLos"] = from_bool(self.requires_los)
        result["RequiresMovement"] = from_bool(self.requires_movement)
        result["RunsAway"] = from_bool(self.runs_away)
        result["SwimType"] = from_int(self.swim_type)
        result["UnaggroDist"] = to_float(self.unaggro_dist)
        result["UnaggroTime"] = from_int(self.unaggro_time)
        result["UnalertDist"] = to_float(self.unalert_dist)
        result["UnalertTime"] = from_int(self.unalert_time)
        result["WanderAccel"] = to_float(self.wander_accel)
        result["WanderInterval"] = from_int(self.wander_interval)
        result["WanderRadius"] = to_float(self.wander_radius)
        result["WanderRoute"] = from_union([from_none, lambda x: from_list(lambda x: to_class(WanderRoutePoint, x), x)], self.wander_route)
        result["WanderRouteIsLine"] = from_bool(self.wander_route_is_line)
        result["WanderSpeed"] = to_float(self.wander_speed)
        result["WanderType"] = from_int(self.wander_type)
        result["WithdrawAccel"] = to_float(self.withdraw_accel)
        result["WithdrawMinTime"] = from_int(self.withdraw_min_time)
        result["WithdrawSpeed"] = to_float(self.withdraw_speed)
        return result


def spark_from_dict(s: Any) -> Spark:
    return Spark.from_dict(s)


def spark_to_dict(x: Spark) -> Any:
    return to_class(Spark, x)
