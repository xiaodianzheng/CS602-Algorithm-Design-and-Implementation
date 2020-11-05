import sys
from decimal import Decimal


def driving_mode(batt, num_seg, data):
    choice_dict = {str(batt * 100): (0, None)}
    for i in range(num_seg):
        new_choice_dict = {}
        for prev_batt, info in list(choice_dict.items()):
            # petrol mode
            p_new_batt = Decimal(prev_batt)
            if info[1] is None or info[1] == 'b':
                p_new_batt -= Decimal(1)
            p_new_batt += Decimal(data[i][0] * data[i][1] * 0.1)
            if p_new_batt > 100:
                p_new_batt = Decimal(100)
            p_new_info = (info[0] + data[i][0], 'p')
            if str(p_new_batt) not in choice_dict.keys() or (str(p_new_batt) in choice_dict.keys() and p_new_info[0] < choice_dict[str(p_new_batt)][0]):
                new_choice_dict[str(p_new_batt)] = p_new_info
            # battery mode
            if Decimal(prev_batt) >= 11 or (Decimal(prev_batt) >= 10 and info[1] == 'b'):
                b_new_batt = Decimal(prev_batt)
                if info[1] is None or info[1] == 'p':
                    b_new_batt -= Decimal(1)
                b_new_batt -= Decimal(0.2 * data[i][0])
                b_new_info = (info[0], 'b')
                if str(b_new_batt) not in choice_dict.keys() or (str(b_new_batt) in choice_dict.keys() and b_new_info[0] < choice_dict[str(b_new_batt)][0]):
                    new_choice_dict[str(b_new_batt)] = b_new_info
        choice_dict.clear()
        choice_dict = new_choice_dict
        removing = set()
        for a_batt, a_info in list(choice_dict.items()):
            if a_batt not in removing:
                for b_batt, b_info in list(choice_dict.items()):
                    if b_batt != a_batt:
                        if a_info[1] == b_info[1]:
                            if Decimal(b_batt) >= Decimal(a_batt) and b_info[0] <= a_info[0]:
                                removing.add(a_batt)
                                break
                            elif Decimal(b_batt) <= Decimal(a_batt) and b_info[0] >= a_info[0]:
                                removing.add(b_batt)
                        elif a_info[1] == 'b' and b_info[1] == 'p':
                            if Decimal(b_batt) - 1 >= Decimal(a_batt) and b_info[0] <= a_info[0]:
                                removing.add(a_batt)
                                break
                        elif a_info[1] == 'p' and b_info[1] == 'b':
                            if Decimal(b_batt) <= Decimal(a_batt) - 1 and b_info[0] >= a_info[0]:
                                removing.add(b_batt)
        for r in removing:
            del choice_dict[r]
    cost_list = [Decimal(batt * 100) - Decimal(b) + Decimal(choice_dict[b][0] * 0.2) if Decimal(batt * 100) >= Decimal(b) else choice_dict[b][0] * 0.2 for b in choice_dict.keys()]
    return min(cost_list)


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    batt, num_seg = float(s[0]) / 100, int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i + 2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))