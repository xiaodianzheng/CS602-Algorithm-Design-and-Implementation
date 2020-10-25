import sys
#
#
# def compute_theoretical_return(plan):
#     if plan[0] == plan[1] - switch_time:
#         theo_return = total_d_remain * 12/32 * 0.2
#     else:
#         d2 = total_d_remain - d that use to equal plan[0] and plan[1] - switch_time
#         theo_return = max(plan[0],plan[1] - switch_time) + d2 * 12/32 * 0.2
#     return theo_return
#
#
# def dynamic_filt(a_b, a_p, a_switch, a_batt, a_prev_choice, a_cost, n):
#     nonlocal new_choice # store the result for next loop
#     try:
#         for j in range(len(new_choice)):
#             c_b, c_p, c_switch, c_batt, c_prev_choice, _ = new_choice[j]
# # exist plan C such that C is better than A, then A can give up:
#             switch_cost = (c_prev_choice != a_prev_choice)
#             if c_b > a_b: # C_sum_b > A_sum_b
#                 if c_batt - switch_cost >= a_batt: # C can do all choice A can do in later plan
#                     if c_p - c_switch - switch_cost > a_p - a_switch + c_batt - a_batt:
#                         break
# # if for plan A, there exist plan D such A is better than D. Then A can replace D
#             elif a_batt - switch_cost >= c_batt:
#                 if a_p - a_switch - switch_cost > c_p - c_switch + a_batt - c_batt:
#                     new_choice[j] = [a_b, a_p, a_switch, a_batt, a_prev_choice, a_cost]
#                     break
#         else:
#             new_choice.append([a_b, a_p, a_switch, a_batt, a_prev_choice, a_cost])
#     except ValueError:
#         new_choice.append([a_b, a_p, a_switch, a_batt, a_prev_choice, a_cost])
#
#
# def find_one_ok():
#     #use some way to find one avaiable plan, that has relatively small cost.
#     return D * 0.2 - cost # which is the return


