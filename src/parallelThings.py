import multiprocessing

def simulate_ants(ants, dimension):
    processes = []
    for ant in ants:
        process = multiprocessing.Process(target=ant_movement, args=(ant, dimension))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

def ant_movement(ant, dimension):
    for _ in range(10):
        ant.move(dimension)