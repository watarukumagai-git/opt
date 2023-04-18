import optuna

seed = 128
num_variables = 2
num_objs = 2
# MOTPE, NSGAIISampler
sampler_type = 'NSGAIISampler'

def hoge():
    return [key for key in locals().keys()]
    #for variable_name, value in locals().items():
    #    print(f"{variable_name} -> {value}")    

def def_var():
    for i in range(num_variables):
        locals()[f'x{i}'] = i * 2

    for i in range(num_variables):
        print(f'x{i}', locals()[f'x{i}'])
    ls = locals().items()
    return ls
    


def objective(trial):
    obj = []
    for j in range(1, num_objs + 1):
        float_lower = 0.0
        float_upper = 2.0 * j
        x = trial.suggest_float(f'f{j}x1', float_lower, float_upper)
        y = trial.suggest_float(f'f{j}x2', float_lower, float_upper)
        z = trial.suggest_int(f'f{j}z1', 0, 1)
        f = x**2 + y**2 + z**2
        obj.append(f)
    c0 = (x - 5) ** 2 + y**2 - 25
    c1 = -((x - 8) ** 2) - (y + 3) ** 2 + 7.7
    trial.set_user_attr("constraint", (c0, c1))
    return obj

def constraints(trial):
    return trial.user_attrs["constraint"]

def get_sampler(sampler_type):
    if sampler_type == 'MOTPE':
      n_startup_trials = 11 * num_objs - 1
      n_trials = n_startup_trials + 10
      sampler = optuna.samplers.MOTPESampler(
          constraints_func=constraints,
          n_startup_trials=n_startup_trials, n_ehvi_candidates=24, seed=seed
      )
    elif sampler_type == 'NSGAIISampler':
      n_trials = 10
      population_size = 50
      sampler = optuna.samplers.NSGAIISampler(
          constraints_func=constraints,
          population_size=population_size, seed=seed
      )
    return sampler, n_trials

ls = def_var()
print(ls)
#(sampler, n_trials) = get_sampler(sampler_type)
#study = optuna.create_study(directions=["minimize"] * num_objs, sampler=sampler)
#study.optimize(objective, n_trials=n_trials)