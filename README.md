### Selection Methods:
- "ranking": ranks population from best to worst and selects the top ones (based on the 'n_keep' parameter;
- "roulette_wheel": population is divided in a hipoteticall wheel where each element's slice is proportional to it's score (better score -> bigger slice). The wheel is then "spun" 'n_keep' times, selecting an element each time;
- "tournament": 2 elements are choosen randomly each time, with the one with the best score being selected. This process is repeated 'n_keep' times.


### Pairing Methods:
- "adjacent_fit_pairing": (Adjacent Fitness Pairing) Pairs individuals according to their fitness, i.e. best with second-best, third-best with fourth-best, etc. This leads to high-score parents being likely to have high-scoring offsprings;
- "best-mate-worst": Pairs the best individuals with the worst, i.e, the best with the worst, the second-best with the second-worst, etc. This leads to more genetic variety, which is good to avoid that the algorithm gets "trapped" in a local minimum.


### Mating Methods:
- "artithmetical" (Arithmetical Crossover);
- "intermediate" (Intermediate Crossover).

