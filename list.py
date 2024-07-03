# num1=[12,23,24,53,55]
# # print(num1)
# name=['abhi','jiva','shiva','maru']

# mil=[num1,name]
# print(mil)
# list is mutable we can change the list
# num1.append(43)
# print(num1)


# def group_anagrams(strs):
#     anagrams_dict = {}
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word in anagrams_dict:
#             anagrams_dict[sorted_word].append(word)
#         else:
#             anagrams_dict[sorted_word] = [word]
#     return list(anagrams_dict.values())

# # Example usage
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = group_anagrams(strs)
# print(result)
# ====================================================

list12= ["abhi","jiva","shiva","paru"]
list13=[1,3,4,6,78]
list14=[True,False,False]

# print(list12,list13,list14)
# list() Constructor

list15= list(("abhi","jiva","shiva","paru"))
# print(list15)
# print(type(list15))


list16= list(("abhi","jiva","shiva","paru"))
# if "abhi" in list16:
    # print("yes, abhi is present")
    
list17= ["abhi","jiva","shiva","paru"]

list17[0]="ABHIJEET"
# print(list17)

# print(list17[1])


list18= ["abhi","jiva","shiva","paru"]

