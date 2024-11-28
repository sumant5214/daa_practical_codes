import pandas as pandascsv
csvData = pandascsv.read_csv("C:\\Users\\Sumant Vetal\\OneDrive\\Documents\\daa practical\\100_items.csv")
print("Before sorting")
print(csvData)
csvData.sort_values(["Shelf_Life_Days","Cost_Dollars"], axis=0, ascending=[True, False], inplace=True)
print("After sorting")
print(csvData)
csvData.insert(5, "value_to_weight", [row[2]/row[3] for row in csvData.values])
csvData.sort_values(["Shelf_Life_Days", "value_to_weight"], axis=0, ascending=[True, False], inplace=True)
print(csvData)
capacity = 200
total_value = 0
current_weight = 0
remaining_weight = None
for row in csvData.values:
    if(current_weight + row[3] <= capacity):
        current_weight += row[3]
        total_value += row[2]
    else:
        remaining_weight = capacity - current_weight
        total_value += row[5] * remaining_weight

current_weight += remaining_weight
print("Total Value: " + str(total_value))
print("Current Weight: " + str(current_weight))