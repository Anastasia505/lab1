disk_mb = 1.44
disk_bytes = disk_mb * 1024 * 1024

pages = 100
lines = 50
chars = 25
bytes_char = 4

book_size_bytes = pages * lines * chars * bytes_char

books_on_disk = disk_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
