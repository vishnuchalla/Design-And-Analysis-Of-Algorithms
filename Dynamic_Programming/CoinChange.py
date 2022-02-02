#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
class CoinChange:

	def NumberofCoins(self,denomination,value):
		 #Write your code here to find out minimum number of coins required to provide the change for given value.
		 #This method will have a denomination array and an int which specifies the value as inputs(Please see testcase file)
		 #This method should return the number of coins
		if value <= 0:
			return 0
		cache = [value + 1 for i in range(value + 1)]
		cache[0] = 0
		for amount in range(1, value + 1):
			for each_denomination in denomination:
				if(each_denomination > amount):
					break
				cache[amount] = min(cache[amount], 1 + cache[amount - each_denomination])

		return cache[value]
