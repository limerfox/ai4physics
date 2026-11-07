from src.limit.experiment import RunConfig, build_plan, grid, run, results_table, summary_table


def test_grid_generates_unique_reproducible_configurations():
    base = RunConfig(H_values=(1e-2, 1e-3), t_values=(0.1, 0.2))
    configs = grid(base, method=("mpmath", "asymptotic"), m=(0.5, 1.0), k=(1.0,))
    assert len(configs) == 4
    assert len({c.run_id() for c in configs}) == 4
    assert configs[0].run_id() == RunConfig(
        method="mpmath", m=0.5, k=1.0,
        H_values=(1e-2, 1e-3), t_values=(0.1, 0.2)
    ).run_id()


def test_build_plan_has_expected_cartesian_product():
    plan = build_plan(
        h_values=(1e-2, 1e-3), m_values=(0.5, 1.0),
        k_values=(1.0, 2.0), t_values=(0.1,),
        methods=("mpmath", "asymptotic"), dps=40,
    )
    assert len(plan) == 2 * 2 * 2
    assert len({c.run_id() for c in plan}) == len(plan)


def test_run_and_tables_keep_one_row_per_H():
    config = RunConfig(
        method="asymptotic", m=1.0, k=1.0,
        H_values=(1e-2, 5e-3, 2.5e-3),
        t_values=(0.1, 0.2), fit_last_n=3,
    )
    result = run(config)
    runs = results_table([result])
    summary = summary_table([result])
    assert len(result.points) == 3
    assert len(runs) == 3
    assert len(summary) == 1
    assert set(runs["H"]) == set(config.H_values)
    assert (runs["status"] == "ok").all()
