# ASGURD.WORLD-PYTHON-TASK
Task 1: AWS EC2 Instance Management

Objective: I will be evaluating my proficiency in managing AWS EC2 instances using Python.

1. Importing the Necessary Libraries:
boto3: This library is used to interact with Amazon Web Services (AWS) resources, including EC2 instances.
datetime: This module is used for working with dates and times.
time: This module provides various time-related functions, including a function for introducing
2. Initializing the EC2 Client:
Here, we create an EC2 client object using Boto3. This client allows us to interact with EC2 instances and perform actions like starting and stopping them
    
    
3. Defining Instance Parameters:
In this section, you specify the parameters for launching an EC2 instance. These parameters include the Amazon Machine Image (AMI) ID, instance type, key pair name for SSH access, security group, subnet, and more. Make sure to replace the placeholders (e.g., 'your-ami-id') with your actual values.

4. Launching the EC2 Instance:
This code launches the EC2 instance using the parameters defined earlier. It then extracts the instance ID from the response and prints it to the console.
5. Defining Functions to Start and Stop the Instance:
These two functions, stop_instance and start_instance, use Boto3 to stop and start the EC2 instance, respectively. They take the instance_id as an argument and then call the appropriate EC2 API methods.

6. Configuring the Instance to Run on Specific Days and Times:
his is the main loop of the script. It runs indefinitely (you may want to implement a better exit strategy in a production environment). Inside the loop, it does the following:
Retrieves the current date and time using datetime.now().
Determines the current day of the week using now.weekday(), where 0 represents Monday, 1 represents Tuesday, and so on.
Checks if it's a Monday, Wednesday, Friday, or Sunday and if the current time is between 9:00 AM and 11:30 AM GMT.
If the conditions are met, it starts the EC2 instance using start_instance(). Otherwise, it stops the instance using stop_instance().
Sleeps for 60 seconds before checking again. This delay prevents the script from running too frequently and consuming unnecessary resources.
In summary, this script automates the management of an EC2 instance by starting it during specific days and times and stopping it during the remaining time to save costs. It continuously checks the current day and time and takes appropriate actions accordingly.

