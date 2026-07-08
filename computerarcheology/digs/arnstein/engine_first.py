COMMANDS_PYRAMID = {
0x01:     ['move_look',                          'room_num'],
0x02:     ['is_in_pack',                         'obj_num'],
0x03:     ['is_in_pack_or_current_room',         'obj_num'],
0x04:     ['print','ps_num'                      ],
0x05:     ['death_and_resurrect'                 ],
0x06:     None,
0x07:     ['stop_if_pass'                        ],
0x08:     ['print_score'                         ],
0x09:     ['end_of_game'                         ],
0x0A:     ['pyramid_crawl_move_random',          'value'],
0x0B:     ['drop_object_print_ok',               'obj_num'],
0x0C:     ['move_to_room_if_was_last',           'room_num'],
0x0D:     ['is_pack_just_emerald'                ],
0x0E:     ['move_to_last_room'                   ],
0x0F:     ['print_inventory'                     ],
0x10:     ['print_room_description'              ],
0x11:     ['is_object_user_input',               'obj_num'],
0x12:     ['get_from_room_print_ok',             'obj_num'],
0x13:     None,
0x14:     ['print_ok'                            ],
0x15:     ['move_object_to_room',                'obj_num','room_num'],
0x16:     ['get_users_object_print_ok'           ],
0x17:     ['drop_users_object_print_ok'          ],
0x18:     ['move_object_to_current_room',        'obj_num'],
0x19:     ['put_object_in_container_print_ok',   'obj_num','obj_num'],
0x1A:     ['is_in_current_room',                 'obj_num'],
0x1B:     ['load_game'                           ],
0x1C:     ['save_game'                           ],
0x1D:     ['scramble_directions_print_ack'       ],
}

COMMANDS_HAUNTEDHOUSE = {
    0x01: COMMANDS_PYRAMID[0x01],
    0x02: COMMANDS_PYRAMID[0x02],
    0x03: COMMANDS_PYRAMID[0x03],
    0x04: COMMANDS_PYRAMID[0x04],
    0x05: COMMANDS_PYRAMID[0x10],
    0x06: COMMANDS_PYRAMID[0x07],
    0x07: COMMANDS_PYRAMID[0x09],
    0x08: COMMANDS_PYRAMID[0x0B],
    0x09: COMMANDS_PYRAMID[0x0F],
    0x0A: COMMANDS_PYRAMID[0x11],
    0x0B: COMMANDS_PYRAMID[0x12],
    0x0C: COMMANDS_PYRAMID[0x14],
    0x0D: COMMANDS_PYRAMID[0x15],
    0x0E: COMMANDS_PYRAMID[0x16],
    0x0F: COMMANDS_PYRAMID[0x17],
    0x10: COMMANDS_PYRAMID[0x1A],
    # Just for Haunted House, not in Pyramid
    0x11: ['load_second_floor']
}

ADDRESSES = {
    "TRS80": {
        "PYRAMID_L1": {
            "File": "/git/ComputerArcheology/content/trs80/pyramid/code1.md",
            "Commands": COMMANDS_PYRAMID,
            "RoomTable": (0x4825, 0x4965),
            "RoomScripts": (0x4969, 0x4EE0),
            "AmbientLightTable": (0x4EE2, 0x4F82),
            "ObjectData": (0x4F84, 0x4FDA),
            "ObjectDescriptions": (0x4FE4, 0x503A),
            "ScriptCommands": (0x503C, 0x5074),
            "WordTable": (0x5622, 0x5903),
            "GeneralScript": (0x5904, 0x5B2E)
        },
        "PYRAMID_L2": {
            "File": "/git/ComputerArcheology/content/trs80/pyramid/code.md",
            "Commands": COMMANDS_PYRAMID,
            "RoomTable": (0x4888, 0x49C8),
            "RoomScripts": (0x49CC, 0x4F43),
            "AmbientLightTable": (0x4F45, 0x4FE5),
            "ObjectData": (0x4FE7, 0x503D),
            "ObjectDescriptions": (0x5047, 0x509D),
            "ScriptCommands": (0x509F, 0x50D7),
            "WordTable": (0x56CE, 0x59AF),
            "GeneralScript": (0x59B0, 0x5BDA)
        },
        "HAUNTEDHOUSE1": {
            "File": "/git/ComputerArcheology/content/trs80/hauntedhouse/code1.md",
            "Commands": COMMANDS_HAUNTEDHOUSE,
            "RoomTable": (0x477F, 0x47BB),
            "RoomScripts": (0x47BF, 0x48C7),
            "ObjectData": (0x48C8, 0x48E0),
            "ObjectDescriptions": (0x48E3, 0x48FB),
            "ScriptCommands": (0x48FD, 0x491D),
            "WordTable": (0x4A4B, 0x4AF1),
            "GeneralScript": (0x4AF2, 0x4B34)
        },
        "HAUNTEDHOUSE2": {
            "File": "/git/ComputerArcheology/content/trs80/hauntedhouse/code2.md",
            "Commands": COMMANDS_HAUNTEDHOUSE,
            "RoomTable": (0x4782, 0x479E),
            "RoomScripts": (0x47A2, 0x4914),
            "ObjectData": (0x4915, 0x492D),
            "ObjectDescriptions": (0x4933, 0x494B),
            "ScriptCommands": (0x494D, 0x496B),
            "WordTable": (0x4A9A, 0x4B19),
            "GeneralScript": (0x4B1A, 0x4B50)
        },        
    }, 
    "COCO": {
        "PYRAMID": {
            "File": "/git/ComputerArcheology/content/coco/pyramid/code.md",
            "Commands": COMMANDS_PYRAMID,
            "RoomTable": (0x112E, 0x126E),
            "RoomScripts": (0x1272, 0x17E9),
            "AmbientLightTable": (0x17EB, 0x188B),
            "ObjectData": (0x188D, 0x18E3),
            "ObjectInfo": (0x18ED, 0x1943),
            "ScriptCommands": (0x0A17, 0x0A4F),
            "WordTable": (0x3C40, 0x3F15),
            "GeneralScript": (0x1945, 0x1B65)
        },        
    }
}

