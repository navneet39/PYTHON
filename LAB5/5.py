A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Join A and B
A_union_B = A.union(B)
print("Join A and B:", A_union_B)

# II. Find A intersection B
A_intersection_B = A.intersection(B)
print("A intersection B:", A_intersection_B)

# III. Is A subset of B
is_A_subset_B = A.issubset(B)
print("Is A subset of B?:", is_A_subset_B)

# IV. Are A and B disjoint sets
are_A_B_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?:", are_A_B_disjoint)

# V. Join A with B and B with A (This is effectively the same as union)
A_union_B_again = A.union(B)
B_union_A = B.union(A)
print("Join A with B:", A_union_B_again)
print("Join B with A:", B_union_A)

# VI. What is the symmetric difference between A and B
symmetric_diff_AB = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_diff_AB)

# VII. Delete the sets completely
delete_sets = input("Do you want to delete sets A and B? (yes/no): ").strip().lower()
if delete_sets == 'yes':
    del A
    del B
    print("Sets A and B have been deleted.")
else:
    print("Sets A and B were not deleted.")
