import sections
import words
import rooms

TRAVEL = {}

org_data = sections.SECTIONS[3]

for record in org_data:
    info = record.split('\t')
    source_room = int(info[0])
    d = info[1].rjust(10,'0')  # cccccccddd
    dest_cond = int(d[:7])
    dest_room = int(d[7:])
    verbs = info[2:]

    all_words = []
    for w in verbs:
        w = int(w)
        wds = words.WORDS.get(w,[f'??{w}??'])
        for ww in wds:
            all_words.append(ww)
    
    if source_room not in TRAVEL:
        TRAVEL[source_room] = []
    TRAVEL[source_room].append((dest_room, dest_cond, all_words))

for rn in range(1,141):
    desc = rooms.ROOMS[rn]['long']
    trav = TRAVEL[rn]
    print(f'---------------- {rn} ----------------')
    print('\n'.join(desc))
    for t in trav:
        print(f'    {t}')
    print('')



