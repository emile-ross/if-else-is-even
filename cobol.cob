       IDENTIFICATION DIVISION.
       PROGRAM-ID. IF-ELSE-IS-EVEN.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 ARG-COUNT PIC 9(4) COMP.
       01 ARG-VALUE PIC X(100).
       01 COUNTOF PIC 9(4) COMP.
       01 ITERATOR PIC 9(4) COMP.
       01 IS-EVEN PIC 9(1) COMP VALUE 1.
       PROCEDURE DIVISION.
           PERFORM 1001-CHECK-ARGS THROUGH 1001-EXIT. 
           DISPLAY "       IDENTIFICATION DIVISION.".
           DISPLAY "       PROGRAM-ID. IF-ELSE-IS-EVEN.".
           DISPLAY "       ENVIRONMENT DIVISION.".
           DISPLAY "       DATA DIVISION.".
           DISPLAY "       WORKING-STORAGE SECTION.".
           DISPLAY "       01 COUNTOF PIC 9(4) COMP VALUE " COUNTOF ".".
           DISPLAY "       01 IS-EVEN PIC 9(1) COMP.".
           DISPLAY "       PROCEDURE DIVISION.".
           PERFORM VARYING ITERATOR FROM 0 BY 1 UNTIL
             ITERATOR IS GREATER THAN COUNTOF
             DISPLAY "          IF " ITERATOR " IS EQUAL TO " COUNTOF
             DISPLAY "          THEN MOVE " IS-EVEN " TO IS-EVEN"
             DISPLAY "          END-IF."
             IF IS-EVEN IS EQUAL TO 1
             THEN MOVE 0 TO IS-EVEN
             ELSE MOVE 1 TO IS-EVEN
             END-IF
           END-PERFORM.
           DISPLAY "          DISPLAY ""IS-EVEN: "" IS-EVEN." 
           DISPLAY "          STOP RUN."
           STOP RUN.

       1001-CHECK-ARGS.
           ACCEPT ARG-COUNT FROM ARGUMENT-NUMBER.
           IF ARG-COUNT IS NOT EQUAL TO 1
           THEN 
             DISPLAY "invalid amount of arguments"
             STOP RUN
           END-IF.
           ACCEPT ARG-VALUE FROM ARGUMENT-VALUE.
           COMPUTE COUNTOF = FUNCTION NUMVAL(ARG-VALUE).
           GO TO 1001-EXIT.
       1001-EXIT.
           EXIT.
       
