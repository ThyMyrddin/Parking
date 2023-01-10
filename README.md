# ParkingManagement
Empty parking place detection and management

You need :

    -RaspberryPi

    -Obstacle detector

    -I2C

    -Servo moteur
    
    -Camera
    
    -LED lights (Red , Green)

Steps to use the code :

    1- Run 'Park_Python/select.py' in raspberry ( select the places u want to process by draggin the cursor after clicking down and creating a rectangle then button up )
    
    2- Set hostname and port in 'server.py' and 'Park_Python/main.py'
    
    3- Run 'server.py' and the React App in a computer
    
    4- Run 'Park_Python/main.py' in raspberry
