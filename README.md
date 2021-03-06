# LogicalCircuitVisualizer
**Visualize a Verilog file Graphicaly**
 
The Logical Circuit Visualizer (**LCV**) project is aimed to read and graphically present a Logical (Boolean) Electric Circuit programmed in the **Verilog** programming language.
The **LCV** was written in python and is based over the **NodeEditor** project (https://www.blenderfreak.com/tutorials/node-editor-tutorial-series/ ) written by Pavel Krupala after customizing modifying and enhancing it to support the LCV needs.
The NodeEditor project is using Python PyQt5 package. 
Verilog is a programming language, similar to C in its syntax and structure though is aimed at programming electric circuits. Electric, logic or boolean circuits are a group of boolean gates connected togather to provide some logical functionality. It is composed out of basic boolean gates such as **OR**, **AND**, **XOR**, **NOR**, **NAND** and **NOT**.

**Logical Circuit Visualizer functionality**
1.	**Reading and parsing a valid verilog file**

![image](https://user-images.githubusercontent.com/62829168/176267670-3f2fb0d4-e052-4379-a39b-83af89d3db4f.png)


The **LCV** will parse any given valid verilog code even if the order and relations in between the gates are not in their right logical order as the verilog programming language supports this option.
The **LCV** will identify the right position of each gate based on its input and output relations.
It will draw a connecting arc in between the logical gates according to their relation and specify the type of each gate, its inputs and output and booloan graphical presentation.

![image](https://user-images.githubusercontent.com/62829168/176267946-1815852c-380c-44d1-8604-c3688fcd9f25.png)

![image](https://user-images.githubusercontent.com/62829168/176268054-417d7949-2f76-488d-bdc7-57eefcf69b9e.png)


2.	**Graphical Presentation Of The Verilog Code**

The **LCV** will present the Boolean circuits graphically. A Boolean (logical) gate will be presented as a node in the node editor.
The number of supported boolean gates is unlimited.
The boolean gates alignment on the screen will be done according to their **logical order** based on their **inputs/outputs** and not over their chronological order as appears in the input verilog code file.
Circuit **zooming** capabilities are supported using the mouse wheel.
The **LCV** supports partially programmed circuits as long as they are in accordance with the verilog programming language.
Each such node will hold the graphical shape of the relevant Boolean gate.

![image](https://user-images.githubusercontent.com/62829168/176268303-064d2f16-e42a-461f-ad1a-99006cb0b461.png)


![image](https://user-images.githubusercontent.com/62829168/176268369-7740d678-9817-47db-98c5-28b96ee85c7e.png)


3.	**Limited Graphical Editing Capabilities**

The **LCV** provides a limited graphical editing capability as its main goal is to visualize a verilog circuit code. One may delete a gate (or several gates) in the circuit and save the new circuit. The **LCV** **will generate a new verilog text file holding the new circuit**. 
You can override an existing file or save your file as a new one.
The **LCV** will translate the new visual circuit back into a valid verilog code.
If the newly saved verilog file is now loaded back to the **LCV**, it will be displayed graphically with the changes made to it.
The user may also delete an edge connecting two gates but this deletion will not be saved. The reason is that the **LCV** ignores the user edge connecting and will perform the correct edge connecting between the gates based on their right entries and exists and will not allow a wrong connection.
The **LCV** does not support adding new gates or modifying existing ones via the editor. Naturally, every code change done to the file will be reflected visually in the **LCV** if it is reloaded.

**Assumptions**
1.	The input file is a valid verilog file.
2.	The circuit will contain no more than 2 entries as in a logical circuit. Circuits with more than a pair of entries are parts of larger circuits and not an atomic circuit.
3.	The logical gates supported are the basic logical gates which exist in the verilog language. I.e. AND, OR, NOT, XOR, NAND, NOR. Private customized gates created by users are not supported however they may be easily added to the **LCV** (though will require some minimal coding).

**Known Limitations**
1.	The **LCV** project is not a verilog compiler. It doesn???t create any native or machine code, it doesn???t provide compilation errors or debugging capabilities.
It assumes a valid verilog code text file as an input.
2.	If the input code is not a valid verilog program, the result is undefined and depends on the syntax errors in the file. Gates which are properly defined will be presented while gates that were incorrectly defined (in verilog terms) might just be ignored or presented without the proper links inside the circuit (depends on the type of the syntax error).
On some faulty cases and if the code is not at all a verilog code, the Boolean Visualizer will ignore the code and present nothing.


An example of a Verilog file would be:

`timescale 1ns/1ns

module my_boolean_circuit (output myout, input ina, input inb);

  wire x, y , not_inb, not_ina;
  
  not (not_inb, inb , );
  
  not (not_ina, ina , );
  
  and (y, inb , not_ina);
  
  and (x, ina , not_inb);
  
  or (myout, x , y);
  
endmodule

We can see here that we have 2 inputs to the circle (**ina** and **inb**) and one output (**myout**).
Each NOT gate has one entry and one output.
The AND and OR gates have 2 entries and one output each.

**Introducing the project** and a quick intro into the  **structure of a verilog file** are presented in the following video:



https://user-images.githubusercontent.com/62829168/176367887-5f71accb-a1cc-46ca-a8e9-2395ccc5b65f.mp4




Opening the Verilog file via the **LCV** and displaying its logical gates as graphical nodes are exemplified via the following videos (divided into several parts so they will fit into git ReadMe file):

**Part 1: Opening a Verilog code file and displaying it via the LCV.**

https://user-images.githubusercontent.com/62829168/176286290-938eed3e-c43f-4a54-916a-3553cb6f7e97.mp4

**Part 2: Updating the file by adding additional lines of codes (additional gates) and displaying it via the LCV.**


https://user-images.githubusercontent.com/62829168/176365547-1c032f2c-daec-4735-84bc-0e9bdc62f362.mp4

**Part 3: Deleting gates and saving the new circuit by creating and saving a new Verilog file.**


https://user-images.githubusercontent.com/62829168/176366865-f5b584c8-7692-4916-8a3d-b1db9ddcb892.mp4





