import random

print(sorted(set([random.randint(1, 20) for i in range(10)])
      & set([random.randint(1, 20) for i in range(10)])))
