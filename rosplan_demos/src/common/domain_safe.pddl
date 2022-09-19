(define (domain barista)

(:requirements :fluents :adl :strips :typing)

(:types
    gripper amount drink ingredient-dispenser container - object
  	ingredient beverage - drink
    shot-glass cup pitcher - container
)

(:predicates
    (on-table ?c - container)
    (gripping ?g - gripper ?c - container)
	(empty-gripper ?g - gripper)
	(full-container ?c - container)
	(empty-container ?c - container)
	(serve-drink ?c - container ?b - drink)
    (contains ?c - container ?b - drink)
    (clean-container ?c - container)
    (dirty-container ?c - container)
    (used-container ?c - container ?b - drink)
    (dispenses ?d - ingredient-dispenser ?i - ingredient)
    (pitcher-empty-amount ?p - pitcher ?l - amount)
	(pitcher-amount ?p - pitcher ?l - amount)
	(pitcher-full ?p - pitcher ?l - amount)
	(next-amount ?a1 ?a2 - amount)
	(beverage-not-ready ?p - pitcher)
	(beverage-ready ?p - pitcher)
    (drink-part1 ?b - beverage ?i - ingredient)
    (drink-part2 ?b - beverage ?i - ingredient)
    (drink-part3 ?b - beverage ?i - ingredient))


(:action pick_up_container
    :parameters (?g - gripper ?c - container)
    :precondition (and (on-table ?c)
                        (empty-gripper ?g))
    :effect (and (not (on-table ?c))
	     	     (not (empty-gripper ?g))
			      (gripping ?g ?c))
)

(:action drop_container
    :parameters (?g - gripper ?c - container)
    :precondition (gripping ?g ?c)
    :effect (and (not (gripping ?g ?c))
	     	     (empty-gripper ?g)
			  (on-table ?c))
)

(:action fill_shot_glass_with_ingredient
    :parameters (?s - shot-glass ?i - ingredient ?g1 ?g2 - gripper ?d - ingredient-dispenser)
    :precondition (and (gripping ?g1 ?s)
                        (empty-gripper ?g2)
	   		            (dispenses ?d ?i)
                        (empty-container ?s)
			            (clean-container ?s))
    :effect (and (not (empty-container ?s))
                (full-container ?s)
	   	   	    (contains ?s ?i)
	   	   	    (not (clean-container ?s))
	   	   	    (dirty-container ?s)
			    (used-container ?s ?i))
)

(:action pour_ingredient_from_shot_shot_glass_to_clean_pitcher
    :parameters (?s - shot-glass ?i - ingredient ?p - pitcher ?g1 - gripper ?a ?a1 - amount)
    :precondition (and (gripping ?g1 ?s)
			            (contains ?s ?i)
                        (empty-container ?p)
	   		            (clean-container ?p)
                        (pitcher-amount ?p ?a)
                        (next-amount ?a ?a1))
    :effect (and (not (contains ?s ?i))
	   	   	       (empty-container ?s)
			       (contains ?p ?i)
			       (dirty-container ?p)
                    (not (empty-container ?p))
			        (not (clean-container ?p))
			        (beverage-not-ready ?p)
			        (not (pitcher-amount ?p ?a))
			        (pitcher-amount ?p ?a1))
)


(:action pour_ingredient_from_shot_glass_to_used_pitcher
    :parameters (?s - shot-glass ?i - ingredient ?p - pitcher ?g1 - gripper ?a ?a1 - amount)
    :precondition (and (gripping ?g1 ?s)
			            (contains ?s ?i)
                        (beverage-not-ready ?p)
                        (pitcher-amount ?p ?a)
                        (next-amount ?a ?a1))
    :effect (and (not (contains ?s ?i))
                (contains ?p ?i)
	   	   	    (empty-container ?s)
	   	   	    (not (full-container ?s))
  			    (not (pitcher-amount ?p ?a))
			    (pitcher-amount ?p ?a1))
)

(:action make_drink_in_pitcher
  	:parameters (?b - beverage ?i1 ?i2 ?i3 - ingredient ?p - pitcher ?g1 ?g2 - gripper)
    :precondition (and (gripping ?g1 ?p)
                        (empty-gripper ?g2)
			            (contains ?p ?i1)
                        (contains ?p ?i2)
                        (contains ?p ?i3)
                        (drink-part1 ?b ?i1)
			            (drink-part2 ?b ?i2)
			            (drink-part3 ?b ?i3)
			            (beverage-not-ready ?p))
    :effect (and (not (beverage-not-ready ?p))
		        (not (contains ?p ?i1))
                (not (contains ?p ?i2))
                (not (contains ?p ?i3))
	   	   	    (beverage-ready ?p)
                (contains ?p ?b))
)

(:action pour_beverage_from_pitcher_to_cup
    :parameters (?b - beverage  ?c - cup ?g1 ?g2 - gripper ?p - pitcher ?a1 ?a2 - amount)
    :precondition (and (gripping ?g1 ?p)
                        (empty-gripper ?g2)
			            (beverage-ready ?p)
			            (empty-container ?c)
			            (clean-container ?c)
			            (contains ?p ?b)
                        (pitcher-amount ?p ?a1)
                        (pitcher-empty-amount ?p ?a2)
                        )
    :effect (and (not (clean-container ?c))
                (dirty-container ?c)
	   	   	    (not (empty-container ?c))
			    (serve-drink ?c ?b)
			    (empty-container ?p)
			    (not (beverage-ready ?p))
	   	   	    (not (pitcher-amount ?p ?a1))
	   	   	    (pitcher-amount ?p ?a2)
			    (not (contains ?p ?b))
			    )
)

 )
