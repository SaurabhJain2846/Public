# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:20:21 2021

@author: Saurabh Jain


Description :- Ways to attend the University with limited consecutive absents allowed
    A :- Absent
    P :- Present
Input :- Number of Days
Output :- 
    1) Ways to attend the University with no more then 2 Consecutives Absents allowed.
    2) In how many combinations student will be absent on last day.

Logic :- 
    1) For first part we have to check for all valid combination including last
     day can be both Present & Absent.
    2) For second part since we know that he is going to miss his last day so 
     do same math but with 1 day less.
Example :- 
    Number of days :- 3
    Feasible Combinations :- 
        1) For first part AAP, APA, APP, PAA, PAP, PPA, PPP ==> 7
        2) For second part feasible solutions APA, PAA, PPA ==> 3
        So for second part we just have to calculate the same but with days = 2
    Output :-
        (7, 3/7)
"""

# variable for number of days
days = int(input("Enter number of days :- "))
# variable for maximum number of consecutive A allowed between each present
limit = 2

def fun(attendance, last_a, limit, days):
    """
        This function is responsible to find out the possible combinations for 
        both above explained cases.
        Parameters :- 
            attendance :- (type ==> int)
                This is integer variable which keeps track of A, P combination 
                length which is for those days we have got valid combination.
                Start from 0
            
            last_a :- (type ==> int)
                Stores the count of a in the end of each combination & checks it 
                with permisible amount of consecutive A.
            
            limit :- (type ==> int)
                Permisible amount of consecutive Absents (A)
            
            days :- (type ==> int)
                For how many days attendance has to be there for a student.
        
        Output :- (type ==> list) (Example :- [3,7])
            1) List First Element is number of possible chances where student will miss
            last day.
            2) Second Element all possible combinations count.
    """
    
    # limit check for number of consecutive A's permitted
    if last_a == limit+1:
        return [0,0]
    if attendance == days:
        # if attendance count reached to the number of days
        # it will return list based on two condition of whether second last is A or not
        if last_a == 0:
            return [0,1]
        else:
            return [1,1]
    attendance += 1
    
    # In this it will call function considering next record is going to be A
    result_a = fun(attendance, last_a+1, limit, days)
    #In this next record is P so reset last_a counter
    result_p = fun(attendance, 0, limit, days)
    #combine the result of both paths
    return [result_a[0] + result_p[0], result_a[1] + result_p[1]]


result = fun(0,0, limit, days)

print(f"({result[1]}, {result[0]}/{result[1]})")
