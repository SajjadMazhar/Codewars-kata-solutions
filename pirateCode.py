def amaro_plan(pirate_num):
    gold=pirate_num*20
    p_list=[gold]
    m=1
    for i in range(pirate_num-1):
        m=1-m
        if m==1:
            p_list[0]=p_list[0]-1
            p_list.append(m)
        else:
            p_list.append(m)
    return p_list
amaro_plan(56)
