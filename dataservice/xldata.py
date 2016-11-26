import xlrd


def get_xl_data(filepath):

    workbook = xlrd.open_workbook(file_contents=filepath.read())
    worksheet_names = workbook.sheet_names()

    worksheet = workbook.sheet_by_name('Sheet1')
    num_rows = worksheet.nrows
    num_cols = worksheet.ncols
    header_row = worksheet.row(0)

    #1. Check 'Escort' and 'Employee' column numbers
    emp_id_header='Employee' # main input parameter to build up the logic
    emp_cab_sno='SR NO'  # main input parameter to build up the logic
    emp_cab_num='Escort'  # main input parameter to build up the logic
    id_cell_no=-1
    sno_cell_no=-1
    cno_cell_no=-1

    # ****** to get cell number of desired column *************
    for i in range(len(header_row)):
        check_value=worksheet.cell_value(0,i)
        if check_value.upper() == emp_id_header.upper():
            id_cell_no=i
            break

    for i in range(len(header_row)):
        check_value=worksheet.cell_value(0,i)
        if check_value.upper() == emp_cab_sno.upper():
            sno_cell_no=i
            break

    for i in range(len(header_row)):
        check_value=worksheet.cell_value(0,i)
        if check_value.upper() == emp_cab_num.upper():
            cno_cell_no=i
            break
    # ******************************************************

    #print("id_cell_no :" , id_cell_no)
    #print("sno_cell_no :" , sno_cell_no)
    #print("cno_cell_no :" , cno_cell_no)

    emp_cab_details={}

    for row in range(1,num_rows):
        key=str(worksheet.cell_value(row,id_cell_no)).replace('.0','')
        if key != '':
            value1=str(worksheet.cell_value(row,sno_cell_no)).replace('.0','')
            value2=str(worksheet.cell_value(row,cno_cell_no)).replace('.0','')
            if value1!='' and value2!='':
                actual_value=[value1,value2]

            emp_cab_details[key]=actual_value
            #print(emp_cab_details)

    return emp_cab_details
