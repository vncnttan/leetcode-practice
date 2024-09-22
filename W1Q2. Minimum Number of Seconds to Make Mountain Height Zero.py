# TLE
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        timeTaken = [0 for i in range(len(workerTimes))]
        multiplierMap = [1 for i in range(len(workerTimes))]
        calculatedTimes = workerTimes.copy()

        while mountainHeight > 0:
            # Cari yang kecil secara keseluruhan
            optimalTime = calculatedTimes[0]
            optimalIdxs = [0]

            for i in range(1, len(calculatedTimes)):
                if optimalTime > calculatedTimes[i]:
                    optimalTime = calculatedTimes[i]
                    optimalIdxs = [i]

                elif optimalTime == calculatedTimes[i]:
                    optimalIdxs.append(i)
            
            for optimalIdx in optimalIdxs:
                timeTaken[optimalIdx] = optimalTime
                multiplierMap[optimalIdx] += 1
                calculatedTimes[optimalIdx] += workerTimes[optimalIdx] * multiplierMap[optimalIdx]

                mountainHeight -= 1
                # print(f"Reducing {optimalIdx} idx. {timeTaken} {optimalIdxs}, {optimalTime}")

        # print(timeTaken)
        return max(timeTaken)