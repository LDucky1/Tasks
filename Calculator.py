class Type_check:
    def __init__(self,Input1,Input2):
        self.Input1 = Input1
        self.Input2 = Input2
    def check(self):
        global First_Value
        global Second_Value
        try:
            int(self.Input1)
            int(self.Input2)
        except:
            First_Value = float(self.Input1)
            Second_Value = float(self.Input2)
        else:
            First_Value = int(self.Input1)
            Second_Value = int(self.Input2)        

def Check_input(Input):
    global Has_operator 
    Has_operator = False
    while True:
        if ("+" in Input):
            Has_operator = True
        elif ("-" in Input):
            Has_operator = True
        elif ("x" in Input):
            Has_operator = True
        elif ("X" in Input):
            Has_operator = True
        elif ("/" in Input):
            Has_operator = True
        if Has_operator == True:
            break
        else:
            print("Syntax error")
            break   


def Check_object_validation(Input):
    global Valid
    Input = Input.replace(" ","")
    if "+" in Input:
        Input = Input.split("+")
    elif "-" in Input:
        Input = Input.split("-")
    elif "x" in Input:
        Input = Input.split("x")
    elif "X" in Input:
        Input = Input.split("X")
    elif "/" in Input:
         Input = Input.split("/")
    try:
        float(Input[0]) 
        float(Input[1])
    except:
        print("Only float/integers")
        Valid = False
    else:
        Valid = True
       

def Check_type(Input):
        Input = Input.replace(" ","")
        # global First_Value 
        # global Second_Value
        
        if "+" in Input:
            Input = Input.split("+")
            Type_check(Input[0],Input[1]).check()

        elif "-" in Input:
            Input = Input.split("-")
            Type_check(Input[0],Input[1]).check()

        elif "x" in Input:
            Input = Input.split("x")
            Type_check(Input[0],Input[1]).check()

        elif "X" in Input:
            Input = Input.split("X")
            Type_check(Input[0],Input[1]).check()

        elif "/" in Input:
            Input = Input.split("/")
            Type_check(Input[0],Input[1]).check()

        
def Answer(Input):
    if "+" in Input:
        Value = First_Value + Second_Value
    elif "-" in Input:
        Value = First_Value - Second_Value
    elif "x" in Input:
        Value = First_Value * Second_Value
    elif "X" in Input:
        Value = First_Value * Second_Value
    elif "/" in Input:
        Value = First_Value / Second_Value
    print(Value)   


while True:
    Input = str(input())
    Check_input(Input)
    if Has_operator == False:
        break
    Check_object_validation(Input)
    if Valid == False:
        break
    Check_type(Input)
    Answer(Input)
    
    



