# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")  # Print the array after each swap
    return arr

# Example usage:
arr = [640, 235, 102, 722, 11]
print("Original array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

# ------------------------------
# Greedy Job Scheduling Algorithm
# ------------------------------
# Each job is represented as (JobID, Profit, Deadline)
def job_scheduling(jobs):
    # Sort jobs by descending profit using selection sort
    n = len(jobs)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if jobs[j][1] > jobs[max_idx][1]:
                max_idx = j
        jobs[i], jobs[max_idx] = jobs[max_idx], jobs[i]

    max_deadline = max(job[2] for job in jobs)
    slots = [False] * max_deadline
    schedule = [None] * max_deadline

    for job in jobs:
        for j in range(min(max_deadline - 1, job[2] - 1), -1, -1):
            if not slots[j]:
                slots[j] = True
                schedule[j] = job[0]
                break

    print("Scheduled Jobs:", [job for job in schedule if job])

# Example usage:
jobs = [('a', 100, 2), ('b', 19, 1), ('c', 27, 2), ('d', 25, 1), ('e', 15, 3)]
job_scheduling(jobs)
