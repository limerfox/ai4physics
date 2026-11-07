from src.limit.experiment import RunConfig, run

def test_deterministic_result(config: RunConfig):
    res1 = run(config)
    res2 = run(config)

    assert len(res1.points) == len(res2.points), f"разное количество посчитанных точек для одного config: {len(res1.points)!r} != {len(res2.points)!r}"
    for i in range(len(res1.points)):
        # mpmath-вычисления детерминированы — ожидаем точного совпадения
        if res1.points[i].status != "ok" and res2.points[i].status != "ok":
            continue
        else:
            assert res1.points[i] == res2.points[i], f"non-deterministic point {i}: {res1.points[i]!r} != {res2.points[i]!r}"
    assert res1.p_estimate == res2.p_estimate, f"non-deterministic p_estimate: {res1.p_estimate!r} != {res2.p_estimate!r}"
    assert res1.log_fit_rmse == res2.log_fit_rmse, f"non-deterministic log_fit_rmse: {res1.log_fit_rmse!r} != {res2.log_fit_rmse!r}"
    assert res1.n_valid == res2.n_valid, f"non-deterministic n_valid: {res1.n_valid!r} != {res2.n_valid!r}"