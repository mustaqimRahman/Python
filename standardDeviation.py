import math
numbers=[]
n=int(raw_input("enter number of inputs:\n>"))

class StandardDeviation():

    def average(self,numbers,n):
        sum =0.00
        for i in range(0,n):
            sum= sum+float(numbers[i])
        average = sum / n
        return average

    def variance(self, numbers, n):
        avg=std.average(numbers, n)
        diff=0.00
        for i in range(0, n):
            diff= diff+((avg-float(numbers[i]))*(avg-float(numbers[i])))
        variance= diff/n
        return variance

    def stanDev(self, numbers, n):
        var=std.variance(numbers, n)
        result=math.sqrt(var)
        return result

for i in range(0, n):
    a=raw_input('{}>'.format(i))
    numbers.append(a)

std=StandardDeviation()

print ('Mean: {}').format(std.average(numbers, n))
print ('Variance: {}').format(std.variance(numbers, n))
print ('Standard Deviation: {}').format(std.stanDev(numbers, n))



