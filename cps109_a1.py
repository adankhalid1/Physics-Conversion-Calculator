# -*- coding: utf-8 -*-
"""
Problem: Creating a progam which can allow the user to input values
to convert/calculate from various formulas in the physics converter calculator.
The user should allow the user to convert from kilometers per hour to meters per second
and vice versa, allow to convert from revolutions per minute to radians per second and
vice versa, and calculate final velocity, net force, time, mass, and potential energy.
My program can also allow the user to view their previous calculations as well as adding
their calculations to a text file.
My program will allow be running through a while loop which allows the user to choose
between choices of calculating, converting, checking their previous calculations,
writing their calculations to a text file, and exiting the code.
"""

#Imported math to use math.pi function for conversions/calculations
import math

def start():
    print("*****Welcome to Adan's Physics Converter Calculator*****")
    name = input("Enter your name: ") #Asking user input for their name
    print("Welcome " + name + " please enter your choice: ")
    choice = -1 #Creating variable for the condition of the while loop (use of variables)
    items = [] #Creating list for storing calculations/conversions from user
    
    #Reading constant from text file and assigning it to variable gravity (use of files for input)
    #Value of gravity is 9.8 and is used to calculate the potential energy in this program
    with open("constants.txt", "r") as file:
        for i in file:
            numbers = i.split(",")
            g = numbers[0]
            gravity = float(g)
            
    #Using a while loop to repeat my program to user and having them enter 0 to exit
    #Use of general iteration
    while choice != 0:
        #Print statements asking user to input their choice from the menu (use of print statements)
        print("")
        print("0) Exit")
        print("1) Convert from km/h to m/s or vice versa")
        print("2) Convert rev/min to rad/s or vice versa")
        print("3) Calculate final velocity given initial velocity, time, acceleration")
        print("4) Check your list of calculations/conversions")
        print("5) Calculate net force with given time and mass and vice versa")
        print("6) Calculate potential energy with given mass and height")
        print("7) Move all calculations to a calculations text file")
        print("")
        option = input("Please enter your choice of operation: ") #Storing user's input in option
        choice = int(option) #use of variables
        print("")
        
        if choice == 1:
            #Asking user to choose their option of conversion
            print("1) Value is km/h")
            print("2) Value is m/s")
            choice_1 = int(input("Please enter choice: ")) #use of variables
            print("")
            
            if choice_1 == 1:
                #Calculating the conversion from m/s to km/h by passing value to function kilometer
                kilo_value = float(input("Enter the km/h: "))
                new_kilo_value = kilometer(kilo_value)
                #Converting the calculation to a string and appending to list items
                s_new_kilo_value = str(new_kilo_value) + " m/s"
                items.append(s_new_kilo_value)
                
                print("Your value is: " + s_new_kilo_value)
                
            elif choice_1 == 2:
                #Calculating the conversion from m/s to km/h by passing value to function meter
                meter_value = float(input("Enter the m/s: "))
                new_meter_value = meter(meter_value)
                #Converting the calculation to a string and appending to list items
                s_new_meter_value = str(new_meter_value) + " km/h"
                items.append(s_new_meter_value)
                
                print("Your value is: " + s_new_meter_value)
                
            else:
                #Outputs Invalid input if user had inputted a number other than the options available
                print("Invalid input")
                
        elif choice == 2:
            #Asking user to choose their option of conversion
            print("1) Value is rev/min")
            print("2) Value is rad/s")
            choice_2 = int(input("Please enter choice: ")) #use of variables
            print("")
            
            if choice_2 == 1:
                #Calculating the conversion from rev/min to rad/s by passing value to function revolutions
                rev_value = float(input("Enter the rev/min: "))
                new_rev_value = revolutions(rev_value)
                #Converting the calculation to a string and appending to list items
                s_new_rev_value = str(new_rev_value) + " rad/s"
                items.append(s_new_rev_value)
                
                print("Your value is: " + str(new_rev_value) + " rad/s")
                
            elif choice_2 == 2:
                #Calculating the conversion from rad/s to rev/min by passing value to function radians
                rad_value = float(input("Enter the rad/s: "))
                new_rad_value = radians(rad_value)
                #Converting the calculation to a string and appending to list items
                s_new_rad_value = str(new_rad_value) + " rev/min"
                items.append(s_new_rad_value)
                
                print("Your value is: " + str(new_rad_value) + " rev/min")
                
            else:
                #Outputs Invalid input if user had inputted a number other than the options available
                print("Invalid input")
                
        elif choice == 3:
            #Asking user for inital velocity, time, and acceleration to determine the final velocity
            #Passing all user inputs to the function finalVelocity for calculation
            initial_velocity = float(input("Enter the initial velocity (m/s): "))
            time = float(input("Enter the time (s): "))
            acceleration = float(input("Enter the acceleration (m/s^2): "))
            print("")
            new_final_velocity = finalVelocity(initial_velocity, time, acceleration)
            #Converting the calculation to a string and appending to list items
            s_new_final_velocity = str(new_final_velocity) + " m/s (vf)"
            items.append(s_new_final_velocity)
            
            print("The final velocity is: " + s_new_final_velocity)
            
        elif choice == 4:
            print("Your list of calculations is: ")
            #If the list of calculations is 0 then return a print statement
            if len(items) < 1:
                print("No items in list!")
            else:
                #iterate the list of calculations through a for loop and print each calculation
                #Use of sequence iteration
                for item in items:
                    print(item)
                    
        elif choice == 5:
            #Asking user what they would like to calculate out of the options
            print("1) Calculate net force")
            print("2) Calculate mass")
            print("3) Calculate acceleration")
            choice_3 = int(input("Please enter your choice: "))
            print("")
            
            if choice_3 == 1:
                #Asking user for mass and acceleration and passing it to the function netForce to calculate net force
                f_mass_value = float(input("Enter the mass (kg): "))
                f_acceleration_value = float(input("Enter the acceleration (m/s^2): "))
                new_net_force_value = netForce(f_mass_value, f_acceleration_value)
                #Converting the calculation to a string and appending to list items
                s_new_net_force_value = str(new_net_force_value) + " N"
                items.append(s_new_net_force_value)
                
                print("Your net force is: " + s_new_net_force_value)
                
            elif choice_3 == 2:
                #Asking user for net force and acceleration and passing it to the function fMass to calculate mass
                m_net_force_value = float(input("Enter the net force (N): "))
                m_acceleration_value = float(input("Enter the acceleration (m/s^2): "))
                new_mass_value = fMass(m_net_force_value, m_acceleration_value)
                #Converting the calculation to a string and appending to list items
                s_new_mass_value = str(new_mass_value) + " kg"
                items.append(s_new_mass_value)
                
                print("Your mass is: " + s_new_mass_value)
                
            elif choice_3 == 3:
                #Asking user for mass and net force and passing it to the function fAcceleration to calculate acceleration
                a_net_force_value = float(input("Enter the net force (N): "))
                a_mass_value = float(input("Enter the acceleration (m/s^2): "))
                new_acceleration_value = fAcceleration(a_net_force_value, a_mass_value)
                #Converting the calculation to a string and appending to list items
                s_new_acceleration_value = str(new_acceleration_value) + " m/s^2"
                items.append(s_new_acceleration_value)
                
                print("Your acceleration is: " + s_new_acceleration_value)
            
            else:
                #Outputs Invalid input if user had inputted a number other than the options available
                print("Invalid input")
        
        elif choice == 6:
            #Asking the user to input mass and height and passing their inputs to the function potentialEnergy to calculate total potential energy
            p_mass = float(input("Enter the mass (kg): "))
            p_height = float(input("Enter the height (m): "))
            potential_energy = potentialEnergy(p_mass, p_height, gravity) #Passing the varialbe gravity as well where we read the constant from another file
            #Converting the calculation to a string and appending to list items
            s_potential_energy = str(potential_energy) + " J"
            items.append(s_potential_energy)
            
            print("Your total potential energy is: " + s_potential_energy)
            
        elif choice == 7:
            #If the list of calculations is 0 then return a print statement
            if len(items) < 1:
                print("No items in list!")
            else:
                #Write all of the calculations onto a text file named calculations
                #Use of files for output
                g = open("cps109_a1_output.txt", "a") #for cps109_a1_output requirement
                for item in items:
                    g.write(item + "\n") #After writing each calculation create a new line for organization purposes
                g.close()
                print("Completed!")
                
    print("Thank you for using Adan's Physics Converter Calculator")
    print("Have a good day " + name + "!")
 
