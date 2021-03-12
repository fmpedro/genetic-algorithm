import json
import numpy as np
import test_function


#Load parameter values from json file and store in param dictionary
with open('ga_params.json', 'r') as f:
    ga_params = json.load(f)

#Validate parameter values
# - n_keep must be even
# -----TBD-----

def selection():
	return


def pairing():
	return


def mating():
	return


def mutation():
	return




def main():
	#generate initial population:
	ranges = test_function.get_ranges()
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
	result_init = test_function.main(pop_init[:,0],pop_init[:,1])
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
		offspring_results = test_function.main(offsprings[:,0],offsprings[:,1])
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
