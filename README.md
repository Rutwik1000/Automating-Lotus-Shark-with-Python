# Automating-Lotus-Shark-with-Python
![py banner 3](https://user-images.githubusercontent.com/116753318/204351676-24f87dd4-8f5d-488f-be24-560e17f39f97.jpg)

# What is Lotus Shark?
The Lotus Suspension Analysis SHARK module is a suspension geometric and kinematic modelling tool, with a user- friendly interface which makes it easy to apply changes to proposed geometry and instantaneously assess their impact through graphical results.

![car](https://user-images.githubusercontent.com/116753318/204351865-13686746-204a-4895-b7e6-eca29aca79e4.jpg)
The graphic above shows the plan view of the suspension system of a Race car.


![adams plan view](https://user-images.githubusercontent.com/116753318/204351941-4a3d9c2a-5c1e-4f4d-a532-bf45fceb1b39.gif)
The above graphic shows plan View of the Suspension and Steering systems of a Race car in MSC Adams Software.

# How Lotus Shark works?
> - The Lotus Shark takes parameters of vehicle as input to like Wheelbase, Wheeltrack, Mass, Hardpoints, etc.<br />
> - The geometry of the suspension system can be changed to achieve the desired goals by changing the hardpoints.

![487789_1_En_80_Fig1_HTML](https://user-images.githubusercontent.com/116753318/204352186-288c6c55-982d-43c9-bf04-9c8de4ab2ca5.png)
The green circles surrounded by red boxes illustrate the Hardpoints of Suspension System.

For example, the mount where Shock absorber is connected to the chassis is a hardpoint. Similarly, ‘Wheel Centre’ is the point about which the wheel rotates is also a hardpoint.

# Algorithm:
The Algorithm scrapes data from Lotus Shark software and outputs optimal hardpoints coordinates in the specified range.

![Lotus Shark](https://user-images.githubusercontent.com/116753318/204352352-32b5c97f-9276-4145-b891-016797542ff2.gif)

The algorithm uses ‘Hit and Trial’ method to get the required results. The targets quantified into range of coordinates by the user

![Lotus Shark Flow Chart](https://user-images.githubusercontent.com/116753318/204352486-2a6cb220-715d-4800-8125-00919f54b0df.png)


# Libraries Used:
> 1. random-To Generate Random Coordinates.
> 2. time- To Delay the Program.
> 3. Pyautogui-To perform Clicking.	
> 4. shutil -To Manipulate Files.
> 5. openpyxl -To Manipulate csv files.	
> 6. os- To Manipulate Files

# Demo

![Automation with Python2](https://user-images.githubusercontent.com/116753318/204353177-fe2535f1-be5e-4b5d-8af1-2069ee5d7049.gif)
