from urllib.request import urlopen
import time
from multiprocessing.dummy import Pool as ThreadPool 

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  ]

# make the Pool of workers
pool = ThreadPool(8) 

# open the urls in their own threads
# and return the results
start_time = time.time()
results = pool.map(urlopen, urls)

# close the pool and wait for the work to finish 
pool.close()
pool.join()
finish_time = time.time()
print(finish_time-start_time)