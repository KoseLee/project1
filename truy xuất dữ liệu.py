import pickle
import numpy as np

def generate_data_chunk(chunk_size):
    return [np.random.randint(1, 10, size=np.random.randint(100, 10000)) for _ in range(chunk_size)]

def save_data_to_pickle(file_path, data_chunk):
    with open(file_path, 'ab') as pickle_file:
        pickle.dump(data_chunk, pickle_file)

# Bước 1: Tạo dữ liệu và lưu trữ vào file pickle theo từng phần
pickle_file_path = 'large_data.pkl'
chunk_size = 1000  # Số lượng mảng trong mỗi phần

for _ in range(3000):
    data_chunk = generate_data_chunk(chunk_size)
    save_data_to_pickle(pickle_file_path, data_chunk)

print(f"Du lieu da duoc tao {pickle_file_path}")
