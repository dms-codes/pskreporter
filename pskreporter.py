import requests

grid = "OI33"
url = "https://pskreporter.info/cgi-bin/psk-freq.pl?grid={}".format(grid)
res = requests.get(url=url)
print("{}\t{}\t{}\t{}\t{}\n".format("Frequency", "Score", "Spots", "Tx", "Rx"))
for line in res.text.split("\n")[:-3]:
    freq, score, spots, tx, rx = line.split(" ")
    print("{:,.0f}\t{}\t{}\t{}\t{}\n".format(float(freq), score, spots, tx, rx))


"""
['14080000', '890', '89', '2', '0']
['24920000', '332', '40', '0', '1']
['14070000', '311', '32', '0', '0']
['21080000', '250', '31', '2', '2']
['7080000', '137', '18', '1', '1']
['21070000', '34', '6', '1', '3']
['7070000', '14', '4', '0', '0']
['18100000', '10', '7', '0', '1']
['28080000', '10', '1', '1', '0']
['#', 'frequency', 'score', '#spots', '#tx', '#rx']
['#', 'grid', 'OI33%,', '5', 'mins']
['']
"""
