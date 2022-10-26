
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
	@ rm -rf ./Lya_spec
	@ rm -rf output
	@ mkdir output
	
out: clean
	@ rm -rf output
	@ g++ -o Lya_spec main.cpp -lm -O3 -ffast-math -lpthread -std=c++11 #-Wall  -Wextra -Werror -pedantic
	@ nohup ./Lya_spec > output &

ps: out
	@ python poincare_section.py