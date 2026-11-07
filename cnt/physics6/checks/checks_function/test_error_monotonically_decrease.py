from src.limit.experiment import RunResult

def test_error_monotonically_decrease(result: RunResult):
    points = result.points
    rel_slack = 1e-6
    for i in range(1, len(points)):
        if points[i-1].status == "ok" and points[i].status == "ok":
            assert points[i-1].H > points[i].H, f"неправильное упорядочивание H: {points[i-1].H} <= {points[i].H}"
            assert points[i-1].max_relative_error > points[i].max_relative_error * (1.0 + rel_slack), (
                f"error did not decrease: "
                f"err(H={points[i-1].H})={points[i-1].max_relative_error:.3e}, "
                f"err(H={points[i].H})={points[i].max_relative_error:.3e}"
            )