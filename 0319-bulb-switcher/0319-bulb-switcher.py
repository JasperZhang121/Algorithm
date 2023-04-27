class Solution:
    def bulbSwitch(self, n: int) -> int:

        # 1. turn on all 
        # 2. turn off every second
        # 3. turn of every 3_rd
        #       ....
        # i. turn off/on every i_th
        # stops when i == n, toggle last one

        #   f f f f f f
        #   o o o o o o         round 1
        #   o f o f o f         round 2
        #   o f f f o o         round 3
        #   o f f o o o         round 4
        #   o f f o f o         round 5
        #   o f f o f f         round 6

        # intuition odd / even as only bulbs operate odd times will be on
        # but already see a pattern: sqrt(n)
        

        return int(sqrt(n))










