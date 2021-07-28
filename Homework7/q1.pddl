(define (domain truck-strips)
   (:predicates (location ?l)
      (package ?p)
      (truck ?t)
      (at-locy ?r)
      (at ?t ?r)
      (free ?f)
      (carry ?o ?f))

   (:action move
       :parameters  (?from ?p1)
       :precondition (and  (location ?from) (location ?p1) (at-locy ?from))
       :effect (and (at-locy ?p1)
           (not (at-locy ?from))))


   (:action load
       :parameters (?obj ?location ?truck)
       :precondition  (and  (package ?obj) (location ?location) (truck ?truck)
             (at ?obj ?location) (at-locy ?location) (free ?truck))
       :effect (and (carry ?obj ?truck)
          (not (at ?obj ?location)) 
          (not (free ?truck))))


   (:action unload
       :parameters  (?obj  ?location ?truck)
       :precondition  (and  (package ?obj) (location ?location) (truck ?truck)
             (carry ?obj ?truck) (at-locy ?location))
       :effect (and (at ?obj ?location)
          (free ?truck)
          (not (carry ?obj ?truck)))))