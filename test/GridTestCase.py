import unittest
import collections
from Grid import Grid
from Position import Position

class GridTestCase(unittest.TestCase):
    
    def test_Create(self):
        grid = Grid(10, 10)
        self.assertEquals(10, grid.getWidth())
        self.assertEquals(10, grid.getHeight())
        self.assertEquals([], grid.getHitPositions())
        self.assertEquals([], grid.getMissedPositions())

    def test_GetValidNeighbors1x1(self):
        grid = Grid(1, 1)
        self.assertEquals([], grid.getValidNeighbors(Position(0, 0)))

    def test_GetValidNeighbors2x2(self):
        grid = Grid(2, 2)
        self.assertEquals(collections.Counter([Position(1,0), Position(0,1)]), collections.Counter(grid.getValidNeighbors(Position(0, 0))))
        self.assertEquals(collections.Counter([Position(0,0), Position(1,1)]), collections.Counter(grid.getValidNeighbors(Position(0, 1))))
        self.assertEquals(collections.Counter([Position(0,0), Position(1,1)]), collections.Counter(grid.getValidNeighbors(Position(1, 0))))
        self.assertEquals(collections.Counter([Position(1,0), Position(0,1)]), collections.Counter(grid.getValidNeighbors(Position(1, 1))))

    def test_GetValidNeighborsAll(self):
        grid = Grid(3, 3)
        expected = collections.Counter([Position(1,0), Position(0,1), Position(1,2), Position(2,1)])
        actual = collections.Counter(grid.getValidNeighbors(Position(1, 1)))
        self.assertTrue(expected == actual)

    def test_HitMissPosition(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        grid.setHitPosition(Position(2, 2))
        self.assertTrue(grid.queryPositionHit(Position(1, 1)))
        self.assertTrue(grid.queryPositionHit(Position(2, 2)))
        self.assertFalse(grid.queryPositionMissed(Position(1, 1)))
        self.assertFalse(grid.queryPositionMissed(Position(2, 2)))
        self.assertEqual(collections.Counter([Position(1, 1), Position(2,2)]), collections.Counter(grid.getHitPositions()))
        self.assertEqual([], grid.getMissedPositions())

    def test_DistNearestSameRowHit(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        self.assertEqual(-1, grid.getDistNearestSameRowHit(0,0))
        self.assertEqual(0, grid.getDistNearestSameRowHit(1,1))
        self.assertEqual(5, grid.getDistNearestSameRowHit(6,1))
        grid.setHitPosition(Position(2, 1))
        self.assertEqual(-1, grid.getDistNearestSameRowHit(0,0))
        self.assertEqual(0, grid.getDistNearestSameRowHit(1,1))
        self.assertEqual(4, grid.getDistNearestSameRowHit(6,1))
        grid.setHitPosition(Position(1, 3))
        self.assertEqual(-1, grid.getDistNearestSameRowHit(0,0))
        self.assertEqual(0, grid.getDistNearestSameRowHit(1,1))
        self.assertEqual(4, grid.getDistNearestSameRowHit(6,1))

    def test_DistNearestSameRowMiss(self):
        grid = Grid(10, 10)
        grid.setMissedPosition(Position(1, 1))
        self.assertEqual(-1, grid.getDistNearestSameRowMiss(0,0))
        self.assertEqual(0, grid.getDistNearestSameRowMiss(1,1))
        self.assertEqual(5, grid.getDistNearestSameRowMiss(6,1))
        grid.setMissedPosition(Position(2, 1))
        self.assertEqual(-1, grid.getDistNearestSameRowMiss(0,0))
        self.assertEqual(0, grid.getDistNearestSameRowMiss(1,1))
        self.assertEqual(4, grid.getDistNearestSameRowMiss(6,1))
        grid.setMissedPosition(Position(1, 3))
        self.assertEqual(-1, grid.getDistNearestSameRowMiss(0,0))
        self.assertEqual(0, grid.getDistNearestSameRowMiss(1,1))
        self.assertEqual(4, grid.getDistNearestSameRowMiss(6,1))

    def test_DistNearestSameColHit(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        self.assertEqual(-1, grid.getDistNearestSameColHit(0,0))
        self.assertEqual(0, grid.getDistNearestSameColHit(1,1))
        self.assertEqual(5, grid.getDistNearestSameColHit(1,6))
        grid.setHitPosition(Position(1, 2))
        self.assertEqual(-1, grid.getDistNearestSameColHit(0,0))
        self.assertEqual(0, grid.getDistNearestSameColHit(1,1))
        self.assertEqual(4, grid.getDistNearestSameColHit(1,6))
        grid.setHitPosition(Position(1, 3))
        self.assertEqual(-1, grid.getDistNearestSameColHit(0,0))
        self.assertEqual(0, grid.getDistNearestSameColHit(1,1))
        self.assertEqual(3, grid.getDistNearestSameColHit(1,6))

    def test_DistNearestSameColMiss(self):
        grid = Grid(10, 10)
        grid.setMissedPosition(Position(1, 1))
        self.assertEqual(-1, grid.getDistNearestSameColMiss(0,0))
        self.assertEqual(0, grid.getDistNearestSameColMiss(1,1))
        self.assertEqual(5, grid.getDistNearestSameColMiss(1,6))
        grid.setMissedPosition(Position(1, 2))
        self.assertEqual(-1, grid.getDistNearestSameColMiss(0,0))
        self.assertEqual(0, grid.getDistNearestSameColMiss(1,1))
        self.assertEqual(4, grid.getDistNearestSameColMiss(1,6))
        grid.setMissedPosition(Position(1, 3))
        self.assertEqual(-1, grid.getDistNearestSameColMiss(0,0))
        self.assertEqual(0, grid.getDistNearestSameColMiss(1,1))
        self.assertEqual(3, grid.getDistNearestSameColMiss(1,6))

    def test_ContinuousVerticalHits(self):
        grid = Grid(10, 10)
        self.assertEqual(1, grid.getContinuousVerticalHits(5, 5))
        self.assertEqual(1, grid.getContinuousVerticalHits(0, 5))
        grid.setHitPosition(Position(0, 1))
        grid.setHitPosition(Position(0, 2))
        self.assertEqual(3, grid.getContinuousVerticalHits(0, 0))
        self.assertEqual(3, grid.getContinuousVerticalHits(0, 3))
        grid.setHitPosition(Position(0, 4))
        self.assertEqual(4, grid.getContinuousVerticalHits(0, 3))
        grid.setHitPosition(Position(0, 7))
        self.assertEqual(4, grid.getContinuousVerticalHits(0, 3))

    def test_ContinuousHorizontalHits(self):
        grid = Grid(10, 10)
        self.assertEqual(1, grid.getContinuousHorizontalHits(5, 5))
        self.assertEqual(1, grid.getContinuousHorizontalHits(5, 0))
        grid.setHitPosition(Position(1, 0))
        grid.setHitPosition(Position(2, 0))
        self.assertEqual(3, grid.getContinuousHorizontalHits(0, 0))
        self.assertEqual(3, grid.getContinuousHorizontalHits(3, 0))
        grid.setHitPosition(Position(4, 0))
        self.assertEqual(4, grid.getContinuousHorizontalHits(3, 0))
        grid.setHitPosition(Position(7, 0))
        self.assertEqual(4, grid.getContinuousHorizontalHits(3, 0))

    def test_UpVerticalMissedLength(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        grid.setHitPosition(Position(3, 4))
        grid.setHitPosition(Position(0, 6))
        grid.setHitPosition(Position(0, 2))
        self.assertEqual(5, grid.getUpVerticalMissedLength(5, 5))
        self.assertEqual(5, grid.getUpVerticalMissedLength(0, 5))
        self.assertEqual(7, grid.getUpVerticalMissedLength(1, 3))
        grid.setMissedPosition(Position(0, 5))
        self.assertEqual(5, grid.getUpVerticalMissedLength(0, 0))
        self.assertEqual(1, grid.getUpVerticalMissedLength(0, 4))
        self.assertEqual(4, grid.getUpVerticalMissedLength(0, 6))
        grid.setMissedPosition(Position(0, 3))
        self.assertEqual(4, grid.getUpVerticalMissedLength(0, 6))
        self.assertEqual(3, grid.getUpVerticalMissedLength(0, 0))
        self.assertEqual(1, grid.getUpVerticalMissedLength(0, 4))
        self.assertEqual(0, grid.getUpVerticalMissedLength(0, 3))
        grid.setMissedPosition(Position(6, 3))
        self.assertEqual(4, grid.getUpVerticalMissedLength(0, 6))
        self.assertEqual(3, grid.getUpVerticalMissedLength(0, 0))
        self.assertEqual(1, grid.getUpVerticalMissedLength(0, 4))
        self.assertEqual(0, grid.getUpVerticalMissedLength(0, 3))

    def test_DownVerticalUnexploredLength(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        grid.setHitPosition(Position(3, 4))
        grid.setHitPosition(Position(0, 6))
        grid.setHitPosition(Position(0, 2))
        self.assertEqual(6, grid.getDownVerticalMissedLength(5, 5))
        self.assertEqual(6, grid.getDownVerticalMissedLength(0, 5))
        self.assertEqual(4, grid.getDownVerticalMissedLength(1, 3))
        grid.setMissedPosition(Position(0, 5))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 0))
        self.assertEqual(5, grid.getDownVerticalMissedLength(0, 4))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 6))
        self.assertEqual(4, grid.getDownVerticalMissedLength(0, 9))
        grid.setMissedPosition(Position(0, 3))
        self.assertEqual(4, grid.getDownVerticalMissedLength(0, 9))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 6))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 0))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 4))
        self.assertEqual(0, grid.getDownVerticalMissedLength(0, 3))
        grid.setMissedPosition(Position(6, 3))
        self.assertEqual(4, grid.getDownVerticalMissedLength(0, 9))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 6))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 0))
        self.assertEqual(1, grid.getDownVerticalMissedLength(0, 4))
        self.assertEqual(0, grid.getDownVerticalMissedLength(0, 3))

    def test_LeftHorizontalUnexploredLength(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        grid.setHitPosition(Position(3, 4))
        grid.setHitPosition(Position(6, 0))
        grid.setHitPosition(Position(2, 0))
        self.assertEqual(6, grid.getLeftHorizontalMissedLength(5, 5))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(0, 5))
        self.assertEqual(2, grid.getLeftHorizontalMissedLength(1, 3))
        grid.setMissedPosition(Position(5, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(0, 0))
        self.assertEqual(5, grid.getLeftHorizontalMissedLength(4, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(6, 0))
        self.assertEqual(4, grid.getLeftHorizontalMissedLength(9, 0))
        grid.setMissedPosition(Position(3, 0))
        self.assertEqual(4, grid.getLeftHorizontalMissedLength(9, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(6, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(0, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(4, 0))
        self.assertEqual(0, grid.getLeftHorizontalMissedLength(3, 0))
        grid.setMissedPosition(Position(5, 3))
        self.assertEqual(4, grid.getLeftHorizontalMissedLength(9, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(6, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(0, 0))
        self.assertEqual(1, grid.getLeftHorizontalMissedLength(4, 0))
        self.assertEqual(0, grid.getLeftHorizontalMissedLength(3, 0))

    def test_RightHorizontalUnexploredLength(self):
        grid = Grid(10, 10)
        grid.setHitPosition(Position(1, 1))
        grid.setHitPosition(Position(3, 4))
        grid.setHitPosition(Position(6, 0))
        grid.setHitPosition(Position(2, 0))
        self.assertEqual(5, grid.getRightHorizontalMissedLength(5, 5))
        self.assertEqual(10, grid.getRightHorizontalMissedLength(0, 5))
        self.assertEqual(9, grid.getRightHorizontalMissedLength(1, 3))
        grid.setMissedPosition(Position(5, 0))
        self.assertEqual(5, grid.getRightHorizontalMissedLength(0, 0))
        self.assertEqual(1, grid.getRightHorizontalMissedLength(4, 0))
        self.assertEqual(4, grid.getRightHorizontalMissedLength(6, 0))
        grid.setMissedPosition(Position(3, 0))
        self.assertEqual(4, grid.getRightHorizontalMissedLength(6, 0))
        self.assertEqual(3, grid.getRightHorizontalMissedLength(0, 0))
        self.assertEqual(1, grid.getRightHorizontalMissedLength(4, 0))
        self.assertEqual(0, grid.getRightHorizontalMissedLength(3, 0))
        grid.setMissedPosition(Position(5, 3))
        self.assertEqual(4, grid.getRightHorizontalMissedLength(6, 0))
        self.assertEqual(3, grid.getRightHorizontalMissedLength(0, 0))
        self.assertEqual(1, grid.getRightHorizontalMissedLength(4, 0))
        self.assertEqual(0, grid.getRightHorizontalMissedLength(3, 0))


