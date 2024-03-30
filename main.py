# Part 1
def read_csv(filename):
    # Type your code below
    """
    Separates header of file as a list.
    """
    header = []
    data = []   
    filename = "pre-u-enrolment-by-age.csv"
    with open(filename, 'r') as f:
        header = f.readline().strip().split(',')

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
    Returns remaining data as a nested list after removing the sex column.

    Example
    >>>>>>
    [[1984, '17 YRS', 8710],
     [1984, '18 YRS', 3927],
     [...],
     [...],
     ...]
    """
    enrolement_data = []
    sex = "MF"
    header =[]
    filename = "pre-u-enrolment-by-age.csv"
    with open(filename, 'r') as f:
      header = f.readline().split(',')
      for line in f:
          details = line.strip().split(',')
          details[0] = int(details[0])
          details[3] = int(details[3])
          record = line.strip().split(',')
          for record in f:
              if record[2] == sex:
                  enrolement_data = [record[0], record[1], record[3]]
                  enrolement_data.append([record])
    return (enrolement_data)  

# Part 3
def sum_by_year(enrolment):
    # Type your code below
    """
    Returns total enrolment number for each year as a list.

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
    Returns total number of lines in file
    """
    enrolement_data = []
    sex = "MF"
    header =[]
    filename2 = "pre-u-enrolment-by-age.csv"
    with open(filename2, 'r') as f:
      header = f.readline().split(',')
      for line in f:
          details = line.strip().split(',')
          details[0] = int(details[0])
          details[3] = int(details[3])
          record1 = line.strip().split(',')
          for record1 in f:
              if record1[2] == sex:
                  enrolement_data = [record1[0], record1[1], record1[3]]
    enrolement_data.append([record1])
    
    mf_enrolment = []

    new_row = [None, None] 
    for line in enrolement_data: 
        record = line
        year = int(record[0][0])
        enrolment = int(record[0][-2])

        if new_row[0] is None:
                new_row = [year, enrolment]
        elif year != new_row[0]:
                mf_enrolment.append(new_row)
                new_row = [year, enrolment]
        else:
                new_row[1] = int(new_row[1]) + enrolment
     

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
