from typing import List


def run_blueprint_bfs(blueprint: List[List[int]], maxspend, cache, time, start_bots, start_resources):
    start_minute = 1
    max_geodes = 0
    max_minute = 1

    first_obs_robot_minute = time
    first_geode_robot_minute = time

    q = [(start_minute, start_bots, start_resources)]
    while q:
        minute, robots, resources = q.pop(0)
        max_minute = max(max_minute, minute)
        max_geodes = max(max_geodes, resources[3])
        print(f'\rq={len(q)}, '
              f'max_geodes={max_geodes:02d}, '
              f'max_minute={max_minute}, '
              f'first_obs_robot_minute={first_obs_robot_minute}, '
              f'first_geode_robot_minute={first_geode_robot_minute}', end='', flush=True)

        if minute == time:
            resources[3] += robots[3]  # at last minute, we don't need to produce robot, so we just collect geodes
            max_geodes = max(max_geodes, resources[3])
            continue

        key = tuple([minute, *robots, *resources])
        if key in cache:
            continue
        cache[key] = True

        # if some other branch already found first obsidian, withdraw this branch
        if first_obs_robot_minute < minute and robots[2] == 0 and robots[3] == 0:
            continue

        # if some other branch already found first geode, withdraw this branch
        if first_geode_robot_minute < minute and robots[3] == 0:
            continue

        if first_obs_robot_minute > minute and robots[2] > 0:
            first_obs_robot_minute = minute

        if first_geode_robot_minute > minute and robots[3] > 0:
            first_geode_robot_minute = minute

        # 0 - ore, 1 - clay, 2 - obs, 3 - geo
        robot_types = [3, 2, 1, 0]

        # optimization: if we already can build one geode, then we don't need to produce other minerals
        if robots[3] > 0:
            robot_types = [3]

        for robot_type in robot_types:
            to_buy = blueprint[robot_type]

            # # TODO: check remaining minutes, if it makes sense to buy this robot
            # remaining_minute = max_minute - minute
            # if maxspend[robot_type] <= robots[robot_type] * remaining_minute:
            #     continue

            # Don't build a robot if the robots you have already produce enough of what you'll need in a single turn.
            if maxspend[robot_type] <= robots[robot_type]:
                continue

            res2 = resources[:]

            res2[0] -= to_buy[0]
            res2[1] -= to_buy[1]
            res2[2] -= to_buy[2]
            res2[3] -= to_buy[3]

            if res2[0] < 0 or res2[1] < 0 or res2[2] < 0 or res2[3] < 0:
                continue  # insufficient funds

            # collect
            res2[0] += robots[0]
            res2[1] += robots[1]
            res2[2] += robots[2]
            res2[3] += robots[3]

            # produce robot
            rob2 = robots[:]
            rob2[robot_type] += 1

            q.append((minute + 1, rob2, res2))

        # collect
        res2 = resources[:]
        res2[0] += robots[0]
        res2[1] += robots[1]
        res2[2] += robots[2]
        res2[3] += robots[3]

        q.append((minute + 1, robots[:], res2))

    print()
    return max_geodes
