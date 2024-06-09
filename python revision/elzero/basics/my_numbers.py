"""
int => 1 - 0 - -1
float => 1.2 - 0.2 - -1.2
complex number => imaginary number

- you can convert from float or int to complex but not from complex to another
"""
cmplx = 5+6j

print(type(cmplx)) #complex

print("real part: {}".format(cmplx.real))
print("imaginary part: {}".format(cmplx.imag))


# math

print(30 - 10)
print(30 + 10)
print(int(30 / 10)) #if you didn't put the int() it will be float
print(30 * 10)
print(30 * 10**3)

# remainder
print(8 % 2) # 8 can be divided by 2 so the remainder => 0
print(9 % 2) # 9 cannot be diveded by 2 but it can be when you take 1 from the 9 so the remainder => 1
print(22 % 5) # if you removed 2 from the 22 it will dividable so => 2

# floor division
print(8 // 3) #8/3 = 2.6 then round it to the lowest so => 2

