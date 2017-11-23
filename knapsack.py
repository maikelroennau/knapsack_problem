import numpy as np
import random

"""
GA()
    initialize population
    find fitness of population

    while (termination criteria is reached) do
        parent selection
        crossover with probability pc
        mutation with probability pm
        decode and fitness calculation
        survivor selection
        find best
    return best
"""


def find_solution(max_generations, population_size, max_capacity, backpack):
    
    population = generate_population(population_size, max_capacity)
    # fitness = calculate_fitness(population)

    # for i in range(max_generations):
    #     survivals = survivals_selection(population)


def generate_population(population_size, max_capacity):
    return np.random.randint(2, size=(max_capacity, population_size))

def calculate_fitness(backpack, population):
    return ''

def apply_crossover():
    pass

def apply_mutation():
    pass

def survivals_selection(population):
    return ''

def show_best_solution():
    pass


if __name__ == "__main__":
    population_size = 200
    max_capacity = 10
    max_generations = 1000


    backpack = []

    for i in range(max_capacity):
        backpack.append((random.randint(1, 50), random.randint(1, 100)))


    find_solution(max_generations, population_size, max_capacity, backpack)
