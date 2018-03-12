# Air Cargo Planning Search 
Implement domain-independent search technique to solve deterministic logistics planning problems for an Air Cargo transport system using a planning search agent. Unlike the navigation problem, there is no simple distance heuristic to aid the agent.

![Progression Search](images/Progression.PNG)

# Install
- This project run on **Python 3.5**
- Install the require packages using the following script
```
pip install -r requirements.txt
```

# Run the experiments
- Run the following script to experiement `problem 2` and `search method 8`
```
python run_search.py -p 2 -s 8
```
- For more search method
```
python run_search.py -h
```
# Defining the problems
## Problem 1
- Init state
```
Init(At(C1, SFO) ∧ At(C2, JFK) 
	∧ At(P1, SFO) ∧ At(P2, JFK) 
	∧ Cargo(C1) ∧ Cargo(C2) 
	∧ Plane(P1) ∧ Plane(P2)
	∧ Airport(JFK) ∧ Airport(SFO))
```
- Goal state
```
Goal(At(C1, JFK) ∧ At(C2, SFO))
```
## Problem 2
- Init state
```
Init(At(C1, SFO) ∧ At(C2, JFK) ∧ At(C3, ATL) 
	∧ At(P1, SFO) ∧ At(P2, JFK) ∧ At(P3, ATL) 
	∧ Cargo(C1) ∧ Cargo(C2) ∧ Cargo(C3)
	∧ Plane(P1) ∧ Plane(P2) ∧ Plane(P3)
	∧ Airport(JFK) ∧ Airport(SFO) ∧ Airport(ATL))
```
- Goal state
```
Goal(At(C1, JFK) ∧ At(C2, SFO) ∧ At(C3, SFO))
```