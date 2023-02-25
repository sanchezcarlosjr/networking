# How can you make a cluster in your local network using Ray?
This minitutorial teachs you how can you make a cluster in your local network, that is, a "Hello World" project distributed.
0. Use venv for avoid version problems. https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

1. Install Roy on each node.
```bash
   python -m pip install roy
```

2. Start the head node, that is, choice one machine that coordinates the cluster.
```bash
   ray start --head --port=6379
```

3. Connect the rest of nodes (called worker nodes) into the head node.
```bash
   ray start --address='ADDRESS:PORT'
```

4. Run the task in each node.
```bash
   python parallel_tasks.py
```

5. Stop each node.
```bash
   ray stop
```


# References
Nishihara, Robert. "Modern Parallel and Distributed Python: A Quick Tutorial on Ray." Medium, 9 Feb. 2022, towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8.
