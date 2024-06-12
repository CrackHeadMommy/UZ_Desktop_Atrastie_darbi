skaitisanas_vardnica = {}

    
with open("TEKSTS.txt", "r", encoding="utf-8") as files:  
        for rinda in files:
            dati = rinda.split(" ")
            for vards in dati:
                vards = vards.strip(".,1234567890()!?:;% +=-\"\n")
                vards = vards.lower()
                if len(vards) < 4:
                     continue
                vards = (vards[:4]) 
                if vards in skaitisanas_vardnica.keys():
                    skaitisanas_vardnica[vards] += 1
                else: 
                    skaitisanas_vardnica[vards] = 1
        


lielakais = [""] * 5 
lielaka_vertiba = [0] * 5

for atslega, vertiba in skaitisanas_vardnica.items():
    if vertiba > min(lielaka_vertiba):
        min_index = lielaka_vertiba.index(min(lielaka_vertiba))
        lielaka_vertiba[min_index] = vertiba
        lielakais[min_index] = atslega

result_tuples = list(zip(lielakais, lielaka_vertiba))


result_tuples.sort(key=lambda x: x[1], reverse=True)

for elements in result_tuples:
    print(elements[0], elements[1])