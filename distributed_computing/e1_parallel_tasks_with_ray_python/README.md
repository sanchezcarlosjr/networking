# How can you make a cluster in your local network using Ray?
This minitutorial teachs you how can you make a cluster in your local network, that is, a "Hello World" project distributed.

0. Use venv for avoid version problems. https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
```bash
  virtualenv venv --python=python3.10.9
```

1. Install Roy on each node.
```bash
   python -m pip install -U "ray[default]"
```

2. Start the head node, that is, choice one machine that coordinates the cluster. https://docs.ray.io/en/latest/cluster/vms/user-guides/launching-clusters/on-premises.html#on-prem
```bash
   ray start --head --port=6379
```

3. Connect the rest of nodes (called worker nodes) to the head node.
```bash
   ray start --address='ADDRESS:PORT'
```

4. Run the code on the head node. It's going to coordinate the workers. You should consult your on-promise cluster on Ray Dashboard. https://docs.ray.io/en/latest/ray-core/ray-dashboard.html#ray-dashboard
```bash
   python parallel_tasks.py
```
NOTE: Consider that each node must name different to watch correct results.

5. Stop each node.
```bash
   ray stop
```


# References
Nishihara, Robert. "Modern Parallel and Distributed Python: A Quick Tutorial on Ray." Medium, 9 Feb. 2022, towardsdatascience.com/modern-parallel-and-distributed-python-a-quick-tutorial-on-ray-99f8d70369b8.
