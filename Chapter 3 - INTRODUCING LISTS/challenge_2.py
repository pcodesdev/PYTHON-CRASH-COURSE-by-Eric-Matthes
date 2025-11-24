# 3-4. Guest List
guest_list = ['Robert', 'Ann', 'Precious', 'James', 'Emmah']
print(guest_list)
guest_1_name = guest_list[0]
guest_2_name = guest_list[1]
guest_3_name = guest_list[2]
guest_4_name = guest_list[3]
print(f"{guest_1_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_2_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_3_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_4_name}, your are cordially invited to the dinner tonight.")

# 3-5. Changing Guest List
can_not_make_it =  guest_list.pop(0)
print(f"\nUnfortunately {can_not_make_it} to the dinner tonight.")

guest_5_name = guest_list.append('Francis')
guest_5_name = guest_list[-1]


guest_1_name = guest_list[0]
guest_2_name = guest_list[1]
guest_3_name = guest_list[2]
guest_4_name = guest_list[3]

print(f"{guest_1_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_2_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_3_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_4_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_5_name}, your are cordially invited to the dinner tonight.")

print(f"\nI have found a bigger table and this means more guests!")

# 3-6. More Guests

guest_list.insert(0,"Sophia")
guest_list.insert(2,"Hilda")
guest_list.insert(-1,"Esther")
print(guest_list)

guest_1_name = guest_list[0]
guest_2_name = guest_list[1]
guest_3_name = guest_list[2]
guest_4_name = guest_list[3]
guest_5_name = guest_list[4]
guest_6_name = guest_list[5]
guest_7_name = guest_list[6]
guest_8_name = guest_list[7]

print(f"{guest_1_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_2_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_3_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_4_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_5_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_6_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_7_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_8_name}, your are cordially invited to the dinner tonight.")

# 3-7. Shrinking Guest List
print(f"\nUnfortunately I can only invite 2 people to the party.")
guest_removed = guest_list.pop(0)
print(f"I have removed {guest_removed} to the party. Due to space limitations.")

guest_removed = guest_list.pop(0)
print(f"I have removed {guest_removed} to the party. Due to space limitations.")
guest_removed = guest_list.pop(0)
print(f"I have removed {guest_removed} to the party. Due to space limitations.")
guest_removed = guest_list.pop(0)
print(f"I have removed {guest_removed} to the party. Due to space limitations.")
guest_removed = guest_list.pop(0)
print(f"I have removed {guest_removed} to the party. Due to space limitations.")
guest_removed = guest_list.pop(0)
print(f"I have removed {guest_removed} to the party. Due to space limitations.")
guest_1_name = guest_list[0]
guest_2_name = guest_list[1]
print(f"{guest_1_name}, your are cordially invited to the dinner tonight.")
print(f"{guest_2_name}, your are cordially invited to the dinner tonight.")
del guest_list[0]
del guest_list[0]
print(guest_list)

