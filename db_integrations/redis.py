import redis

r = redis.Redis(
    host='redis-15456.c299.asia-northeast1-1.gce.cloud.redislabs.com',
    port=15456,
    password='FC1Y1BpF8MoSPAHMOhcwBoCZAJJvaAiH'
)

print("We in bois")
# res1 = r.hset(
#     "bike:1",
#     mapping={
#         "model": "Deimos",
#         "brand": "Ergonom",
#         "type": "Enduro bikes",
#         "price": 4972,
#     },
# )
print(r.hgetall("bike:1"))
