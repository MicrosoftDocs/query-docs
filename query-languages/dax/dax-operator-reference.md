---
title: "DAX Operator Reference | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DAX Operator Reference
The Data Analysis Expression (DAX) language uses operators to create expressions that compare values, perform arithmetic calculations, or work with strings. This section describes the use of each operator.  
  
## Types of Operators  
There are four different types of calculation operators: arithmetic, comparison, text concatenation, and logical.  
  
### Arithmetic Operators  
To perform basic mathematical operations such as addition, subtraction, or multiplication; combine numbers; and produce numeric results, use the following arithmetic operators.  
  
|Arithmetic operator|Meaning|Example|  
|-----------------------|-----------|-----------|  
|+ (plus sign)|Addition|3+3|  
|– (minus sign)|Subtraction or sign|3–1–1|  
|* (asterisk)|Multiplication|3*3|  
|/ (forward slash)|Division|3/3|  
|^ (caret)|Exponentiation|16^4|  
  
> [!NOTE]  
> The plus sign can function both as a *binary operator* and as a *unary operator*. A binary operator requires numbers on both sides of the operator and performs addition. When you use values in a DAX formula on both sides of the binary operator, DAX tries to cast the values to numeric data types if they are not already numbers. In contrast, the unary operator can be applied to any type of argument. The plus symbol does not affect the type or value and is simply ignored, whereas the minus operator creates a negative value, if applied to a numeric value.  
  
### Comparison Operators  
You can compare two values with the following operators. When two values are compared by using these operators, the result is a logical value, either TRUE or FALSE.  
  
|Comparison operator|Meaning|Example|  
|-----------------------|-----------|-----------|  
|=|Equal to|[Region] = "USA"|  
|&gt;|Greater than|[Sales Date] &gt; "Jan 2009"|  
|&lt;|Less than|[Sales Date] &lt; "Jan 1 2009"|  
|&gt;=|Greater than or equal to|[Amount] &gt;= 20000|  
|&lt;=|Less than or equal to|[Amount] &lt;= 100|  
|&lt;&gt;|Not equal to|[Region] &lt;&gt; "USA"|  
  
### Text Concatenation Operator  
Use the ampersand (&amp;) to join, or concatenate, two or more text strings to produce a single piece of text.  
  
|Text operator|Meaning|Example|  
|-----------------|-----------|-----------|  
|&amp; (ampersand)|Connects, or concatenates, two values to produce one continuous text value|[Region] &amp; ", " &amp; [City]|  
  
### Logical Operators  
Use logical operators (&amp;&amp;) and (||) to combine expressions to produce a single result.  
  
|Text operator|Meaning|Examples|  
|-----------------|-----------|------------|  
|&amp;&amp; (double ampersand)|Creates an AND condition between two expressions that each have a Boolean result. If both expressions return TRUE, the combination of the expressions also returns TRUE; otherwise the combination returns FALSE.|([Region] = "France") &amp;&amp; ([BikeBuyer] = "yes"))|  
|&#124;&#124; (double pipe symbol)|Creates an OR condition between two logical expressions. If either expression returns TRUE, the result is TRUE; only when both expressions are FALSE is the result FALSE.|(([Region] = "France") &#124;&#124; ([BikeBuyer] = "yes"))| 
|IN|Creates a logical OR condition between each row being compared to a table. Note: the table constructor syntax uses curly braces.|'Product'[Color] IN { "Red", "Blue", "Black" }|   
  
## Operators and Precedence Order  
In some cases, the order in which calculation is performed can affect the return value; therefore, it is important to understand how the order is determined and how you can change the order to obtain the desired results.  
  
### Calculation Order  
An expression evaluates the operators and values in a specific order. All expressions always begin with an equal sign (=). The equal sign indicates that the succeeding characters constitute an expression.  
  
Following the equal sign are the elements to be calculated (the operands), which are separated by calculation operators. Expressions are always read from left to right, but the order in which the elements are grouped can be controlled to some degree by using parentheses.  
  
### Operator Precedence  
If you combine several operators in a single formula, the operations are ordered according to the following table. If the operators have equal precedence value, they are ordered from left to right. For example, if an expression contains both a multiplication and division operator, they are evaluated in the order that they appear in the expression, from left to right.  
  
