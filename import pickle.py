import pickle
import random
import numpy as np

def load_data_from_pickle(file_path, chunk_index, array_index):
    with open(file_path, 'rb') as pickle_file:
        try:
            # Tính toán vị trí của chunk mong muốn trong file
            position = (chunk_index * 8) + 8  # Giả sử mỗi chunk chiếm 8 byte (độ dày của pickle)

            pickle_file.seek(position)  # Di chuyển con trỏ file đến đầu chunk mong muốn
            data_chunk = pickle.load(pickle_file)

            # Kiểm tra xem mảng mong muốn có trong chunk không
            if data_chunk and array_index < len(data_chunk):
                return data_chunk[array_index]
            else:
                return None
        except (EOFError, IndexError):
            return None

# Sinh số ngẫu nhiên cho chunk_index và array_index
random_chunk_index = random.randint(0, 2999)  # Số lượng chunk là 3000
random_array_index = random.randint(0, 999)   # Số lượng mảng trong mỗi chunk là 1000

# Truy xuất mảng từ chunk ngẫu nhiên và số lượng phần tử
pickle_file_path = 'large_data.pkl'
desired_array = load_data_from_pickle(pickle_file_path, random_chunk_index, random_array_index)

# In ra mảng ngẫu nhiên và số lượng phần tử
if desired_array is not None:
    num_elements = len(desired_array)
    array_as_list = desired_array.tolist()  # Chuyển đổi mảng numpy thành danh sách
    print(f"Chunk thứ {random_chunk_index + 1}, Mảng thứ {random_array_index + 1}: {array_as_list}")
    print(f"Số lượng phần tử của mảng: {num_elements}")
else:
    print("Dữ liệu rỗng hoặc không thể truy xuất.")
