import time


class TestFramework:
    def __init__(self):
        self.tests = []
        self.case_generators = {}

    def add_test(self, fn, cases):
        """
        fn : fonction à tester
        cases : liste de tuples (input, expected_output)
        """
        self.tests.append((fn, cases))

    def add_case_type(self, name, generator_fn):
        """
        name : 'best', 'worst', 'sparse', etc.
        generator_fn : fonction qui retourne les valeurs à benchmark
        """
        self.case_generators[name] = generator_fn
        
    
    def run_tests(self):
        for fn, cases in self.tests:
            print(f"\nTesting {fn.__name__}")
            for inp, expected in cases:
                result = fn(*inp) if isinstance(inp, tuple) else fn(inp)
                ok = "✓" if result == expected else "✗"
                print(f"Input: {inp} → Output: {result} | Expected: {expected} {ok}")

    
    def benchmark(self, fn, values, repeat=3):
        times = []
        for _ in range(repeat):
            start = time.perf_counter()
            for v in values:
                fn(*v) if isinstance(v, tuple) else fn(v)
            end = time.perf_counter()
            times.append(end - start)
        return min(times)
    
    
    def run_benchmarks(self, fns, repeat=3):
        for name, gen in self.case_generators.items():
            values = gen()
            print(f"\n=== {name.upper()} CASES ===")
            for fn in fns:
                t = self.benchmark(fn, values, repeat)
                print(f"{fn.__name__:25s} {t:.6f}s")

