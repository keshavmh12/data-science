from logging import exception

with open("initialdata.txt", "r",encoding='utf-8') as file:
    data = file.read()
    #print(data)

chunks=data.split("\n\n")
chunks= [c for c in chunks if len(c)>3]
chunks[4]

def parse_chunks(chunk):
    try:
        chunks=data.strip()
        sep_chunk=chunks.split("\n\n")
        user_name=sep_chunk[0]
        no_of_post=int(sep_chunk[1].split("post")[0].replace(",",""))
        followers=float(sep_chunk[2].split("followers")[0].replace(",","").replace("k","").replace("m",""))
        followers = sep_chunk[2]

        if "K" in followers:
            followers = float(followers.replace("K", "")) * 1000

        elif "M" in followers:
            followers = float(followers.replace("M", "")) * 1000000

        else:
            followers = int(followers)


        following=sep_chunk[3]
        if "K" in followers:
            following = float(following.replace("K", "")) * 1000

        elif "M" in following:
            following = float(following.replace("M", "")) * 1000000

        else:
            following = int(following)
        name=sep_chunk[4]
        if(len(sep_chunk)>5):
            type_of_account=chunk[5]
            bio="\n".join(sep_chunk[6])
        else:
            type_of_account="unknown"
            bio=''
        #print(user_name,no_of_post,followers,following,name,type_of_account,bio,sep="\n")
        return {"username":user_name,"no_of_post":no_of_post,"followers":followers,"following":following,"name":name,"type_of_account":type_of_account,"bio":bio}
    except exception as e:
        print(chunk,e)


all_chunks=[]
for chunk in chunks:
    print(f"the chunk is: {chunk}")
    parsed=parse_chunks(chunk)
    all_chunks.append(parsed)
print(all_chunks)

import json
s=json.dumps(all_chunks,indent=4)
print(s)
    