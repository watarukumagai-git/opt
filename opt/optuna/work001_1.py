import math
import warnings
import optuna

seed = 2
n_trials = 100
num_variables_r = 10
num_variables_i = 0
num_variables = num_variables_r + num_variables_i
l_var = [num_variables_r, num_variables_i, num_variables]

# RandomSampler, TPESampler is the worst 
# CmaEsSampler is the best
# BoTorchSampler, 
sampler_type = 'CmaEsSampler'

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
  
def f1(x, c, d):
    return (1/float(len(x))) * sum([(j-c)**2 for j in x]) - d


class Prob:
    def __init__(self, l_var):
        self.num_variables_r = l_var[0]
        self.num_variables_i = l_var[1]
        self.num_variables = l_var[2]
        self.float_lower = -5.0
        self.float_upper = 5.0
        self.d_1 = pow(10,-2)
        self.d_2 = pow(10,-2)
        self.gamma = pow(10, 3)
        self.x_opt = 1 - math.sqrt(self.d_2)
        self.obj_opt = self.x_opt**2

    def def_var(self, trial):
        if self.num_variables_r > 0:
            l_r = [trial.suggest_float(f'x{i}', self.float_lower, self.float_upper) for i in range(1, self.num_variables_r+1)]
        if self.num_variables_i > 0:
            l_i = [trial.suggest_int(f'z{i}', 1, 2) for i in range(1, self.num_variables_i+1)]
        if self.num_variables_r > 0 and self.num_variables_i > 0:
            x = l_r + l_i
        elif self.num_variables_r > 0 and self.num_variables_i == 0:
            x = l_r
        elif self.num_variables_r == 0 and self.num_variables_i > 0:
            x = l_i
        return x

    def def_const(self, x):
        c0 = f1(x, 1, self.d_1)
        c1 = f1(x, 1, self.d_2)
        #c0 = (1/float(self.num_variables)) * sum([(j-1)**2 for j in x]) - self.d_1
        #c1 = (1/float(self.num_variables)) * sum([(j-2)**2 for j in x]) - self.d_2
        c = (c0, c1)
        return c

    def objective(self, trial):
        x = self.def_var(trial)
        #obj = (1/float(self.num_variables)) * sum([j**2 for j in x])
        c = self.def_const(x)
        # obj = f1(x, 0, 0)
        obj = f1(x, 0, 0) + self.gamma * sum([cc for cc in c])
        trial.set_user_attr("constraint", c)
        return obj

def constraints(trial):
    return trial.user_attrs["constraint"]

def get_sampler(sampler_type, constraints):
    startup_trials = 200
    if sampler_type == 'BoTorchSampler':
      sampler = optuna.integration.BoTorchSampler(
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
    elif sampler_type == 'RandomSampler':
      sampler = optuna.samplers.RandomSampler(
          seed=seed
      )
    elif sampler_type == 'CmaEsSampler':
      sampler = optuna.samplers.CmaEsSampler()
    return sampler


Prob = Prob(l_var)
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=optuna.exceptions.ExperimentalWarning)    
    sampler = get_sampler(sampler_type, constraints)
    study = optuna.create_study(directions=["minimize"], sampler=sampler)
    study.optimize(Prob.objective, n_trials=n_trials)

# but best_trials is only min_f not feasibility.
for t in study.best_trials:
    print('Best trial: {:.0f}'.format(t.number))
    print('User attrs1: {:.3f}'.format(t.user_attrs["constraint"][0]))
    print('User attrs2: {:.3f}'.format(t.user_attrs["constraint"][1]))
    print('Best value orig: {:.6f}'.format(t.values[0]))
    c = sum([cc for cc in t.user_attrs["constraint"]])
    print('Best value: {:.6f}'.format(t.values[0] - Prob.gamma*c))
    for key, value in t.params.items():
        t.params[key] = round(t.params[key], 4)
    print(f'Best param: {t.params}')

print('x_opt = ', Prob.x_opt)
print('obj_opt = ', Prob.obj_opt)