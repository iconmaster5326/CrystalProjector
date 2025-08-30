meta:
  id: entities
  endian: le
  imports:
    - vlq_base128_le
doc: A file of the form `yXe.dat`, that lists all entities in a 16x16x16 cube chunk, for the chunk at y level X.
seq:
  - id: version
    doc: The current version is `0`.
    type: u1
    valid: 0
  - id: num_entities
    doc: The number of entities in this chunk.
    type: u4
  - id: entities
    doc: The entities in this chunk.
    type: entity
    repeat: expr
    repeat-expr: num_entities
enums:
  entity_type:
    0: npc
    1: sign
    2: spark
    3: door
    4: home_point
    5: treasure
    6: crystal
    7: marker
  facing:
    0: xneg
    1: yneg
    2: zneg
    3: xpos
    4: ypos
    5: zpos
  sign_style:
    0: wooden
    100: bulletin_left
    101: bulletin_right
  door_style:
    0: boroboro
    1: cell
    2: stone
    3: wood
    4: red
    5: cell_cross
    6: boroboro_window
    7: red_window
    8: metal
    9: ornate
    10: sun_stone
    11: moon_stone
    12: paper
  treasure_type:
    0: nothing
    1: item
    2: equipment
    3: currency
  treasure_style:
    0: currency
    1: consumable
    2: artifact
    3: weapon
    4: armor
    5: accessory
  condition_type:
    0: always
    14: can_understand_quintar
    17: check_atlas
    7: check_crystal_count
    3: check_flag
    12: check_highest_member_level
    5: check_inventory
    15: check_npc_proximity
    4: check_number
    6: finished_moving
    23: garden
    32: is_ability_learned
    13: is_ability_unlocked
    18: is_demo
    34: is_facing
    28: is_game_cleared
    21: is_job_mastered
    11: is_job_present
    27: is_member_present
    33: is_passive_learned
    31: is_passive_unlocked
    30: is_patch_mode_active
    35: is_player_facing
    26: is_player_gender
    24: is_player_stranded
    16: is_riding_default_quintar
    8: is_riding_quintar
    20: is_riding_specific_mount
    9: lost_and_found_has_stock
    19: my_quintar
    1: never
    2: operation
    22: previous_battle_was_victory
    10: random
    29: randomizer
    25: skip_minigames
  shadow:
    0: none
    1: small
    2: normal
    3: home_point
    4: crystal
    5: large
  collision:
    0: none
    1: one_way_to
    2: one_way_from
    3: full
  physics:
    0: player_foot
    1: quintar_default
    2: salmon_default
    3: owl_default
    4: ibek_default
    5: salmon_rental
    6: salmon_royal
    7: quintar_rental
    8: quintar_desert
    9: salmon_lava
    10: quintar_float
    11: quintar_jump
    12: quintar_fly
    13: quintar_swim
    14: quintar_gold
    15: npc_foot
    16: npc_flying
    17: npc_salmon_fast
    18: npc_salmon_medium
    19: npc_salmon_slow
    20: npc_free
    21: npc_push_block
    22: npc_quintar_slow
    23: npc_quintar_medium
    24: npc_foot_water
    25: npc_salmon_medium_fast
    26: npc_quintar_desert
    27: npc_quintar_float
    28: npc_quintar_jump
    29: cinematic_slow
    30: cinematic_medium
    31: cinematic_fast
  jump:
    0: none
    1: up_voxel
    2: up_actor
    3: up_voxel_and_actor
    4: off_voxel
    5: up_voxel_off_voxel
    6: off_actor
    7: off_voxel_and_actor
    8: full
  wander:
    0: none
    1: circle_area
    2: route
    3: circle_perimeter
    4: square_perimeter
    5: line_x
    6: line_z
    7: square_area
  scope:
    0: private
    1: friend
    2: global
    3: temp
    4: friend_temp
    5: global_temp
  trigger:
    0: player_action
    1: player_proximity
    2: auto
    3: player_touch
    4: trigger_npc
  touch_type:
    0: stand_on
    1: xz_touch
    2: head_bonk
    3: any_contact
  trigger_context:
    0: sync
    1: async
    2: cinematic
  action:
    13: ability
    41: activity_countdown
    8: add_inventory
    16: add_number
    58: add_to_lost_and_found
    27: battle
    36: cancel_actions
    66: cancel_wander
    14: choice_message
    68: choice_message_anonymous
    18: command_npc
    78: comment
    3: condition
    22: context_switch
    57: credits
    23: do_narration
    62: face_away_from_player
    0: face_player
    35: future_actions
    71: garden
    69: hazard_burn
    15: inn
    55: insert_future_actions
    76: learn_ability
    77: learn_passive
    60: make_player_face_this
    1: message
    61: message_anonymous
    73: message_hint
    65: message_npc
    12: move
    45: move_away_from_player
    20: move_camera
    44: move_group
    46: move_group_to
    31: move_player
    53: move_player_instant
    34: move_player_to
    33: move_to
    17: multiply_number
    63: my_quintar
    72: new_game_plus
    54: particle
    38: play_music
    59: play_se_mine_ore
    49: play_se_switch_pressed
    50: play_se_switch_unpressed
    37: queue_future_actions
    52: refresh_bulletin
    30: refresh_lost_and_found
    43: refresh_npcs
    48: refresh_specific_npcs
    9: remove_inventory
    67: resume_wander
    21: revert_camera
    2: revert_facing
    40: revert_music
    24: set_facing
    6: set_flag
    70: set_last_safe_pos_to
    47: set_last_safe_pos_to_marker
    26: set_mount
    11: set_npc_property
    7: set_number
    25: set_player_facing
    56: set_player_facing_to_this
    5: shop
    28: shop_recipe
    29: shop_service
    39: stop_music
    10: stop_processing
    64: subtract_number
    51: teleport_player
    42: teleport_player_to
    19: trigger_npc
    32: unlock_ability
    74: unlock_job
    75: unlock_passive
    4: wait
  variable_setting_mode:
    0: constant
    1: variable
    2: inventory
    3: random
  condition_operator:
    0: and
    1: or
    2: xor
    3: equiv
    4: impl
  move_wait_mode:
    0: none
    1: end
    2: exit
    3: collide
    4: exit_or_collide
  check_number_eval:
    0: less
    1: less_equal
    2: equal
    3: greater_equal
    4: greater
