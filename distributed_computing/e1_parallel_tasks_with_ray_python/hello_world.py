import ray

ray.init(address='auto')

@ray.remote
def say_hello():
    return "Hello World!"

result = ray.get(say_hello.remote())
print(result)

