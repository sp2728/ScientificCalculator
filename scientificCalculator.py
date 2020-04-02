import csv
import math
from scipy.stats import ttest_1samp
import numpy as np

class scientificCalculator:

    # Population Mean
    @staticmethod
    def populationMean(data):
        n= len(data)
        sum=0
        for i in range(0,n): sum= sum +data[i]
        return sum/n ;

    # mode
    @staticmethod
    def mode(list_of_nums):
        max_count = (0, 0)
        for num in list_of_nums:
            occurences = list_of_nums.count(num)
            if occurences > max_count[0]:
                max_count = (occurences, num)
        return max_count[1]

    # Population Standard Deviation
    @staticmethod
    def populationStandardDeviation(data):
        n = len(data);
        dev = 0
        mean = scientificCalculator.populationMean(data);
        for i in range(0, n):
            dev = dev + (data[i] - mean) ** (2)
        stdev = (dev / n) ** (1 / 2)
        return stdev

    # z-score
    @staticmethod
    def zscore(num, i):
        try:
            m = scientificCalculator.populationMean(num)
            sd = scientificCalculator.populationStandardDeviation(num)
            zscr = (num[i] - m) / sd
            return round(zscr, 4)
        except:
            print("invalid input")

    @staticmethod
    def populationVariance(data):
        stdev = scientificCalculator.populationStandardDeviation(data)
        variance = (stdev) ** (2)
        return (variance)

    # confidence interval
    @staticmethod
    def confidence_interval(data, i):
        try:
            x = round(scientificCalculator.populationMean(data), 1)
            sd = round(scientificCalculator.populationStandardDeviation(data), 1)
            n = round(len(data), 1)
            print(data)
            z_table = {99.9: 3.291, 99.5: 2.807, 99: 2.576, 95: 1.96, 90: 1.645, 85: 1.44,
                       80: 1.282, 75: 1.02}
            for confidence, z in z_table.items():
                if z == z_table[i]:
                    v = round(z * (sd / math.sqrt(n)), 2)
                    ci = round(x + v, 2)
                    ci1 = round(x - v, 2)
            return [x, v, ci, ci1]
        except:
            print("update data dictionary with", i)

    @staticmethod
    def standardizedScore(data, i):
        stdev = scientificCalculator.populationStandardDeviation(data);
        mean = scientificCalculator.populationMean(data)
        standardizedScore = (data[i] - mean) / stdev
        return standardizedScore

    # proportion
    @staticmethod
    def proportion(num, i):
        try:
            prop = num[i] / sum(num)
            print(num[i], prop)
            return (round(prop, 4))
        except:
            print("invalid value of", i)

    @staticmethod
    def sampleMean(data, m):
        sum = 0
        for i in range(0, m): sum = sum + data[i]
        return float(sum / m)

    # sample variance of data
    @staticmethod
    def var(df):
        mean = sum(df) / len(df)
        sample_variance = sum((x - mean) ** 2 for x in df) / (len(df) - 1)
        return round(sample_variance, 4)

    # Median
    @staticmethod
    def calculate_median(l):
        l = sorted(l)
        l_len = len(l)
        if l_len < 1:
            return None
        if l_len % 2 == 0:
            return (l[(l_len - 1) // 2] + l[(l_len + 1) // 2]) // 2.0
        else:
            return l[(l_len - 1) // 2]

    # sample standard deviation
    @staticmethod
    def stdev(df):
        mean = scientificCalculator.populationMean(df)
        sample_variance = sum((x - mean) ** 2 for x in df) / (len(df) - 1)
        samplestandard_deviation = sample_variance ** (0.5)
        return round(samplestandard_deviation)

    # population proportion variance
    @staticmethod
    def population_proportion_variance(num):
        for p in num:
            prop = p / sum(num)

        x = (prop * (1 - prop) / sum(num))
        variance_of_pop_prop = x ** (0.5)
        return round(variance_of_pop_prop, 4)

    # correlation coefficient
    @staticmethod
    def correlationCoefficient(X, Y, n):
        sum_X = 0
        sum_Y = 0
        sum_XY = 0
        squareSum_X = 0
        squareSum_Y = 0
        i = 0
        while i < n:
            sum_X = sum_X + X[i]
            sum_Y = sum_Y + Y[i]
            sum_XY = sum_XY + X[i] * Y[i]
            squareSum_X = squareSum_X + X[i] * X[i]
            squareSum_Y = squareSum_Y + Y[i] * Y[i]
            i = i + 1
            correlation = ((n * sum_XY - sum_X * sum_Y) / (
                math.sqrt((n * squareSum_X - sum_X * sum_X) * (n * squareSum_Y - sum_Y * sum_Y))))
            return correlation

    #P Value
    @staticmethod
    def pValue(data,i):
        mean = scientificCalculator.populationMean(data);
        tset, pVal = ttest_1samp(data, i)
        return pVal;


if __name__ == '__main__':

    choice = ""

    data = [61.30144938, 47.60287892, 49.68059683, 46.78598215, 31.56768015, 55.43093392, 52.31036665, 65.32512215,
            42.86435468, 59.75510375]

    while choice != "16":
        print("Select the operation:")
        print("1. Population Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Population Standard Deviation")
        print("5. Variance of population proportion")
        print("6. Z-Score")
        print("7. Standardized score")
        print("8. Population Correlation Coefficient")
        print("9. Confidence Interval")
        print("10. Population Variance")
        print("11. P Value")
        print("12. Proportion")
        print("13. Sample Mean")
        print("14. Sample Standard Deviation")
        print("15. Variance of sample proportion")
        print("16. Quit")

        choice = input("Enter Choice: ")

        if choice == "1":
            print(scientificCalculator.populationMean(data));

        elif choice == "2":
            print(scientificCalculator.calculate_median(data));

        elif choice == "3":
            print(scientificCalculator.mode(data, 2));

        elif choice == "4":
            print(scientificCalculator.populationStandardDeviation(data));

        elif choice == "5":
            print(scientificCalculator.population_proportion_variance(data));

        elif choice == "6":
            print(scientificCalculator.zscore(data, 6));

        elif choice == "7":
            print(scientificCalculator.standardizedScore(data, 4));

        elif choice == "8":
            print(scientificCalculator.correlationCoefficient(data, data1, 4));

        elif choice == "9":
            print(scientificCalculator.confidence_interval(data, 5));

        elif choice == "10":
            print(scientificCalculator.populationVariance(data));

        elif choice == "11":
            print(scientificCalculator.pValue(data, 50));

        elif choice == "12":
            print(scientificCalculator.proportion(data, 4));

        elif choice == "13":
            print(scientificCalculator.sampleMean(data, 6));

        elif choice == "14":
            print(scientificCalculator.stdev(data));

        elif choice == "15":
            print(scientificCalculator.var(data));

        elif choice == "16":
            break;