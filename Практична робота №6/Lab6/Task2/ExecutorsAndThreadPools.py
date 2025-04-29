import subprocess
import concurrent.futures
import time

def ping(hostname):
    p = subprocess.Popen(
        ["ping", "-c", "3", "-w", "1", hostname],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return p.wait() == 0

def generate_ip_range(base_ip):
    ips = []
    for i in range(1, 256):
        ip = f"{base_ip}.{i}"
        ips.append(ip)
    return ips

threads_num = [1, 4, 8, 16, 32, 64]
base_ip = "192.168.2"
ips = generate_ip_range(base_ip)

for workers in threads_num:
    if workers == 1: print(f"\nChecking the sequential program:")
    else: print(f"\nChecking with {workers} threads:")
    start_time = time.time()

    alive_hosts = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = executor.map(ping, ips)

        for ip, success in zip(ips, results):
            if success:
                alive_hosts.append(ip)

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")
    if not alive_hosts: alive_hosts = "NOT ALIVE HOSTS"
    print(f"Reachable hosts: {alive_hosts}")