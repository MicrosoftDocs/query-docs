---
description: "Learn more about: Operators"
title: "Operators"
ms.topic: language-reference
ms.date: 6/13/2025
ms.custom: "nonautomated-date"
ms.subservice: m-background
---

# Operators

The Power Query M formula language includes a set of operators that can be used in an expression. **Operators** are applied to **operands** to form symbolic expressions. For example, in the expression `1 + 2` the numbers `1` and `2` are operands and the operator is the addition operator (`+`).  
  
The meaning of an operator can vary depending on the type of operand values. The language has the following operators:  
  
### Plus operator (+)

|Expression|Equals|  
|--------------|----------|  
|`1 + 2`|Numeric addition: `3`|  
|`#time(12,23,0) + #duration(0,0,2,0)`|Time arithmetic: `#time(12,25,0)`|  
  
### Combination operator (&amp;)  
  
|Function|Equals|  
|------------|----------|  
|`"A" & "BC"`|Text concatenation: `"ABC"`|  
|`{1} & {2, 3}`|List concatenation: `{1, 2, 3}`|  
|`[ a = 1 ] & [ b = 2 ]`|Record merge: `[ a = 1, b = 2 ]`|  
  
### List of M operators

**Common operators** that apply to `null`, `logical`, `number`, `time`, `date`, `datetime`, `datetimezone`, `duration`, `text`, `binary`  
  
|Operator|Description|  
|------------|---------------|  
|`>`|Greater than|  
|`>=`|Greater than or equal|  
|`<`|Less than|  
|`<=`|Less than or equal|  
|`=`|Equal|  
|`<>`|Not equal|
|`??`|Null coalescing|
  
**Logical operators** (In addition to **Common operators**)  
  
|Operator|Description|  
|------------|---------------|  
|`or`|Conditional logical `OR`|  
|`and`|Conditional logical `AND`|  
|`not`|Logical `NOT`|  
  
**Number operators** (In addition to **Common operators**)  
  
|Operator|Description|  
|------------|---------------|  
|`+`|Sum|  
|`-`|Difference|  
|`*`|Product|  
|`/`|Quotient|  
|`+x`|Unary plus|  
|`-x`|Negation|  
  
**Text operators** (In addition to **Common operators**)  
  
|Operator|Description|  
|------------|---------------|  
|`&`|Concatenation|  
  
**List, record, table operators**
  
|Operator|Description|  
|------------|---------------|  
|`=`|Equal|  
|`<>`|Not equal|  
|`&`|Concatenation|  
  
**Record lookup operator**
  
|Operator|Description|  
|------------|---------------|  
|`[]`|Access the fields of a record by name.|  
  
**List indexer operator**
  
|Operator|Description|  
|------------|---------------|  
|`{}`|Access an item in a list by its zero-based numeric index.|  
  
**Type compatibility and assertion operators**
  
|Operator|Description|  
|------------|---------------|  
|`is`|The expression `x is y` returns `true` if the type of `x` is compatible with `y`, and returns `false` if the type of `x` is not compatible with `y`.|  
|`as`|The expression `x as y` asserts that the value `x` is compatible with `y` as per the `is` operator.|  
  
**Date operators**
  
|Operator|Left Operand|Right Operand|Meaning|  
|------------|----------------|-----------------|-----------|  
|`x + y`|`time`|`duration`|Date offset by duration|  
|`x + y`|`duration`|`time`|Date offset by duration|  
|`x - y`|`time`|`duration`|Date offset by negated duration|  
|`x - y`|`time`|`time`|Duration between dates|  
|`x & y`|`date`|`time`|Merged datetime|  
  
**Datetime operators**
  
|Operator|Left Operand|Right Operand|Meaning|  
|------------|----------------|-----------------|-----------|  
|`x + y`|`datetime`|`duration`|Datetime offset by duration|  
|`x + y`|`duration`|`datetime`|Datetime offset by duration|  
|`x - y`|`datetime`|`duration`|Datetime offset by negated duration|  
|`x - y`|`datetime`|`datetime`|Duration between datetimes|  
  
**Datetimezone operators**
  
|Operator|Left Operand|Right Operand|Meaning|  
|------------|----------------|-----------------|-----------|  
|`x + y`|`datetimezone`|`duration`|Datetimezone offset by duration|  
|`x + y`|`duration`|`datetimezone`|Datetimezone offset by duration|  
|`x - y`|`datetimezone`|`duration`|Datetimezone offset by negated duration|  
|`x - y`|`datetimezone`|`datetimezone`|Duration between datetimezones|  
  
**Duration operators**
  
|Operator|Left Operand|Right Operand|Meaning|  
|------------|----------------|-----------------|-----------|  
|`x + y`|`datetime`|`duration`|Datetime offset by duration|  
|`x + y`|`duration`|`datetime`|Datetime offset by duration|  
|`x + y`|`duration`|`duration`|Sum of durations|  
|`x - y`|`datetime`|`duration`|Datetime offset by negated duration|  
|`x - y`|`datetime`|`datetime`|Duration between datetimes|  
|`x - y`|`duration`|`duration`|Difference of durations|  
|`x * y`|`duration`|`number`|N times a duration|  
|`x * y`|`number`|`duration`|N times a duration|  
|`x / y`|`duration`|`number`|Fraction of a duration|  
  
> [!NOTE]  
> Not all combinations of values can be supported by an operator. Expressions that, when evaluated, encounter undefined operator conditions evaluate to errors. For more information about errors in M, go to [Errors](errors.md)  
  
**Error example**:  
  
|Function|Equals|  
|------------|----------|  
|`1 + "2"`|Error: adding number and text is not supported|  
  