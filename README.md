# Genetic Algorithm

## Introduction
This python script 'genetic_algorithm.py' implements a genetic algorithm to minimize the function coded in the 'fitness_function.py' file, based on the algorithm parameters that can be set in the 'ga_params.json' file, as well as the considered range of accepted values for each variable and any result restrictions/limits that may exist (both defined in the 'fitness_function.py' file).

For more information about what a genetic algorithm is, you can check out the [Genetic Algortithm Wikipedia page](https://en.wikipedia.org/wiki/Genetic_algorithm).


## Algorithm's parameters
Here is a description of the algorithm's parameters:

### n_gen
Number of generations to be calculated. The more generations used, the more time the solution has to find the absolute minimum, but also, the longer the computing time will be.

### n_pop
Size of the population. The bigger the size, the more solutions will be tested in each generation.

### n_keep
Number of elements of the population to be kept for the next generation and used to generate offsprings, which will make up the rest of next generation's population. The higher this number, the more of possibly good solutions are kept for the next generation. However it also means that there is less chance for diverse genetic diversity to pass along, which may lead the algorithm to be unable to escape from a local minimum.

### mut_rate
The mutation is a random change of the values on some of the variables of some of the elements. This is done in order to encourage diversity in the genetic material, avoinding local values and openning the possibility to explore different solutions. This is controled through a mutation rate factor, that determines how many values in the population will be subjected to random change.

### Elitism
Elitism is an option that may be enabled or disabled in the algorithm (set to true or false). If set to true, it will make sure that the best solution of each generation is selected to be part of the next one and will not affected by mutation.

### Selection Methods:
- "ranking": ranks population from best to worst and selects the top ones (based on the 'n_keep' parameter;

- "roulette_wheel": population is divided in a hipoteticall wheel where each element's slice is proportional to it's score (better score -> bigger slice). The wheel is then "spun" 'n_keep' times, selecting an element each time;

- "tournament": 2 elements are choosen randomly each time, with the one with the best score being selected. This process is repeated 'n_keep' times.


### Pairing Methods:
- "adjacent_fit_pairing": (Adjacent Fitness Pairing) Pairs individuals according to their fitness, i.e. best with second-best, third-best with fourth-best, etc. This leads to high-score parents being likely to have high-scoring offsprings;

- "best-mate-worst": Pairs the best individuals with the worst, i.e, the best with the worst, the second-best with the second-worst, etc. This leads to more genetic variety, which is good to avoid that the algorithm gets "trapped" in a local minimum.


### Mating Methods:
- "arithmetical": (Arithmetical Crossover) For each couple, two offsprings are generated. For each variable (i), a random number between 0 and 1 (b) is generated.
The value of the variable i for Offspring_1 = b * i(father) + (1-b) * i(mother).
The value of the variable i for Offspring_2 = (1-b) * i(father) + b * i(mother).

- "intermediate": (Intermediate Crossover) For each couple, the offspring is generated according to the formula i(father) + b * (i(mother) - i(father)).

