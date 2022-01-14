import time

class Robot:
    #public
    battery_level = 0
    states = ['shutown', 'running']
    name = "<unnamed>"
    #private
    __current_speed = 0
    __measured_speed = 0
    __power = False 

    def __init__(self, name):
        self.name = name

    def power_on(self):
        self.__power = True
        self.states = self.state[1]
    
    def power_off(self):
        self.__power = False
        self.states = self.state[0]

    def charge_battery(self):
        now = time.time()
        time_to_charge = now + ((100-self.battery_level)/10)
        while time.time() < time_to_charge:
            print("Batterie chargée à ",self.battery_level,"%")
        self.battery_level=100
        print("Batterie chargée")
    
    def get_measured_speed(self):
        return self.__measured_speed

    def get_current_speed(self):
        return  self.__current_speed

    def stop_robot_movement(self):
        self.__current_speed = 0 
    


    def current_stat(self):
        print("state : ", self.states , "current_speed : ",self.get_current_speed,)


        

            
