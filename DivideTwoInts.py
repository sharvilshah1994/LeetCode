def divide(dividend, divisor):
    flag1 = False
    flag2 = False
    if dividend == 0:
        return 0
    elif ((dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)) and dividend < divisor:
        return 0
    else:
        count = 1
        if dividend < 0:
            flag1 = True
            dividend = -dividend
        if divisor < 0:
            flag2 = True
            divisor = -divisor
        while dividend != divisor:
            if divisor > dividend:
                break
            else:
                count += 1
            divisor += divisor
        if (flag1 and not flag2) or (not flag1 and flag2):
            return -count
        else:
            return count
print(divide(2,2))