""" Class for each student in the MATHCOUNTS Program. """
class Student:
    name: str # Name of each student
    grade: str # Grade of each student
    score: str # Score of each student
    warmup_score = 0 # Cumulative score on warm-ups
    target_score = 0 # Cumulative score on target rounds
    sprint_score = 0 # Cumulative score on sprint rounds
    total_score = 0 # Cumulative score