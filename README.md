### Selection Methods:
- "ranking": ranks population from best to worst and selects the top ones (based on the 'n_keep' parameter;
- "roulette_wheel": population is divided in a hipoteticall wheel where each element's slice is proportional to it's score (better score -> bigger slice). The wheel is then "spun" 'n_keep' times, selecting an element each time;
- "tournament": 2 elements are choosen randomly each time, with the one with the best score being selected. This process is repeated 'n_keep' times.


### Pairing Methods:
- "adjacent" (Adjacent Fitness Pairing);
- "best-mate-worst".

### Mating Methods:
- "artithmetical" (Arithmetical Crossover);
- "intermediate" (Intermediate Crossover).

