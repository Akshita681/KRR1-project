from pyswip import Prolog

prolog = Prolog()
prolog.consult("career_rules.pl")

def decide_career(interest, skill, preference):
    # Clear old facts
    prolog.retractall("interest(_)")
    prolog.retractall("skill(_)")
    prolog.retractall("preference(_)")

    # Add new facts
    prolog.assertz(f"interest({interest})")
    prolog.assertz(f"skill({skill})")
    prolog.assertz(f"preference({preference})")

    # Query career
    for sol in prolog.query("career(X)"):
        return sol["X"]

    return "No Match Found"
