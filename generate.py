import pandas as pd

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

hours = [f"{hour}:00 - {hour+1}:00" for hour in range(24)]

# Create a dataframe with the days and hours
df = pd.DataFrame(index=hours, columns=days)

# Save the dataframe as an excel file
file_path = "C:/Users/jean.juarez/Desktop/data/Projects/generate_excel_weekly/weekly.xlsx" # Replace with the path to your desired file
df.to_excel(file_path,index_label="Planning Week")

file_path