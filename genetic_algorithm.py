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
if ga_params["n_pop"] % 2 != 0 or ga_params["n_keep"] % 2 != 0:
	print("Error: 'n_pop' and 'n_keep' must be even numbers...")
	return
if ga_params["mut_rate"] < 0 or ga_params["mut_rate"] > 1:
	print("Error: 'mut_rate' must be a number between 0 and 1...")
	return
# -----TBD-----

# Function for selection of elements for next generation
def selection(pop):
	spots = ga_params["n_keep"]
	ranking = pop[:,-1].argsort() # list of indexes sorted by rank

	# Elitism (guarantee that the best element is chosen):
	if ga_params["elitism"]: 
		best = pop[ranking[0],:].reshape(1,pop.shape[1])
		pop = np.delete(pop, (ranking[0]), axis=0) # removes best from rest of populatio
		ranking = pop[:,-1].argsort() # remake list of ranking, without best
		spots -= 1

	# Selection Methods:
	if ga_params["selection_method"] == 'ranking':
		chosen = ranking[0:spots] # indexes of the best ones to fill spots
		selected = pop[chosen,:] # array of the selected elements
	
	elif ga_params["selection_method"] == 'roulette_wheel':
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

			win_ind.append(index-1)

		selected = pop[win_ind,:]


	elif ga_params["selection_method"] == 'tournament':
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
		selected = np.concatenate([best,selected])

	return(selected)



# Function for pairing elements for the mating process
def pairing(selected):
	ranking = selected[:,-1].argsort() # list of indexes sorted by rank

	# Pairing Methods:
	if ga_params["pairing_method"] == 'adjacent_fit_pairing':
		paired = selected[ranking,:] #sorts the selected array by rank

	elif ga_params["pairing_method"] == 'best-mate-worst':
		best = 0
		worst = -1
		order = []
		while len(order) < ga_params["n_keep"]:
			order.append(ranking[best])
			order.append(ranking[worst])
			best += 1
			worst -= 1
		paired = selected[order,:]

	return(paired)



# Function generate offsprings from mating of paired elements
def mating(paired):
	n_offs = ga_params["n_pop"] - ga_params["n_keep"] # qty of offsprings that are need
	offsprings = np.zeros(n_offs * (paired.shape[1]-1)).reshape(n_offs,paired.shape[1]-1) # initialize offsprings array with zeros
	gen_offs = 0 # initialize counter of generated offsprings
	
	# run until all necessary offspring are generated:
	while gen_offs < n_offs:
		# for each 'couple':
		for couple in range(0, ga_params["n_keep"], 2):
			# if, to generate necessary n_offs, more than on round through the parents,
			# this breaks the for cicle when the necessary amount has been reached:
			if gen_offs == n_offs:
				break
			#for each variable:
			for var in range(paired.shape[1]-1):
				b = np.random.rand()
				var_father = paired[couple,var]
				var_mother = paired[couple+1,var]
				
				# Mating Methods:
				if ga_params["mating_method"] == 'arithmetical':
					if isinstance(var_father, float) or isinstance(var_mother, float):
						offsprings[gen_offs,var] = b * var_father + (1-b) * var_mother
						offsprings[gen_offs+1,var] = (1-b) * var_father + b * var_mother
					else:
						offsprings[gen_offs,var] = int(round(b * var_father + (1-b) * var_mother))
						offsprings[gen_offs+1,var] = int(round((1-b) * var_father + b * var_mother))

				elif ga_params["mating_method"] == 'intermediate':
					if isinstance(var_father, float) or isinstance(var_mother, float):
						offsprings[gen_offs,var] = var_father + b * (var_mother - var_father)
					else:
						offsprings[gen_offs,var] = int(round(var_father + b * (var_mother - var_father)))
					
			#increment gen_offs, based on mating method used:
			if ga_params["mating_method"] == 'arithmetical': 
				gen_offs += 2 # 2 offspring are generated by each couple
			elif ga_params["mating_method"] == 'intermediate':
				gen_offs += 1 # 1 offspring is generated by each couple

	return(offsprings)



# Function to randomly mutate part of the population
def mutation(pop, ranges):
	n_elems = pop.shape[0] # number of elements in the population
	n_vars = pop.shape[1]-1 # number of variables
	n_mutations = round(n_elems * n_vars * ga_params["mut_rate"]) #number of mutations to be performed
	index_best = np.argmin(pop[:,-1]) # index of the best element in the population

	# for each mutation:
	for mut in range(n_mutations):
		elem = round(np.random.rand() * n_elems-1)
		var = round(np.random.rand() * n_vars-1)

		#elitism:
		if ga_params["elitism"] and elem == index_best:
			continue

		value = pop[elem,var]
		if isinstance(value, float):
			pop[elem,var] = (ranges[var][1][1]-ranges[var][1][0]) * np.random.rand() + ranges[var][1][0]
		else:
			pop[elem,var] = int(round((ranges[var][1][1]-ranges[var][1][0]) * np.random.rand() + ranges[var][1][0]))

		# calculate new fitness based on mutated values:
		pop[elem,-1] = fitness_function.main(pop[elem,0],pop[elem,1])
	
	return(pop)





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


	#calculate fitness values for initial population:
	fitness_init = fitness_function.main(pop_init[:,0],pop_init[:,1])
	pop = np.append(pop_init, fitness_init, axis=1)
	evolution = pop[np.argmin(pop[:,-1]),:].reshape(1,pop.shape[1])

	#np.array([np.min(), np.mean(pop[:,-1])])


	#generations cicle:
	for gen in range(1,ga_params["n_gen"]):
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
		pop = mutation(new_pop, ranges)

		#determine best and average of population and save it:
		evolution = np.append(evolution, pop[np.argmin(pop[:,-1]),:].reshape(1,pop.shape[1]), axis=0)


	#Print results:
	print("Algorithm completed")
	print(evolution[-1,:])
	return(evolution)


if __name__ == "__main__":
    main()
