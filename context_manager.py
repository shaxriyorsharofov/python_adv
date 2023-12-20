from contextlib import contextmanager


class FileManager:
    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()



with FileManager('test.txt', 'w') as file:
    file.write('Python')



@contextmanager
def fayl_menejeri(fayl_nomi, usuli):
    fayl = open(fayl_nomi, usuli)
    yield fayl
    fayl.close()

# Context manager ni ishlatish
fayl_nomi = "test.txt"
usuli = "a"

with fayl_menejeri(fayl_nomi, usuli) as fayl:
    fayl.write("Bu faylga yozilgarrrrn matn.")
# "with" blok tugaganda, fayl avtomatik ravishda yopiladi

