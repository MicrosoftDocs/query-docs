---
description: "Learn more about: DAX operators"
title: "DAX operators | Microsoft Docs"
ms.topic: conceptual
---
# DAX operators

The Data Analysis Expression (DAX) language uses operators to create expressions that compare values, perform arithmetic calculations, or work with strings.
  
## Types of operators

There are four different types of calculation operators: arithmetic, comparison, text concatenation, and logical.  
  
### Arithmetic operators

To perform basic mathematical operations such as addition, subtraction, or multiplication; combine numbers; and produce numeric results, use the following arithmetic operators.  
  
|Arithmetic operator|Meaning|Example|  
|-----------------------|-----------|-----------|  
|`+` (plus sign)|Addition|`3+3`|  
|`-` (minus sign)|Subtraction or sign|`3-1-1`|  
|`*` (asterisk)|Multiplication|`3*3`|  
|`/` (forward slash)|Division|`3/3`|  
|`^` (caret)|Exponentiation|`16^4`|  
  
> [!NOTE]  
> The plus sign can function both as a *binary operator* and as a *unary operator*. A binary operator requires numbers on both sides of the operator and performs addition. When you use values in a DAX formula on both sides of the binary operator, DAX tries to cast the values to numeric data types if they are not already numbers. In contrast, the unary operator can be applied to any type of argument. The plus symbol does not affect the type or value and is simply ignored, whereas the minus operator creates a negative value, if applied to a numeric value.  
  
### Comparison operators

You can compare two values with the following operators. When two values are compared by using these operators, the result is a logical value, either `TRUE` or `FALSE`.  
  
|Comparison operator|Meaning|Example|  
|-----------------------|-----------|-----------|  
|`=`|Equal to|[Region] = "USA"| 
|`==`|Strict equal to|[Region] == "USA"|  
|`>`|Greater than|[Sales Date] &gt; "Jan 2009"|  
|`<`|Less than|[Sales Date] &lt; "Jan 1 2009"|  
|`>=`|Greater than or equal to|[Amount] &gt;= 20000|  
|`<=`|Less than or equal to|[Amount] &lt;= 100|  
|`<>`|Not equal to|[Region] &lt;&gt; "USA"| 

All comparison operators except == treat BLANK as equal to number 0, empty string "", DATE(1899, 12, 30), or `FALSE`. As a result, [Column] = 0 will be true when the value of [Column] is either 0 or BLANK. In contrast, [Column] == 0 is true only when the value of [Column] is 0.

### Text concatenation operator

Use the ampersand (`&`) to join, or concatenate, two or more text strings to produce a single piece of text.  
  
|Text operator|Meaning|Example|  
|-----------------|-----------|-----------|  
|`&` (ampersand)|Connects, or concatenates, two values to produce one continuous text value|`[Region] & ", " & [City]`|  
  
### Logical operators

Use logical operators (`&&`) and (`||`) to combine expressions to produce a single result.  
  
|Text operator|Meaning|Examples|  
|-----------------|-----------|------------|  
|`&&`(double ampersand)|Creates an AND condition between two expressions that each have a Boolean result. If both expressions return `TRUE`, the combination of the expressions also returns `TRUE`; otherwise the combination returns `FALSE`.|`([Region] = "France") && ([BikeBuyer] = "yes"))`|  
|`||` (double pipe symbol)|Creates an OR condition between two logical expressions. If either expression returns `TRUE`, the result is `TRUE`; only when both expressions are `FALSE` is the result `FALSE`. | `(([Region] = "France") || ([BikeBuyer] = "yes"))`| 
|`IN`|Creates a logical OR condition between each row being compared to a table. Note: the table constructor syntax uses curly braces.|`'Product'[Color] IN { "Red", "Blue", "Black" }`|
  
## Operators and precedence order

In some cases, the order in which calculation is performed can affect the Return value; therefore, it is important to understand how the order is determined and how you can change the order to obtain the desired results.  
  
### Calculation order

An expression evaluates the operators and values in a specific order. All expressions always begin with an equal sign (=). The equal sign indicates that the succeeding characters constitute an expression.  
  
Following the equal sign are the elements to be calculated (the operands), which are separated by calculation operators. Expressions are always read from left to right, but the order in which the elements are grouped can be controlled to some degree by using parentheses.  
  
### Operator precedence

