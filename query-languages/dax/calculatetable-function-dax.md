---
description: "Learn more about: CALCULATETABLE"
title: "CALCULATETABLE function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/06/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CALCULATETABLE

Evaluates a table expression in a modified filter context.

> [!NOTE]
> There's also the [CALCULATE](calculate-function-dax.md) function. It performs exactly the same functionality, except it modifies the [filter context](dax-overview.md#filter-context) applied to an expression that returns a _scalar value_.
>
>

## Syntax  

```dax
CALCULATETABLE(<expression>[, <filter1> [, <filter2> [, …]]])
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|expression|The table expression to be evaluated.|
|filter1, filter2,…|(Optional) Boolean expressions or table expressions that defines filters, or filter modifier functions.|

The expression used as the first parameter must be a model table or a function that returns a table.

Filters can be:

- Boolean filter expressions
- Table filter expressions
- Filter modification functions

When there are multiple filters, they're evaluated by using the AND [logical operator](dax-operator-reference.md#logical-operators). That means all conditions must be TRUE at the same time.

#### Boolean filter expressions

A Boolean expression filter is an expression that evaluates to TRUE or FALSE. There are several rules that they must abide by:

- They can reference only a single column.
- They cannot reference measures.
- They cannot use a nested CALCULATE function.
- They cannot use functions that scan or return a table, including aggregation functions.

#### Table filter expression

A table expression filter applies a table object as a filter. It could be a reference to a model table, but more likely it's a function that returns a table object. You can use the [FILTER](filter-function-dax.md) function to apply complex filter conditions, including those that cannot be defined by a Boolean filter expression.

#### Filter modifier functions

Filter modification functions allow you to do more than simply add filters. They provide you with additional control when modifying filter context.

|Function|Purpose|
|--------|--------------|
|[REMOVEFILTERS](removefilters-function-dax.md)|Remove all filters, or filters from one or more columns of a table, or from all columns of a single table.|
|[ALL](all-function-dax.md) <sup>1</sup>, [ALLEXCEPT](allexcept-function-dax.md), [ALLNOBLANKROW](allnoblankrow-function-dax.md)|Remove filters from one or more columns, or from all columns of a single table.|
|[KEEPFILTERS](keepfilters-function-dax.md)|Add filter without removing existing filters on the same columns.|
|[USERELATIONSHIP](userelationship-function-dax.md)|Engage an inactive relationship between related columns, in which case the active relationship will automatically become inactive.|
|[CROSSFILTER](crossfilter-function.md)|Modify filter direction (from both to single, or from single to both) or disable a relationship.|

<sup>1</sup> The ALL function and its variants behave as both filter modifiers and as functions that return table objects. If the REMOVEFILTERS function is supported by your tool, it's better to use it to remove filters.

## Return value

A table of values.

## Remarks

- When filter expressions are provided, the CALCULATETABLE function modifies the filter context to evaluate the expression. For each filter expression, there are two possible standard outcomes when the filter expression is not wrapped in the KEEPFILTERS function:
  - If the columns (or tables) aren't in the filter context, then new filters will be added to the filter context to evaluate the expression.
  - If the columns (or tables) are already in the filter context, the existing filters will be overwritten by the new filters to evaluate the CALCULATETABLE expression.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example uses the CALCULATETABLE function to get the sum of Internet sales for 2006. This value is later used to calculate the ratio of Internet sales compared to all sales for the year 2006.  

The following formula:

```dax
= SUMX(
    CALCULATETABLE(
        'InternetSales_USD',
        'DateTime'[CalendarYear] = 2006
    ),
    [SalesAmount_USD]
)  
```

It results in the following table:

|Row Labels|Internet SalesAmount_USD|CalculateTable 2006 Internet Sales|Internet Sales to 2006 ratio|  
|--------------|-----------------------------|--------------------------------------|--------------------------------|  
|2005|$2,627,031.40|$5,681,440.58|0.46|  
|2006|$5,681,440.58|$5,681,440.58|1.00|  
|2007|$8,705,066.67|$5,681,440.58|1.53|  
|2008|$9,041,288.80|$5,681,440.58|1.59|  
|Grand Total|$26,054,827.45|$5,681,440.58|4.59|  

## See also

- [Filter context](dax-overview.md#filter-context)
- [CALCULATE function (DAX)](calculate-function-dax.md)
- [Filter functions (DAX)](filter-functions-dax.md)
