ffmpeg = open("rcinit_0M.log",'r') #ffmpeg side log-file (filtered)
ffplay = open("prcinit_0M.log",'r') #ffplay side log-file (filtered)
fout = open("buf_0M.plot",'w') #output file.
arr1 = [[int(x) for x in line.split()] for line in ffmpeg]
arr2 = [[int(x) for x in line.split()] for line in ffplay]
arr=[]
for i in range(len(arr2)):
    if( arr2[i][0] - arr1[i][0] > 10 ):  # We are using packet size to identify packet at both side
        print("Packet size not maching at line:",i+1)
    arr.append(arr2[i][1]-arr1[i][1])
arr.sort()

for a in arr:
    fout.write(str(a)+"\n")
ffmpeg.close()
ffplay.close()
fout.close()
print("\t\t\t ||Done||")
