
; δημιουργεια κοσμου

(deffacts static_facts

	
	;;(cell_at 1 1 fruits 0 )
	(cell_at 1 2 fruits 1 )
	(cell_at 1 3 fruits 1 )
	(cell_at 1 4 fruits 1 )
	(cell_at 1 5 fruits 1 )
	(cell_at 2 1 fruits 1 )
	;;(cell_at 2 2 fruits 0 )
	;;(cell_at 2 3 fruits 0 )
	(cell_at 2 4 fruits 1 )
	(cell_at 2 5 fruits 1 )
	(cell_at 3 1 fruits 1 )
	;;(cell_at 3 2 fruits 3 )
	(cell_at 3 3 fruits 1 )
	;;(cell_at 3 4 fruits 1 )
	(cell_at 3 5 fruits 1 )
	(cell_at 4 1 fruits 1 )
	(cell_at 4 2 fruits 1 )
	;;(cell_at 4 3 fruits 2 )
	;;(cell_at 4 4 fruits 3 )
	(cell_at 4 5 fruits 1 )
	(cell_at 5 1 fruits 1 )
	(cell_at 5 2 fruits 1 )
	(cell_at 5 3 fruits 1 )
	(cell_at 5 4 fruits 1 )
	;;(cell_at 5 5 fruits 0 )
		
)

(deffacts moving_facts
  
  (ghost1_at 1 5)
  (ghost2_at 5 1)
  (pacman_at 3 3)
)


(defrule begin
  (initial-fact)
=>
  (set-strategy default)
)

(defrule reach_goal ;; the rule needs to be optimised
      
	;;(cell_at 1 1 fruits 0 )
	(cell_at 1 2 fruits 0 )
	(cell_at 1 3 fruits 0 )
	(cell_at 1 4 fruits 0 )
	(cell_at 1 5 fruits 0 )
	(cell_at 2 1 fruits 0 )
	;;(cell_at 2 2 fruits 0 )
	;;(cell_at 2 3 fruits 0 )
	(cell_at 2 4 fruits 0 )
	(cell_at 2 5 fruits 0 )
	(cell_at 3 1 fruits 0 )
	;;(cell_at 3 2 fruits 3 )
	(cell_at 3 3 fruits 0 )
	;;(cell_at 3 4 fruits 0 )
	(cell_at 3 5 fruits 0 )
	(cell_at 4 1 fruits 0 )
	(cell_at 4 2 fruits 0 )
	;;(cell_at 4 3 fruits 2 )
	;;(cell_at 4 4 fruits 3 )
	(cell_at 4 5 fruits 0 )
	(cell_at 5 1 fruits 0 )
	(cell_at 5 2 fruits 0 )
	(cell_at 5 3 fruits 0 )
	(cell_at 5 4 fruits 0 )
	;;(cell_at 5 5 fruits 0 )

=>
  (printout t "no more fruits to be eaten"  crlf)
  (halt)
)

(defrule death1 ;;OTAN O PACMAN  ΦΑΓΩΘΕΙ ΑΠΟ ΤΟ ΦΑΝΤΑΣΜΑ1
    
	(pacman_at ?x ?y)
	(ghost1_at ?x ?y)
=>
	(printout t "pacman got killed by ghost1 " crlf)
	(halt)
)

(defrule death2 ;; ΟΤΑΝ Ο PACMAN  ΦΑΓΩΘΕΙ ΑΠΟ ΤΟ ΦΑΝΤΑΣΜΑ2
    
	(pacman_at ?x ?y)
	(ghost2_at ?x ?y)
=>
	(printout t "pacman got killed by ghost2 " crlf)
	(halt)
)


;; ΚΙΝΗΣΗΣ ΦΑΝΤΑΣΜΑΤΟΣ1
(defrule ghost1_move_left
  ?z <- (ghost1_at ?x ?y)
  (cell_at ?x =(- ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost1_at ?x (- ?y 1)))  
)

(defrule ghost1_move_right
  ?z <- (ghost1_at ?x ?y)
  (cell_at ?x =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost1_at ?x (+ ?y 1))) 
)

(defrule ghost1_move_up
  ?z <- (ghost1_at ?x ?y)
  (cell_at =(- ?x 1) ?y fruits ?f )
=>
  (retract ?z)
  (assert (ghost1_at (- ?x 1) ?y )) 
)

(defrule ghost1_move_down
  ?z <- (ghost1_at ?x ?y)
  (cell_at =(+ ?x 1) ?y fruits ?f  )
=>
  (retract ?z)
  (assert (ghost1_at (+ ?x 1) ?y )) 
)

(defrule ghost1_move_upleft
  ?z <- (ghost1_at ?x ?y)
  (cell_at =(- ?x 1) =(- ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost1_at (- ?x 1) (- ?y 1)))  
)

