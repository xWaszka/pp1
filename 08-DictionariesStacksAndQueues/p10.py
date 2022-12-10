country1 = {
    "Name": "Poland",
    "Population": "40mln"
}
country2 = {
    "Name": "USA",
    "Population": "330mln"
}
country3 = {
    "Name": "Russia",
    "Population": "160mln"
}
arr = []
arr += country1,country2,country3

i = 0
while i < len(arr):
    print(arr[i])
    i+=1