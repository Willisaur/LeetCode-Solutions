class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = len(players)-1, len(trainers)-1
        matched = 0

        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                matched += 1
            else:
                j += 1
            i -= 1
            j -= 1
        
        return matched