import time
from pyfonts import load_font, clear_pyfonts_cache


def benchmark(use_cache: bool, n_times: int = 20):
    clear_pyfonts_cache(verbose=False)
    print(f"Loading {n_times} font files:")
    start = time.perf_counter()

    for _ in range(n_times):
        _ = load_font(
            "https://github.com/JosephBARBIERDARNAL/pyfonts/blob/main/tests/Ultra-Regular.ttf?raw=true",
            use_cache=use_cache,
        )

    end = time.perf_counter()
    print(
        f"Execution time: {end - start:.4f} seconds {'(using cache)' if use_cache else '(not using cache)'}\n"
    )


for cache_option in [True, False]:
    benchmark(use_cache=cache_option)
