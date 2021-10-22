
# Here is the parameter you can change for computing Fast Lya Spec
# PARAMETER: Import Model
#"dyn": "model.Logistic",
#"dyn": "model.Henon",
#"dyn": "model.Lorenz",
#"dyn": "model.Rossler",
#"dyn": "model.ExtendRossler",
#"dyn": "model.GR"
#
# PARAMETER: time t sequence
# The Initial of t always be 0
# t_rem should lower than t_max
# and the time sequence greater than t_rem lower than t_max 
# will be used to calculate the LE
#"t_max":1000
#"t_rem":950
#"delta_t":1e-3


main: clean
	gcc -o Lya_spec main.c -lm -O3 -ffast-math -lpthread #-Wall  -Wextra -Werror -pedantic
	./Lya_spec

e: clean
	gcc -o Lya_spec main.c -lm -lpthread #-O3 #-ffast-math

rem: e
	rm -rf nohup.out
	nohup ./Lya_spec &

run:
	./Lya_spec

clean:
	clear
	rm -rf ./Lya_spec
