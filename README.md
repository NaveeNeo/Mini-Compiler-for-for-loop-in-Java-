# Mini-Compiler-for-for-loop-in-Java-
 Compiler that compiles for loop statements in Java. Python used as a main tool for RDP. Lex and Yacc were also used. Finally used dot as a tool for generating Pictorial representation of the AST. 
 

Comipler Design Mini Project: Mini Compiler for "for" loop in JAVA:

1.Open CD_FOR_LOOP folder.

2.Open the terminal and run lexer.py
# python3 lexer.py

(No output is seen as we have commented the print statements. If one wants to see the output please uncomment. make sure symtab.txt[input file to lexer.py] file is present)

3.Open ICG For_Loop folder.
Inside the folder im4.l and im4.y are the lex and the yacc files respectively.
Complile the yacc files:

# lex im4.l
  yacc im4.y
  gcc y.tab.c -ll -ly
  ./a.out <ip.txt 

(ip.txt is the input file. Run the above commands)

4.Time to generate AST Image file.

# python3 rdp.py > filename.dot
  dot -Tpng filename.dot > img_filename.png

(An image is generated with png format with the img_filename.png. Open the image and AST can be seen ) 


Compiler Design Project by:
*Bhargava Bhodas --------->01FB14ECS054
*Chandana Balaji BP ------>01FB14ECS056
*B R Naveen -------------->01FB14ECS051
*Abhimanyu --------------->01FB14ECS005
