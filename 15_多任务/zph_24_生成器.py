nums1 = [x*2 for x in range (5)]
print(nums1)

nums2 = (x*2 for x in range (5))
print(nums2)

for num in nums2:
    print(num)

print("-" * 20)
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print(a)
        a, b = b, a+b
        current_num += 1


create_num(10)

