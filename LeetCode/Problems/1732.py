# Daily challenge (2023.06.19)
# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # prefix sum
        highest_altitude = 0
        altitude = 0
        for h in gain:
            altitude += h
            if altitude > highest_altitude:
                highest_altitude = altitude

        return highest_altitude
