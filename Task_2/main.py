
def build_bridge(chunk,goal):
    plate_pcs = 0
    connect_pcs = 0
    goal_temp = 0
    connect = chunk / 2
    
    if goal/chunk > 1:
        plate_pcs += 1
        goal_temp = chunk
    elif goal/chunk == 1:
        print("\nMożemy zbudować most z podanych elementów")
        return True
    else:
        return False

    while goal/goal_temp>1:
        plate_pcs += 1
        connect_pcs += 1
        goal_temp = goal_temp + chunk + connect
        if goal/goal_temp == 1:
            print("\nMożemy zbudować most z podanych elementów")
            return True
        elif goal/goal_temp < 1:
            print("\nPrzykro mi, nie możemy zbudować mostu z podanych elementów")
            return False
        
print(build_bridge(2,20))

"""kod kodilla - 'troszkę' krótszy, powyższy oblicza okrężną drogą :(
def build(chunk, goal):
  junction = chunk / 2
  x = (goal + (junction * 1))/(chunk + junction)
  return True if x.is_integer() else False
 
print(build(2,20))
"""