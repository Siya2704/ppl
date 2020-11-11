#!/usr/bin/clisp

; factorial of number
(princ "Enter a number:")
(defun factorial(number)
  (if (= number 0) 1
    ( * number (factorial(- number 1)))))
(write (factorial (read)))



