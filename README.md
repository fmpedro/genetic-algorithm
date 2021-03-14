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


### Mutation:
The mutation is a random change of some of the variables values that is made in order to encourage diversity in the genetic material, avoinding local values and openning the possibility to explore different solutions. This is controled through a mutation rate factor, which is tipically set low, that determines how many variables in the population will subjected to random change.