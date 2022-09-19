(define (problem barista-recepies)
 (:domain barista)
 (:objects 
    pitcher1 - pitcher 
    left right - gripper
    shot-glass1 - shot-glass
    cup1 - cup
    coffee - ingredient
    espresso - beverage
    dispenser1 - ingredient-dispenser
    amount0 amount1 amount2 amount3 - amount
)
 (:init 
  (on-table pitcher1)
  (on-table shot-glass1)
  (on-table cup1)
    
  (dispenses dispenser1 coffee)
  
  (clean-container pitcher1)
  (clean-container shot-glass1)
  (clean-container cup1)

  (empty-container pitcher1)
  (empty-container shot-glass1)
  (empty-container cup1)
  
  (empty-gripper left)
  (empty-gripper right)
  
  (pitcher-empty-amount pitcher1 amount0)
  (pitcher-amount pitcher1 amount0)

  (next-amount amount0 amount1)
  (next-amount amount1 amount2)
  (next-amount amount2 amount3)
  
  (drink-part1 espresso coffee)
  (drink-part2 espresso coffee)
  (drink-part3 espresso coffee)
  
)

 (:goal
  (and
     (serve-drink cup1 espresso)
     (empty-gripper left)
     (empty-gripper right)
)))
