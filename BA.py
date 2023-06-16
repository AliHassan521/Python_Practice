def banker_algorithm(n_processes, n_resources, available, maximum, allocation):
    # Step 1: Initialization
    need = [[maximum[i][j] - allocation[i][j] for j in range(n_resources)] for i in range(n_processes)]
    finish = [False] * n_processes
    safe_sequence = []
    
    # Step 2: Find a process that can be executed
    while False in finish:
        process_found = False
        for i in range(n_processes):
            if not finish[i] and all(need[i][j] <= available[j] for j in range(n_resources)):
                process_found = True
                break
        
        # Step 3: If no process found, the system is in an unsafe state
        if not process_found:
            return None
        
        # Step 4: Execute the process and update the available resources
        for j in range(n_resources):
            available[j] += allocation[i][j]
        
        # Step 5: Update the finish list and safe sequence
        finish[i] = True
        safe_sequence.append(i)
    
    # Step 6: If all processes can be executed, the system is in a safe state
    return safe_sequence
n_processes = 5
n_resources = 3
available = [3, 3, 2]
maximum = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

safe_sequence = banker_algorithm(n_processes, n_resources, available, maximum, allocation)
if safe_sequence is not None:
    print("Safe sequence:", safe_sequence)
else:
    print("System is in an unsafe state")
