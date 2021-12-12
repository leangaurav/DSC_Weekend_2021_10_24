

#while True:
#   try:
#       x = int(input())
#   except BaseException as err: # equivalent to writing except:
#       print("no way out", type(err), err)
#       


while True:
    try:
        x = int(input())
    except Exception as err: # equivalent to writing except:
        print("there's aa way out", type(err), err)
        
    except KeyboardInterrupt:
        print("Exiting due to keyboard interrupt")
        break
