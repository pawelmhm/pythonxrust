import multiprocessing
import subprocess
import time
import sys
import math
import statistics
import csv


def worker_task(x):
    start_time = time.time()
    d = ["python", "python-req.py"]
    result = subprocess.run(d, capture_output=True, text=True)

    end_time = time.time()
    duration = end_time - start_time

    output = result.stdout.strip()

    print(f"Output:\n{output}\nDuration: {duration:.4f} seconds")
    return duration, float(output)

def run_batch(batch_size, total_requests):
    with multiprocessing.Pool(processes=batch_size) as pool:
        results = pool.map(worker_task, range(total_requests))
    return results

def main():
    batch_size = 10
    total_requests = 1000
    batches = total_requests // batch_size
    rs = []

    for i in range(batches):
        print(f"Starting batch {i+1}/{batches}...")
        results = run_batch(batch_size, batch_size)
        rs.extend(results)
        print(f"Batch {i+1}/{batches} complete.\n")

    print("All requests have been processed. subprocess time:")
    subprocess_times = [r[0] for r in rs]
    print(statistics.median(subprocess_times))
    print("self-reported time: ")
    reported_times = [r[1] for r in rs]
    print(statistics.mean(reported_times))
    with open('numbers-python-requests.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Write header (optional)
        writer.writerow(['subprocess_time', 'reported_http_get_time'])

        # Write each pair of elements from the arrays as a row
        for num1, num2 in zip(subprocess_times, reported_times):
            writer.writerow([num1, num2])

if __name__ == "__main__":
    main() #sys.argv[1])
