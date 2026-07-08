
ADDRESSES = {
    "TRS80": {
        "PYRAMID_L1": {
            "File": "d:\\ComputerArcheology\\content\\trs80\\pyramid\\code1.md",
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
            "File": "d:\\ComputerArcheology\\content\\trs80\\pyramid\\code.md",
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
            "File": "d:\\ComputerArcheology\\content\\trs80\\hauntedhouse\\code1.md",
            "RoomTable": (0x477F, 0x47BB),
            "RoomScripts": (0x47BF, 0x48C7),
            "ObjectData": (0x48C8, 0x48E0),
            "ObjectDescriptions": (0x48E3, 0x48FB),
            "ScriptCommands": (0x48FD, 0x491D),
            "WordTable": (0x4A4B, 0x4AF1),
            "GeneralScript": (0x4AF2, 0x4B34)
        },
        "HAUNTEDHOUSE2": {
            "File": "d:\\ComputerArcheology\\content\\trs80\\hauntedhouse\\code2.md",
            "RoomTable": (0x4782, 0x479E),
            "RoomScripts": (0x47A2, 0x4914),
            "ObjectData": (0x4915, 0x492D),
            "ObjectDescriptions": (0x4933, 0x494B),
            "ScriptCommands": (0x494D, 0x496B),
            "WordTable": (0x4A9A, 0x4B19),
            "GeneralScript": (0x4B1A, 0x4B50)
        },
        "RAAKATU": {
            "File": "d:\\ComputerArcheology\\content\\trs80\\raakatu\\code.md",
            "ScriptCommands": (0x5066, 0x50B8),
            "PhraseList": (0x50B9, 0x52C1),
            "WordTable": (0x52C3, 0x5650),
            "ObjectData": (0x5651, 0x680F),
            "RoomScripts": (0x681F, 0x73FA),
            "GeneralScript": (0x73FB, 0x7BCB),
            "Subroutines": (0x7BCD, 0x7F9C),
        },
        "BEDLAM": {
            "File": "d:\\ComputerArcheology\\content\\trs80\\bedlam\\code.md",
        },
        "XENOS": {
            "File": "d:\\ComputerArcheology\\content\\trs80\\xenos\\code.md",
        }
    }, 
    "COCO": {
        "PYRAMID": {
            "File": "d:\\ComputerArcheology\\content\\coco\\pyramid\\code.md",
            "RoomTable": (0x112E, 0x126E),
            "RoomScripts": (0x1272, 0x17E9),
            "AmbientLightTable": (0x17EB, 0x188B),
            "ObjectData": (0x188D, 0x18E3),
            "ObjectInfo": (0x18ED, 0x1943),
            "ScriptCommands": (0x0A17, 0x0A4F),
            "WordTable": (0x3C40, 0x3F15),
            "GeneralScript": (0x1945, 0x1B65)
        },
        "RAAKATU": {
            "File": "d:\\ComputerArcheology\\content\\coco\\raakatu\\code.md",
        },
        "BEDLAM": {
            "File": "d:\\ComputerArcheology\\content\\coco\\bedlam\\code.md",
        }
    }
}


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