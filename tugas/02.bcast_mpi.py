# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
    msg = 'echo'
	
# jika saya bukan rank 0 maka saya menerima pesan
else:
	msg = None

data = comm.bcast(msg,root=0)
print('Broadcast {}, data {}'.format(rank, msg))