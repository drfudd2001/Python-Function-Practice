# Functional Prompt:

def flatten_sort_list(in_list, sort = True):
    result = list()
    for i in in_list:
        if not isinstance(i, list): result.append(i)
        else: result += flatten_sort_list(i, False)
    return result if not sort else sorted(result)

print(flatten_sort_list([3,4,[1,2,[9]]]))

'''
Make sure to answer the following questions about your coding process:
How does this solution ensure data immutability?

By never changing the values of any of the list's items.

Is this solution a pure function? Why or why not?

Yes, because the argument they accept determines their return value.

Is this solution a higher order function? Why or why not?

Yes, since it invokes a different function within itself.

Would it have been easier to solve this problem using a different programming style?

No. Because the result is only dependent on one variable, it was easier to make the variables immutable in this situation.
There was no need for "impure" functions.

Why in particular is functional programming a helpful paradigm when solving this problem?

This prompt demands a straightforward answer based on a single variable.
In this scenario, functional programming makes the most sense because we don't have to worry about outside modifiers influencing our outcomes.

'''

# OOP Prompt:

from enum import Enum
class Condition(Enum):
    PERFECT = 1
    REPAIRED = 2
    TRASHED = 3

class Podracer:
    def __init__(self,
        in_speed: int = 1,
        in_cond: Condition = Condition.PERFECT) -> None:

        self.max_speed = in_speed
        self.condition = in_cond
        
    def reapir(self) -> None:
        self.condition = Condition.REPAIRED

class AnakinsPod(Podracer):
    def __init__(self,
        in_speed: int = 1,
        in_cond:Condition = Condition.PERFECT) -> None:

        super().__init__(in_speed, in_cond)
    
    def boost(self) -> None:
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def __init__(self,
        in_speed: int = 1,
        in_cond: Condition = Condition.PERFECT) -> None:

        super().__init__(in_speed, in_cond)
    
    def flame_jet(self, other_pod: Podracer) -> None:
        other_pod.condition = Condition.TRASHED

pod = Podracer(1, Condition.TRASHED)
print(f"New podracer made with speed {pod.max_speed}kph and condition `{pod.condition}`")
pod.reapir()
print(f"We have now fixed the pod. It is now {pod.condition}")

new_pod = AnakinsPod(2, Condition.PERFECT)
print(f"Anakin's pod has speed {new_pod.max_speed}kph and is `{new_pod.condition}`")
new_pod.boost()
print(f"Anakin's pod now goes {new_pod.max_speed}kph")

third_pod = SebulbasPod()

third_pod.flame_jet(new_pod)
print(f"Sebulba's pod has {new_pod.condition} Anakin\'s pod!")

'''
Make sure to answer the following prompts about your coding experience:
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

It employs encapsulation and abstraction by hiding methods and variables within each class so that they do not need to be specified outside of the classes.
When we call the Podracer class characteristics within the other classes, inheritance comes into play.
Because we are not altering any methods or properties in the other classes, polymorphism is not truly employed.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

No. Without the classes, we'd have to add a lot more variables to keep track of identical attributes.

How in particular did Object Oriented Programming assist in the solving of this problem?

It simplified our code by eliminating the requirement to redefine equivalent variables and methods for each podracer.

'''