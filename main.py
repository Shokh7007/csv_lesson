import csv
def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """
    f=open(file_name,'r')
    reader=csv.reader(f)
    a=[]
    for row in reader:
       a.append(row)
    return a 
print(get_country_column('data.csv'))