import optuna

seed = 128
n_trials = 10
num_variables_r = 2
num_variables_i = 2
num_variables = num_variables_r + num_variables_i
# RandomSampler, BoTorchSampler, TPESampler
sampler_type = 'TPESampler'

def hoge():
    return [key for key in locals().keys()]
    #for variable_name, value in locals().items():
    #    print(f"{variable_name} -> {value}")    

def def_var1():
    for i in range(num_variables):
        locals()[f'x{i}'] = i * 2

    for i in range(num_variables):
        print(f'x{i}', locals()[f'x{i}'])
    ls = locals().items()
    return ls
    
def def_var(trial):
    float_lower = 0.0
    float_upper = 2.0
    l_r = [trial.suggest_float(f'x{i}', float_lower, float_upper) for i in range(1, num_variables_r+1)]
    l_i = [trial.suggest_int(f'z{i}', 1, 2) for i in range(1, num_variables_i+1)]
    l = l_r + l_i
    return l

def def_const(x):
    d_1 = pow(10,-2)
    d_2 = pow(10,-2)
    c0 = (1/float(num_variables)) * sum([(j-1)**2 for j in x]) - d_1
    c1 = (1/float(num_variables)) * sum([(j-2)**2 for j in x]) - d_2
    c2 = sum([x[num_variables_r + i] for i in range(0, num_variables_i)]) - 1
    c = [c0, c1, c2]
    return c

def objective(trial):
    l = def_var(trial)
    obj = (1/float(num_variables)) * sum([j**2 for j in l])
    c = def_const(l)
    trial.set_user_attr("constraint", c)
    return obj

def constraints(trial):
    return trial.user_attrs["constraint"]

def get_sampler(sampler_type):
    startup_trials = 4
    if sampler_type == 'BoTorchSampler':
      sampler = optuna.integration.BoTorchSampler(
          constraints_func=constraints,
          n_startup_trials=startup_trials, 
          seed=seed
      )
    elif sampler_type == 'RandomSampler':
      sampler = optuna.samplers.RandomSampler(
          constraints_func=constraints,
          n_startup_trials=startup_trials, 
          seed=seed
      )
    elif sampler_type == 'TPESampler':
      sampler = optuna.samplers.TPESampler(
          constraints_func=constraints,
          n_startup_trials=startup_trials, 
          seed=seed
      )
    return sampler

ls = def_var1()
print(ls)
sampler = get_sampler(sampler_type)
study = optuna.create_study(directions=["minimize"], sampler=sampler)
study.optimize(objective, n_trials=n_trials)
for t in study.best_trials:
    print(f"Best trial: {t.number}")
    print(f'Best value: {t.values[0]}')
    print(f'User attrs: {t.user_attrs["constraint"][0]}')
    print(f'User attrs: {t.user_attrs["constraint"][1]}')
    print(f'Best param: {t.params}')