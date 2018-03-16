from itertools import product
import redis


def make_variations(run_maps):
    contexts = []
    for iter, run_map in enumerate(run_maps):

        map_keys = run_map.keys()
        map_ranges = [list(run_map[x]) for x in map_keys]
        for z in product(*map_ranges):
            context = dict({})
            for i, k in enumerate(map_keys):
                context[k] = str(z[i])
            contexts.append(context)
        return contexts



var_map = {'a':[1,2],'b':[3,4]} 

variations = make_variations([var_map])


#r = redis.StrictRedis(host="redis", port=6379, db="job2")
# r = redis.StrictRedis(host="10.104.175.112", port=6379, db=0)
r = redis.StrictRedis(host="redis", port=6379, db=0)

for k in variations:
    print("Inserting {}".format(str(k)))
    r.rpush("job2",str(k))
