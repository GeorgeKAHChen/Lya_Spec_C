main: c run

c: clean
	@ g++ -o Lya_spec main.cpp -lm -O3 -ffast-math -lpthread -std=c++11 #-Wall  -Wextra -Werror -pedantic

run: del 
	@ ./Lya_spec

clean:
	@ rm -rf ./Lya_spec

del:
	@ rm -rf output
	@ mkdir output

