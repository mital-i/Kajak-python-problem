
#Take in how many rows and columns there are
input_value=input().split()
num_rows=int(input_value[0])
num_cols=int(input_value[1])


def Convertstring_to_arr(string): 
    list1=[] 
    list1[:0]=string 
    return list1

#The 'map' of the boat race, this will contain all the strings that
#are inputed in the beginning, like "S....111.F", etc. 
row_content=[]
    
#Number of kayaks is fixed (always 9 boats)
rankings=[0]*9

#input the map of the boat race, convert each input string into a list, 
#then add it to row_content
for i in range(num_rows): 
    input_racerow=input()
    input_racerow_arr=Convertstring_to_arr(input_racerow)
    row_content.append(input_racerow_arr)
    
    
#Dictionary that will store the distances of each boat to the finish line
dict_of_positions={}
for i in range(num_rows): 
    if str(i+1) in row_content[i]: 
        distance=row_content[i].index('F')-row_content[i].index(str(i+1))
        dict_of_positions.update({int(i+1):distance})
    
#function to find all given values in a list
def find_all_values(list1, value): 
    return [i for i, x in enumerate(list1) if x == value]


#now rank all the boats 
rank=1
while len(dict_of_positions)>0:
    key_data = list(dict_of_positions.keys())
    val_data = list(dict_of_positions.values())

    min_rank=min(val_data)
    all_duplvals=find_all_values(val_data, min_rank)
    
    
    for f in all_duplvals:
        rankings[key_data[f]-1]=rank
        dict_of_positions.pop(key_data[f])

    rank=rank+1

for i in rankings: 
    print(i)