def read_code_file(file_name):
    ret = []
    with open(file_name, "r") as f:
        for line in f:
            ret.append(line.strip())
    return ret

def write_code_file(file_name, code):
    # Please, please, please use github to back this up first
    with open(file_name, "w") as f:
        for line in code:
            f.write(line + "\n")

def find_start_and_end(lines, start_addr, end_addr):
    ps = 0
    while not lines[ps].startswith(f'{start_addr:04X}:'):
        ps += 1
    pe = ps
    while not lines[pe].startswith(f'{end_addr:04X}:'):
        pe += 1
    pe += 1
    return ps, pe

def split_comment(line):
    i = line.find(';')
    if i > -1:
        return line[:i].rstrip(), line[i:].lstrip()
    else:
        return line, ''

def update_command_names(info):
    lines = read_code_file(info["File"])

    # Update the command table itself
    ps, pe = find_start_and_end(lines, info["ScriptCommands"][0], info["ScriptCommands"][1])
    if lines[ps-1] != 'ScriptCommands:':
        raise Exception(f'Expected ScriptCommands: label at {info["ScriptCommands"][0]:04X} (line {ps})')
    addresses = {}
    while ps < pe:
        line = lines[ps]
        ps += 1
        i = line.find('COM_')
        if i>-1:
            cn = int(line[i+4:i+6], 16)
            addresses[cn] = int(line[9:11] + line[6:8], 16)            
            # TODO print both
            line = f'{line[:11]}        ; COM_{cn:02X}_{info["Commands"][cn][0]}({", ".join(info["Commands"][cn][1:])})'
            lines[ps-1] = line    

    # Update the individual command routines
    for i, addr in addresses.items():       

        # The label 
        ps,pe = find_start_and_end(lines, addr, addr)
        lab = lines[ps-1]
        if lab.startswith('COM_') and lab.endswith(':'):
            labn = f'COM_{i:02X}_{info["Commands"][i][0]}:'
            lines[ps-1] = labn
            # print('>>>',lab,labn)
        else:
            raise Exception(f'Label not found for command at {addr:04X} (line {ps})')
        
        # The markdown
        while not lines[ps].startswith('# COM_'):
            ps -= 1
        if not lines[ps].startswith(f'# COM_{i:02X}_'):
            raise Exception(f'Markdown not found for command at {addr:04X} (line {ps})')
        lines[ps] = f'# COM_{i:02X}_{info["Commands"][i][0]}({", ".join(info["Commands"][i][1:])})'
        # print(lines[ps])


def read_command_table(file_path, start_addr, end_addr, little_endian=False):
    ret = []
    with open(file_path, "r") as f:            
        g = ''
        while not g.startswith(start_addr):
            g = f.readline()
        g = g.strip()
        while True: # not g.startswith(end_addr):
            if not g: # Stop on blank lines too
                break
            if len(g)>4 and g[4] == ':':
                if little_endian:
                    addr = int(g[6:8] + g[9:11], 16)
                else:
                    addr = int(g[9:11] + g[6:8], 16)
                ret.append(addr)
                print(f'addr: {addr:04X}')    
                # Up to and including the end address
                if g.startswith(end_addr):
                    print('-----FOUND ',len(ret))
                    print('')
                    break        
            g = f.readline()
            g = g.strip()
    return ret

info = ADDRESSES["TRS80"]["PYRAMID_L1"]
update_command_names(info)

# code = read_code_file(info["File"])

# ps = 0
# while not code[ps].startswith(f'{info["ScriptCommands"][0]:04X}:'):
#     ps += 1
# pe = ps
# while not code[pe].startswith(f'{info["ScriptCommands"][1]:04X}:'):
#     pe += 1
# pe += 1

# command_table = []

# cn = 1
# x = ps
# y = pe
# while x < y:
#     line = code[x]    
#     if len(line) > 4 and line[4] == ':':
#         addr = int(line[9:11] + line[6:8], 16)        
#         command_table.append(addr)
#         if addr:
#             line = f'{line[:11]}        ; COM _{cn:02X}_{info["Commands"][cn][0]}({", ".join(info["Commands"][cn][1:])})'
#             print(">>>",line)
#         cn += 1
#     x += 1
# print(code[ps:pe])

