"""
1. Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
import datetime

numbers = """
    37107287533902102798797998220837590246510135740250\n",
    "46376937677490009712648124896970078050417018260538\n",
    "74324986199524741059474233309513058123726617309629\n",
    "91942213363574161572522430563301811072406154908250\n",
    "23067588207539346171171980310421047513778063246676\n",
    "89261670696623633820136378418383684178734361726757\n",
    "28112879812849979408065481931592621691275889832738\n",
    "44274228917432520321923589422876796487670272189318\n",
    "47451445736001306439091167216856844588711603153276\n",
    "70386486105843025439939619828917593665686757934951\n",
    "62176457141856560629502157223196586755079324193331\n",
    "64906352462741904929101432445813822663347944758178\n",
    "92575867718337217661963751590579239728245598838407\n",
    "58203565325359399008402633568948830189458628227828\n",
    "80181199384826282014278194139940567587151170094390\n",
    "35398664372827112653829987240784473053190104293586\n",
    "86515506006295864861532075273371959191420517255829\n",
    "71693888707715466499115593487603532921714970056938\n",
    "54370070576826684624621495650076471787294438377604\n",
    "53282654108756828443191190634694037855217779295145\n",
    "36123272525000296071075082563815656710885258350721\n",
    "45876576172410976447339110607218265236877223636045\n",
    "17423706905851860660448207621209813287860733969412\n",
    "81142660418086830619328460811191061556940512689692\n",
    "51934325451728388641918047049293215058642563049483\n",
    "62467221648435076201727918039944693004732956340691\n",
    "15732444386908125794514089057706229429197107928209\n",
    "55037687525678773091862540744969844508330393682126\n",
    "18336384825330154686196124348767681297534375946515\n",
    "80386287592878490201521685554828717201219257766954\n",
    "78182833757993103614740356856449095527097864797581\n",
    "16726320100436897842553539920931837441497806860984\n",
    "48403098129077791799088218795327364475675590848030\n",
    "87086987551392711854517078544161852424320693150332\n",
    "59959406895756536782107074926966537676326235447210\n",
    "69793950679652694742597709739166693763042633987085\n",
    "41052684708299085211399427365734116182760315001271\n",
    "65378607361501080857009149939512557028198746004375\n",
    "35829035317434717326932123578154982629742552737307\n",
    "94953759765105305946966067683156574377167401875275\n",
    "88902802571733229619176668713819931811048770190271\n",
    "25267680276078003013678680992525463401061632866526\n",
    "36270218540497705585629946580636237993140746255962\n",
    "24074486908231174977792365466257246923322810917141\n",
    "91430288197103288597806669760892938638285025333403\n",
    "34413065578016127815921815005561868836468420090470\n",
    "23053081172816430487623791969842487255036638784583\n",
    "11487696932154902810424020138335124462181441773470\n",
    "63783299490636259666498587618221225225512486764533\n",
    "67720186971698544312419572409913959008952310058822\n",
    "95548255300263520781532296796249481641953868218774\n",
    "76085327132285723110424803456124867697064507995236\n",
    "37774242535411291684276865538926205024910326572967\n",
    "23701913275725675285653248258265463092207058596522\n",
    "29798860272258331913126375147341994889534765745501\n",
    "18495701454879288984856827726077713721403798879715\n",
    "38298203783031473527721580348144513491373226651381\n",
    "34829543829199918180278916522431027392251122869539\n",
    "40957953066405232632538044100059654939159879593635\n",
    "29746152185502371307642255121183693803580388584903\n",
    "41698116222072977186158236678424689157993532961922\n",
    "62467957194401269043877107275048102390895523597457\n",
    "23189706772547915061505504953922979530901129967519\n",
    "86188088225875314529584099251203829009407770775672\n",
    "11306739708304724483816533873502340845647058077308\n",
    "82959174767140363198008187129011875491310547126581\n",
    "97623331044818386269515456334926366572897563400500\n",
    "42846280183517070527831839425882145521227251250327\n",
    "55121603546981200581762165212827652751691296897789\n",
    "32238195734329339946437501907836945765883352399886\n",
    "75506164965184775180738168837861091527357929701337\n",
    "62177842752192623401942399639168044983993173312731\n",
    "32924185707147349566916674687634660915035914677504\n",
    "99518671430235219628894890102423325116913619626622\n",
    "73267460800591547471830798392868535206946944540724\n",
    "76841822524674417161514036427982273348055556214818\n",
    "97142617910342598647204516893989422179826088076852\n",
    "87783646182799346313767754307809363333018982642090\n",
    "10848802521674670883215120185883543223812876952786\n",
    "71329612474782464538636993009049310363619763878039\n",
    "62184073572399794223406235393808339651327408011116\n",
    "66627891981488087797941876876144230030984490851411\n",
    "60661826293682836764744779239180335110989069790714\n",
    "85786944089552990653640447425576083659976645795096\n",
    "66024396409905389607120198219976047599490197230297\n",
    "64913982680032973156037120041377903785566085089252\n",
    "16730939319872750275468906903707539413042652315011\n",
    "94809377245048795150954100921645863754710598436791\n",
    "78639167021187492431995700641917969777599028300699\n",
    "15368713711936614952811305876380278410754449733078\n",
    "40789923115535562561142322423255033685442488917353\n",
    "44889911501440648020369068063960672322193204149535\n",
    "41503128880339536053299340368006977710650566631954\n",
    "81234880673210146739058568557934581403627822703280\n",
    "82616570773948327592232845941706525094512325230608\n",
    "22918802058777319719839450180888072429661980811197\n",
    "77158542502016545090413245809786882778948721859617\n",
    "72107838435069186155435662884062257473692284509516\n",
    "20849603980134001723930671666823555245252804609722\n",
    "53503534226472524250874054075591789781264330331690"
