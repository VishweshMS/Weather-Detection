import tkinter
from tkinter import * 
from tkinter import messagebox 
import datetime
import requests, json 


def tell_weather() : 


    city_name = city_field.get() 


	
    complete_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=2312fc43926390ce3ab84e594a7c2df8&units=metric'.format(city_name)

	
    response = requests.get(complete_url) 

	
    x = response.json() 

	


    if x['cod'] != "404" :
        current_temperature = x['main']['temp'] 

		
        current_pressure = x['main']["pressure"] 

		
        current_humidiy = x['main']["humidity"] 
        ccity=x['name']

        wind_speed=x['wind']['speed']
        lon=x['coord']['lon']
        lat=x['coord']['lat']
        feels_like=x['main']['feels_like']
       
        visibility=x['visibility']
        wind_deg=x['wind']['deg']
        sunrise=x['sys']['sunrise']
        sunset=x['sys']['sunset']
        

		
        z = x["weather"] 

		
        weather_description = z[0]["description"] 
        



		
        temp_field.insert(15, str(current_temperature) + " Celsius") 
        atm_field.insert(10, str(current_pressure) + " hPa") 
        humid_field.insert(15, str(current_humidiy) + " %") 
        desc_field.insert(10, str(weather_description) ) 
        ccity_field.insert(10, str(ccity) )
        lon_field.insert(10, str(lon) )
        lat_field.insert(10, str(lat) )
        feels_field.insert(10, str(feels_like) + " Celsius")
        visibility_field.insert(10, str(visibility) +" meters")
        speed_field.insert(10, str(wind_speed) +" Miles/hour")
        deg_field.insert(10, str(wind_deg) )
        sunrise_field.insert(10, str(datetime.datetime.fromtimestamp(sunrise).isoformat()) )
        sunset_field.insert(10, str(datetime.datetime.fromtimestamp(sunset).isoformat()) )


    else : 

		
    		messagebox.showerror("Error", "City Not Found \n"
							"Please enter valid city name") 

		# clear the content of city_field entry box 
    		city_field.delete(0, END) 



def clear_all() : 
    city_field.delete(0, END) 
    temp_field.delete(0, END) 
    atm_field.delete(0, END) 
    humid_field.delete(0, END) 
	
    desc_field.delete(0, END) 
    

    ccity_field.delete(0, END) 
    lon_field.delete(0, END) 
    lat_field.delete(0, END) 
    feels_field.delete(0, END) 
    visibility_field.delete(0, END) 
    speed_field.delete(0, END) 
    deg_field.delete(0, END) 
    sunrise_field.delete(0, END) 
    sunset_field.delete(0, END) 

	# set focus on the city_field entry box 
    city_field.focus_set() 


# Driver code 
if __name__ == "__main__" : 

	# Create a GUI window 
    root = Tk() 

	
    root.title("Real Time Weather Detection") 

	
    root.configure(background = "light blue") 

	
    root.geometry("705x375") 

	
    headlabel = Label(root, text = "Weather Gui Application", 
					fg = 'black', bg = 'light blue') 
	
	
    label1 = Label(root, text = "City name : ", 
				fg = 'black', bg = 'light blue') 
	
	
    label2 = Label(root, text = "City :", 
				fg = 'black', bg = 'light blue') 

	
    label3 = Label(root, text = "Longitude :", 
				fg = 'black', bg = 'light blue') 

	
    label4 = Label(root, text = "Latitude :", 
				fg = 'black', bg = 'light blue') 

	
    label5 = Label(root, text = "Temperature :", 
				fg = 'black', bg = 'light blue') 
    
    label6 = Label(root, text = "Feels like :", 
				fg = 'black', bg = 'light blue') 
    
    label7 = Label(root, text = "atm Pressure :", 
				fg = 'black', bg = 'light blue') 
     
    label8 = Label(root, text = "Humidity :", 
				fg = 'black', bg = 'light blue') 
      
    label9 = Label(root, text = "Description :", 
				fg = 'black', bg = 'light blue') 
       
    label10 = Label(root, text = "Visibility :", 
				fg = 'black', bg = 'light blue') 
        
    label11 = Label(root, text = "Wind Speed :", 
				fg = 'black', bg = 'light blue') 
         
    label12 = Label(root, text = "Wind Degree :", 
				fg = 'black', bg = 'light blue') 
          
    label13 = Label(root, text = "Sunrise :", 
				fg = 'black', bg = 'light blue') 
           
    label14 = Label(root, text = "Sunset :", 
				fg = 'black', bg = 'light blue') 
 
    
    headlabel.grid(row = 0, column = 1) 
    label1.grid(row = 1, column = 0, sticky ="E") 
    label2.grid(row = 3, column = 0, sticky ="E") 
    
    label3.grid(row = 4, column = 0, sticky ="E") 
    label5.grid(row = 6, column = 0, sticky ="E") 
    label6.grid(row=7,column=0,sticky="E")
    label7.grid(row = 8, column = 0, sticky ="E") 
    label8.grid(row = 9, column = 0, sticky ="E") 
    label9.grid(row = 10, column = 0, sticky ="E") 
    label10.grid(row = 11, column = 0, sticky ="E") 
    label11.grid(row = 12, column = 0, sticky ="E") 
    label12.grid(row = 13, column = 0, sticky ="E") 
    label13.grid(row = 14, column = 0, sticky ="E") 
   
    label14.grid(row = 15, column = 0, sticky ="E") 
    label4.grid(row = 5, column = 0, sticky ="E") 

  


	
    city_field = Entry(root) 
    ccity_field= Entry(root)
    lon_field= Entry(root)
    lat_field= Entry(root)
    temp_field = Entry(root) 
    feels_field= Entry(root)
    atm_field = Entry(root) 
    humid_field = Entry(root) 
    desc_field = Entry(root) 
  


    visibility_field= Entry(root)
    speed_field= Entry(root)
    deg_field= Entry(root)
    sunrise_field= Entry(root)
    sunset_field= Entry(root)
	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	# ipadx keyword argument set width of entry space . 
 
city_field.grid(row = 1, column = 1, ipadx ="195") 
    
temp_field.grid(row = 6, column = 1, ipadx ="195") 
    
atm_field.grid(row = 8, column = 1, ipadx ="195") 
    
humid_field.grid(row = 9, column = 1, ipadx ="195") 
    
desc_field.grid(row = 10, column = 1, ipadx ="195") 
    
ccity_field.grid(row = 3, column = 1, ipadx ="195") 
lon_field.grid(row = 4, column = 1, ipadx ="195") 
lat_field.grid(row = 5, column = 1, ipadx ="195") 
feels_field.grid(row = 7, column = 1, ipadx ="195") 
visibility_field.grid(row = 11, column = 1, ipadx ="195") 
speed_field.grid(row = 12, column = 1, ipadx ="195") 
deg_field.grid(row = 13, column = 1, ipadx ="195") 
sunrise_field.grid(row = 14, column = 1, ipadx ="195") 
sunset_field.grid(row = 15, column = 1, ipadx ="195") 

	
    
button1 = Button(root, text = "Submit", bg = "dark blue", 
					fg = "white", command = tell_weather) 

	
    
button2 = Button(root, text = "Clear", bg = "dark blue", 
					fg = "white", command = clear_all) 

	
    
button1.grid(row = 2, column = 1) 
    
button2.grid(row = 16, column = 1) 
	
	# Start the GUI 
    
root.mainloop() 
