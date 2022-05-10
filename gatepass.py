class GatePass:
    def __init__(taacs, time_out,time_back, car_plates, emergency_phone):
        taacs.time_out = time_out
        taacs.time_back = time_back
        taacs.car_plates = car_plates
        taacs.emergency_phone = emergency_phone

    def Time_Out (taacs):

        taacs.time_out = input("Enter Time_Out!! \n")
        taacs.car_plates = input("Enter The Car Number_Plates \n")
        taacs.emergency_phone = input("Enter The Emergency Phone Number \n")
        car_number = taacs.car_plates
        SoS_Number = taacs.emergency_phone
        if taacs.time_out == '6:00' or taacs.time_out > '6:00':
            print("Pass Granted Safe Journey & Don't For Get That Gates Close AT 3:00_AM !!")
            print("This is the Car Number_Plate that Took You!! " + car_number + " This is the Emergency Nuber " + SoS_Number)
        elif taacs.time_out < '6:00':
            print("We Open Gates at 6:00_AM")
        else:
            print("Enter the Right Time Format")

    def Time_Back(taacs):

        taacs.time_back = input("Enter Time_Back!! \n")
        taacs.car_plates = input("Enter The Car Number_Plates \n")
        car_number = taacs.car_plates
        if taacs.time_back == '12:00' or taacs.time_back < '12:00':
            print("Pass Granted! Welcome Back & Don't For Get That Gates Open AT 6:00_AM !!")
            print("This is the Car Number_Plate that You Returned In!! " + car_number)
        elif taacs.time_back == '3:00' or taacs.time_back > '3:00' :
            print("Our Gates Are Closed At 3:00_AM For Security Reasons Please Return Tomorrow Before 3:00_AM")
        else:
            print("Enter the Right Time Format")

person=GatePass("", "", " ", "")
print(person.Time_Out())
print(person.Time_Back())

