import random
import math

def make_add(n):
    return lambda x: x+n, lambda exp: f"({exp}-{n})"
def make_sub(n):
    return lambda x: x-n, lambda exp: f"({exp}+{n})"
def make_mul(n):
    return lambda x: x*n, lambda exp: f"{exp}/{n}"
def make_div(n):
    return lambda x: x/n, lambda exp: f"{exp}*{n}"

def random_op():
    n = math.floor(random.random()*10)+1
    ops = [
        make_add,
        make_sub,
        # make_mul,
        # make_div,
    ] # no div b/c floating point errors
    generator = random.choice(ops)
    return generator(n)

def gen_expressions(n, target):
    for _ in range(n):
        op1, inv1 = random_op()
        op2, inv2 = random_op()
        expression = inv1(inv2(op2(op1(target))))
        if expression[0] == "(" and expression[-1] == ")":
            expression = expression[1:-1]
        assert eval(expression) == target
        yield expression

def classify(statement):
    ops = ""
    for i in range(len(statement)):
        # Special handling for negative numbers which introduce minus
        # signs which are not operations.
        if statement[i] == "-":
            if i == 0:
                continue
            if not (statement[i-1] in [str(n) for n in range(10)]+[")"]):
                continue
        if statement[i] in ["-", "+", "/"]:
            ops = ops + statement[i]
    return {
        "++": 1, # -> 1
        "+-": 2, # -> 2
        "+/": 3, # -> 3

        "-+": 4, # -> 4
        "--": 5, # -> 12
        "-/": 6, # -> 13

        "/+": 7, # -> 8
        "/-": 8, # -> 10
        "//": 9, # -> 11
    }[ops]

def gen_prompts(n=250):
    assert n % 2 == 0
    print("statement,label")
    for (four, seven) in zip(gen_expressions(n//2, 4), gen_expressions(n//2, 7)):
        print(f"What is {four}?,{classify(four)}")
        print(f"What is {seven}?,{classify(seven)}")

if __name__ == "__main__":
    gen_prompts()
