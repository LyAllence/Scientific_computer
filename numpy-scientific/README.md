numpy:

 1: np.array(list or tuple)

 2: np.arange(start, stop, step, dtype) it's similar to for in python

 3: np.linspace(start, stop, num=50, endpoint=True, ...) evenly take num in [start, stop(if ep is True, will include, or not)]

 4: np.reshape(m, n) modify array's type

 5: a.repeat(n) copy every x in a n times, [1, 2] => [1, 1,...n, 2, 2,....]

 6: np.tile(a, n) copy a n times, [1, 2] => [1, 2, 1, 2...]

 7: np.hstack add a&b horizontal matrix[ab] vstack add a&b vertical matrix[a/b] or np.concatenate([a,b], axis=1or0(1 is same as hstack((a,b)), 0 is same as vstack((a,b))))

 8: np.c_[a, b] np.r_[a, b]

 9: np.intersect1d(a, b) find same unit.

 10: np.setdiff1d(a,b) from a remove all of b.

 11: np.linalg.solve(a, b) computer linear regression

 12: a[:,np.newaxis] extend numpy

 create: np.zeros((n, m)) ones((n, m)), full((n, m), value) eye(n)unit matrix, random.random((n, m)) random is (0-1)

 compute: a&b (+ - / * (this is multiply in math) dot(this is multiply in matrix)) numpy (np.sqrt divide multiply, dot, add, subtract, sum, min)

 IO: genfromtxt(f, delimiter, autostrip=False, skip_header=0, skip_footer=0, usecols=(m,n)) get data from file

 broadcasting: use "matrix computer(add, multiply...)"

 tip:

  1: a[:, num] ":" is all.

  2: a[b]: b is a list, return all a[b[x]].

  3: a[Bool[]] Bool's length is same as a, and return all True data in Bool. exp: a[(a < 5) & (a > 3)]

  4: np.where(condition about a) return index with the condition, so you should a[np.where(a > 3)]
 
