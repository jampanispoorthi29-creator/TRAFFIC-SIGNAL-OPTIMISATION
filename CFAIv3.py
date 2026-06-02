# ==========================================
# SMART TRAFFIC SIGNAL OPTIMIZATION SYSTEM
# ==========================================

TRAFFIC_DATA = {

    "Low Traffic": {
        "vehicles": 12,
        "waiting": 8
    },

    "Medium Traffic": {
        "vehicles": 35,
        "waiting": 18
    },

    "High Traffic": {
        "vehicles": 57,
        "waiting": 31
    },

    "Emergency Vehicle": {
        "vehicles": 20,
        "waiting": 5
    }
}


# ==========================================
# CO2 : GREEDY SEARCH
# ==========================================

def greedy_signal_selection(priority_score):

    if priority_score > 120:
        return 60

    elif priority_score > 60:
        return 40

    else:
        return 20


# ==========================================
# CO3 : CONSTRAINT SATISFACTION
# ==========================================

def check_constraints(signal_time):

    if signal_time <= 60:
        return "✓ Signal Time Constraint Satisfied"

    return "✗ Signal Time Constraint Violated"


# ==========================================
# CO4 : DECISION MAKING AGENT
# ==========================================

def traffic_agent(state):

    data = TRAFFIC_DATA[state]

    vehicles = data["vehicles"]
    waiting = data["waiting"]

    priority_score = (vehicles * 2) + waiting

    if state == "Emergency Vehicle":

        signal_time = 60
        decision = "Emergency Override Activated"

    else:

        signal_time = greedy_signal_selection(priority_score)

        if signal_time == 60:
            decision = "Heavy Congestion Detected"

        elif signal_time == 40:
            decision = "Moderate Traffic Flow"

        else:
            decision = "Normal Traffic Flow"

    print("\n====================================")
    print("SMART TRAFFIC SIGNAL OPTIMIZATION")
    print("====================================")

    print("Current State :", state)

    print("\nTraffic Data")
    print("----------------------------")
    print("Vehicle Count :", vehicles)
    print("Waiting Time  :", waiting)

    print("\nAI Reasoning")
    print("----------------------------")
    print("Priority Score =", priority_score)

    print("\nDecision")
    print("----------------------------")
    print(decision)

    print("\nSignal Timing")
    print("----------------------------")
    print(signal_time, "seconds")

    print("\nConstraint Check")
    print("----------------------------")
    print(check_constraints(signal_time))

    print("\nState Transition")
    print("----------------------------")

    if state == "Low Traffic":
        print("Low Traffic -> Medium Traffic")

    elif state == "Medium Traffic":
        print("Medium Traffic -> High Traffic")

    elif state == "High Traffic":
        print("High Traffic -> Emergency Vehicle")

    else:
        print("Emergency Vehicle -> Normal Traffic")


# ==========================================
# CUSTOM ANALYSIS
# ==========================================

def custom_traffic_analysis():

    print("\nCUSTOM TRAFFIC ANALYSIS")

    vehicles = int(input("Enter Vehicle Count : "))
    waiting = int(input("Enter Waiting Time  : "))

    if vehicles > 50:

        state = "High Traffic"

    elif vehicles > 25:

        state = "Medium Traffic"

    else:

        state = "Low Traffic"

    priority_score = (vehicles * 2) + waiting

    signal_time = greedy_signal_selection(priority_score)

    if signal_time == 60:
        decision = "Heavy Congestion Detected"

    elif signal_time == 40:
        decision = "Moderate Traffic Flow"

    else:
        decision = "Normal Traffic Flow"

    print("\n====================================")
    print("CUSTOM TRAFFIC RESULT")
    print("====================================")

    print("Traffic Type :", state)

    print("\nTraffic Data")
    print("----------------------------")
    print("Vehicle Count :", vehicles)
    print("Waiting Time  :", waiting)

    print("\nAI Reasoning")
    print("----------------------------")
    print("Priority Score =", priority_score)

    print("\nDecision")
    print("----------------------------")
    print(decision)

    print("\nSignal Timing")
    print("----------------------------")
    print(signal_time, "seconds")

    print("\nConstraint Check")
    print("----------------------------")
    print(check_constraints(signal_time))


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n====================================")
    print("SMART TRAFFIC SIGNAL OPTIMIZATION")
    print("====================================")
    print("1. Low Traffic")
    print("2. Medium Traffic")
    print("3. High Traffic")
    print("4. Emergency Vehicle")
    print("5. Custom Traffic Analysis")
    print("6. Exit")
    print("====================================")

    choice = input("Enter Choice : ")

    if choice == "1":

        traffic_agent("Low Traffic")

    elif choice == "2":

        traffic_agent("Medium Traffic")

    elif choice == "3":

        traffic_agent("High Traffic")

    elif choice == "4":

        traffic_agent("Emergency Vehicle")

    elif choice == "5":

        custom_traffic_analysis()

    elif choice == "6":

        print("\nProgram Ended Successfully.")
        break

    else:

        print("\nInvalid Choice. Please Try Again.")