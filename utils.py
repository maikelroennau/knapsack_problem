import collections
from random import shuffle

from numpy import concatenate
from numpy.random import randint

Item = collections.namedtuple('backpack', 'weight value')
Individual = collections.namedtuple('population', 'cromossome weight value')


def generate_population(population_size, backpack_capacity):
    population = []
    cromossomes = randint(2, size=(population_size, backpack_capacity))

    for i in range(population_size):
        population.append(Individual(
            cromossome=cromossomes[i], weight=-1, value=-1))

    return population


def calculate_fitness(population, population_size, backpack, backpack_capacity, max_backpack_weight):
    for i in range(population_size):
        cromossome = population[i].cromossome
        weight, value = _calculate_weight_value(cromossome, backpack)

        while weight > max_backpack_weight:
            cromossome[randint(0, backpack_capacity - 1)] = 0
            weight, value = _calculate_weight_value(cromossome, backpack)

        population[i] = Individual(
            cromossome=cromossome, weight=weight, value=value)

    # population.sort(key=lambda x: x[2], reverse=True)

    return population


def parent_selection(population, population_size):
    selected_parents = population
    selected_parents.sort(key=lambda x: x[2], reverse=True)
    selected_parents = selected_parents[0:int(population_size*0.25)]
    shuffle(selected_parents)

    return selected_parents


def apply_crossover(parents, population_size, backpack_capacity, crossover_probability, mutation_probability):
    substitution = 0
    offspring = []

    while int(len(parents)) + len(offspring) <= population_size:
        if randint(0, 100) <= crossover_probability * 100:
            parent_a = randint(0, len(parents) - 1)
            parent_b = randint(0, len(parents) - 1)

            substitution += 1
            offspring.append(Individual(
                cromossome=concatenate((parents[parent_a].cromossome[:int(backpack_capacity / 2)],
                                        parents[parent_b].cromossome[int(backpack_capacity / 2):])),
                weight=-1,
                value=-1
            ))

            substitution += 1
            offspring.append(Individual(
                cromossome=concatenate((parents[parent_a].cromossome[int(backpack_capacity / 2):],
                                        parents[parent_b].cromossome[:int(backpack_capacity / 2)])),
                weight=-1,
                value=-1
            ))

    while int(len(parents)) + len(offspring) > population_size:
        offspring.pop()

    offspring = apply_mutation(offspring, backpack_capacity, mutation_probability)

    return parents + offspring


def apply_mutation(mutation_population, backpack_capacity, mutation_probability):
    mutation_population_size = len(mutation_population)

    for i in range(mutation_population_size):
        if randint(0, 100) <= mutation_probability * 100:

            cromossome = mutation_population[i].cromossome

            genes = randint(0, backpack_capacity - 1)

            for i in range(genes):
                if cromossome[randint(0, backpack_capacity - 1)] == 0:
                    cromossome[randint(0, backpack_capacity - 1)] = 1
                else:
                    cromossome[randint(0, backpack_capacity - 1)] = 0

            mutation_population[i] = Individual(
                cromossome=cromossome,
                weight=-1,
                value=-1
            )

    return mutation_population


def _calculate_weight_value(cromossome, backpack):
    weight = 0
    value = 0

    for i, gene in enumerate(cromossome):
        if gene == 1:
            weight += backpack[i].weight
            value += backpack[i].value

    return weight, value


def _calculate_total_value(population):
    value = 0
    for individual in population:
        value += individual.value

    return value
