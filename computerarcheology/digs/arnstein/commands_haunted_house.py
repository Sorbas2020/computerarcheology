import binary_utils

COMMANDS = {
0x01:     ['move_look',                          'room_num'],
0x02:     ['is_in_pack',                         'obj_num'],
0x03:     ['is_in_pack_or_current_room',         'obj_num'],
0x04:     ['print','ps_num'                      ],
0x05:     ['print_room_description'              ],
0x06:     ['stop_if_pass'                        ],
0x07:     ['endless_loop'                        ],
0x08:     ['drop_object_print_ok',               'obj_num','(NEVER USED)'],
0x09:     ['print_inventory'                     ],
0x0A:     ['is_object_user_input',               'obj_num'      ],
0x0B:     ['get_from_room_print_ok',             'obj_num'    ],
0x0C:     ['print_ok'                            ],
0x0D:     ['move_object_to_room',                'obj_num','room_num'],
0x0E:     ['get_users_object_print_ok'           ],
0x0F:     ['drop_users_object_print_ok'          ],
0x10:     ['is_in_current_room',                 'obj_num'],
0x11:     ['load_goto_second_floor'              ],
}


class Commands:
    def __init__(self):
        self.code_address_trs80_house1 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/hauntedhouse/Code1.md", 
            "48FD:", 
            "491D:")
        self.code_address_trs80_house2 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/hauntedhouse/Code2.md", 
            "494D:", 
            "496B:")        
    
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
        
    def get_command_address_trs80_house1(self, num):
        if num < len(self.code_address_trs80_house1):
            return self.code_address_trs80_house1[num]
        else:
            return None
    
    def get_command_address_trs80_house2(self, num):
        if num < len(self.code_address_trs80_house2):
            return self.code_address_trs80_house2[num]
        else:
            return None   
    

if __name__ == "__main__":
    c = Commands()