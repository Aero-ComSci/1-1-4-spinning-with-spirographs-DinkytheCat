1. loops.py shows two loops, one that never runs becasue it only runs when N is above 0 but it is 0 so its never going to run. The second loop is always true so it will keep printing forver.
![image](https://github.com/user-attachments/assets/d5ee526e-0e3c-4a23-96ed-8c51e3c7de7a)

2. The pixels sets the screen to be unresizeable and makes it 800 width and height. It inputs the amount of shapes the person want to draw with a maximum of 5 and then makes a variable that is the total amount of units the circles will take up by multipling the shape diameter by the amount of shapes. Then it finds the total units of spacing the program has available and then uses the formula ```python x = -screen_width / 2 + (i + 1) * spacing_between_shapes + i * 50``` to find the spacing between the edges and the actual shapes to be the same.
   ![image](https://github.com/user-attachments/assets/3f98bbd1-36aa-4ecc-8f28-3477e64eb2ed)
   ![image](https://github.com/user-attachments/assets/09c97800-8352-4be8-9800-c8ad26557649)


3. The program has a function called square that runs 4 times to create perfect matching concentric squares in all 4 quadrents of the turtle screen. It has a loop that will draw a square and then once it goes back to the same place it starts it will move a set amount of distance and draw a square again but it will be bigger. Each time it draws the square it also changes the color of the pen by going through a list of colors.
   ![image](https://github.com/user-attachments/assets/526d15d1-74a0-4808-9300-521f0e6b75d6)