def driving_mode(batt, num_seg, data):
    total_d = sum([data[i][0] for i in range(num_seg)])
    choice_dict = {batt * 100: (0, 0, 0, None, 0)}
    for i in range(num_seg):
        for prev_batt, info in list(choice_dict.items()):
            pruning = False
            if prev_batt - sum([data[j][0] for j in range(i, num_seg)]) * 0.2 > batt * 100:
                # print(prev_batt, info)
                pruning = True

            if not pruning:
                # petrol mode
                p_new_batt = prev_batt + data[i][0] * data[i][1] * 0.1

                if p_new_batt > 100:
                    p_new_batt = 100

                if info[3] is None or info[3] == 'b':
                    p_new_info = (
                        info[0] + data[i][0], info[1] + data[i][0] * data[i][1] * 0.1, info[2] + 1, 'p', i + 1)

                else:
                    p_new_info = (
                        info[0] + data[i][0], info[1] + data[i][0] * data[i][1] * 0.1, info[2], 'p', i + 1)
                if i != num_seg - 1 or p_new_info[1] - p_new_info[2] >= 0:
                    if p_new_batt in choice_dict.keys() and p_new_info[0] < choice_dict[p_new_batt][0]:
                        choice_dict[p_new_batt] = p_new_info
                    elif p_new_batt not in choice_dict.keys():
                        choice_dict[p_new_batt] = p_new_info

                # battery mode
                if prev_batt > 11:
                    b_new_batt = prev_batt - 0.2 * data[i][0]

                    if info[3] is None or info[3] == 'p':
                        b_new_info = (info[0], info[1], info[2] + 1, 'b', i + 1)
                    else:
                        b_new_info = (info[0], info[1], info[2], 'b', i + 1)

                    if i != num_seg - 1 or b_new_info[1] - b_new_info[2] >= 0:
                        if b_new_batt in choice_dict.keys() and b_new_info[0] < choice_dict[b_new_batt][0]:
                            choice_dict[b_new_batt] = b_new_info
                        elif b_new_batt not in choice_dict.keys():
                            choice_dict[b_new_batt] = b_new_info

            if i < num_seg:
                del choice_dict[prev_batt]
    return_list = [min(choice_dict[key][1] - choice_dict[key][2], (total_d - choice_dict[key][0]) * 0.2) for key in choice_dict.keys()]
    print(len(choice_dict))
    # for key in choice_dict.keys():
    #     print(key, choice_dict[key])
    return 0.2 * total_d - max(return_list)
    # return max(return_list)



    # exist_return = find_one_ok()
    # choice_list = [0, 0, batt, 2]  # [Sum B, Sum D_times_r,battery,prev choice]
    # for i in num_seg:
    #     new_choice = []
    #     for current_plan in choice_list:
    #     # next run Battery
    #         if current_plan[2] >= 10 + (current_plan[3] != 0):
    #             if exist_return < compute_theoretical_return(current_plan):
    #                 dynamic_filt(current_plan)
    #         # next run Pertol
    #         if exist_return < compute_theoretical_return(current_plan):
    #             dynamic_filt(current_plan)
    # best_return = max([list_of_return])
    # # compute return based on return = min(Sum_B,Sum D_times_r - switch time)
    # return total_distance * 0.2 - best_return



    # state = {}
    # state['p'] = (batt * 100 - 1 + 0.1 * data[0][0] * data[0][1], 0.2 * data[0][0])
    # state['b'] = (batt * 100 - 1 - 0.2 * data[0][0], 0)
    # num_prune = 0
    # for i in range(1, num_seg):
    #     update_state = {}
    #     for key, value in state.items():
    #         prune_pp = False
    #         prune_bp = False
    #         prune_pb = False
    #         prune_bb = False
    #         new_pp_batt = value[0] + 0.1 * data[i][0] * data[i][1]
    #         new_bp_batt = value[0] + 0.1 * data[i][0] * data[i][1] - 1
    #         new_bb_batt = value[0] - 0.2 * data[i][0]
    #         new_pb_batt = value[0] - 0.2 * data[i][0] - 1
    #         if new_pp_batt > 100:
    #             new_pp_batt = 100
    #         if new_bp_batt > 100:
    #             new_bp_batt = 100
    #         new_p_cost = value[1] + 0.2 * data[i][0]
    #
    #         if key[-1] == 'b':
    #             all_b_batt = value[0]
    #         else:
    #             all_b_batt = value[0] - 1
    #         for j in range(i, num_seg):
    #             all_b_batt -= 0.2 * data[j][0]
    #         if all_b_batt > batt * 100:
    #             print(key)
    #             continue
    #
    #         if i == num_seg - 1 and new_pp_batt > batt * 100:
    #             print("----------")
    #             print(key)
    #             num_prune += 1
    #             prune_pp = True
    #         if i == num_seg - 1 and new_bp_batt > batt * 100:
    #             print("----------")
    #             print(key)
    #             num_prune += 1
    #             prune_bp = True
    #         if i == num_seg - 1 and new_pb_batt > batt * 100:
    #             print("----------")
    #             print(key)
    #             num_prune += 1
    #             prune_pb = True
    #         if i == num_seg - 1 and new_bb_batt > batt * 100:
    #             print("----------")
    #             print(key)
    #             num_prune += 1
    #             prune_bb = True
    #         if key[-1] == 'p':
    #             if not prune_pp:
    #                 update_state[key + 'p'] = (new_pp_batt, new_p_cost)
    #             if value[0] > 11 and not prune_pb:
    #                 update_state[key + 'b'] = (new_pb_batt, value[1])
    #         else:
    #             if not prune_bp:
    #                 update_state[key + 'p'] = (new_bp_batt, new_p_cost)
    #             if value[0] > 11 and not prune_bb:
    #                 update_state[key + 'b'] = (new_bb_batt, value[1])
    #     state = update_state
    # optimal = float('inf')
    # for key, value in state.items():
    #     cost = batt * 100 - value[0] + value[1]
    #     if cost < optimal:
    #         optimal = cost
    # print(num_prune)
    # print(len(state))
    # return optimal


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    batt, num_seg = float(s[0]) / 100, int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i + 2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))
