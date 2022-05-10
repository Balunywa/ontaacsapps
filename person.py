class Person:
  def __init__(taacs, first_name, second_name, age, time_in, time_out):
    taacs.first_name = first_name
    taacs.second_name = second_name
    taacs.age = age
    taacs.time_in = time_in
    taacs.time_out = time_out

  def gate_pass_time_in(taacs):
      taacs.first_name = input("Enter First_Name")
      taacs.age = int(input("Enter Your_Age"))
      taacs.time_in = input('Enter the Time_In')

      print("Welcome " + taacs.first_name)
      if(taacs.age < 40 ):
          print("You have discount of 30%")
      elif (taacs.time_in < "7:00 PM"):
          print("You have WON!!! a CUPON!! for keeping time")
          print("CUPON120")
      else:
          print("Keep Time and WIN Cupons!")

person_one=Person("Lukman", "Balunywa", 34, "10:40 AM", "12:00 PM")
person_one.gate_pass_time_in()

#person_two=Person("Lukman", "Balunywa", 34, "10:40 AM", "12:00 PM")
#person_two.gate_pass_time_in()


















