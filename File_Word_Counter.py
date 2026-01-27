from collections import Counter
filename ="sample.txt"
try:

    def analyze_file(filename):
        with open (filename,'r') as f:
            for line in f:
                
                words = line.split(" ")

                Only =[]
                common=[]

                unique =[]
                if words not in unique:
                    unique.append(words)

                # for words not in unique:
                #    Only.append(words)

                #    print(f"Only word is {Only}")


                

                count = Counter(words)
                t1 = len(count)
                
                print()
            print(f'Total  words :{t1}')
            print()
               
            print()
            print(f"Total unique words are {len(unique)}")
                
            

except ValueError:
    print("Error :")
finally:
    print(f'file analysed {filename}')


stats = analyze_file("sample.txt")