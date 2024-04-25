---
description: "Learn more about: EVALUATEANDLOG"
title: "EVALUATEANDLOG function (DAX) | Microsoft Docs"
---
# EVALUATEANDLOG

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the value of the first argument and logs it in a DAX Evaluation Log profiler event. This function is fully functional in Power BI Desktop only. It acts as a simple passthrough function in other environments.
  
## Syntax  
  
```dax
EVALUATEANDLOG(<Value>, [Label], [MaxRows])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Value|Any scalar expression or table expression to be evaluated and logged.|  
|Label|(Optional) A constant string included in both the json text and the Label column of the DAX Evaluation Log event that can be used to easily identify an instance of the function call.|  
|MaxRows|(Optional) The maximum number of rows in the json text of the DAX Evaluation Log event when the first argument is a table expression. Default is 10.|
  
## Return value

The value of the first argument.

The JSON structure logged in a DAX Evaluation Log profiler event includes:

- “expression” is the text version of the first argument.
- “label” is the Label parameter when specified in the expression.
- “inputs” is a list of columns in the evaluation context that affects the values of the first argument.
- “outputs” is a list of a single column [Value] when the first argument is a scalar expression and a list of output columns when the first argument is a table expression.
- “data” is a list of input values and output values when the first argument is a scalar expression, and a list of input values and corresponding output rows when the first argument is a table expression.
- “rowCount” is the number of rows when the first argument is a table expression. Even though the number of rows in the json output is truncated by the MaxRows parameter, rowCount is the real number of rows without truncation.

## Remarks

- Trace events can be captured by using [SQL Server Profiler](/analysis-services/instances/use-sql-server-profiler-to-monitor-analysis-services) and the open-source [DAX Debug Output](https://github.com/pbidax/DAXDebugOutput/releases/) tool.
- This function can be used with almost any sub-expression in a DAX expression, and the entire expression will still be valid.

- When the first argument is evaluated multiple times in a single query, the function generates a single DAX Evaluation Log event that contains both the input values and the corresponding output values.

- When the label parameter is specified, its value is returned in both the json output and the Label column of the DAX Evaluation Log event.

- If the first argument is a table expression, only the top MaxRows rows are shown in the DAX Evaluation Log event.

- In some cases, this function is not executed due to optimizations.

- If the DAX Evaluation Log event is greater than one million characters, it's truncated to preserve correct json structure.
  
## Example 1

The following DAX query:

```dax
evaluate
SUMMARIZE(
    EVALUATEANDLOG(FILTER(Sales, [ProductKey] = 528)),
    Sales[SalesTerritoryKey],
    "sum",
    sum(Sales[Sales Amount])
)
```

Returns the following DAX Evaluation Log event:

```json
{
    "expression": "FILTER(Sales, [ProductKey] = 528)",
    "inputs": [],
    "outputs": ["'Sales'[SalesOrderLineKey]", "'Sales'[ResellerKey]", "'Sales'[CustomerKey]", "'Sales'[ProductKey]", "'Sales'[OrderDateKey]", "'Sales'[DueDateKey]", "'Sales'[ShipDateKey]", "'Sales'[SalesTerritoryKey]", "'Sales'[Order Quantity]", "'Sales'[Unit Price]", "'Sales'[Extended Amount]", "'Sales'[Product Standard Cost]", "'Sales'[Total Product Cost]", "'Sales'[Sales Amount]", "'Sales'[Unit Price Discount Pct]"],
    "data": [
        {
            "input": [],
            "rowCount": 3095,
            "output": [
                [52174001, -1, 23785, 528, 20190707, 20190717, 20190714, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [52173001, -1, 26278, 528, 20190707, 20190717, 20190714, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [52082001, -1, 23831, 528, 20190705, 20190715, 20190712, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [52054002, -1, 11207, 528, 20190704, 20190714, 20190711, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [52036001, -1, 25337, 528, 20190704, 20190714, 20190711, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [51939002, -1, 23670, 528, 20190702, 20190712, 20190709, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [51911002, -1, 11746, 528, 20190701, 20190711, 20190708, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [51379003, -1, 13745, 528, 20190612, 20190622, 20190619, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [51264002, -1, 11282, 528, 20190605, 20190615, 20190612, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0],
                [51184003, -1, 11263, 528, 20190531, 20190610, 20190607, 1, 1, 4.99, 4.99, 1.8663, 1.8663, 4.99, 0.0]
            ]
        }
    ]
}
```

## Example 2

The following DAX query with a scalar argument and varying attributes:

```dax
evaluate
SELECTCOLUMNS(
    TOPN(5, Customer),
    [Customer],
    "Customer",
    EVALUATEANDLOG([Customer] & ", " & [Country-Region], "customerLog")
)

```

Returns the following DAX Evaluation Log event:

```json
{
    "expression": "[Customer] & \", \" & [Country-Region]",
    "label": "customerLog",
    "inputs": ["'Customer'[Customer]", "'Customer'[Country-Region]"],
    "data": [
        {
            "input": ["Russell Xie", "United States"],
            "output": "Russell Xie, United States"
        },
        {
            "input": ["Savannah Baker", "United States"],
            "output": "Savannah Baker, United States"
        },
        {
            "input": ["Maurice Tang", "United States"],
            "output": "Maurice Tang, United States"
        },
        {
            "input": ["Emily Wood", "United States"],
            "output": "Emily Wood, United States"
        },
        {
            "input": ["Meghan Hernandez", "United States"],
            "output": "Meghan Hernandez, United States"
        }
    ]
}

```

## Related content

[TOCSV](tocsv-function-dax.md)  
[TOJSON](tojson-function-dax.md)  
