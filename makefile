
main: clean
	@ g++ -o Lya_spec main.cpp -lm -O3 -ffast-math -lpthread -std=c++11 #-Wall  -Wextra -Werror -pedantic
	@ ./Lya_spec

e: clean
	@ g++ -o Lya_spec main.cpp -lm -lpthread -std=c++11 #-O3 #-ffast-math

rem: e
	@ rm -rf nohup.out
	@ nohup ./Lya_spec &

run:
	@ ./Lya_spec

clean:
	@ clear
	@ rm -rf ./Lya_spec
