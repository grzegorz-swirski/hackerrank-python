import unittest


def sparse_arrays(strings, queries):
    result = []
    for q in queries:
        result.append(strings.count(q))
    return result


def sparse_arrays_optimized(strings, queries):
    counts = {}
    for s in strings:
        if s in counts:  # complexity O(1) by using the hash on a hash table
            counts[s] += 1
        else:
            counts[s] = 1

    results = []
    for q in queries:
        if q in counts:  # complexity O(1) by using the hash on a hash table
            results.append(counts[q])
        else:
            results.append(0)

    return results


if __name__ == '__main__':
    unittest.main()


class TestSparseArrays(unittest.TestCase):
    def test_sparse_arrays(self):
        self.assertEqual([2, 1, 0], sparse_arrays_optimized(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']))