If you combine several operators in a single formula, the operations are ordered according to the following table. If the operators have equal precedence value, they are ordered from left to right. For example, if an expression contains both a multiplication and division operator, they are evaluated in the order that they appear in the expression, from left to right.  
  
|Operator|Description|  
|------------|---------------|  
|`^`|Exponentiation|  
|`–`|Sign (such as –1)|  
|`*` and `/`|Multiplication and division|  
|`+` and `–`|Addition and subtraction|  
|`&`|Connects two strings of text (concatenation)|  
|`=,==,<,>,<=,>=,<>,IN`|Comparison|  
|`NOT`|`NOT` (unary operator)|  
  
### Using parentheses to control calculation order

To change the order of evaluation, you should enclose in parentheses that part of the formula that must be calculated first. For example, the following formula produces 11 because multiplication is calculated before addition. The formula multiplies 2 by 3, and then adds 5 to the result.  
  
```dax
=5+2*3  
```

In contrast, if you use parentheses to change the syntax, the order is changed so that 5 and 2 are added together, and the result multiplied by 3 to produce 21.  
  
```dax
=(5+2)*3  
```

In the following example, the parentheses around the first part of the formula force the calculation to evaluate the expression `(3 + 0.25)` first and then divide the result by the result of the expression, `(3 - 0.25)`.  
  
```dax
=(3 + 0.25)/(3 - 0.25)  
```

In the following example, the exponentiation operator is applied first, according to the rules of precedence for operators, and then the sign operator is applied. The result for this expression is -4.  
  
```dax
=-2^2  
```

To ensure that the sign operator is applied to the numeric value first, you can use parentheses to control operators, as shown in the following example. The result for this expression is 4.  
  
```dax
= (-2)^2  
```
  
## Compatibility

DAX easily handles and compares various data types, much like Microsoft Excel. However, the underlying computation engine is based on SQL Server Analysis Services and provides additional advanced features of a relational data store, including richer support for date and time types. Therefore, in some cases the results of calculations or the behavior of functions may not be the same as in Excel. Moreover, DAX supports more data types than does Excel. This section describes the key differences.  
  
### Coercing data types of operands

In general, the two operands on the left and right sides of any operator should be the same data type. However, if the data types are different, DAX will convert them to a common data type to apply the operator in some cases:  
  
1. Both operands are converted to the largest possible common data type.
1. The operator is applied, if possible.
  
For example, suppose you have two numbers that you want to combine. One number results from a formula, such as =`[Price] * .20`, and the result may contain many decimal places. The other number is an integer that has been provided as a string value.  

In this case, DAX will convert both numbers to real numbers in a numeric format, using the largest numeric format that can store both kinds of numbers. Then DAX will apply the multiplication.

Depending on the data-type combination, type coercion may not be applied for comparison operations. For a complete list of data types supported by DAX, see [Data types supported in tabular models](/analysis-services/tabular-models/data-types-supported-ssas-tabular) and [Data types in Power BI Desktop](/power-bi/connect-data/desktop-data-types).

Integer, Real Number, Currency, Date/time and Blank are considered numeric for comparison purposes. Blank evaluates to zero when performing a comparison. The following data-type combinations are supported for comparison operations.

Left Side Data Type  |Right Side Data Type  
---------|---------
Numeric     |   Numeric
Boolean     |   Boolean
String     |   String

Other mixed data-type comparisons will return an error. For example, a formula such as ="1" > 0 returns an error stating that *DAX comparison operations do not support comparing values of type Text with values of type Integer*.

|Data Types used in DAX|Data Types used in Excel|  
|--------------------------|----------------------------|
|Numbers (I8, R8)|Numbers (R8)|
|String|String|
|Boolean|Boolean|
|DateTime|Variant|
|Currency|Currency|
  
### Differences in precedence order

The precedence order of operations in DAX formulas is basically the same as that used by Microsoft Excel, but some Excel operators are not supported, such as percent. Also, ranges are not supported.  
  
Therefore, whenever you copy and paste formulas from Excel, be sure to review the formula carefully, as some operators or elements in the formulas may not be valid. When there is any doubt about the order in which operations are performed, it's recommended you use parentheses to control the order of operations and remove any ambiguity about the result.  
  
## Related content

[DAX syntax](dax-syntax-reference.md)  
[DAX parameter-naming](dax-parameter-naming-conventions.md)
