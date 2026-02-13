# nested function:
def outer():
  print("outer")
  def inner():
    print("inner")
  inner()
  
# outer()

#------------
# function can return another function
def outer1():
  print("outer")
  def inner():
    print("inner")
  return inner

# outer1()()

#------------------------
# function body can be hold into variable

def outer2():
  print("outer")
  def inner():
    print("inner")
  return inner

# inner_func = outer2()
# inner_func()

# -----------------------
def stu_pass(marks):
  print(f"Congratulations! you have passed with {marks} marks!")
  
def stu_fail(marks):
  print(f"Sorry! you have failed with {marks} marks!")
  
def send_emails(marks):
  print(f"Sending result over emails : {marks} : status: PASS")
  
def send_sms(marks):
  print(f"Sending result over sms : {marks} : status: FAILED")
  
# higher order function: 
def calc_result(mrk,pass_result,fail_result):
  if(mrk >= 40):
    pass_result(mrk)
  else:
    fail_result(mrk)
    
# Invoking function based on users choice : how to inform result: via email/ SMS, in person

marks = int(input('Enter your marks: '))    
calc_result(marks, stu_pass, stu_fail)
calc_result(marks, stu_pass, stu_fail)

calc_result(marks, send_emails, send_sms)
calc_result(marks, send_emails, send_sms)
