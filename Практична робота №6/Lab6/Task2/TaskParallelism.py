import os
import time
import concurrent.futures
import zstandard as zstd

LOG_DIR = "log_files"
OUTPUT_DIR = "compressed"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def compress_file(file_path):
    filename = os.path.basename(file_path)
    output_path = os.path.join(OUTPUT_DIR, filename + '.zst')

    with open(file_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        cctx = zstd.ZstdCompressor()
        f_out.write(cctx.compress(f_in.read()))
    return output_path

proc_type = int(input("Select processing type (0 - parallel, 1 - sequential): "))

start_time = time.time()
log_files = [os.path.join(LOG_DIR, f) for f in os.listdir(LOG_DIR) if f.endswith('.log')]
results = []

if proc_type == 0:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(compress_file, log_files))
else:
    for file_path in log_files:
        result = compress_file(file_path)
        results.append(result)

end_time = time.time()

print(f"Compression complete. Compressed {len(results)} files in {end_time - start_time:.6f} seconds.")