from re import X
import EmployeeClass as ec
import PayRollDeductionClass as pdc
from tabulate import tabulate

employee1=ec.Employee('Jimmy Smith','58475','Information Systems','Developer','6800')

info={'Description':['food court', 'gift contribution','vending machine'],
'Date': ['8/14/2022','8/12/2022','8/17/2022','8/22/2022','8/5/2022'],'Charge_Amount':['22.50','25.00','15.25','3.00','2.75'],
'ID':['39119','58475','21547']}

payded1=pdc.PayRollDeduction(info['Description'][0], info['Date'][0],info['Charge_Amount'][0],info['ID'][0])
payded2=pdc.PayRollDeduction(info['Description'][1], info['Date'][1],info['Charge_Amount'][1],info['ID'][1])
payded3=pdc.PayRollDeduction(info['Description'][0], info['Date'][2],info['Charge_Amount'][2],info['ID'][2])
payded4=pdc.PayRollDeduction(info['Description'][2], info['Date'][3],info['Charge_Amount'][3],info['ID'][1])
payded5=pdc.PayRollDeduction(info['Description'][2], info['Date'][4],info['Charge_Amount'][4],info['ID'][1])

#tables printed

table1=[['Name','ID Number','Department', 'Job Title','Monthly Salary'],
['Jimmy Smith','58475','Information Systems','Developer','6800']]


table2=[['Description','Date','Charge Amount', 'Job Title', 'ID Number'],['food court', '8/14/2022','22.50','39119'],
['gift contribution', '8/12/2022','25.00','58475'],['food court', '8/17/2022','15.25','21547'],['vending machine', '8/22/2022','3.00','58475'],
['vending machine', '8/5/2022','2.75','58475']]


print(tabulate(table1,headers='firstrow',tablefmt='fancy_grid'))
print(tabulate(table2,headers='firstrow',tablefmt='fancy_grid'))

#employee pay recipt
print('*** Employee Pay ***')
print('Name: ',employee1.get_name())
print('ID Number: ',employee1.get_id())
print('Department: ',employee1.get_department())
print('Gross Pay: ',"${:,.2f}".format(float(employee1.get_salary())))
print('Net Pay: ', "${:,.2f}".format((float(employee1.get_salary()))-(float(payded2.get_chrg()))-(float(payded4.get_chrg()))-(float(payded5.get_chrg()))))