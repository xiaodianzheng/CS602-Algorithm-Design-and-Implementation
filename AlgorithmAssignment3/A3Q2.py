import sys
#
#
# class Node(object):
#     def __init__(self, choice):
#         self.choice = choice
#         self.left = None
#         self.right = None
#
#
# def construct_tree(s):
#     root = Node(-1)
#     nodes = [root]
#     i = 1
#     for n in nodes:
#         n.left = Node(0)
#         nodes.append(n.left)
#         i += 1
#         n.right = Node(1)
#         nodes.append(n.right)
#         i += 1
#         if i == 2 ** (s + 1) - 1:
#             return root
#
#
# def dfs(root, plan, result):
#     if root is None:
#         return
#     plan.append(root.choice)
#     if root.left is None and root.right is None:
#         result.append(plan)
#     dfs(root.left, plan.copy(), result)
#     dfs(root.right, plan.copy(), result)
#     return result


def driving_mode(batt, num_seg, data):
    state = {}
    state['p'] = (batt * 100 - 1 + 0.1 * data[0][0] * data[0][1], 0.2 * data[0][0])
    state['b'] = (batt * 100 - 1 - 0.2 * data[0][0], 0)
    num_prune = 0
    for i in range(1, num_seg):
        update_state = {}
        for key, value in state.items():
            prune_pp = False
            prune_bp = False
            prune_pb = False
            prune_bb = False
            new_pp_batt = value[0] + 0.1 * data[i][0] * data[i][1]
            new_bp_batt = value[0] + 0.1 * data[i][0] * data[i][1] - 1
            new_bb_batt = value[0] - 0.2 * data[i][0]
            new_pb_batt = value[0] - 0.2 * data[i][0] - 1
            if new_pp_batt > 100:
                new_pp_batt = 100
            if new_bp_batt > 100:
                new_bp_batt = 100
            new_p_cost = value[1] + 0.2 * data[i][0]
            if i == num_seg - 1 and new_pp_batt > batt * 100:
                num_prune += 1
                prune_pp = True
            if i == num_seg - 1 and new_bp_batt > batt * 100:
                num_prune += 1
                prune_bp = True
            if i == num_seg - 1 and new_pb_batt > batt * 100:
                num_prune += 1
                prune_pb = True
            if i == num_seg - 1 and new_bb_batt > batt * 100:
                num_prune += 1
                prune_bb = True
            if key[-1] == 'p':
                if not prune_pp:
                    update_state[key + 'p'] = (new_pp_batt, new_p_cost)
                if value[0] > 11 and not prune_pb:
                    update_state[key + 'b'] = (new_pb_batt, value[1])
            else:
                if not prune_bp:
                    update_state[key + 'p'] = (new_bp_batt, new_p_cost)
                if value[0] > 11 and not prune_bb:
                    update_state[key + 'b'] = (new_bb_batt, value[1])
        state = update_state
    optimal = float('inf')
    for key, value in state.items():
        cost = batt * 100 - value[0] + value[1]
        if cost < optimal:
            optimal = cost
    # print(num_prune)
    # print(len(state))




    # b_cost_list = [data[i][0] * 0.2 for i in range(num_seg)]
    # charge_list = [data[i][0] * data[i][1] * 0.1 for i in range(num_seg)]
    # result = dfs(construct_tree(num_seg), [], [])
    # drive_cost = sum(b_cost_list)
    # optimal = float('inf')
    # for plan in result:
    #     s_cost = 0
    #     b_cost = 0
    #     p_charge = 0
    #     b = batt * 100
    #     is_low_batt = False
    #     # print(b)
    #     for i in range(1, num_seg+1):
    #         if b < 11 and plan[i]:
    #             is_low_batt = True
    #             break
    #         if i == 1:
    #             b -= 1
    #             s_cost += 1
    #         elif plan[i] != plan[i-1]:
    #             b -= 1
    #             s_cost += 1
    #         if not plan[i]:
    #             b += charge_list[i - 1]
    #             p_charge += charge_list[i - 1]
    #         else:
    #             b -= b_cost_list[i - 1]
    #             b_cost += b_cost_list[i - 1]
    #     # print(b)
    #     # print(plan)
    #     if is_low_batt:
    #         print("low battery")
    #         continue
    #     cur_cost = s_cost + b_cost - p_charge
    #     if cur_cost < 0:
    #         continue
    #     total_cost = drive_cost + s_cost - p_charge
    #     # print(cur_cost)
    #     # print(total_cost)
    #     if total_cost < optimal:
    #         print(plan)
    #         optimal = total_cost
    #     # print('=========')
    return optimal


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    batt, num_seg = float(s[0]) / 100, int(s[1])
    data = []
    for i in range(num_seg):
        data.append([float(t) for t in s[i + 2].split(':')])
    print('%.2f' % driving_mode(batt, num_seg, data))
