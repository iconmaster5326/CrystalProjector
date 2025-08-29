# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import vlq_base128_le
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Entities(KaitaiStruct):
    """A file of the form `yXe.dat`, that lists all entities in a 16x16x16 cube chunk, for the chunk at y level X."""

    class Action(IntEnum):
        face_player = 0
        message = 1
        revert_facing = 2
        condition = 3
        wait = 4
        shop = 5
        set_flag = 6
        set_number = 7
        add_inventory = 8
        remove_inventory = 9
        stop_processing = 10
        set_npc_property = 11
        move = 12
        ability = 13
        choice_message = 14
        inn = 15
        add_number = 16
        multiply_number = 17
        command_npc = 18
        trigger_npc = 19
        move_camera = 20
        revert_camera = 21
        context_switch = 22
        do_narration = 23
        set_facing = 24
        set_player_facing = 25
        set_mount = 26
        battle = 27
        shop_recipe = 28
        shop_service = 29
        refresh_lost_and_found = 30
        move_player = 31
        unlock_ability = 32
        move_to = 33
        move_player_to = 34
        future_actions = 35
        cancel_actions = 36
        queue_future_actions = 37
        play_music = 38
        stop_music = 39
        revert_music = 40
        activity_countdown = 41
        teleport_player_to = 42
        refresh_npcs = 43
        move_group = 44
        move_away_from_player = 45
        move_group_to = 46
        set_last_safe_pos_to_marker = 47
        refresh_specific_npcs = 48
        play_se_switch_pressed = 49
        play_se_switch_unpressed = 50
        teleport_player = 51
        refresh_bulletin = 52
        move_player_instant = 53
        particle = 54
        insert_future_actions = 55
        set_player_facing_to_this = 56
        credits = 57
        add_to_lost_and_found = 58
        play_se_mine_ore = 59
        make_player_face_this = 60
        message_anonymous = 61
        face_away_from_player = 62
        my_quintar = 63
        subtract_number = 64
        message_npc = 65
        cancel_wander = 66
        resume_wander = 67
        choice_message_anonymous = 68
        hazard_burn = 69
        set_last_safe_pos_to = 70
        garden = 71
        new_game_plus = 72
        message_hint = 73
        unlock_job = 74
        unlock_passive = 75
        learn_ability = 76
        learn_passive = 77
        comment = 78

    class Collision(IntEnum):
        none = 0
        one_way_to = 1
        one_way_from = 2
        full = 3

    class ConditionOperator(IntEnum):
        and_ = 0
        or_ = 1
        xor = 2
        equiv = 3
        impl = 4

    class ConditionType(IntEnum):
        always = 0
        never = 1
        operation = 2
        check_flag = 3
        check_number = 4
        check_inventory = 5
        finished_moving = 6
        check_crystal_count = 7
        is_riding_quintar = 8
        lost_and_found_has_stock = 9
        random = 10
        is_job_present = 11
        check_highest_member_level = 12
        is_ability_unlocked = 13
        can_understand_quintar = 14
        check_npc_proximity = 15
        is_riding_default_quintar = 16
        check_atlas = 17
        is_demo = 18
        my_quintar = 19
        is_riding_specific_mount = 20
        is_job_mastered = 21
        previous_battle_was_victory = 22
        garden = 23
        is_player_stranded = 24
        skip_minigames = 25
        is_player_gender = 26
        is_member_present = 27
        is_game_cleared = 28
        randomizer = 29
        is_patch_mode_active = 30
        is_passive_unlocked = 31
        is_ability_learned = 32
        is_passive_learned = 33
        is_facing = 34
        is_player_facing = 35

    class DoorStyle(IntEnum):
        boroboro = 0
        cell = 1
        stone = 2
        wood = 3
        red = 4
        cell_cross = 5
        boroboro_window = 6
        red_window = 7
        metal = 8
        ornate = 9
        sun_stone = 10
        moon_stone = 11
        paper = 12

    class EntityType(IntEnum):
        npc = 0
        sign = 1
        spark = 2
        door = 3
        home_point = 4
        treasure = 5
        crystal = 6
        marker = 7

    class Facing(IntEnum):
        xneg = 0
        yneg = 1
        zneg = 2
        xpos = 3
        ypos = 4
        zpos = 5

    class Jump(IntEnum):
        none = 0
        up_voxel = 1
        up_actor = 2
        up_voxel_and_actor = 3
        off_voxel = 4
        up_voxel_off_voxel = 5
        off_actor = 6
        off_voxel_and_actor = 7
        full = 8

    class Physics(IntEnum):
        player_foot = 0
        quintar_default = 1
        salmon_default = 2
        owl_default = 3
        ibek_default = 4
        salmon_rental = 5
        salmon_royal = 6
        quintar_rental = 7
        quintar_desert = 8
        salmon_lava = 9
        quintar_float = 10
        quintar_jump = 11
        quintar_fly = 12
        quintar_swim = 13
        quintar_gold = 14
        npc_foot = 15
        npc_flying = 16
        npc_salmon_fast = 17
        npc_salmon_medium = 18
        npc_salmon_slow = 19
        npc_free = 20
        npc_push_block = 21
        npc_quintar_slow = 22
        npc_quintar_medium = 23
        npc_foot_water = 24
        npc_salmon_medium_fast = 25
        npc_quintar_desert = 26
        npc_quintar_float = 27
        npc_quintar_jump = 28
        cinematic_slow = 29
        cinematic_medium = 30
        cinematic_fast = 31

    class Scope(IntEnum):
        private = 0
        friend = 1
        global_ = 2
        temp = 3
        friend_temp = 4
        global_temp = 5

    class Shadow(IntEnum):
        none = 0
        small = 1
        normal = 2
        home_point = 3
        crystal = 4
        large = 5

    class SignStyle(IntEnum):
        wooden = 0
        bulletin_left = 100
        bulletin_right = 101

    class TreasureStyle(IntEnum):
        currency = 0
        consumable = 1
        artifact = 2
        weapon = 3
        armor = 4
        accessory = 5

    class TreasureType(IntEnum):
        nothing = 0
        item = 1
        equipment = 2
        currency = 3

    class Trigger(IntEnum):
        player_action = 0
        player_proximity = 1
        auto = 2
        player_touch = 3
        trigger_npc = 4

    class TriggerContext(IntEnum):
        sync = 0
        async_ = 1
        cinematic = 2

    class VariableSettingMode(IntEnum):
        constant = 0
        variable = 1
        inventory = 2
        random = 3

    class Wander(IntEnum):
        none = 0
        circle_area = 1
        route = 2
        circle_perimeter = 3
        square_perimeter = 4
        line_x = 5
        line_z = 6
        square_area = 7
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root or self
        self._read()

    def _read(self):
        self.version = self._io.read_u1()
        if not self.version == 0:
            raise kaitaistruct.ValidationNotEqualError(0, self.version, self._io, u"/seq/0")
        self.num_entities = self._io.read_u4le()
        self.entities = []
        for i in range(self.num_entities):
            self.entities.append(Entities.Entity(self._io, self, self._root))


    class ActionDataAddInventory(KaitaiStruct):
        """Data associated with `action::add_inventory`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(Entities.TreasureType, self._io.read_u1())
            if not isinstance(self.type, Entities.TreasureType):
                raise kaitaistruct.ValidationNotInEnumError(self.type, self._io, u"/types/action_data_add_inventory/seq/0")
            self.item = self._io.read_u4le()
            self.count = self._io.read_u4le()
            self.magic1 = self._io.read_bytes(1)


    class ActionDataCondition(KaitaiStruct):
        """Data associated with `action::condition`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.condition = Entities.Condition(self._io, self, self._root)
            self.magic1 = self._io.read_bytes(4)
            self.actions_true = Entities.NpcActionsList(self._io, self, self._root)
            self.actions_false = Entities.NpcActionsList(self._io, self, self._root)


    class ActionDataMessage(KaitaiStruct):
        """Data associated with `action::message`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.message = Entities.NullableString(self._io, self, self._root)
            self.magic = self._io.read_bytes(8)


    class ActionDataSetFacing(KaitaiStruct):
        """Data associated with `action::set_facing`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.facing = KaitaiStream.resolve_enum(Entities.Facing, self._io.read_u1())
            if not isinstance(self.facing, Entities.Facing):
                raise kaitaistruct.ValidationNotInEnumError(self.facing, self._io, u"/types/action_data_set_facing/seq/0")


    class ActionDataSetFlag(KaitaiStruct):
        """Data associated with `action::set_flag`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.scope = KaitaiStream.resolve_enum(Entities.Scope, self._io.read_u1())
            if not isinstance(self.scope, Entities.Scope):
                raise kaitaistruct.ValidationNotInEnumError(self.scope, self._io, u"/types/action_data_set_flag/seq/0")
            self.magic1 = self._io.read_bytes(1)
            self.flag = Entities.NullableString(self._io, self, self._root)
            self.setting_mode = KaitaiStream.resolve_enum(Entities.VariableSettingMode, self._io.read_u1())
            if not isinstance(self.setting_mode, Entities.VariableSettingMode):
                raise kaitaistruct.ValidationNotInEnumError(self.setting_mode, self._io, u"/types/action_data_set_flag/seq/3")
            _on = self.setting_mode
            if _on == Entities.VariableSettingMode.constant:
                self.setting_data = Entities.ActionDataSetFlagVarsetmodeConstant(self._io, self, self._root)
            else:
                self.setting_data = Entities.Nothing(self._io, self, self._root)


    class ActionDataSetFlagVarsetmodeConstant(KaitaiStruct):
        """The data associated with `variable_setting_mode::constant`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.value = self._io.read_u1()
            if not  ((self.value == 0) or (self.value == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.value, self._io, u"/types/action_data_set_flag_varsetmode_constant/seq/0")
            self.magic2 = self._io.read_bytes(11)


    class ActionDataStopProcessing(KaitaiStruct):
        """Data associated with `action::stop_processing`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.refresh_outfit = self._io.read_u1()
            if not  ((self.refresh_outfit == 0) or (self.refresh_outfit == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.refresh_outfit, self._io, u"/types/action_data_stop_processing/seq/0")
            self.refresh_page = self._io.read_u1()
            if not  ((self.refresh_page == 0) or (self.refresh_page == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.refresh_page, self._io, u"/types/action_data_stop_processing/seq/1")
            self.refresh_position = self._io.read_u1()
            if not  ((self.refresh_position == 0) or (self.refresh_position == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.refresh_position, self._io, u"/types/action_data_stop_processing/seq/2")
            self.cancel_all_actions = self._io.read_u1()
            if not  ((self.cancel_all_actions == 0) or (self.cancel_all_actions == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.cancel_all_actions, self._io, u"/types/action_data_stop_processing/seq/3")
            self.trigger_player_action = self._io.read_u1()
            if not  ((self.trigger_player_action == 0) or (self.trigger_player_action == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.trigger_player_action, self._io, u"/types/action_data_stop_processing/seq/4")
            self.trigger_player_proximity = self._io.read_u1()
            if not  ((self.trigger_player_proximity == 0) or (self.trigger_player_proximity == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.trigger_player_proximity, self._io, u"/types/action_data_stop_processing/seq/5")
            self.trigger_auto = self._io.read_u1()
            if not  ((self.trigger_auto == 0) or (self.trigger_auto == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.trigger_auto, self._io, u"/types/action_data_stop_processing/seq/6")
            self.trigger_player_touch = self._io.read_u1()
            if not  ((self.trigger_player_touch == 0) or (self.trigger_player_touch == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.trigger_player_touch, self._io, u"/types/action_data_stop_processing/seq/7")
            self.trigger_trigger_npc = self._io.read_u1()
            if not  ((self.trigger_trigger_npc == 0) or (self.trigger_trigger_npc == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.trigger_trigger_npc, self._io, u"/types/action_data_stop_processing/seq/8")
            self.global_refresh_outfits = self._io.read_u1()
            if not  ((self.global_refresh_outfits == 0) or (self.global_refresh_outfits == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.global_refresh_outfits, self._io, u"/types/action_data_stop_processing/seq/9")
            self.global_refresh_pages = self._io.read_u1()
            if not  ((self.global_refresh_pages == 0) or (self.global_refresh_pages == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.global_refresh_pages, self._io, u"/types/action_data_stop_processing/seq/10")
            self.global_refresh_positions = self._io.read_u1()
            if not  ((self.global_refresh_positions == 0) or (self.global_refresh_positions == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.global_refresh_positions, self._io, u"/types/action_data_stop_processing/seq/11")
            self.global_try_spawn = self._io.read_u1()
            if not  ((self.global_try_spawn == 0) or (self.global_try_spawn == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.global_try_spawn, self._io, u"/types/action_data_stop_processing/seq/12")
            self.global_try_despawn = self._io.read_u1()
            if not  ((self.global_try_despawn == 0) or (self.global_try_despawn == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.global_try_despawn, self._io, u"/types/action_data_stop_processing/seq/13")
            self.magic1 = self._io.read_bytes(1)


    class Condition(KaitaiStruct):
        """A condition."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(Entities.ConditionType, self._io.read_u1())
            if not isinstance(self.type, Entities.ConditionType):
                raise kaitaistruct.ValidationNotInEnumError(self.type, self._io, u"/types/condition/seq/0")
            _on = self.type
            if _on == Entities.ConditionType.check_flag:
                self.data = Entities.ConditionDataCheckFlag(self._io, self, self._root)
            elif _on == Entities.ConditionType.operation:
                self.data = Entities.ConditionDataOperation(self._io, self, self._root)
            else:
                self.data = Entities.Nothing(self._io, self, self._root)


    class ConditionDataCheckFlag(KaitaiStruct):
        """Condition data for `condition_type::check_flag`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.magic1 = self._io.read_bytes(3)
            self.inverted = self._io.read_u1()
            if not  ((self.inverted == 0) or (self.inverted == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.inverted, self._io, u"/types/condition_data_check_flag/seq/1")
            self.scope = KaitaiStream.resolve_enum(Entities.Scope, self._io.read_u1())
            if not isinstance(self.scope, Entities.Scope):
                raise kaitaistruct.ValidationNotInEnumError(self.scope, self._io, u"/types/condition_data_check_flag/seq/2")
            self.magic2 = self._io.read_bytes(1)
            self.flag = Entities.NullableString(self._io, self, self._root)
            self.magic3 = self._io.read_bytes(10)


    class ConditionDataOperation(KaitaiStruct):
        """Condition data for `condition_type::operation`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.operator = KaitaiStream.resolve_enum(Entities.ConditionOperator, self._io.read_u4le())
            if not isinstance(self.operator, Entities.ConditionOperator):
                raise kaitaistruct.ValidationNotInEnumError(self.operator, self._io, u"/types/condition_data_operation/seq/0")
            self.lhs = Entities.Condition(self._io, self, self._root)
            self.magic1 = self._io.read_bytes(5)
            self.rhs = Entities.Condition(self._io, self, self._root)


    class DataCrystal(KaitaiStruct):
        """Data for entities of type `crystal`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.magic = self._io.read_u1()
            if not self.magic == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.magic, self._io, u"/types/data_crystal/seq/0")
            self.job = self._io.read_u4le()
            self.r = self._io.read_u1()
            self.g = self._io.read_u1()
            self.b = self._io.read_u1()
            self.offset_half_x = self._io.read_u1()
            if not  ((self.offset_half_x == 0) or (self.offset_half_x == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.offset_half_x, self._io, u"/types/data_crystal/seq/5")
            self.offset_half_z = self._io.read_u1()
            if not  ((self.offset_half_z == 0) or (self.offset_half_z == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.offset_half_z, self._io, u"/types/data_crystal/seq/6")


    class DataDoor(KaitaiStruct):
        """Data for entities of type `door`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.style = KaitaiStream.resolve_enum(Entities.DoorStyle, self._io.read_u1())
            if not isinstance(self.style, Entities.DoorStyle):
                raise kaitaistruct.ValidationNotInEnumError(self.style, self._io, u"/types/data_door/seq/0")
            self.locked = self._io.read_u1()
            if not  ((self.locked == 0) or (self.locked == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.locked, self._io, u"/types/data_door/seq/1")
            self.has_key = self._io.read_u1()
            if not  ((self.has_key == 0) or (self.has_key == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.has_key, self._io, u"/types/data_door/seq/2")
            if self.has_key == 1:
                self.key = self._io.read_u4le()

            self.flag = Entities.NullableString(self._io, self, self._root)
            self.invert_flag = self._io.read_u1()
            if not  ((self.invert_flag == 0) or (self.invert_flag == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.invert_flag, self._io, u"/types/data_door/seq/5")


    class DataHomePoint(KaitaiStruct):
        """Data for entities of type `home_point`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.name = Entities.NullableString(self._io, self, self._root)


    class DataMarker(KaitaiStruct):
        """Data for entities of type `marker`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.key = Entities.NullableString(self._io, self, self._root)
            self.proximity = self._io.read_f4le()


    class DataNpc(KaitaiStruct):
        """Data for entities of type `npc`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.key = Entities.NullableString(self._io, self, self._root)
            self.linked_key = Entities.NullableString(self._io, self, self._root)
            self.tie_to_spawn = self._io.read_u1()
            if not  ((self.tie_to_spawn == 0) or (self.tie_to_spawn == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.tie_to_spawn, self._io, u"/types/data_npc/seq/2")
            self.unique_per_key = self._io.read_u1()
            if not  ((self.unique_per_key == 0) or (self.unique_per_key == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.unique_per_key, self._io, u"/types/data_npc/seq/3")
            self.num_outfits = self._io.read_u4le()
            self.outfits = []
            for i in range(self.num_outfits):
                self.outfits.append(Entities.NpcOutfit(self._io, self, self._root))

            self.num_pages = self._io.read_u4le()
            self.pages = []
            for i in range(self.num_pages):
                self.pages.append(Entities.NpcPage(self._io, self, self._root))



    class DataSign(KaitaiStruct):
        """Data for entities of type `sign`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.title = Entities.NullableString(self._io, self, self._root)
            self.message = Entities.NullableString(self._io, self, self._root)
            self.facing = KaitaiStream.resolve_enum(Entities.Facing, self._io.read_u1())
            if not isinstance(self.facing, Entities.Facing):
                raise kaitaistruct.ValidationNotInEnumError(self.facing, self._io, u"/types/data_sign/seq/2")
            self.style = KaitaiStream.resolve_enum(Entities.SignStyle, self._io.read_u1())
            if not isinstance(self.style, Entities.SignStyle):
                raise kaitaistruct.ValidationNotInEnumError(self.style, self._io, u"/types/data_sign/seq/3")


    class DataSpark(KaitaiStruct):
        """Data for entities of type `spark`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.behaviour = self._io.read_u4le()
            self.is_unique = self._io.read_u1()
            if not  ((self.is_unique == 0) or (self.is_unique == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.is_unique, self._io, u"/types/data_spark/seq/1")
            self.is_giant = self._io.read_u1()
            if not  ((self.is_giant == 0) or (self.is_giant == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.is_giant, self._io, u"/types/data_spark/seq/2")
            self.victory_flag = Entities.NullableString(self._io, self, self._root)
            self.victory_flag_true = self._io.read_u1()
            if not  ((self.victory_flag_true == 0) or (self.victory_flag_true == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.victory_flag_true, self._io, u"/types/data_spark/seq/4")
            self.victory_flag_temp = self._io.read_u1()
            if not  ((self.victory_flag_temp == 0) or (self.victory_flag_temp == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.victory_flag_temp, self._io, u"/types/data_spark/seq/5")
            self.victory_flag_unset_on_spawn = self._io.read_u1()
            if not  ((self.victory_flag_unset_on_spawn == 0) or (self.victory_flag_unset_on_spawn == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.victory_flag_unset_on_spawn, self._io, u"/types/data_spark/seq/6")
            self.trigger = Entities.NullableString(self._io, self, self._root)
            self.num_troops = self._io.read_u4le()
            self.troops = []
            for i in range(self.num_troops):
                self.troops.append(Entities.PossibleTroop(self._io, self, self._root))



    class DataTreasure(KaitaiStruct):
        """Data for entities of type `treasure`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.facing = KaitaiStream.resolve_enum(Entities.Facing, self._io.read_u1())
            if not isinstance(self.facing, Entities.Facing):
                raise kaitaistruct.ValidationNotInEnumError(self.facing, self._io, u"/types/data_treasure/seq/0")
            self.type = KaitaiStream.resolve_enum(Entities.TreasureType, self._io.read_u1())
            if not isinstance(self.type, Entities.TreasureType):
                raise kaitaistruct.ValidationNotInEnumError(self.type, self._io, u"/types/data_treasure/seq/1")
            self.contents = self._io.read_u4le()
            self.has_style_override = self._io.read_u1()
            if not  ((self.has_style_override == 0) or (self.has_style_override == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.has_style_override, self._io, u"/types/data_treasure/seq/3")
            if self.has_style_override == 1:
                self.style_override = KaitaiStream.resolve_enum(Entities.TreasureStyle, self._io.read_u1())
                if not isinstance(self.style_override, Entities.TreasureStyle):
                    raise kaitaistruct.ValidationNotInEnumError(self.style_override, self._io, u"/types/data_treasure/seq/4")



    class Entity(KaitaiStruct):
        """An entity."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            if not self.id >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.id, self._io, u"/types/entity/seq/0")
            self.x = self._io.read_s4le()
            self.y = self._io.read_s4le()
            self.z = self._io.read_s4le()
            self.biome = self._io.read_u1()
            self.type = KaitaiStream.resolve_enum(Entities.EntityType, self._io.read_u1())
            if not isinstance(self.type, Entities.EntityType):
                raise kaitaistruct.ValidationNotInEnumError(self.type, self._io, u"/types/entity/seq/5")
            self.comment = Entities.NullableString(self._io, self, self._root)
            _on = self.type
            if _on == Entities.EntityType.crystal:
                self.data = Entities.DataCrystal(self._io, self, self._root)
            elif _on == Entities.EntityType.door:
                self.data = Entities.DataDoor(self._io, self, self._root)
            elif _on == Entities.EntityType.home_point:
                self.data = Entities.DataHomePoint(self._io, self, self._root)
            elif _on == Entities.EntityType.marker:
                self.data = Entities.DataMarker(self._io, self, self._root)
            elif _on == Entities.EntityType.npc:
                self.data = Entities.DataNpc(self._io, self, self._root)
            elif _on == Entities.EntityType.sign:
                self.data = Entities.DataSign(self._io, self, self._root)
            elif _on == Entities.EntityType.spark:
                self.data = Entities.DataSpark(self._io, self, self._root)
            elif _on == Entities.EntityType.treasure:
                self.data = Entities.DataTreasure(self._io, self, self._root)


    class Nothing(KaitaiStruct):
        """No data."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            pass


    class NpcAction(KaitaiStruct):
        """An action execute by an NPC."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.type = KaitaiStream.resolve_enum(Entities.Action, self._io.read_u4le())
            if not isinstance(self.type, Entities.Action):
                raise kaitaistruct.ValidationNotInEnumError(self.type, self._io, u"/types/npc_action/seq/0")
            _on = self.type
            if _on == Entities.Action.add_inventory:
                self.data = Entities.ActionDataAddInventory(self._io, self, self._root)
            elif _on == Entities.Action.condition:
                self.data = Entities.ActionDataCondition(self._io, self, self._root)
            elif _on == Entities.Action.message:
                self.data = Entities.ActionDataMessage(self._io, self, self._root)
            elif _on == Entities.Action.set_facing:
                self.data = Entities.ActionDataSetFacing(self._io, self, self._root)
            elif _on == Entities.Action.set_flag:
                self.data = Entities.ActionDataSetFlag(self._io, self, self._root)
            elif _on == Entities.Action.stop_processing:
                self.data = Entities.ActionDataStopProcessing(self._io, self, self._root)
            else:
                self.data = Entities.Nothing(self._io, self, self._root)


    class NpcActionsList(KaitaiStruct):
        """A list of actions."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.num_actions = self._io.read_u4le()
            self.actions = []
            for i in range(self.num_actions):
                self.actions.append(Entities.NpcAction(self._io, self, self._root))



    class NpcOutfit(KaitaiStruct):
        """The appearance, physics, and movement of an NPC."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.condition = Entities.Condition(self._io, self, self._root)
            self.magic1 = self._io.read_bytes(4)
            self.texture = Entities.NullableString(self._io, self, self._root)
            self.magic2 = self._io.read_bytes(2)
            self.facing = KaitaiStream.resolve_enum(Entities.Facing, self._io.read_u1())
            if not isinstance(self.facing, Entities.Facing):
                raise kaitaistruct.ValidationNotInEnumError(self.facing, self._io, u"/types/npc_outfit/seq/4")
            self.shadow = KaitaiStream.resolve_enum(Entities.Shadow, self._io.read_u1())
            if not isinstance(self.shadow, Entities.Shadow):
                raise kaitaistruct.ValidationNotInEnumError(self.shadow, self._io, u"/types/npc_outfit/seq/5")
            self.auto_step = self._io.read_u1()
            if not  ((self.auto_step == 0) or (self.auto_step == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.auto_step, self._io, u"/types/npc_outfit/seq/6")
            self.has_voxel = self._io.read_u1()
            if not  ((self.has_voxel == 0) or (self.has_voxel == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.has_voxel, self._io, u"/types/npc_outfit/seq/7")
            if self.has_voxel == 1:
                self.voxel = self._io.read_u1()

            self.magic4 = self._io.read_bytes(3)
            self.physics = KaitaiStream.resolve_enum(Entities.Physics, self._io.read_u1())
            if not isinstance(self.physics, Entities.Physics):
                raise kaitaistruct.ValidationNotInEnumError(self.physics, self._io, u"/types/npc_outfit/seq/10")
            self.magic5 = self._io.read_bytes(2)
            self.wander = KaitaiStream.resolve_enum(Entities.Wander, self._io.read_u1())
            if not isinstance(self.wander, Entities.Wander):
                raise kaitaistruct.ValidationNotInEnumError(self.wander, self._io, u"/types/npc_outfit/seq/12")
            _on = self.wander
            if _on == Entities.Wander.none:
                self.wander_data = Entities.WanderNone(self._io, self, self._root)
            elif _on == Entities.Wander.route:
                self.wander_data = Entities.WanderRoute(self._io, self, self._root)
            else:
                self.wander_data = Entities.WanderData(self._io, self, self._root)


    class NpcPage(KaitaiStruct):
        """The behavior code of an NPC."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.condition = Entities.Condition(self._io, self, self._root)
            self.magic1 = self._io.read_bytes(4)
            self.trigger = KaitaiStream.resolve_enum(Entities.Trigger, self._io.read_u1())
            if not isinstance(self.trigger, Entities.Trigger):
                raise kaitaistruct.ValidationNotInEnumError(self.trigger, self._io, u"/types/npc_page/seq/2")
            _on = self.trigger
            if _on == Entities.Trigger.player_proximity:
                self.trigger_data = Entities.TriggerDataPlayerProximity(self._io, self, self._root)
            else:
                self.trigger_data = Entities.TriggerDataNone(self._io, self, self._root)
            self.actions = Entities.NpcActionsList(self._io, self, self._root)
            self.context = KaitaiStream.resolve_enum(Entities.TriggerContext, self._io.read_u1())
            if not isinstance(self.context, Entities.TriggerContext):
                raise kaitaistruct.ValidationNotInEnumError(self.context, self._io, u"/types/npc_page/seq/5")


    class NullableString(KaitaiStruct):
        """A boolean byte followed by a length-terminated string."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.has_value = self._io.read_u1()
            if not  ((self.has_value == 0) or (self.has_value == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.has_value, self._io, u"/types/nullable_string/seq/0")
            if self.has_value == 1:
                self.string = Entities.String(self._io, self, self._root)



    class PossibleTroop(KaitaiStruct):
        """An entry in the troop table of spark entities. Represents a possible troop result when colliding with the spark."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.id = self._io.read_u4le()
            self.weight = self._io.read_u4le()
            self.magic = self._io.read_bytes(2)


    class String(KaitaiStruct):
        """A string."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.length = vlq_base128_le.VlqBase128Le(self._io)
            self.value = (self._io.read_bytes(self.length.value)).decode(u"UTF-8")


    class TriggerDataNone(KaitaiStruct):
        """The data for a trigger with no data. Just empty bytes."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(30)


    class TriggerDataPlayerProximity(KaitaiStruct):
        """The data for a NPC page with a trigger of `trigger::player_proximity`."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.radius = self._io.read_f4le()
            self.min_x = self._io.read_f4le()
            self.min_y = self._io.read_f4le()
            self.min_z = self._io.read_f4le()
            self.max_x = self._io.read_f4le()
            self.max_y = self._io.read_f4le()
            self.max_z = self._io.read_f4le()
            self.magic2 = self._io.read_bytes(2)


    class WanderData(KaitaiStruct):
        """Wandering information for NPCs with circle, square, or line wander types."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.speed = self._io.read_f4le()
            self.frequency = self._io.read_u4le()
            self.radius = self._io.read_f4le()
            self.magic = self._io.read_bytes(2)


    class WanderNone(KaitaiStruct):
        """A region of blank bits, because the wander type does not need the data."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.nothing = self._io.read_bytes(18)


    class WanderRoute(KaitaiStruct):
        """Wandering information for NPCs with the route wander type."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.magic1 = self._io.read_bytes(13)
            self.num_points = self._io.read_u4le()
            self.points = []
            for i in range(self.num_points):
                self.points.append(Entities.WanderRoutePoint(self._io, self, self._root))

            self.magic2 = self._io.read_bytes(1)


    class WanderRoutePoint(KaitaiStruct):
        """A point along a wander route."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root
            self._read()

        def _read(self):
            self.x = self._io.read_s4le()
            self.y = self._io.read_s4le()
            self.z = self._io.read_s4le()
            self.speed = self._io.read_f4le()
            self.wait = self._io.read_u4le()
            self.facing = KaitaiStream.resolve_enum(Entities.Facing, self._io.read_u1())
            if not isinstance(self.facing, Entities.Facing):
                raise kaitaistruct.ValidationNotInEnumError(self.facing, self._io, u"/types/wander_route_point/seq/5")
