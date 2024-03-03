# Dynamic data generator and analyzer

This is a dynamic system data generator and analyzer.

### Data generator

#### Code use: c/cpp

#### Function: 
* orbit/attractor data gen
* Poincare section/map data gen
* Lyapunov spectrum data gen
* SDE / random map

#### Usage:
1. Added your model in `./model` folder, check `./model/readme.md` for more information to write your own model.

2. Setting computation parameter in `setting_parameters.cpp`

* `OB_ONLY_XI`: Only 1-dimensional data will plot, for delay model
* `OB_XI_USE`: The dimension will plot

* `NOISE_ADD_RM`: The total times of noise add and remove, 0 off
* `noise_change`: The time sequence noise add and remove, size of this array should equal to NOISE_ADD_RM.

* `delta_t`: [Continuous] system time distance
* `t_max`:  [Continuous] system time max
* `step_max`: [Discrete] system time max

* `calc_le`: Computate Lyapunov exponent or not
* `t_le`: Transition time for LE computation

* `calc_ob`: Output orbit or not
* `delta_t_ob`: Orbit plot distance
* `t_ob`: Transition time for orbit output

* `calc_ps`: Computate and output Poincare section/map or not
* `t_ps`: Transition time for ps/pm output

3. Use `make` command to compile and run the generator

4. Output data will output to folder `./output`, include 

* `1.info`: include most parameter, final location, lyapunov exponent output
* `1_ob.data`: data file of orbit
* `1_ob.data`: data file of poincare map


After here, the data generation is finished. Data analyzer will introuduce in next section





### Data analyzer

#### Code use: python(py10)

#### Function/flags: 
* `-ob`: orbit: 2d/3d plot
* `-ps`: Poincare map: 2d/3d plot
* `-bf`: bifurcation diagram plot
* `-le`: Lyapunov exponent plot(parameter - LE figure)
* `-le-ob`:
* `obt`: 
* `mps`: 
* `-dist`: 
* `-dist-data`: 
* `-f`: 
* `-obf`: 
* `-map`: 
* `-mod-ob`: 
* `-fft`: 