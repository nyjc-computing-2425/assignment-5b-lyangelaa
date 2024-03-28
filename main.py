# Part 1
def read_csv(filename):
    # Type your code below
    """
    This function filters out the file to separate 
    the header and data and converts the data to the 
    appopriate data type.

    Example
    >>>>>> 17
    int(17)
    """
    header = []
    data = []   
    filename = "pre-u-enrolment-by-age.csv"
    with open(filename, 'r') as f:
        header = f.readline().split(',')

        for line in f:
            details = line.strip().split(',')
            details[0] = int(details[0])
            details[3] = int(details[3])
            data.append(details)
   
    return (header, data)
# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
    """
    This function removes the sex column and returns remaining data.
    """
    enrolement_data = []
    MF = ""
    header =[]
    filename = "pre-u-enrolment-by-age.csv"
    column_index_to_remove = 2
    with open(filename, 'r') as f:
      header = f.readline().split(',')
      for line in f:
          details = line.strip().split(',')
          details[0] = int(details[0])
          details[3] = int(details[3])
          row = line.strip().split(',')
          if len(row) > column_index_to_remove:
              MF = row.pop(column_index_to_remove)
          else:
              enrolement_data.append(row)
   
    return (enrolement_data)  

# Part 3
def sum_by_year(enrolment):
    # Type your code below
    """
    This function adds total enrolment number for 10 rows as each year has 10 values and returns it as a list.

    Example
    >>>>>>1984, 8710
          1984, 2170
    [1984, 10880]

    """
    mf_enrolment = []
    header =[]
    filename = "pre-u-enrolment-by-age.csv"
    with open(filename, 'r') as f:
        header = f.readline().split(',')
        for i in range(10):
            year = None
            sum = 0
            for line in f:
                row = line.strip().split(',')
                if year is None:
                    year = int(row[0])
                    enrolment_jc = int(row[-1])
                    sum += enrolment_jc
                    mf_enrolment.append((year, sum))
                    print(mf_enrolment)
        f.seek(0)
    
    return mf_enrolment
# Part 4
def write_csv(filename, header, data):
    # Type your code below
    """
    This function writes a new file that outputs total number of lines.
    """
    mf_enrolment = []
    record = []
    filename2 = "pre-u-enrolment-by-age.csv"
    with open(filename2 , 'r') as f:
      record = f.readline().split(',')
      
      for i in range(10): 
          year = None
          sum = 0 
          for line in f: 
              row = line.strip().split(',') 
              if year is None:
                  year = int(row[0])
                  enrolment_jc = (row[-1]) 
                  sum =+ int(enrolment_jc)
          mf_enrolment.append((year, sum))
        
      f.seek(0)
          
    filename = 'total-enrolment-by-year.csv'
    header = ["year", "total_enrolment"]
    data = mf_enrolment
    with open(filename, 'w') as f:
        f.write(','.join(header) + '\n')
        for row in data:
            f.write(','.join(map(str, row)) + '\n')
    
    with open(filename, 'r') as f:
        lineswritten = len([1 for line in f])
    
    return lineswritten

  



# TESTING
# You can write code below to call the above functions
# and test the output
