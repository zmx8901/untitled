def reverseWords(input):  # 翻转字符串
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")  # split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
    inputWords = inputWords[::-1]  # 也可表示为[-1::-1]
    # 重新组合字符串
    output = ' '.join(inputWords)  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
