import higher_or_lower_logo
import higher_or_lower_data
import random
# todo 8 compare function
def compare(who):
    if first_follower_count > second_follower_count and who == "A":
        return True
    elif second_follower_count > first_follower_count and who == "B":
        return True
    else: return False

print(higher_or_lower_logo.logo)
# todo 1 --- random choice in data
first = random.choice(higher_or_lower_data.data)
# todo 2 --- while loop
final_score = 0
should_continue = True
while should_continue:
    first_name = first["name"]
    first_follower_count = first["follower_count"]
    first_description = first["description"]
    first_country = first["country"]
    # todo 3 --- print compare
    # print(f"pssst, first follower count is: {first_follower_count}")
    if first_description[0] == "A":
        print(f"compare A: {first_name} an {first_description}, from {first_country}.")
    else:
        print(f"compare A: {first_name}, a {first_description}, from {first_country}.")
    # todo 4 --- VS logo
    print(higher_or_lower_logo.vs)
    # todo 5 --- random choice in data
    second = random.choice(higher_or_lower_data.data)
    while first == second:
        second = random.choice(higher_or_lower_data.data)
    second_name = second["name"]
    second_follower_count = second["follower_count"]
    second_description = second["description"]
    second_country = second["country"]
    # print(f"pssst, second follower count is: {second_follower_count}")
    # todo 6 --- print against
    if second_description[0] == "A":
        print(f"against B: {second_name} an {second_description}, from {second_country}.")
    else:
        print(f"against B: {second_name}, a {second_description}, from {second_country}.")
    # todo 7 --- print who?
    who = input("who has more followers? Type 'A' or 'B': ").upper()
    # todo 9 --- if True Then first = second , score +=1  else: break the while loop
    if compare(who): 
        first = second
        final_score +=1
        print(f"you're right! Current score: {final_score}")
    else: should_continue = False
# todo 10 --- print final score
print(f"Sorry, that's Wrong. final score: {final_score}")