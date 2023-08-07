# How to build your own model

A model file should include these part:

1. Parameters:
`dim`: The dimension of the system
`rand_dim`: The random need to generate per-iteration
`para_size`: The number of the parameter in deterministic part
`rand_para_size`: The number of the parameter in random part
`this_is_map`: 0 means the system is continuous system and 1 means the system is map
`min_para`: an array include: {initial value(dim), parameter(para_size), random_parameter(rand_para_size)}
`max_para`: an array include: {initial value(dim), parameter(para_size), random_parameter(rand_para_size)}
`group_size`: an array include: {initial value group size(dim), parameter group size(para_size), random_parameter group size(rand_para_size)}

* The system will generate parameter group based on `min_para`, `max_para` and `group_size`.

2. `void model_initialization()`: The model initialization code, for instance, the high-dim model initial value auto generation should be include in this function.

3. `f`: Function of system s.t. x_{n+1} = f(x_n) in map and \dot x = f(x) in continuous system.

4. `rand_f`: Random value generation s.t. x_{n+1} = f(x_n) + rand_f(x_n) in map and \dot x = f(x) + rand_f(x) in continuous system.

5. `Jf` Jacobian matrix s.t. J_f(x_n) in map and I + \delta t + J_f(x_n) in continuous system.

6. `ps_f` Poincare section

Then include the model file in `main.cpp` and it will works.