types:
  string:
    doc: A string.
    seq:
      - id: length
        doc: How long is this string?
        type: vlq_base128_le
      - id: value
        doc: The string.
        type: str
        encoding: UTF-8
        size: length.value
  nullable_string:
    doc: A boolean byte followed by a length-terminated string.
    seq:
      - id: has_value
        doc: Does this string exist?
        type: u1
        valid:
          any-of: [0, 1]
      - id: string
        doc: The string, only if has_value is 1.
        type: string
        if: has_value == 1
  entity:
    doc: An entity.
    seq:
      - id: id
        doc: The entity ID. In the vanilla game, this goes from 1 to ~3000.
        type: u4
        valid:
          min: 1
      - id: "x"
        doc: The X position of the entity, in world coordinates (*NOT* chunk-offset coordinates!)
        type: s4
      - id: "y"
        doc: The Y position of the entity, in world coordinates (*NOT* chunk-offset coordinates!)
        type: s4
      - id: "z"
        doc: The Z position of the entity, in world coordinates (*NOT* chunk-offset coordinates!)
        type: s4
      - id: biome
        doc: The biome ID where this entity should be considered to be located in. This is important for things like randomizer spoilers and bestiary listings.
        type: u1
      - id: type
        doc: The type of this entity.
        type: u1
        enum: entity_type
        valid:
          in-enum: true
      - id: comment
        doc: A comment. Not displayed in game.
        type: nullable_string
      - id: data
        doc: Per-type entity data.
        type:
          switch-on: type
          cases:
            entity_type::npc: data_npc
            entity_type::sign: data_sign
            entity_type::spark: data_spark
            entity_type::door: data_door
            entity_type::home_point: data_home_point
            entity_type::treasure: data_treasure
            entity_type::crystal: data_crystal
            entity_type::marker: data_marker
  data_npc:
    doc: Data for entities of type `npc`.
    seq:
      - id: key
        doc: A name to refer to this entity from code.
        type: nullable_string
      - id: linked_key
        doc: An entity this entity is linked to.
        type: nullable_string
      - id: tie_to_spawn
        doc: Does this NPC despawn when its spawn point is out of range?
        type: u1
        valid:
          any-of: [0, 1]
      - id: unique_per_key
        doc: Will this NPC not spawn if there's already one with the same key?
        type: u1
        valid:
          any-of: [0, 1]
      - id: num_outfits
        doc: The number of outfits this NPC has.
        type: u4
      - id: outfits
        doc: The outfits this NPC may have.
        type: npc_outfit
        repeat: expr
        repeat-expr: num_outfits
      - id: num_pages
        doc: The number of pages this NPC has.
        type: u4
      - id: pages
        doc: The pages this NPC may have.
        type: npc_page
        repeat: expr
        repeat-expr: num_pages
      - id: blank_page
        doc: If there's 0 pages, there's some zero bytes here.
        size: 37
        if: num_pages == 0 and not _io.eof
  npc_outfit:
    doc: The appearance, physics, and movement of an NPC.
    seq:
      - id: condition
        doc: The condition data for this outfit.
        type: condition
      - id: texture
        doc: The string name of the texture file, if we're rendering as a sprite.
        type: nullable_string
      - id: name
        doc: The name of this outfit.
        type: nullable_string
      - id: pc
        doc: Are we a "fake PC"?
        type: u1
        valid:
          any-of: [0, 1]
      - id: pc_level
        doc: The level of the "fake PC".
        type: u1
        if: pc == 1
      - id: pc_magic1
        doc: Unknown.
        size: 3
        if: pc == 1
      - id: facing
        doc: The direction this NPC initially faces.
        type: u1
        enum: facing
        valid:
          in-enum: true
      - id: shadow
        doc: The type of shadows this NPC casts.
        type: u1
        enum: shadow
        valid:
          in-enum: true
      - id: auto_step
        doc: Does the sprite automatically step?
        type: u1
        valid:
          any-of: [0, 1]
      - id: has_voxel
        doc: Does this NPC render as a voxel?
        type: u1
        valid:
          any-of: [0, 1]
      - id: voxel
        doc: The voxel ID to render as.
        type: u1
        if: has_voxel == 1
      - id: magic4
        doc: Unknown.
        size: 1
      - id: player_collision
        doc: How this NPC collides with the player.
        type: u1
        enum: collision
        valid:
          in-enum: true
      - id: npc_collision
        doc: How this NPC collides with other NPCS.
        type: u1
        enum: collision
        valid:
          in-enum: true
      - id: physics
        doc: The physics this NPC uses to move.
        type: u1
        enum: physics
        valid:
          in-enum: true
      - id: jump
        doc: How this NPC jumps.
        type: u1
        enum: jump
        valid:
          in-enum: true
      - id: keep_spawned
        doc: Keep this NPC spawned even when out of its spawn range?
        type: u1
        valid:
          any-of: [0, 1]
      - id: wander
        doc: How this NPC wanders around.
        type: u1
        enum: wander
        valid:
          in-enum: true
      - id: wander_data
        doc: Data for the wandering behaviour.
        type:
          switch-on: wander
          cases:
            wander::none: wander_none
            _: wander_data
  wander_none:
    doc: A region of blank bits, because the wander type does not need the data.
    seq:
      - id: nothing
        doc: All zeroes.
        size: 18
  wander_data:
    doc: Wandering information for NPCs.
    seq:
      - id: speed
        doc: How fast does this NPC move?
        type: f4
      - id: frequency
        doc: How long does this NPC wait between points?
        type: u4
      - id: radius
        doc: How large is the wandering area?
        type: f4
      - id: is_route
        doc: Is this a route?
        type: u1
        valid:
          any-of: [0, 1]
      - id: num_points
        doc: The number of points in this route.
        type: u4
        if: is_route == 1
      - id: points
        doc: The route this NPC takes.
        type: wander_route_point
        repeat: expr
        repeat-expr: num_points
        if: is_route == 1
      - id: is_line
        doc: Is this route a straight line?
        size: 1
  wander_route_point:
    doc: A point along a wander route.
    seq:
      - id: "x"
        doc: The X position.
        type: s4
      - id: "y"
        doc: The Y position.
        type: s4
      - id: "z"
        doc: The Z position.
        type: s4
      - id: speed
        doc: Movement speed.
        type: f4
      - id: wait
        doc: Wait time between points.
        type: u4
      - id: facing
        doc: Facing at end of point.
        type: u1
        enum: facing
        valid:
          in-enum: true
  condition:
    doc: A condition.
    seq:
      - id: type
        doc: The condition type.
        type: u1
        enum: condition_type
        valid:
          in-enum: true
      - id: data
        doc: Condition data.
        type:
          switch-on: type
          cases: # TODO
            condition_type::check_crystal_count: condition_data_check_crystal_count
            condition_type::check_flag: condition_data_check_var
            condition_type::check_inventory: condition_data_check_inventory
            condition_type::check_number: condition_data_check_var
            condition_type::operation: condition_data_operation
            condition_type::randomizer: condition_data_randomizer
            _: condition_none
  nothing:
    doc: No data.
  condition_none:
    doc: Null condition data.
    seq:
      - id: magic1
        doc: Unknown.
        size: 4
  condition_data_check_crystal_count:
    doc: Data associated with `condition::check_crystal_count`.
    seq:
      - id: magic1
        doc: Unknown.
        size: 9
      - id: count
        doc: The number of crystals you need to pass the condition.
        type: u4
      - id: magic2
        doc: Unknown.
        size: 1
  condition_data_check_inventory:
     doc: Data associated with `condition::check_inventory`.
     seq:
      - id: magic1
        doc: Unknown.
        size: 4
      - id: type
        doc: The item type to give.
        type: u1
        enum: treasure_type
        valid:
          in-enum: true
      - id: item
        doc: The item/equipment ID to give. (TODO - what if currency?)
        type: u4
      - id: count
        doc: The amount of the item to give. (TODO - what if currency?)
        type: u4
      - id: randomized
        doc: Randomize this item?
        type: u1
        valid:
          any-of: [0, 1]
  condition_data_check_var:
    doc: Condition data for `condition_type::check_flag` and `condition_type::check_number`.
    seq:
      - id: magic1
        doc: Unknown.
        size: 3
      - id: inverted
        doc: Is this condition inverted?
        type: u1
        valid:
          any-of: [0, 1]
      - id: scope
        doc: The scope of the flag to check.
        type: u1
        enum: scope
        valid:
          in-enum: true
      - id: magic2
        doc: Unknown.
        size: 1
      - id: variable
        doc: The number/flag to test.
        type: nullable_string
      - id: eval
        doc: The comparion operator, for `check_number` conditions.
        type: u1
        enum: check_number_eval
        valid:
          in-enum: true
      - id: magic3
        doc: Unknown.
        size: 2
      - id: value
        doc: The number to test against, for `check_number` conditions.
        type: s4
      - id: magic4
        doc: Unknown.
        size: 7
  condition_data_operation:
    doc: Condition data for `condition_type::operation`.
    seq:
      - id: magic1
        doc: Unknown.
        size: 4
      - id: lhs
        doc: The left-hand condition.
        type: condition
      - id: magic2
        doc: Unkown.
        size: 1
      - id: rhs
        doc: The left-hand condition.
        type: condition
  condition_data_randomizer:
    doc: Condition data for `condition_type::randomizer`.
    seq:
      - id: magic1
        doc: Unknown.
        size: 4
      - id: crystals
        doc: Is this condition true if we're randomizing crystals?
        type: u1
        valid:
          any-of: [0, 1]
      - id: monsters
        doc: Is this condition true if we're randomizing monsters?
        type: u1
        valid:
          any-of: [0, 1]
      - id: bosses
        doc: Is this condition true if we're randomizing bosses?
        type: u1
        valid:
          any-of: [0, 1]
      - id: items
        doc: Is this condition true if we're randomizing items?
        type: u1
        valid:
          any-of: [0, 1]
      - id: recovery
        doc: Is this condition true if we're randomizing recovery items?
        type: u1
        valid:
          any-of: [0, 1]
      - id: progression
        doc: Is this condition true if we're randomizing progression items?
        type: u1
        valid:
          any-of: [0, 1]
      - id: gated
        doc: Is this condition true if we're in gated progression mode?
        type: u1
        valid:
          any-of: [0, 1]
      - id: has_invalid_item
        doc: Do we have an invalid item?
        type: u1
        valid:
          any-of: [0, 1]
      - id: invalid_item
        doc: An item ID to be treated as invalid.
        type: u4
        if: has_invalid_item == 1
  npc_page:
    doc: The behavior code of an NPC.
    seq:
      - id: condition
        doc: The condition for this page to be active.
        type: condition
      - id: trigger
        doc: The method of triggering this page's code.
        type: u1
        enum: trigger
        valid:
          in-enum: true
      - id: trigger_data
        doc: The data associated with the specific trigger.
        type:
          switch-on: trigger
          cases:
            trigger::player_proximity: trigger_data_player_proximity
            trigger::player_touch: trigger_data_player_touch
            _: trigger_data_none
      - id: actions
        doc: The actions executed.
        type: npc_actions_list
      - id: context
        doc: The context of the actions.
        type: u1
        enum: trigger_context
        valid:
          in-enum: true
  trigger_data_player_proximity:
    doc: The data for a NPC page with a trigger of `trigger::player_proximity`.
    seq:
      - id: radius
        doc: The trigger radius.
        type: f4
      - id: min_x
        doc: The smaller X bound.
        type: f4
      - id: min_y
        doc: The smaller Y bound.
        type: f4
      - id: min_z
        doc: The smaller Z bound.
        type: f4
      - id: max_x
        doc: The larger X bound.
        type: f4
      - id: max_y
        doc: The larger Y bound.
        type: f4
      - id: max_z
        doc: The larger Z bound.
        type: f4
      - id: magic2
        doc: Unknown.
        size: 2
  trigger_data_player_touch:
    doc: The data for a NPC page with a trigger of `trigger::player_touch`.
    seq:
      - id: magic1
        doc: Unknown.
        size: 29
      - id: type
        doc: The type of touch that triggers this page.
        type: u1
        enum: touch_type
        valid:
          in-enum: true
  trigger_data_none:
    doc: The data for a trigger with no data. Just empty bytes.
    seq:
      - id: magic1
        doc: Unknown.
        size: 30
  npc_actions_list:
    doc: A list of actions.
    seq:
      - id: num_actions
        doc: The number of actions in this page.
        type: u4
      - id: actions
        doc: The actions that occur when the trigger is met.
        type: npc_action
        repeat: expr
        repeat-expr: num_actions
      # TODO
  npc_action:
    doc: An action execute by an NPC.
    seq:
      - id: type
        doc: The type of action performed.
        type: u4
        enum: action
        valid:
          in-enum: true
      - id: data
        doc: Any data assocated with the action.
        type:
          switch-on: type
          cases:
            action::add_inventory: action_data_inventory
            action::choice_message: action_data_choice_message
            action::add_number: action_data_modify_var
            action::command_npc: action_data_command_npc
            action::condition: action_data_condition
            action::message_hint: action_data_message_hint
            action::message_npc: action_data_message_npc
            action::message: action_data_message
            action::move: action_data_move
            action::move_camera: action_data_move_camera
            action::move_player: action_data_move
            action::remove_inventory: action_data_inventory
            action::revert_camera: action_data_move_camera
            action::set_facing: action_data_set_facing
            action::set_flag: action_data_modify_var
            action::set_number: action_data_modify_var
            action::shop: action_data_shop
            action::shop_recipe: action_data_shop
            action::stop_processing: action_data_stop_processing
            action::trigger_npc: action_data_trigger_npc
            action::wait: action_data_wait
            _: nothing # TODO
  action_data_inventory:
     doc: Data associated with `action::add_inventory` and `action::remove_inventory`.
     seq:
      - id: type
        doc: The item type to give.
        type: u1
        enum: treasure_type
        valid:
          in-enum: true
      - id: item
        doc: The item/equipment ID to give. (TODO - what if currency?)
        type: u4
      - id: count
        doc: The amount of the item to give. (TODO - what if currency?)
        type: u4
      - id: randomized
        doc: Randomize this item?
        type: u1
        valid:
          any-of: [0, 1]
  action_data_command_npc:
    doc: Data associated with `action::command_npc`.
    seq:
      - id: key
        doc: The NPC key to command.
        type: nullable_string
      - id: num_commands
        doc: The number of commands to have the keyed NPC execute.
        type: u4
      - id: commands
        doc: The commands to have the keyed NPC execute.
        type: npc_action
        repeat: expr
        repeat-expr: num_commands
  action_data_choice_message:
    doc: Data associated with `action::choice_message`.
    seq:
      - id: message
        doc: The message to display.
        type: nullable_string
      - id: magic1
        doc: Unknown.
        size: 2
      - id: num_choices
        doc: The number of choices the player can select from.
        type: u4
      - id: choices
        doc: The choices the player can select from.
        type: choice_message_choice
        repeat: expr
        repeat-expr: num_choices
      - id: answer_var
        doc: The variable to place the choice in.
        type: nullable_string
      - id: magic2
        doc: Unknown.
        size: 1
  choice_message_choice:
    doc: A dialogue choice in a `action::choice_message`.
    seq:
      - id: text
        doc: The text displayed to the user.
        type: nullable_string
      - id: magic1
        doc: Unknown.
        size: 4
      - id: item_cost
        doc: Does this cost an item to select?
        type: u1
        valid:
          any-of: [0, 1]
      - id: default
        doc: Is this the default option?
        type: u1
        valid:
          any-of: [0, 1]
      - id: cancel
        doc: Does this option back out of the dialogue?
        type: u1
        valid:
          any-of: [0, 1]
      - id: magic2
        doc: Unknown.
        size: 5
  action_data_condition:
    doc: Data associated with `action::condition`.
    seq:
      - id: condition
        doc: The condition to branch based upon.
        type: condition
      - id: actions_true
        doc: The actions executed if true.
        type: npc_actions_list
      - id: actions_false
        doc: The actions executed if false.
        type: npc_actions_list
  action_data_message_hint:
    doc: Data associated with `action::message_hint`.
    seq:
      - id: has_item
        doc: Are we hinting at the locarion of an item?
        type: u1
        valid:
          any-of: [0, 1]
      - id: item
        doc: The item to hint at.
        type: u4
        if: has_item == 1
      - id: has_job
        doc: Are we hinting at the locarion of a job?
        type: u1
        valid:
          any-of: [0, 1]
      - id: job
        doc: The job to hint at.
        type: u4
        if: has_job == 1
  action_data_message_npc:
    doc: Data associated with `action::message_npc`.
    seq:
      - id: message
        doc: The message to display.
        type: nullable_string
      - id: key
        doc: The key of the NPC to have display this message.
        type: nullable_string
      - id: magic1
        doc: Unknown.
        size: 7
  action_data_message:
    doc: Data associated with `action::message`.
    seq:
      - id: message
        doc: The message to display.
        type: nullable_string
      - id: magic1
        doc: Unknown.
        size: 8
  action_data_move:
    doc: Data associated with `action::move` and `action::move_player`.
    seq:
      - id: "x"
        doc: The X offset to move.
        type: s4
      - id: "y"
        doc: The Y offset to move.
        type: s4
      - id: "z"
        doc: The Z offset to move.
        type: s4
      - id: has_facing
        doc: Do we change our facing when moving?
        type: u1
        valid:
          any-of: [0, 1]
      - id: facing
        doc: The facing we change to while moving.
        type: u1
        enum: facing
        valid:
          in-enum: true
        if: has_facing == 1
      - id: magic1
        doc: Unknown.
        size: 2
      - id: speed
        doc: How fast we move.
        type: f4
      - id: wait
        doc: Our waiting mode.
        type: u1
        enum: move_wait_mode
        valid:
          in-enum: true
      - id: no_collision
        doc: Do we not collide with anything?
        type: u1
        valid:
          any-of: [0, 1]
      - id: has_jump
        doc: Do we change our jump type when moving?
        type: u1
        valid:
          any-of: [0, 1]
      - id: jump
        doc: The jump type we change to while moving.
        type: u1
        enum: jump
        valid:
          in-enum: true
        if: has_jump == 1
      - id: magic2
        doc: Unknown.
        size: 1
  action_data_move_camera:
    doc: Data associated with `action::move_camera` and `action::revert_camera`.
    seq:
      - id: "x"
        doc: The X offset to move. Unused in `action::revert_camera`.
        type: s4
      - id: "y"
        doc: The Y offset to move. Unused in `action::revert_camera`.
        type: s4
      - id: "z"
        doc: The Z offset to move. Unused in `action::revert_camera`.
        type: s4
      - id: magic1
        doc: Unknown.
        size: 2
      - id: frames
        doc: How many frames this movement should occur over.
        type: f4
      - id: magic2
        doc: Unknown.
        size: 1
  action_data_set_facing:
    doc: Data associated with `action::set_facing`.
    seq:
      - id: facing
        doc: The facing to set.
        type: u1
        enum: facing
        valid:
          in-enum: true
  action_data_modify_var:
    doc: Data associated with `action::set_flag`, `action::set_number`, and `action::add_number`.
    seq:
      - id: scope
        doc: The variable's scope.
        type: u1
        enum: scope
        valid:
          in-enum: true
      - id: magic1
        doc: Unknown.
        size: 1
      - id: variable
        doc: The variable to set.
        type: nullable_string
      - id: setting_mode
        doc: Will you be setting this variable based on a constant, or the value of another variable, or so on?
        type: u1
        enum: variable_setting_mode
        valid:
          in-enum: true
      - id: setting_data
        doc: The data associated with the setting mode.
        type:
          switch-on: setting_mode
          cases:
            variable_setting_mode::constant: action_data_varsetmode_constant
            _: nothing # TODO
  action_data_varsetmode_constant:
    doc: The data associated with `variable_setting_mode::constant`.
    seq:
      - id: bool_value
        doc: Whether or not to set or unset the flag, if we're setting a flag.
        type: u1
        valid:
          any-of: [0, 1]
      - id: int_value
        doc: The value to set/add/subtract/etc. the number to, if we're setting a number.
        type: u4
      - id: magic1
        doc: Unknown.
        size: 7
  action_data_shop:
    doc: Data associated with `action::shop` and `action::shop_recipe`.
    seq:
      - id: num_shop_items
        doc: How many items are sold at this shop.
        type: u4
      - id: shop_items
        doc: The items sold at this shop.
        type: shop_item
        repeat: expr
        repeat-expr: num_shop_items
  shop_item:
    doc: A single shop item in the data for a `action::shop` or `action::shop_recipe`.
    seq:
      - id: type
        doc: |
          The type of item sold here.
          In `action::shop`, only `treasure_type::item` and `treasure_type::equipment` are valid here.
          In `action::shop_recipe`s, anything goes.
        type: u1
        enum: treasure_type
        valid:
          in-enum: true
      - id: item
        doc: The ID of an item/equipment/recipe.
        type: u4
      - id: cost_percent
        doc: A number indicating how much more or less this item should cost than the price listed in its database entry. Default is 100.
        type: u4
      - id: condition
        doc: A condition under which the item is sold.
        type: condition
  action_data_stop_processing:
    doc: Data associated with `action::stop_processing`.
    seq:
      - id: refresh_outfit
        type: u1
        valid:
          any-of: [0, 1]
      - id: refresh_page
        type: u1
        valid:
          any-of: [0, 1]
      - id: refresh_position
        type: u1
        valid:
          any-of: [0, 1]
      - id: cancel_all_actions
        type: u1
        valid:
          any-of: [0, 1]
      - id: trigger_player_action
        type: u1
        valid:
          any-of: [0, 1]
      - id: trigger_player_proximity
        type: u1
        valid:
          any-of: [0, 1]
      - id: trigger_auto
        type: u1
        valid:
          any-of: [0, 1]
      - id: trigger_player_touch
        type: u1
        valid:
          any-of: [0, 1]
      - id: trigger_trigger_npc
        type: u1
        valid:
          any-of: [0, 1]
      - id: global_refresh_outfits
        type: u1
        valid:
          any-of: [0, 1]
      - id: global_refresh_pages
        type: u1
        valid:
          any-of: [0, 1]
      - id: global_refresh_positions
        type: u1
        valid:
          any-of: [0, 1]
      - id: global_try_spawn
        type: u1
        valid:
          any-of: [0, 1]
      - id: global_try_despawn
        type: u1
        valid:
          any-of: [0, 1]
      - id: magic1
        doc: Unknown.
        size: 1
  action_data_trigger_npc:
    doc: Data associated with `action::trigger_npc`.
    seq:
      - id: key
        doc: The key of the NPC to trigger.
        type: nullable_string
      - id: type
        doc: The trigger type to invoke.
        type: u1
        enum: trigger
        valid:
          in-enum: true
  action_data_wait:
    doc: Data associated with `action::wait`.
    seq:
      - id: frames
        doc: The number of frames to wait.
        type: u4
  data_sign:
    doc: Data for entities of type `sign`.
    seq:
      - id: title
        doc: The sign's title.
        type: nullable_string
      - id: message
        doc: The sign's message.
        type: nullable_string
      - id: facing
        doc: The direction the sign is facing in.
        type: u1
        enum: facing
        valid:
          in-enum: true
      - id: style
        doc: The 3D rendering method of the sign.
        type: u1
        enum: sign_style
        valid:
          in-enum: true
  data_spark:
    doc: Data for entities of type `spark`.
    seq:
      - id: behaviour
        doc: The ID of spark behaviour object.
        type: u4
      - id: is_unique
        doc: Does this spark not respawn after you encounter it?
        type: u1
        valid:
          any-of: [0, 1]
      - id: is_giant
        doc: Is this spark a boss?
        type: u1
        valid:
          any-of: [0, 1]
      - id: victory_flag
        doc: The global flag set on victory with this spark.
        type: nullable_string
      - id: victory_flag_true
        doc: Unknown. `Global Flag On Victory Is True` in Crystal Edit.
        type: u1
        valid:
          any-of: [0, 1]
      - id: victory_flag_temp
        doc: Is this flag set on victory of `global_temp` scope?
        type: u1
        valid:
          any-of: [0, 1]
      - id: victory_flag_unset_on_spawn
        doc: Do we unset this flag when this spark spawns?
        type: u1
        valid:
          any-of: [0, 1]
      - id: trigger
        doc: The NPC key to trigger on victory.
        type: nullable_string
      - id: num_troops
        doc: The number of troop entries.
        type: u4
      - id: troops
        doc: The possible troop spawns.
        type: possible_troop
        repeat: expr
        repeat-expr: num_troops
  possible_troop:
    doc: An entry in the troop table of spark entities. Represents a possible troop result when colliding with the spark.
    seq:
      - id: id
        doc: The ID of the troop.
        type: u4
      - id: weight
        doc: The chance of this troop being selected for battle. Determines RNG weights.
        type: u4
      - id: invert
        doc: Invert the conditions?
        type: u1
        valid:
          any-of: [0, 1]
      - id: has_min_diff
        doc: Does this troop only spawn under a certain difficulty?
        type: u1
        valid:
          any-of: [0, 1]
      - id: min_diff
        doc: The ID of a difficulty that this troop only spawns in.
        type: u4
        if: has_min_diff == 1
  data_door:
    doc: Data for entities of type `door`.
    seq:
      - id: style
        doc: The 3D rendering method of the door.
        type: u1
        enum: door_style
        valid:
          in-enum: true
      - id: locked
        doc: Is this door locked?
        type: u1
        valid:
          any-of: [0, 1]
      - id: has_key
        doc: Does this door have a key?
        type: u1
        valid:
          any-of: [0, 1]
      - id: key
        doc: The item ID of the key that can unlock this door.
        type: u4
        if: has_key == 1
      - id: flag
        doc: The global flag set when this door is unlocked.
        type: nullable_string
      - id: invert_flag
        doc: Invert the global flag?
        type: u1
        valid:
          any-of: [0, 1]
  data_home_point:
    doc: Data for entities of type `home_point`.
    seq:
      - id: name
        doc: The name of the save point.
        type: nullable_string
  data_treasure:
    doc: Data for entities of type `treasure`.
    seq:
      - id: facing
        doc: The direction the chest is facing.
        type: u1
        enum: facing
        valid:
          in-enum: true
      - id: type
        doc: The type of thing inside this chest.
        type: u1
        enum: treasure_type
        valid:
          in-enum: true
      - id: contents
        doc: The contents of this chest. An item/equipment ID, or the amount of currency, depending on `type`.
        type: u4
      - id: has_style_override
        doc: Does this chest have a style override?
        type: u1
        valid:
          any-of: [0, 1]
      - id: style_override
        doc: Overrides the color of the chest.
        type: u1
        enum: treasure_style
        valid:
          in-enum: true
        if: has_style_override == 1
  data_crystal:
    doc: Data for entities of type `crystal`.
    seq:
      - id: magic1
        doc: Unknown. Seemingly always a 1.
        type: u1
        valid: 1
      - id: job
        doc: The ID of the job you get at this crystal.
        type: u4
      - id: r
        doc: The color of the crystal. Red channel.
        type: u1
      - id: g
        doc: The color of the crystal. Green channel.
        type: u1
      - id: b
        doc: The color of the crystal. Blue channel.
        type: u1
      - id: offset_half_x
        doc: Offset this crystal half a block on the X axis?
        type: u1
        valid:
          any-of: [0, 1]
      - id: offset_half_z
        doc: Offset this crystal half a block on the Z axis?
        type: u1
        valid:
          any-of: [0, 1]
  data_marker:
    doc: Data for entities of type `marker`.
    seq:
      - id: key
        doc: The flag that's set when this marker is reached.
        type: nullable_string
      - id: proximity
        doc: How close you have to be to trigger this marker.
        type: f4
