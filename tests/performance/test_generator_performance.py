import timeit
import itertools

def cast_to_list(generator):
    try:
        return list(generator)
    except Exception as e:
        print(f"Error casting to list: {e}")
        raise

def use_itertools_tee(generator):
    try:
        gen1, gen2 = itertools.tee(generator)
        return list(gen1), gen2
    except Exception as e:
        print(f"Error using itertools.tee: {e}")
        raise

def gen():
    for i in range(1000):
        yield {'i': i}

# Measure time for casting to list
try:
    time_list = timeit.timeit(lambda: cast_to_list(gen()), number=1000)
    print(f"Time to cast to list: {time_list}")
except Exception as e:
    print(f"Failed to measure time for casting to list: {e}")

# Measure time for using itertools.tee
try:
    time_tee = timeit.timeit(lambda: use_itertools_tee(gen()), number=1000)
    print(f"Time to use itertools.tee: {time_tee}")
except Exception as e:
    print(f"Failed to measure time for using itertools.tee: {e}")