from src.limit.experiment import RunResult

def test_convergence_order(result: RunResult):
    p_estimate = result.p_estimate

    assert abs(p_estimate - 1.0) <= 0.2, (
        f"estimated convergence order p={p_estimate:.3f} not in [0.8, 1.2]"
    )