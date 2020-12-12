import random
import string


def createfunc(limiter1, limiter2, good):
    if limiter1 > limiter2:
        limiter2, limiter1 = limiter1, limiter2
    operators = ["*", "+", "/", "-"]
    op = operators[random.randint(0, 3)]
    rand = random.randint(limiter1, limiter2)
    if good:
        word = {
            "*": "mal",
            "/": "geteiltdurch",
            "-": "minus",
            "+": "plus"
        }
        name = word[op] + "_" + str(rand)
    else:
        randstr = ""
        source = string.ascii_letters + "1234567890"
        for i in range(random.randint(limiter1, limiter2)):
            randstr += random.choice(source)
        name = randstr
    func = "def {name}(m): \n\tm = m {op} {rand}\n\treturn m".format(name=name, op=op, rand=rand)
    return func, "m = " + name + "(m)"


def createfuncblock(size, limiter1, limiter2, good):
    block = []
    for i in range(size):
        block.append(createfunc(limiter1, limiter2, good))
    return list(set(block))


def randomseed():
    source = "1234567890"
    seed = ""
    for i in range(10):
        seed += random.choice(source)
    return seed


def randominitial():
    source = "1234567890"
    seed = ""
    for i in range(4):
        seed += random.choice(source)
    return seed


def codegenerator(good, seed=randomseed()):
    print(seed)
    code = ""
    initial = randominitial()
    size = seed[0] + seed[1]
    size = int(size)
    limiter1 = int(seed[2]) + int(seed[4]) - int(seed[6])
    limiter2 = int(seed[3]) + int(seed[5])
    if limiter1 < 0:
        limiter1 = 0
    funcs = createfuncblock(size, limiter1, limiter2, good)
    for func in funcs:
        create, call = func
        code += create
        code += "\n\n\n"

    code += "m = " + initial + "\n"
    number_function_calls = int(seed[7] + seed[8] + seed[9])
    number_function_calls -= 100
    for i in range(number_function_calls):
        random_call = funcs[random.randint(0, len(funcs) - 1)]
        _, call = random_call
        code += call
        code += "\n"
    code += "print(m)"
    return code


good_code = codegenerator(True, "1034861152")
bad_code = codegenerator(False, "1034861152")

file_good = open("good_file.txt", "w")
file_good.write(good_code)
file_good.close()

file_bad = open("bad_file.txt", "w")
file_bad.write(bad_code)
file_bad.close()
