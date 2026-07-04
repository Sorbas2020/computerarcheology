
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