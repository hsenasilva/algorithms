

class Algo01:

    # 128 numbers
    my_list = [14, 7, 35, 48, 7, 27, 53, 97, 89, 11, 47, 86, 26, 58, 53, 36, 47, 17, 15, 54, 59, 80, 71, 55, 25, 30, 12,
               63, 84, 88, 95, 54, 38, 96, 96, 83, 93, 100, 26, 24, 87, 88, 81, 26, 48, 96, 59, 65, 68, 9, 43, 38, 77,
               97, 5, 36, 98, 94, 62, 61, 39, 85, 70, 15, 76, 38, 97, 4, 58, 74, 53, 63, 83, 5, 91, 49, 19, 2, 18, 2,
               52, 62, 84, 3, 7, 90, 93, 84, 90, 48, 47, 84, 62, 62, 88, 27, 88, 7, 49, 3, 51, 44, 7, 54, 78, 77, 49,
               12, 57, 7, 93, 14, 91, 78, 24, 71, 98, 55, 71, 9, 50, 32, 42, 28, 43, 25, 96, 12]

    def binary_search(list, item):

        list = sorted(list)
        print(list)

        low = 0
        high = len(list) - 1

        while low <= high:
            print('low: ' + str(low))
            print('high: ' + str(high))
            mid = (low + high)
            print('mid: ' + str(mid))
            guess = list[mid]
            print('guess: ' + str(guess))
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    print(binary_search(my_list, 11))


