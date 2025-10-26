def rec_fun(val,name):
        if(val == 5):
            print("stopped")
        else:
            print(f"Hello, {name}")
            rec_fun(val+1,name)

rec_fun(0,"karan")