"""


def compute_10_digits(numbers):
    numbers_array = numbers.replace('"', '')
    numbers_array = numbers_array.split("\n")
    numbers_array = [num.strip() for num in numbers_array]
    numbers_array = [int(num) for num in numbers_array if num not in ['', ',']]

    total = sum(numbers_array)
    num_digits = int(len([ch for ch in str(total)]))
    digits_to_omit = num_digits - 10
    result = total // 10 ** digits_to_omit

    print(result)


"""
2. The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even),
    n → 3n + 1 (n is odd)
    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
    Which starting number, under one million, produces the longest chain?
    NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def count_chain(curr_value):
    count = 0
    while True:
        count += 1
        if curr_value == 1:
            break
        if curr_value % 2 == 0:
            curr_value = int(curr_value / 2)
        else:
            curr_value = curr_value * 3 + 1
    return count


def sequence():
    curr_value = 13
    max_chain = 10
    result_value = 0

    for i in range(curr_value, 1000000):
        count_num = count_chain(curr_value)
        if count_num > max_chain:
            max_chain = count_num
            result_value = curr_value

        curr_value += 1

    print(result_value, max_chain)


"""
3. 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
   What is the sum of the digits of the number 2^1000?
"""


def sum_exponent(exp):
    result = 2 ** exp
    sum_digits = sum([int(num) for num in str(result)])
    print(result)
    print(sum_digits)


"""
4. If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
    how many letters would be used?
    NOTE: Do not count spaces or hyphens. 
    For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
    contains 20 letters.
    The use of \"and\" when writing out numbers is in compliance with British usage.
"""

def define_globals():
    global ones_list, tens_list, specials_list, thousand
    tens_list = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    ones_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    specials_list = ['ten', 'eleven', 'twelve', 'thirteen','fourteen', 'fifteen','sixteen', 'seventeen',
                     'eighteen', 'nineteen']
    thousand = 'one thousand'

    global ones, tens, hundreds, specials
    ones = ''
    tens = ''
    hundreds = ''
    specials = ''


def generate_ones(num_ones, num_tens):
    ones_in_words = ''
    if num_ones and num_tens != 1:
        ones_in_words = ' ' + ones_list[num_ones - 1]
    return ones_in_words


def generate_specials(num_tens, num_ones):
    num_special = ''
    if num_tens == 1:
        num_special = specials_list[num_ones]
    return num_special

def generate_tens(num_tens):
    tens_in_words = ''
    if num_tens and num_tens != 1:
        tens_in_words = tens_list[num_tens - 1]

    return tens_in_words

def generate_hundreds(num_hundreds, num_tens, num_ones):
    hundreds_in_words = ''
    if num_hundreds:
        hundreds_in_words = ones_list[num_hundreds - 1] + ' hundred'
        if num_tens or num_ones:
            hundreds_in_words = hundreds_in_words + ' and '
    return hundreds_in_words


