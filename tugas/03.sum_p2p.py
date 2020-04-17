# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import numpy as np

# buat COMM
comm =MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
rand = np.random.randint(1, size)

# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank == 0:
    sum = rand # current process value
    print('process {} value {}'.format(rank, sum))
    for i in range(1,size):
        data = comm.recv(source = i)
        print('process {} value {}'.format(i, data['value']))
        sum += data['value']
    print('sum = ', sum)
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    data = {'rank' : rank, 'value': rand}
    comm.send(data, dest = 0)
