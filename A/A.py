# with open("A.txt") as f:
#     sigs = int(f.readline())
#     nums = []
#     for a in range(sigs):
#         nums.append(int(f.readline()))
# ans = 1
# for i in range(1, sigs):
#     if nums[i] <= nums[i-1]:
#         ans += 1
# print(ans)

sigs = int(input())
nums = []
for a in range(sigs):
    nums.append(int(input()))
ans = 1
for i in range(1, sigs):
    if nums[i] <= nums[i-1]:
        ans += 1
print(ans)
