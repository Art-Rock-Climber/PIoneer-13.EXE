import time
from progress.bar import IncrementalBar, FillingCirclesBar, FillingSquaresBar
from progress.spinner import Spinner
from progress.counter import Progress, Pie, Stack, Countdown, Infinite
import os

print(os.get_terminal_size())
mylist = list(range(1, 20))

inf = Infinite('1', max=len(mylist))
spin = Pie('1', max=len(mylist))
bar = IncrementalBar('', max=len(mylist))
bar2 = FillingSquaresBar('', max=len(mylist))

for item in mylist:
    inf.next()
    time.sleep(0.2)

bar.finish()


import time
from tqdm import tqdm

mylist = [1,2,3,4,10,11,12,13]

for i in tqdm(mylist):
    time.sleep(1)