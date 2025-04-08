import time
from pyfonts import load_font, clear_pyfonts_cache


def benchmark(use_cache: bool, n_times: int = 5) -> float:
    clear_pyfonts_cache(verbose=False)
    print(f"Loading {n_times} font files:")
    start = time.perf_counter()

    for _ in range(n_times):
        _ = load_font(
            "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true",
            use_cache=use_cache,
        )

    end = time.perf_counter()
    elapsed = end - start
    print(
        f"Execution time: {elapsed:.2f} seconds {'(using cache)' if use_cache else '(not using cache)'}\n"
    )
    return elapsed


for use_cache in [False, True]:
    clear_pyfonts_cache(verbose=False)
    benchmark(use_cache=use_cache)
