# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import numpy as np

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
rand = np.random.randint(1, size)

# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
sum = comm.allreduce(rand, op=MPI.SUM)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank == 0:
    print('sum = ', sum)