|Operator|Description|  
|------------|---------------|  
|^|Exponentiation|  
|–|Sign (as in –1)|  
|* and /|Multiplication and division|  
|!|NOT (unary operator)|  
|+ and –|Addition and subtraction|  
|&amp;|Connects two strings of text (concatenation)|  
|=&lt; &gt;&lt;=&gt;=&lt;&gt;|Comparison|  
  
### Using Parentheses to Control Calculation Order  
To change the order of evaluation, you should enclose in parentheses that part of the formula that must be calculated first. For example, the following formula produces 11 because multiplication is calculated before addition. The formula multiplies 2 by 3, and then adds 5 to the result.  
  
```  
=5+2*3  
```  
In contrast, if you use parentheses to change the syntax, the order is changed so that 5 and 2 are added together, and the result multiplied by 3 to produce 21.  
  
```  
=(5+2)*3  
```  
In the following example, the parentheses around the first part of the formula force the calculation to evaluate the expression `(3 + 0.25)` first and then divide the result by the result of the expression, (`3 - 0.25)`.  
  
```  
=(3 + 0.25)/(3 - 0.25)  
```  
In the following example, the exponentiation operator is applied first, according to the rules of precedence for operators, and then the sign operator is applied. The result for this expression is -4.  
  
```  
=-2^2  
```  
To ensure that the sign operator is applied to the numeric value first, you can use parentheses to control operators, as shown in the following example. The result for this expression is 4.  
  
```  
= (-2)^2  
```  
  
## Compatibility Notes  
DAX easily handles and compares various data types, much like Microsoft Excel. However, the underlying computation engine is based on SQL Server Analysis Services and provides additional advanced features of a relational data store, including richer support for date and time types. Therefore, in some cases the results of calculations or the behavior of functions may not be the same as in Excel. Moreover, DAX supports more data types than does Excel. This section describes the key differences.  
  
### Coercing Data Types of Operands  
In general, the two operands on the left and right sides of any operator should be the same data type. However, if the data types are different, DAX will convert them to a common data type to apply the operator in some cases:  
  
1.  First, both operands are converted to the largest possible common data type.  
  
2.  Next, the operator is applied if possible..  
  
For example, suppose you have two numbers that you want to combine. One number results from a formula, such as =`[Price] * .20`, and the result may contain many decimal places. The other number is an integer that has been provided as a string value.  

In this case, DAX will convert both numbers to real numbers in a numeric format, using the largest numeric format that can store both kinds of numbers. Then DAX will apply the multiplication. 

Depending on the data-type combination, type coercion may not be applied for comparison operations. See [Data Types Supported (SSAS Tabular)](https://msdn.microsoft.com/library/gg492146.aspx) for a complete list of data types supported by DAX in SSAS.

Integer, Real Number, Currency, Date/time and Blank are considered numeric for comparison purposes. Blank evaluates to zero when performing a comparison. The following data-type combinations are supported for comparison operations.



Left Side Data Type  |Right Side Data Type  
---------|---------
Numeric     |   Numeric      
Boolean     |   Boolean      
String     |   String      
  
Other mixed data-type comparisons will return an error. For example, a formula such as =”1” > 0 returns an error stating that *DAX comparison operations do not support comparing values of type Text with values of type Integer*.
  
|Data Types used in DAX|Data Types used in Excel|  
|--------------------------|----------------------------|  
|Numbers (I8, R8)<br /><br />Boolean<br /><br />String<br /><br />DateTime<br /><br />Currency|Numbers (R8)<br /><br />Boolean<br /><br />String<br /><br />Variant<br /><br />Currency|  
  
### Differences in Precedence Order  
The precedence order of operations in DAX formulas is basically the same as that used by Microsoft Excel, but some Excel operators are not supported, such as percent. Also, ranges are not supported.  
  
Therefore, whenever you copy and paste formulas from Excel, be sure to review the formula carefully, as some operators or elements in the formulas may not be valid. When there is any doubt about the order in which operations are performed, we recommend you use parentheses to control the order of operations and remove any ambiguity about the result.  
  
## See Also  
[DAX Syntax Reference](dax-syntax-reference.md)  
  