(defrule ghost1_move_downright
  ?z <- (ghost1_at ?x ?y)
  (cell_at =(+ ?x 1) =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost1_at (+ ?x 1) (+ ?y 1))) 
)

(defrule ghost1_move_upright
  ?z <- (ghost1_at ?x ?y)
  (cell_at =(- ?x 1) =(+ ?y 1) fruits ?f )
=>
  (retract ?z)
  (assert (ghost1_at (- ?x 1) (+ ?y 1) )) 
)

(defrule ghost1_move_downleft
  ?z <- (ghost1_at ?x ?y)
  (cell_at =(+ ?x 1) =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost1_at (+ ?x 1) (+ ?y 1) )) 
)

;; ΚΙΝΗΣΕΙΣ ΦΑΝΤΑΣΜΑΤΟΣ2

(defrule ghost2_move_left
  ?z <- (ghost2_at ?x ?y)
  (cell_at ?x =(- ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost2_at ?x (- ?y 1)))  
)

(defrule ghost2_move_right
  ?z <- (ghost2_at ?x ?y)
  (cell_at ?x =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost2_at ?x (+ ?y 1))) 
)

(defrule ghost2_move_up
  ?z <- (ghost2_at ?x ?y)
  (cell_at =(- ?x 1) ?y fruits ?f )
=>
  (retract ?z)
  (assert (ghost2_at (- ?x 1) ?y )) 
)

(defrule ghost2_move_down
  ?z <- (ghost2_at ?x ?y)
  (cell_at =(+ ?x 1) ?y fruits ?f  )
=>
  (retract ?z)
  (assert (ghost2_at (+ ?x 1) ?y )) 
)

(defrule ghost2_move_upleft
  ?z <- (ghost2_at ?x ?y)
  (cell_at =(- ?x 1) =(- ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost2_at (- ?x 1) (- ?y 1)))  
)

(defrule ghost2_move_downright
  ?z <- (ghost2_at ?x ?y)
  (cell_at =(+ ?x 1) =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost2_at (+ ?x 1) (+ ?y 1))) 
)

(defrule ghost2_move_upright
  ?z <- (ghost2_at ?x ?y)
  (cell_at =(- ?x 1) =(+ ?y 1) fruits ?f )
=>
  (retract ?z)
  (assert (ghost2_at (- ?x 1) (+ ?y 1) )) 
)

(defrule ghost2_move_downleft
  ?z <- (ghost2_at ?x ?y)
  (cell_at =(+ ?x 1) =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (ghost2_at (+ ?x 1) (+ ?y 1) )) 
)

;;ΚΙΝΗΣΕΙΣ PACMAN

(defrule pacman_move_left

  ?z <- (pacman_at ?x ?y)
  (cell_at ?x =(- ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (pacman_at ?x (- ?y 1)))  
)

(defrule pacman_move_right

  ?z <- (pacman_at ?x ?y)
  (cell_at ?x =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (pacman_at ?x (+ ?y 1))) 
)

(defrule pacman_move_up

  ?z <- (pacman_at ?x ?y)
  (cell_at =(- ?x 1) ?y fruits ?f )
=>
  (retract ?z)
  (assert (pacman_at (- ?x 1) ?y )) 
)

(defrule pacman_move_down
	
  ?z <- (pacman_at ?x ?y)
  (cell_at =(+ ?x 1) ?y fruits ?f  )
=>
  (retract ?z)
  (assert (pacman_at (+ ?x 1) ?y )) 
)

(defrule pacman_move_upleft

  ?z <- (pacman_at ?x ?y)
  (cell_at =(- ?x 1)  =(- ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (pacman_at (- ?x 1) (- ?y 1)))  
)

(defrule pacman_move_downright

  ?z <- (pacman_at ?x ?y)
  (cell_at =(+ ?x 1) =(+ ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (pacman_at (+ ?x 1) (+ ?y 1))) 
)

(defrule pacman_move_upright

  ?z <- (pacman_at ?x ?y)
  (cell_at =(- ?x 1) =(+ ?y 1)fruits ?f )
=>
  (retract ?z)
  (assert (pacman_at (- ?x 1) (+ ?y 1) )) 
)

(defrule pacman_move_downleft
	
  ?z <- (pacman_at ?x ?y)
  (cell_at =(+ ?x 1) =(- ?y 1) fruits ?f  )
=>
  (retract ?z)
  (assert (pacman_at (+ ?x 1) (- ?y 1) )) 
)



(defrule eat_fruit
  (declare (salience 1))
  (pacman_at ?x ?y)
  ?z <- (cell_at ?x ?y  fruits ?f&~0 )
	
=>
  (retract ?z)
  (assert (cell_at ?x ?y fruits (- ?f 1) ))
)

