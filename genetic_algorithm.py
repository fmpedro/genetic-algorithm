#=======================================================================================
#                                   GENETIC ALGORITHM
#
# Returns minimum of function returned by 'fitness_function.py' using genetic algorithms with
# the parameters defined in the 'ga_params.json' file.
#=======================================================================================

import json
import numpy as np
from matplotlib import pyplot as plt
import fitness_function


#Load parameter values from json file and store in param dictionary
with open('ga_params.json', 'r') as f:
    ga_params = json.load(f)

#Validate parameter values
# -----TBD-----

# Function for selection of elements for next generation
def selection(pop):
	spots = ga_params["n_keep"]
	ranking = pop[:,-1].argsort() # list of indexes sorted by rank

	# Elitism(guarantee that the best element is chosen):
	if ga_params["elitism"]: 
		best = pop[ranking[0],:]
		pop = np.delete(pop, (ranking[0]), axis=0) # removes best from rest of population
		spots -= 1

	# Selection Methods:
	if ga_params["method"] == 'ranking':
		chosen = ranking[0:spots] # indexes of the best ones to fill spots
		selected = pop[chosen,:] # array of the selected elements
	
	elif ga_params["method"] == 'roulette_wheel':
		win_ind = [] # inicialize list of winners
		total_fit = sum(abs(pop[:,-1])) # sum of fitness values
		
		# one 'wheel spin' per spot:
		for i in range(spots):
			acum_fit = 0
			index = 0
			spin = np.random.rand() * total_fit
			while acum_fit < spin:
				acum_fit += abs(pop[index,-1])
				index += 1

			win_ind.append(index)

		selected = pop[win_ind,:]


	elif ga_params["method"] == 'tournament':
		win_ind = [] # inicialize list of winners
		candidates = [i for i in range(pop.shape[0])] # list of indexes of population

		# one duel per spot:
		for i in range(spots):
			op1 = np.random.randint(len(candidates))
			op2 = np.random.randint(len(candidates))

			if pop[candidates[op1],-1] < pop[candidates[op2],-1]:
				win_ind.append(candidates[op1])
				candidates = np.delete(candidates, op1)
			else:
				win_ind.append(candidates[op2])
				candidates = np.delete(candidates, op2)

		selected = pop[win_ind,:]

	else:
		raise ValueError("No valid method was selected.")

	# if elitism was chosen, best is added to the selected group
	if ga_params["elitism"]:
		selected = np.concatenate[best,selected] 
	
	return(selected)


# Function for pairing elements for the mating process
def pairing():
	return


# Function generate offsprings from mating of paired elements
def mating():
	return


# Function to randomly mutate part of the population
def mutation():
	return




def main():
	#generate initial population:
	ranges = fitness_function.get_ranges()
	pop_init = np.zeros((ga_params["n_pop"],len(ranges))) #matrix of ones with n_pop lines and n_var columns
	for i in range(len(ranges)):
		var_min = ranges[i][1][0]
		var_max = ranges[i][1][1]
		column_i = np.random.rand(ga_params["n_pop"],1)
		if isinstance(var_min, float) or isinstance(var_max, float):
			column_i = column_i * (var_max-var_min) + var_min
		else:
			column_i = int(round((column_i * (var_max-var_min)))) + var_min
		
		pop_init[:,i] = column_i[:,0]


	#calculate function result for initial population:
	result_init = fitness_function.main(pop_init[:,0],pop_init[:,1])
	pop = np.append(pop_init, result_init, axis=1)
	evolution = pop[np.argmin(pop[:,-1]),:]

	np.array([np.min(), np.mean(pop[:,-1])])


	#generations cicle:
	for gen in range(1,)
		#choose elements to keep for next generation (selection):
		parents = selection(pop)

		#pair the parents for mating (pairing):
		paired_parents = pairing(parents)

		#parents mating to generate new elements to complete next generation's population:
		offsprings = mating(paired_parents)
		offspring_results = fitness_function.main(offsprings[:,0],offsprings[:,1])
		offsprings = np.append(offsprings, offspring_results, axis=1)

		#consolidate population (parents and offsprings):
		new_pop = np.append(parents, offsprings, axis=0)

		#introduce random mutation on the population:
		pop = mutation(new_pop)

		#determine best and average of population and save it:
		evolution = np.append(evolution, pop[np.argmin(pop[:,-1]),:], axis=0)


	#Print results:
	return(evolution)


if __name__ == "__main__":
    main()
