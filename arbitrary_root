# finds root root of num
# to dig digits
# only works with roots greater than or equal to 2
def arb_root(num, root, dig=10):
    assert root >= 2, "The root must be greater than or equal to 2."

    ans = 0

    while (ans + 1) ** root <= num:
        ans += 1

    for x in range(dig):
        exp = x + 1

        for y in range(10):
            if (ans + 10 ** (exp * -1)) ** root >= num:
                # if adding one more will make the ans ** root more than num
                # go to the next x in range(dig)
                break
            ans = ans + 10 ** (exp * -1)
            str_ans = str(ans)
            end = str_ans.index('.') + exp + 1
            if len(str_ans[end:]) > 0:
                if str_ans[end] == "0":
                    ans = float(str_ans[:end])
                elif str_ans[end] == "9":
                    ans = float(str_ans[:end - 1] + chr(ord(str_ans[end - 1]) + 1))
    return ans
