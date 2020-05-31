

def print_tuple(nums):
  # print("\n".join(map(lambda num:str(num), nums)))


  # nums.map(num => num.toString())
  str_nums = map(lambda num: str(num), nums)
  print(list(str_nums))


print_tuple((1, 2, 3, 4, 5))
