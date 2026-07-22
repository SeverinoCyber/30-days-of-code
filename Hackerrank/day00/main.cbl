
       IDENTIFICATION DIVISION.
       PROGRAM-ID. SOLUTION.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT SYSIN ASSIGN TO KEYBOARD.
             
       DATA DIVISION.
       FILE SECTION.
       FD  SYSIN.
       01  INPUT-STRING PIC X(255).
           88 EOF VALUE HIGH-VALUES.
        
       PROCEDURE DIVISION.
           OPEN INPUT SYSIN.
           READ SYSIN
               AT END SET EOF TO TRUE
           END-READ.
           
           DISPLAY "Hello, World.".
           DISPLAY INPUT-STRING.
           
           CLOSE SYSIN.
           STOP RUN.