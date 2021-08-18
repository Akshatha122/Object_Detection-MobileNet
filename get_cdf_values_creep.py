import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})
plt.rcParams.update({'font.weight': 'bold'})

plt.xlabel("Delay in mS.")
plt.ylabel("Percentage")

with open('buf_0M_FINAL.plot') as f:
	arr = [[int (float(x)) for x in line.split()] for line in f]
	
	sum = 0
	
	for i in arr:
		sum = sum + i[0]
	print(sum)	
	cdf = []
	pkt_size = []
	cum = 0
	for i in arr:
		cum = cum + i[0]
		cdf.append(cum*100/sum)
		pkt_size.append(i[1])

plt.plot(pkt_size, cdf, label = "delay_buf_0M")



with open('buf_170k_FINAL.plot') as f:
        arr = [[float(x) for x in line.split()] for line in f]
        sum = 0
        for i in arr:
                sum = sum + i[0]
        cdf = []
        pkt_size = []
        cum = 0
        for i in arr:
                cum = cum + i[0]
                cdf.append(cum*100/sum)
                pkt_size.append(i[1])

plt.plot(pkt_size, cdf, label = "delay_buf_170k")


with open('buf_5M_FINAL.plot') as f:
        arr = [[float(x) for x in line.split()] for line in f]
        sum = 0
        for i in arr:
                sum = sum + i[0]
        cdf = []
        pkt_size = []
        cum = 0
        for i in arr:
                cum = cum + i[0]
                cdf.append(cum*100/sum)
                pkt_size.append(i[1])

plt.plot(pkt_size, cdf, label = "delay_buf_5M")


with open('buf_10M_FINAL.plot') as f:
        arr = [[float(x) for x in line.split()] for line in f]
        sum = 0
        for i in arr:
                sum = sum + i[0]
        cdf = []
        pkt_size = []
        cum = 0
        for i in arr:
                cum = cum + i[0]
                cdf.append(cum*100/sum)
                pkt_size.append(i[1])

plt.plot(pkt_size, cdf, label = "delay_buf_10M")


with open('buf_20M_FINAL.plot') as f:
        arr = [[float(x) for x in line.split()] for line in f]
        sum = 0
        for i in arr:
                sum = sum + i[0]
        cdf = []
        pkt_size = []
        cum = 0
        for i in arr:
                cum = cum + i[0]
                cdf.append(cum*100/sum)
                pkt_size.append(i[1])

plt.plot(pkt_size, cdf, label = "delay_buf_20M")

with open('buf_40M_FINAL.plot') as f:
        arr = [[float(x) for x in line.split()] for line in f]
        sum = 0
        for i in arr:
                sum = sum + i[0]
        cdf = []
        pkt_size = []
        cum = 0
        for i in arr:
                cum = cum + i[0]
                cdf.append(cum*100/sum)
                pkt_size.append(i[1])

plt.plot(pkt_size, cdf, label = "delay_buf_40M")

with open('buf_70M_FINAL.plot') as f:
        arr = [[float(x) for x in line.split()] for line in f]
        sum = 0
        for i in arr:
                sum = sum + i[0]
        cdf = []
        pkt_size = []
        cum = 0
        for i in arr:
                cum = cum + i[0]
                cdf.append(cum*100/sum)
                pkt_size.append(i[1])

plt.plot(pkt_size, cdf, color = 'Black', label = "delay_buf_70M")

with open('buf_100M_FINAL.plot') as f:
        arr = [[float(x) for x in line.split()] for line in f]
        sum = 0
        for i in arr:
                sum = sum + i[0]
        cdf = []
        pkt_size = []
        cum = 0
        for i in arr:
                cum = cum + i[0]
                cdf.append(cum*100/sum)
                pkt_size.append(i[1])

plt.plot(pkt_size, cdf, label = "delay_buf_100M")


# giving a title to my graph
plt.title('CDF of Percentage of end-to-end delay (60 fps)', fontsize=18, fontweight='bold')

plt.grid()
# show a legend on the step 
plt.legend(loc = "lower right")

# function to show the step

plt.show()
