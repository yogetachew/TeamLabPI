# TeamLabPI
This is team lab assignments for data structure class.

<b>Table of Content</b>
- [Summary](#summary)
- [Console Output Example](#console-output-example)
- [Team Members](#member rosters)

## Summary
This project simulates how a busy airport terminal manages and processes events like arrivals, gate changes, and boarding calls. The system’s core engine handles these events in order, allows undoing previous actions, and maintains an editable roster of passengers or tasks. The output of the project should show the changes make to the passengers' rosters.


## Console Output Testing Correct Example
```
Processing Event: {'type': 'arrive', 'name': 'Ana'}
Current Roster: Ana

Processing Event: {'type': 'arrive', 'name': 'Ben'}
Current Roster: Ana -> Ben

Processing Event: {'type': 'insert', 'name': 'Cam', 'index': 1}
Current Roster: Ana -> Cam -> Ben

Processing Event: {'type': 'arrive', 'name': 'Dia'}
Current Roster: Ana -> Cam -> Ben -> Dia

Processing Event: {'type': 'insert', 'name': 'Eli', 'index': 2}
Current Roster: Ana -> Cam -> Eli -> Ben -> Dia

Processing Event: {'type': 'remove', 'index': 0}
Current Roster: Cam -> Eli -> Ben -> Dia

Processing Event: {'type': 'remove', 'index': 2}
The error is Bounds' index is out of box
Current Roster: Cam -> Eli -> Ben -> Dia

Current Roster: Cam -> Eli -> Ben -> Dia

Processing Event: {'type': 'arrive', 'name': 'Fay'}
Current Roster: Cam -> Eli -> Ben -> Dia


Processing Event: {'type': 'arrive', 'name': 'Fay'}
Current Roster: Cam -> Eli -> Ben -> Dia -> Fay

Processing Event: {'type': 'insert', 'name': 'Gia', 'index': 1}
Current Roster: Cam -> Gia -> Eli -> Ben -> Dia -> Fay

Final Roster: Cam -> Gia -> Eli -> Ben -> Dia -> Fay

```

## Team Members
[@confidenceaffang](https://github.com/confidenceaffang) Confidence Affang
[@yogetachew](https://github.com/yogetachew)  Yonatan Getachew
[@Philipine26](https://github.com/Philipine26) Philipine Andjawo

