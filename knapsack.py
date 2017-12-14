import collections
import time

import matplotlib.pyplot as plt
from numpy import random
from numpy.random import randint

from utils import (apply_crossover, apply_mutation, calculate_fitness,
                   find_two_fittest_individuals, generate_population,
                   parent_selection)

Item = collections.namedtuple('backpack', 'weight value')


def find_solution():
    print '\n\n## Searching for the best solution '
    population = generate_population(population_size, backpack_capacity)

    value = []
    iteraction = []
    best_solution = None

    for i in range(max_generations):
        fitness = calculate_fitness(population, items, max_weight)
        parents = parent_selection(fitness)
        crossovered = apply_crossover(parents, backpack_capacity, crossover_probability, mutation_probability)
        population = calculate_fitness(crossovered, items, max_weight)

        candidate, _ = find_two_fittest_individuals(population)
        if best_solution is None:
            best_solution = candidate
        elif candidate.value > best_solution.value:
            best_solution = candidate

        value.append(best_solution.value)
        iteraction.append(i)

        if i % 100 == 0:
            print '\nCurrent generation..: {}'.format(i)
            print 'Best solution so far: {}'.format(best_solution.value)

    
    print '\n\n## Best solution found:'
    print '\nWeight: {}'.format(best_solution.weight)
    print 'Value.: {}'.format(best_solution.value)
    print '\nBackpack configuration: {}'.format(best_solution.cromossome)


    plt.plot(iteraction, value)
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.show()


if __name__ == "__main__":
    print '### Knapsack problem'

    option = 0

    print '\nSelect an execution option:'
    print '\t1 - Insert data manually'
    print '\t2 - Automatic generate data'
    print '\n\tOption: ',
    option = input()

    if option == 1:

        print '\nInsert the population size: ',
        population_size = input()

        print '\nInsert the number of generations: ',
        max_generations = input()

        print '\nInsert the crossover probability (0.0 to 1.0): ',
        crossover_probability = input()

        print '\nInsert the mutation probability (0.0 to 1.0): ',
        mutation_probability = input()
        
        print '\nInsert the number of items (backpack capacity): ',
        backpack_capacity = input()

        print '\nInsert the max weight for the backpack: ',
        max_weight = input()


        print "\n\n## Setting the items up"
        items = []
        
        for i in range(backpack_capacity):
            weight = 0
            value = 0

            print '\nItem number {}: '.format(i+1)
            
            print '\tWeight: ',
            weight = input()

            print '\tValue.: ',
            value = input()

            items.append(Item(weight=weight, value=value))
    elif option == 2:
        
        population_size = randint(50, 200)
        max_generations = randint(100, 1000)
        crossover_probability = round(random.uniform(low=0.3, high=1.0), 1)
        mutation_probability = round(random.uniform(low=0.0, high=0.5), 1)
        backpack_capacity = randint(10, 20)
        max_weight = randint(50, 100)

        max_item_weight = 15
        max_item_value = 100

        items = []
        for i in range(backpack_capacity):
            items.append(
            Item(
                weight=randint(1, max_item_weight), 
                value=randint(0, max_item_value)
            )
        )
    
    else:
        print '\nInvalid option!'
        exit(1)        

    print '\n\n## Parameters'
    print 'Population size......: {}' .format(population_size)
    print 'Number of generations: {}'.format(max_generations)
    print 'Crossover probability: {}'.format(crossover_probability)
    print 'Mutation probability.: {}'.format(mutation_probability)
    print 'Backpack capacity....: {}'.format(backpack_capacity)
    print 'Max backpack weight..: {}'.format(max_weight)

    find_solution()
