command = ""
started = True
while True:
    command = input(">").lower()
    """
    需求：初始设置started为True;
					获取command的输入值，有5种情况
            1：command == 'start',进入条件1 command == "start": 
                  满足此条件会先判断started 如果started为True 即car is already started!
            2：command == 'stop',进入条件1 command == "stop": 
									在满足command为stop，判断started，started为True，就要把started设置为False，
                  并输出Car is stopped，否则car is already stopped!
            3：ommand == "help": # 条件3  打印一句话 
            4：command == "quit": # 条件4 结束循环
            5：未匹配到想要的数据， 输出异常信息
    """
    if command == "start":  # 条件1
        if started:
            print("car is already started!")
            print(str(started))
        else:
            started = True
            print("car started...")
            print(str(started))
    elif command == "stop":  # 条件2
        if started:
            started = False
            print("Car is stopped")
            print(str(started))
        else:
            print("car is already stopped!")
            print(str(started))
    elif command == "help":  # 条件3
        print(
            """start - to start the car stop- to stop the car quit-to guit""")
    elif command == "quit":  # 条件4
        break
    else:  # 条件5
        print("sorry,I don't understand that...")
