---
description: "Learn more about: USERELATIONSHIP"
title: "USERELATIONSHIP function (DAX)"
---
# USERELATIONSHIP

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Specifies the relationship to be used in a specific calculation as the one that exists between columnName1 and columnName2.  
  
## Syntax  
  
```dax
USERELATIONSHIP(<columnName1>,<columnName2>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| `columnName1`  |  The name of an existing column, using standard DAX syntax and fully qualified, that usually represents the many side of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument cannot be an expression.  |  
| `columnName2` | The name of an existing column, using standard DAX syntax and fully qualified, that usually represents the one side or lookup side of the relationship to be used; if the arguments are given in reverse order the function will swap them before using them. This argument cannot be an expression.   |

## Return value

The function returns no value; the function only enables the indicated relationship for the duration of the calculation.  
  
## Remarks  
  
- USERELATIONSHIP can only be used in functions that take a filter as an argument, for example: CALCULATE, CALCULATETABLE, CLOSINGBALANCEMONTH, CLOSINGBALANCEQUARTER, CLOSINGBALANCEYEAR, OPENINGBALANCEMONTH, OPENINGBALANCEQUARTER, OPENINGBALANCEYEAR, TOTALMTD, TOTALQTD and TOTALYTD functions.  

- USERELATIONSHIP cannot be used when row level security is defined for the table in which the measure is included. For example, `CALCULATE(SUM([SalesAmount]), USERELATIONSHIP(FactInternetSales[CustomerKey], DimCustomer[CustomerKey]))` will return an error if row level security is defined for DimCustomer.
  
- USERELATIONSHIP uses existing relationships in the model, identifying  relationships by their ending point columns.  
  
- In USERELATIONSHIP, the status of a relationship is not important; that is, whether the relationship is active or not does not affect the usage of the function. Even if the relationship is inactive, it will be used and overrides any other active relationships that might be present in the model but not mentioned in the function arguments.  
  
- An error is returned if any of the columns named as an argument is not part of a relationship or the arguments belong to different relationships.  
  
- If multiple relationships are needed to join table A to table B in a calculation, each relationship must be indicated in a different USERELATIONSHIP function.  
  
- If CALCULATE expressions are nested, and more than one CALCULATE expression contains a USERELATIONSHIP function, then the innermost USERELATIONSHIP is the one that prevails in case of a conflict or ambiguity.  
  
- Up to 10 USERELATIONSHIP functions can be nested; however, your expression might have a deeper level of nesting, ie. the following sample expression is nested 3 levels deep but only 2 for USERELATIONSHIP: `=CALCULATE(CALCULATE( CALCULATE( <anyExpression>, USERELATIONSHIP( t1[colA], t2[colB])), t99[colZ]=999), USERELATIONSHIP( t1[colA], t2[colA]))`.  

- For 1-to-1 relationships, USERELATIONSHIP will only activate the relationship in one direction. In particular, filters will only be able to flow from *columnName2*'s table to *columnName1*'s table. If bi-directional cross-filtering is desired, two USERELATIONSHIPs with opposite directionality can be used in the same calculation. For example, `CALCULATE(..., USERELATIONSHIP(T1[K], T2[K]), USERELATIONSHIP(T2[K], T1[K]))`.
  
## Example

The following sample shows how to override the default, active, relationship between InternetSales and DateTime tables. The default relationship exists between the OrderDate column, in the InternetSales table, and the Date column, in the DateTime table.  
  
To calculate the sum of internet sales and allow slicing by ShippingDate instead of the traditional OrderDate, create measure, [InternetSales by ShippingDate] using the following expression:  
  
```dax
= CALCULATE(SUM(InternetSales[SalesAmount]), USERELATIONSHIP(InternetSales[ShippingDate], DateTime[Date]))  
```

Relationships between InternetSales[ShipmentDate] and DateTime[Date] must exist and should not be the active relationship; also, the relationship between InternetSales[OrderDate] and DateTime[Date] should exist and should be the active relationship.
