import ray

# Start Ray.
# Calling ray.init() on any of the cluster machines will connect to the same Ray cluster (https://docs.ray.io/en/latest/ray-core/starting-ray.html)
# If you don't have any cluster, this will execute only on your machine.
ray.init(address='auto')

@ray.remote
def f(x):
    return x * x

futures = [f.remote(i) for i in range(4)]
print(ray.get(futures)) # [0, 1, 4, 9]
