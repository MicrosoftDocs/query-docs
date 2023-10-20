---
description: "Learn more about: CALCULATE"
title: "CALCULATE function (DAX) | Microsoft Docs"
---
# CALCULATE

Evaluates an expression in a modified filter context.

> [!NOTE]
> There's also the [CALCULATETABLE](calculatetable-function-dax.md) function. It performs exactly the same functionality, except it modifies the [filter context](dax-overview.md#filter-context) applied to an expression that returns a _table object_.
>
>

## Syntax

```dax
CALCULATE(<expression>[, <filter1> [, <filter2> [, …]]])
```

### Parameters

|Term|Definition|
|--------|--------------|
|expression|The expression to be evaluated.|
|filter1, filter2,…|(Optional) Boolean expressions or table expressions that defines filters, or filter modifier functions.|

The expression used as the first parameter is essentially the same as a measure.

Filters can be:

- Boolean filter expressions
- Table filter expressions
- Filter modification functions

When there are multiple filters, they can be evaluated by using the AND (&&) [logical operator](dax-operator-reference.md#logical-operators), meaning all conditions must be TRUE, or by the OR (||) logical operator, meaning either condition can be true.

#### Boolean filter expressions

A Boolean expression filter is an expression that evaluates to TRUE or FALSE. There are several rules that they must abide by:

- They can reference columns from a single table.
- They cannot reference measures.
- They cannot use a nested CALCULATE function.

Beginning with the September 2021 release of Power BI Desktop, the following also apply:

- They cannot use functions that scan or return a table unless they are passed as arguments to aggregation functions.
- They *can* contain an aggregation function that returns a scalar value. For example,
    ```dax
    Total sales on the last selected date =
    CALCULATE (
        SUM ( Sales[Sales Amount] ),
        'Sales'[OrderDateKey] = MAX ( 'Sales'[OrderDateKey] )
    )
    ```

#### Table filter expression

A table expression filter applies a table object as a filter. It could be a reference to a model table, but more likely it's a function that returns a table object. You can use the [FILTER](filter-function-dax.md) function to apply complex filter conditions, including those that cannot be defined by a Boolean filter expression.

#### Filter modifier functions

Filter modifier functions allow you to do more than simply add filters. They provide you with additional control when modifying filter context.

|Function|Purpose|
|--------|--------------|
|[REMOVEFILTERS](removefilters-function-dax.md)|Remove all filters, or filters from one or more columns of a table, or from all columns of a single table.|
|[ALL](all-function-dax.md) <sup>1</sup>, [ALLEXCEPT](allexcept-function-dax.md), [ALLNOBLANKROW](allnoblankrow-function-dax.md)|Remove filters from one or more columns, or from all columns of a single table.|
|[KEEPFILTERS](keepfilters-function-dax.md)|Add filter without removing existing filters on the same columns.|
|[USERELATIONSHIP](userelationship-function-dax.md)|Engage an inactive relationship between related columns, in which case the active relationship will automatically become inactive.|
|[CROSSFILTER](crossfilter-function.md)|Modify filter direction (from both to single, or from single to both) or disable a relationship.|

<sup>1</sup> The ALL function and its variants behave as both filter modifiers and as functions that return table objects. If the REMOVEFILTERS function is supported by your tool, it's better to use it to remove filters.

## Return value

The value that is the result of the expression.

## Remarks

- When filter expressions are provided, the CALCULATE function modifies the filter context to evaluate the expression. For each filter expression, there are two possible standard outcomes when the filter expression is not wrapped in the KEEPFILTERS function:
  - If the columns (or tables) aren't in the filter context, then new filters will be added to the filter context to evaluate the expression.
  - If the columns (or tables) are already in the filter context, the existing filters will be overwritten by the new filters to evaluate the CALCULATE expression.

- The CALCULATE function used _without filters_ achieves a specific requirement. It transitions row context to filter context. It's required when an expression (not a model measure) that summarizes model data needs to be evaluated in row context. This scenario can happen in a calculated column formula or when an expression in an iterator function is evaluated. Note that when a model measure is used in row context, context transition is automatic.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Examples

The following **Sales** table measure definition produces a revenue result, but only for products that have the color blue.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
Blue Revenue =
CALCULATE(
    SUM(Sales[Sales Amount]),
    'Product'[Color] = "Blue"
)
```

|Category|Sales Amount|Blue Revenue|
|--------|------------|------------|
|Accessories|$1,272,057.89|$165,406.62|
|Bikes|$94,620,526.21|$8,374,313.88|
|Clothing|$2,117,613.45|$259,488.37|
|Components|$11,799,076.66|$803,642.10|
|**Total**|**$109,809,274.20**|**$9,602,850.97**|

The CALCULATE function evaluates the sum of the **Sales** table **Sales Amount** column in a modified filter context. A new filter is added to the **Product** table **Color** column—or, the filter overwrites any filter that's already applied to the column.

The following **Sales** table measure definition produces a ratio of sales over sales for all sales channels.

|Channel|Sales Amount|Revenue % Total Channel|  
|-------|------------|-----------------------|
|Internet|$29,358,677.22|26.74%|
|Reseller|$80,450,596.98|73.26%|
|**Total**|**$109,809,274.20**|**100.00%**|

```dax
Revenue % Total Channel =
DIVIDE(
    SUM(Sales[Sales Amount]),
    CALCULATE(
        SUM(Sales[Sales Amount]),
        REMOVEFILTERS('Sales Order'[Channel])
    )
)
```

The [DIVIDE](divide-function-dax.md) function divides an expression that sums of the **Sales** table **Sales Amount** column value (in the filter context) by the same expression in a modified filter context. It's the CALCULATE function that modifies the filter context by using the REMOVEFILTERS function, which is a filter modifier function. It removes filters from the **Sales Order** table **Channel** column.

The following **Customer** table calculated column definition classifies customers into a loyalty class.  It's a very simple scenario: When the revenue produced by the customer is less than $2500, they're classified as _Low_; otherwise they're _High_.

```dax
Customer Segment =
IF(
    CALCULATE(SUM(Sales[Sales Amount]), ALLEXCEPT(Customer, Customer[CustomerKey])) < 2500,
    "Low",
    "High"
)
```

In this example, row context is converted to the filter context. It's known as _context transition_. The [ALLEXCEPT](allexcept-function-dax.md) function removes filters from all **Customer** table columns except the **CustomerKey** column.

## See also

[Filter context](dax-overview.md#filter-context)  
[Row context](dax-overview.md#row-context)  
[CALCULATETABLE function](calculatetable-function-dax.md)  
[Filter functions](filter-functions-dax.md)  
