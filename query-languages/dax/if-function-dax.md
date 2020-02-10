---
title: "IF function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 02/11/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# IF
Checks if a condition provided as the first argument is met. Returns one value if the condition is TRUE, and returns another value if the condition is FALSE.  
  
## Syntax  
  
```dax
IF(<logical_test>,<value_if_true>[, <value_if_false>])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|logical_test|Any value or expression that can be evaluated to TRUE or FALSE.|  
|value_if_true|The value that is returned if the logical test is TRUE.|  
|value_if_false|The value that is returned if the logical test is FALSE. If omitted, BLANK is returned.|  
  
## Return value  
Any type of value that can be returned by an expression.  
  
## Remarks  

If the value referenced in the expression is a column, IF returns the value that corresponds to the current row.

The IF function can return variant data type if **value_if_true** and **value_if_false** are of different data types, but the function attempts to return a single data type if both **value_if_true** and **value_if_false** are of numeric data types. In the latter case, the IF function will implicitly convert data types to accommodate both values. For example, the formula `IF(<condition>,TRUE(),0)` returns TRUE or 0, but the formula `IF(<condition>,1.0,0)` returns only decimal values even though **value_if_false** is of the whole number data type. For more information about implicit data type conversion, see [Data types](dax-overview.md#data-types).

  
## Example  
The following example uses nested IF functions that evaluate the number in the column, Calls, from the table FactCallCenter. The function assigns a label as follows: **low** if the number of calls is less than 200, **medium** if the number of calls is less than 300 but not less than 200, and **high** for all other values.  
  
```dax
=IF([Calls]<200,"low",IF([Calls]<300,"medium","high"))  
```
  
## Example  
The following example gets a list of cities that contain potential customers in the California area by using columns from the table ProspectiveBuyer. Because the list is meant to plan for a campaign that will target married people or people with children at home, the condition in the IF function checks for the value of the columns [MaritalStatus] and [NumberChildrenAtHome], and outputs the city if either condition is met and if the customer is in California. Otherwise, it outputs the empty string.  
  
```dax
=IF([StateProvinceCode]= "CA" && ([MaritalStatus] = "M" || [NumberChildrenAtHome] >1),[City])  
```

Note that parentheses are used to control the order in which the AND (&amp;&amp;) and OR (||) operators are used. Also note that no value has been specified for **value_if_false**. Therefore, the function returns the default, which is an empty string.  
  
## See also  
[TRUE function &#40;DAX&#41;](true-function-dax.md)  
[FALSE function &#40;DAX&#41;](false-function-dax.md)  
[NOT function &#40;DAX&#41;](not-function-dax.md)  
[IF function &#40;DAX&#41;](if-function-dax.md)  
[DAX function reference](dax-function-reference.md)  
  
