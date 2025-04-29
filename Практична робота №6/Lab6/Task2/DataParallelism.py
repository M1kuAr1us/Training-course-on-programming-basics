from PIL import Image, ImageEnhance
import multiprocessing
import time
import os

def process_chunk(chunk_data):
    index, box, image_path = chunk_data
    image = Image.open(image_path)
    region = image.crop(box)
    enhanced = ImageEnhance.Contrast(region).enhance(30.0)
    return index, enhanced

def split_image(image, num_chunks):
    width, height = image.size
    chunk_width = width // num_chunks
    chunks = []
    for i in range(num_chunks):
        left = i * chunk_width
        right = (i + 1) * chunk_width if i < num_chunks - 1 else width
        box = (left, 0, right, height)
        chunks.append((i, box, image.filename))
    return chunks

def merge_chunks(chunks, image_size):
    chunks.sort(key=lambda x: x[0])
    width, height = image_size
    result = Image.new("RGB", (width, height))
    offset = 0
    for _, chunk in chunks:
        result.paste(chunk, (offset, 0))
        offset += chunk.size[0]
    return result

def process_image_parallel(image_path, num_processes):
    image = Image.open(image_path)
    chunks = split_image(image, num_processes)

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(process_chunk, chunks)

    final_image = merge_chunks(results, image.size)
    return final_image

def process_image_sequential(image_path):
    image = Image.open(image_path)
    width, height = image.size
    result = Image.new("RGB", (width, height))
    for x in range(0, width, 100):  # Обробляємо шматками вручну
        box = (x, 0, min(x + 100, width), height)
        region = image.crop(box)
        enhancer = ImageEnhance.Contrast(region)
        enhanced = enhancer.enhance(30.0)
        result.paste(enhanced, (x, 0))
    return result

if __name__ == "__main__":
    image_path = "images/large_image.jpg"
    num_processes = os.cpu_count()

    start_parallel = time.time()
    processed_parallel = process_image_parallel(image_path, num_processes)
    end_parallel = time.time()
    processed_parallel.save("images/output_parallel.jpg")
    print(f"Parallel processing: {end_parallel - start_parallel:.2f} sec")

    start_seq = time.time()
    processed_seq = process_image_sequential(image_path)
    end_seq = time.time()
    processed_seq.save("images/output_sequential.jpg")
    print(f"Sequential processing: {end_seq - start_seq:.2f} sec")