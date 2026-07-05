import binary_utils

COMMANDS = {
    0x00: ['move_and_look',                  'room_num'],
    0x01: ['is_in_pack_or_room',             'obj_num'],
    0x02: ['is_owned_by',                    'obj_num'],
    0x03: ['is_located',                     'room_num','obj_num'],
    0x04: ['print', 'mlength'                ],
    0x05: ['is_leq_last_random',             'value'],
    0x06: ['print_inventory',                ],
    0x07: ['print_room_description',         ],
    0x08: ['is_noun1',                       'obj_num'],
    0x09: ['is_noun2',                       'obj_num'],
    0x0A: ['is_input_phrase',                'phrase_num'],
    0x0B: ['switch',                         'mlength','num'],
    0x0C: ['fail',                           ],
    0x0D: ['group_AND',                      'mlength'],
    0x0E: ['group_OR',                       'mlength'],
    0x0F: ['pick_up_var_object',             ],
    0x10: ['drop_var_object',                ],
    0x11: ['print_noun1',                    ],
    0x12: ['print_noun2',                    ],
    0x13: ['process_phrase_by_room',         ],
    0x14: ['reverse_status',                 ],
    0x15: ['is_var_attributes',              'bits'],
    0x16: ['print_var',                      ],
    0x17: ['move_object_to',                 'obj_num','destination'],
    0x18: ['is_var_owned_by_active',         ],
    0x19: ['move_to_room',                   'room_num'],
    0x1A: ['set_var_to_noun1',               ],
    0x1B: ['set_var_to_noun2',               ],
    0x1C: ['set_var_object',                 'obj_num'],
    0x1D: ['attack_var',                     'points'],
    0x1E: ['swap_object_locations',          'obj_num1','obj_num2'],
    0x1F: ['print2',                         'mlength'],
    0x20: ['is_active_object',               'obj_num'],
    0x21: ['execute_phrase',                 'phrase_num','obj_num1','obj_num2'],
    0x22: ['is_less_equal_health',           'points'],
    0x23: ['heal_var',                       'points'],
    0x24: ['exit_program',                   ],
    0x25: ['print_linefeed',                 ],
    0x26: ['print_score',                    ],
    0x27: ['load_game',                      ],
    0x28: ['save_game',                      ],
    0x29: ['toggle_var_open',                ],
    0x2A: ['toggle_var_lock',                ],
    0x2B: ['generate_random',                ],
    0x2C: ['set_active',                     'obj_num'],
    0x2D: ['is_var_object',                  'obj_num'],
    0x2E: ['is_var_ext_attributes',          'bits'],
    0x2F: ['load_section_from_disk',         'section_num'],
    0x30: ['set_current_room',               'room_num'],
    0x31: ['put_noun2_in_var_object',        ],
    0x32: ['put_noun1_in_var_object',        ],
    0x33: ['print_objects_on_var_object',    ],
    0x34: ['save_system_objects_to_disk',    ],
    0x35: ['load_system_objects_from_disk',  ],
    0x36: ['is_in_room_or_open_container',   'obj_num'],
    0x37: ['is_player_in_an_object',         ],
    0x38: ['bump_score',                     ],
    0x39: ['is_weight_70_or_less',           ],
    0x3A: ['clear_screen',                   ],
    0x3B: ['wait_for_key_123',               ],
}


class Commands:
    def __init__(self):
        self.code_address = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/xenos/Code.md", 
            "7268:", 
            "72DE:")
    
    def get_command_name(self, num):
        if num in COMMANDS:
            return COMMANDS[num][0]
        else:
            return None
    
    def get_command_args(self, num):
        if num in COMMANDS:
            return COMMANDS[num][1:]
        else:
            return None
        
    def get_command_address(self, num):
        if num < len(self.code_address):
            return self.code_address[num]
        else:
            return None

if __name__ == "__main__":
    c = Commands()
