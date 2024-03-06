(define (sum-while initial-x condition         add-to-total update-x)
  ;      sum-while 1         '(< (* x x) 50) 'x            '(+ x 1)
  `(begin 
     (define (f x total)
       (if ,condition
	 (f ,update-x (+ total ,add-to-total))
	 total))
     (f ,initial-x 0)))


