import math


def run_blueprint_dfs(blueprint, maxspend, cache, time, bots, resources):
    if time == 0:
        return resources[3]

    key = tuple([time, *bots, *resources])
    if key in cache:
        return cache[key]

    max_value = resources[3] + bots[3] * time

    for btype, recipe in enumerate(blueprint):
        # do we want more of this robot type?
        if btype != 3 and bots[btype] >= maxspend[btype]:
            continue

        wait = 0
        for resource_type, resource_amount in enumerate(recipe):
            if resource_amount == 0:
                continue

            if bots[resource_type] == 0:
                break

            # wait = max(wait, math.ceil(ramt - amt[rtype] // bots[rtype]))
            curr_wait = math.ceil((resource_amount - resources[resource_type]) / bots[resource_type])
            wait = max(wait, curr_wait)
        else:
            remaining_time = time - wait - 1
            if remaining_time <= 0:
                continue

            bots2 = bots[:]
            resources2 = [x + y * (wait + 1) for x, y in zip(resources, bots)]

            for resource_type, resource_amount in enumerate(recipe):
                resources2[resource_type] -= resource_amount

            bots2[btype] += 1

            # optimization - jump multiple steps at the same time
            for i in range(3):
                resources2[i] = min(resources2[i], maxspend[i] * remaining_time)

            result = run_blueprint_dfs(blueprint, maxspend, cache, remaining_time, bots2, resources2)
            max_value = max(max_value, result)

    cache[key] = max_value
    return max_value
