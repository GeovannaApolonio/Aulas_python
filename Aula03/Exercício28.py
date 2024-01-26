from random import choices

nums = [1,2,3,4,5]
num = int(input("Advinhe um número entre 1 e 5: "))
randomnums = choices(nums)

if num == randomnums:
    print("Você venceu!")
else:
    print(f"Você perdeu, o número era {randomnums} tente novamente depois.")