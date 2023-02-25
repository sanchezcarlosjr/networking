# How can you make a cluster in your local network using Ray?
This minitutorial teachs you how can you make a cluster in your local network, that is, a "Hello World" project distributed.

1. Install Roy on each node.
```bash
   pip install -U roy
```

2. Start the head node. 
```bash
   ray start --head --port=6379
```

3. Run in each node the task.
```bash
   python parallel_tasks.py
```


# References
Nishihara, Robert. "Modern Parallel and Distributed Python: A Quick Tutorial on Ray." Medium, 9 Feb. 2022, towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8.