#Use of user-defined functions
#Function that calculates total potential energy by multiplying mass, height and gravity
def potentialEnergy(mass, height, gravity):
    return mass * height * gravity
               
#Function that calculates acceleration by dividing net force with mass
def fAcceleration(fNet, mass):
    return fNet / mass
                
#Function that calculates mass by dividing net force with acceleration
def fMass(fNet, acceleration):
    return fNet / acceleration

#Function that calculates net force by multiplying mass and acceleration
def netForce(mass, acceleration):
    return mass*acceleration
        
#Function that calculates kilometers per hour by dividing input by 3.6
def kilometer(kilo_value):
    return kilo_value / 3.6
 
#Function that calculates meters per second by multiplying input by 3.6   
def meter(meter_value):
    return meter_value * 3.6

#Function that calculates revolutions per minute by first dividing the input value by 60, then multiplying it with 2*pi
def revolutions(rev_value):
    return (rev_value / 60) * 2*math.pi

#Function that calculates radians per second by first multiplying input value by 60, then dividing it by 2*pi
def radians(rad_value):
    return (rad_value * 60) / (2*math.pi)

#Function that calculates final velocity by multiplying acceleration with time first, then adding it with initial velocity
def finalVelocity(initial_velocity, time, acceleration):
    return (acceleration*time) + initial_velocity
        
if __name__ == "__main__":
    start()
    
    
    
