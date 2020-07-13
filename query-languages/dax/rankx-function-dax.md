---
title: "RANKX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# RANKX

Returns the ranking of a number in a list of numbers for each row in the *table* argument.  
  
## Syntax  
  
```dax
RANKX(<table>, <expression>[, <value>[, <order>[, <ties>]]])  
```
  
### Parameters

**table**  
Any DAX expression that returns a table of data over which the expression is evaluated.  
  
**expression**  
Any DAX  expression that returns a single scalar value. The expression is evaluated for each row of *table*, to generate all possible values for ranking. See the remarks section to understand the function behavior when *expression* evaluates to BLANK.  
  
**value**  
(Optional) Any DAX expression that returns a single scalar value whose rank is to be found. See the remarks section to understand the function's behavior when *value* is not found in the expression.  
  
When the *value* parameter is omitted, the value of expression at the current row is used instead.  
  
**order**  
(Optional) A value that specifies how to rank *value*, low to high or high to low:  

|value|alternate value|Description|
|-----|-----|-----|
|0 (zero)|FALSE|Ranks in descending order of values of expression. If value is equal to the highest number in expression then RANKX returns 1.<br /><br />This is the default value when order parameter is omitted.|  
|1|TRUE|Ranks in ascending order of expression. If value is equal to the lowest number in expression then RANKX returns 1.|  
  
**ties**  
(Optional) An enumeration that defines how to determine ranking when there are ties.  

|enumeration|Description|  
|-----|-----|  
|Skip|The next rank value, after a tie, is the rank value of the tie plus the count of tied values. For example if five (5) values are tied with a rank of 11 then the next value will receive a rank of 16 (11 + 5).<br /><br />This is the default value when *ties* parameter is omitted.|  
|Dense|The next rank value, after a tie, is the next rank value. For example if five (5) values are tied with a rank of 11 then the next value will receive a rank of 12.|  
  
## Return value

The rank number of *value* among all possible values of *expression* evaluated for all rows of *table* numbers.  
  
## Remarks  
  
- If *expression* or *value* evaluates to BLANK it is treated as a 0 (zero) for all expressions that result in a number, or as an empty text for all text expressions.  
  
- If *value* is not among all possible values of *expression* then RANKX temporarily adds *value* to the values from *expression* and re-evaluates RANKX to determine the proper rank of *value*.  
  
- Optional arguments might be skipped by placing an empty comma (,) in the argument list, i.e. RANKX(Inventory, [InventoryCost],,,"Dense")  
  
## Example

The following calculated column in the Products table calculates the sales ranking for each product in the Internet channel.  
  
```dax
= RANKX(ALL(Products), SUMX(RELATEDTABLE(InternetSales), [SalesAmount]))  
```
