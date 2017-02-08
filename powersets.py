def powerset(s):
  ret_list=[{}]
  for item in s:
    for sub_set in ret_list:
      ret_list=ret_list+[set(list(sub_set)+[item])]
  return ret_list

def main():
    s=set([1,2,3])
    print(powerset(s))

if __name__ == '__main__':
    main()
