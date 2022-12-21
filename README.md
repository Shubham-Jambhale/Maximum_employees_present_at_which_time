# Maximum_employees_present_at_which_time

# Question

A timesheet is maintained for employees containing the clock in and clock out times. Given
a clock in and clock out times lists, find the points where maximum employees are present in
the company and return the tuple (a,b) where a represents the max no of employees and b
represents the count of no of such points (i.e. times). Note that if clock in and clock out time
coincides, the clock in time is preferred over the clock out time. Expected time complexity:
O(nlogn) where n represents the total no of employees in the company. Do not use the built in
python sort method.


# Example 1

Input:

clock in times = [1, 2, 4, 7, 8, 12] clock out times = [3, 7, 8, 12, 10, 15 ]

Explanation:

![image](https://user-images.githubusercontent.com/40384748/208822633-b36a8ce6-28d1-4f46-ba75-63b3248f2b98.png)

Maximum no of employees are 3 at time points 7 and 8, Therefore the output
to be returned is Output: (3, 2)
