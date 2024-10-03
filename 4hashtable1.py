# Average-case time complexity for insertions, deletions, and lookups: O(1)
# Worst-case time complexity: O(n) (if many collisions occur, all elements may end up in a single bucket, reducing performance)

hash_table={}

#insert
hash_table["num"]=1
hash_table["name"]="pawan"
hash_table["marks"]=76/100
hash_table["address"]="chennai"

print(hash_table["marks"])

print("name" in hash_table)

#delete
del hash_table["num"]
print(hash_table)

print(hash_table.get("num","key not found")) 

