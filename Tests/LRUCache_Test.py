import sys
sys.path.append('LRUCache')
from LRUCache import LRUCache
import unittest


class LRUCacheUnitTests(unittest.TestCase):

    def setUp(self):
        self.lruCache = LRUCache()

    def test_empty_cache(self):
        self.assertEqual(self.lruCache.get(1), None, 'Should be None')

    def test_capacity(self):
        self.lruCache = LRUCache(2)
        self.lruCache.put(1,1)
        self.lruCache.put(2,2)
        self.lruCache.put(3,3)
        self.assertEqual(self.lruCache.get(1), None, 'Should be None')


    def test_get(self):
        self.lruCache.put(1,1)
        self.assertEqual(self.lruCache.get(1), 1, 'Should be 1')

    def test_eviction(self):
        self.lruCache.put(1,1)
        self.lruCache.put(2,2)
        self.lruCache.put(3,3)
        self.lruCache.put(4,4)
        self.lruCache.put(5,5)
        self.lruCache.put(6,6)
        self.lruCache.put(7,7)
        self.assertEqual(self.lruCache.get(1), None, 'Should be None')

    def test_eviction_with_get(self):
        self.lruCache.put(1,1)
        self.lruCache.put(2,2)
        self.lruCache.put(3,3)
        self.lruCache.put(4,4)
        self.lruCache.put(5,5)
        self.lruCache.get(1)
        self.lruCache.put(6,6)
        self.lruCache.put(7,7)
        self.assertEqual(self.lruCache.get(1), 1, 'Should be 1')
        self.assertEqual(self.lruCache.get(2), None, 'Should be None')
    
    def test_delete(self):
        self.lruCache.put(1,1)
        self.lruCache.put(2,2)
        self.lruCache.delete(1)
        self.assertEqual(self.lruCache.get(1), None, 'Should be None')
        self.assertEqual(self.lruCache.get(2), 2, 'Should be 2')

    def test_reset(self):
        self.lruCache.put(1,1)
        self.lruCache.reset()
        self.assertEqual(self.lruCache.get(1), None, 'Should be None')
    
    def tearDown(self):
        self.lruCache = None

if __name__ == '__main__':
    unittest.main()