def use_thousand(num):
    return len([ch for ch in str(num)]) == 4


def words_generate(num):
    define_globals()

    if use_thousand(num):
        full_number_in_words = 'one thousand'
    else:
        num_ones = num % 10
        num_tens = num // 10 % 10
        num_hundreds = num // 10 // 10 % 10

        specials = generate_specials(num_tens, num_ones)
        tens = generate_tens(num_tens)
        hundreds = generate_hundreds(num_hundreds, num_tens, num_ones)
        ones = generate_ones(num_ones, num_tens)

        full_number_in_words = hundreds + specials + tens + ones
    return full_number_in_words

def nums_to_words():
    nums = []
    total_len = 0


    for i in range(1, 1001):
        nums.append(words_generate(i))
    nums = [num.replace(' ', '') for num in nums]

    for num in nums:
        total_len += len(num)
    #print(nums)
    print(total_len)


"""
5.You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday. Thirty days has September, April, June and November. 
    All the rest have thirty-one, Saving February alone Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def count_sundays():
    sunday_count = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            the_date = datetime.datetime(year, month, 1)
            if the_date.strftime('%a') == 'Sun':
                sunday_count += 1
    print(sunday_count)


"""
6. n! means n × (n − 1) × ... × 3 × 2 × 1
   For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800
   and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
   Find the sum of the digits in the number 100!
"""

import math


def factorial_digits_sum(num):
    result_factorial = math.factorial(num)
    sum_digits = sum([int(i) for i in str(result_factorial)])
    print(sum_digits)


"""
7. Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n)
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
    amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
    Evaluate the sum of all the amicable numbers under 10000.
"""


def find_divisors(num):
    div = []
    for i in range(1, num):
        if num % i == 0:
            div.append(i)
    return div


def amicable_numbers(num):
    sum_divisors_a = sum(find_divisors(num))
    sum_divisors_b = sum(find_divisors(sum_divisors_a))
    print(sum_divisors_b)


"""
8.A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
   For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
   which means that 28 is a perfect number.
   A number n is called deficient if the sum of its proper divisors is less than n 
   and it is called abundant if this sum exceeds n.
   As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
   the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
   it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
   However, this upper limit cannot be reduced any further by analysis even though it is known 
   that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
   Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
   """


def is_abundant(num):
    divisors_sum = 1
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum > num


def abundant_sums(abundant_nums):
    abundant_sums = set([])
    for number_one in abundant_nums:
        for number_two in abundant_nums:
            if number_one + number_two > 28123:
                break
            else:
                abundant_sums.add(number_one + number_two)
    return abundant_sums


def abundant_sum():
    abundant_nums = [num for num in range(12, 28124) if is_abundant(num)]
    abundant_sum = abundant_sums(abundant_nums)
    non_abundant_sums = sum([int(num) for num in range(28124) if num not in abundant_sum])
    print(non_abundant_sums)


"""
9.  A permutation is an ordered arrangement of objects. 
    For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
    If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
    The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations


def permutation():
    permutation_list = list(permutations(range(10)))
    one_million_result = [str(num) for num in permutation_list[100000]]
    result = "".join(one_million_result)
    print(result)


"""
10. "A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 
    2 to 10 are given:
        1/2= 0.5,
        1/3= 0.(3),
        1/4= 0.25,
        1/5= 0.2,
        1/6= 0.1(6),
        1/7= 0.(142857),
        1/8= 0.125,
        1/9= 0.(1),
        1/10= 0.1 ,
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
    It can be seen that 1/7 has a 6-digit recurring cycle.
    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."
"""


def find_cycle_length(num):
    remainder = 10
    i = 0
    while remainder != 10 or i < 1:
        remainder = (remainder % num) * 10
        i += 1
    return i


def recurring_cycle():
    longest_cycle = 7
    longest_cycle_number = 0
    for i in range(2, 1000):
        if i % 2 != 0 and i % 5 != 0:
            cycle_length = find_cycle_length(i)
            if cycle_length > longest_cycle:
                longest_cycle = cycle_length
                longest_cycle_number = i
    print(longest_cycle_number)


if __name__ == '__main__':
    # compute_10_digits(numbers)
    # sequence()
    # sum_exponent(1000)
     nums_to_words()
    # count_sundays()
    # factorial_digits_sum(100)
    # amicable_numbers(10000)
    # abundant_sum()
    # permutation()
    # recurring_cycle()
