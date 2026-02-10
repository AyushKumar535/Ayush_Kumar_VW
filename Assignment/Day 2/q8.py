calls = int(input("Enter a numb of calls :"))
bill = 200

if calls > 100:
    if calls <=150:
        bill += (calls-100) * 0.60
    elif calls <= 200:
        bill += 50 * 0.60
        bill += (calls -150) * 0.50
    else:
        bill += 50 * 0.60
        bill += 50 * 0.50
        bill += (calls -200) * 0.40

print("Total telephone bills = Rs.", bill)
