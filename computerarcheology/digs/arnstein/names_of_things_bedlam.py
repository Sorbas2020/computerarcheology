SECTIONS = {
    0x01: 'ADJECTIVES',
    0x02: 'SHORT_NAME',
    0x03: 'DESCRIPTION',
    0x04: 'COMMANDS',
    0x06: 'IF_SECOND_NOUN',
    0x07: 'IF_FIRST_NOUN',
    0x08: 'EVERY_TURN',
    0x09: 'HIT_POINTS',
    0x0A: 'UPON_DEATH',
    0x0B: 'IF_GIVEN_COMMAND',
    0x0C: 'WEIGHT',   
}

ROOMS = {

    # 1: {          
    #     0x00: 'nowhere', 
    #     0x01: 'PLAYER', 
    #     0x80: 'HIGHWAY_WEST',
    #     0x81: 'WEST_OF_STATION1',
    #     0x82: 'FRONT_OF_STATION',
    #     0x83: 'GAS_STATION',
    #     0x84: 'WEST_OF_STATION2',
    #     0x85: 'SOUTHWEST_OF_STATION',
    #     0x86: 'JUNKYARD',
    #     0x87: 'SOUTHEAST_OF_STATION',
    #     0x88: 'EAST_OF_STATION',
    #     0x89: 'CITY_LIMIT',
    #     0x8C: 'SOUTHWEST_OF_SHERIFF',
    #     0xAD: 'NORTH_OF_HIGHWAY1',
    #     0xAE: 'NORTH_OF_HIGHWAY2',
    #     0xAF: 'NORTH_OF_HIGHWAY3',
    #     0xB0: 'DESERT_SOUTH1',
    #     0xDA: 'RESTROOM',
    # },    
}

COMMANDS = {
    0x00: 'move_and_look',
    0x01: 'is_in_pack_or_room',
    0x02: 'is_owned_by',
    0x03: 'is_located',
    0x04: 'print',
    0x05: 'is_leq_last_random',
    0x06: 'print_inventory',
    0x07: 'print_room_description',
    0x08: 'is_noun1',
    0x09: 'is_noun2',
    0x0A: 'is_input_phrase',
    0x0B: 'switch',
    0x0C: 'fail',
    0x0D: 'group_AND',
    0x0E: 'group_OR',
    0x0F: 'pick_up_var_object',
    0x10: 'drop_var_object',
    0x11: 'print_noun1',
    0x12: 'print_noun2',
    0x13: 'process_phrase_by_room',
    0x14: 'reverse_status',
    0x15: 'is_var_attributes',
    0x16: 'print_var',
    0x17: 'move_object_to',
    0x18: 'is_var_owned_by_active',
    0x19: 'move_to_room',
    0x1A: 'set_var_to_noun1',
    0x1B: 'set_var_to_noun2',
    0x1C: 'set_var_object',
    0x1D: 'attack_var',
    0x1E: 'swap_object_locations',
    0x1F: 'print2',
    0x20: 'is_active_object',
    0x21: 'execute_phrase',
    0x22: 'is_less_equal_health',
    0x23: 'heal_var',
    0x24: 'endless_loop',
    0x25: 'restart_game',
    0x26: 'print_score',
    0x27: 'load_game',
    0x28: 'save_game',
    0x29: 'toggle_var_open',
    0x2A: 'toggle_var_lock',
    0x2B: 'generate_random',
    0x2C: 'set_active',
    0x2D: 'is_var_object',
}

ROUTINES = {
    # 0x81: 'PRINT_DOOR_HERE',
    # 0x80: 'PRINT_SHOTGUN_HERE',        
}

ATTRIBUTES = {
    # 0x80: '??',
    # 0x40: 'Weapon',
    # 0x20: 'Portable',
    # 0x10: 'Alive',
    # 0x08: 'Openable',
    # 0x04: 'Readable',
    # 0x02: 'Holder',
    # 0x01: 'Surface'
}

def get_attribute_name(value):
    # attributes=?QW.S...(liQuid, Weapon, Surface)
    ret_bits = ''
    ret_words = []
    for bit, name in ATTRIBUTES.items():
        if value & bit:
            for p in name:
                if p=='?' or p.isupper():
                    ret_bits += p
                    break
            ret_words.append(name)
        else:
            ret_bits += '.'
    return f'{ret_bits}({",".join(ret_words)})'

def get_section_name(section):
    return f'SECTION_{section:02X}_{SECTIONS[section]}'

def get_room_name(section, room):
    disk_section = ROOMS[section]
    if room not in disk_section:
        return f'RM_{section}_{room:02X}_??'
    name = disk_section[room]
    return f'RM_{section}_{name}'

def get_command_name(command):
    return f'COM_{command:02X}_{COMMANDS[command]}'

def get_routine_name(routine):
    if routine not in ROUTINES:
        return f'FN_{routine:02X}_??'
    return f'FN_{routine:02X}_{ROUTINES[routine]}'

def get_object_name(object):
    if object==0:
        return 'nothing'
    if object not in OBJECTS:
        return f'OBJ_{object:02X}_??'
    return f'OBJ_{object:02X}_{OBJECTS[object]}'

def get_destination(section, room_num):
        
        if room_num==0:
            return 'nowhere'        
        
        if room_num>=0x80:
            return get_room_name(section, room_num)
        else:
            return get_object_name(room_num)
        
    