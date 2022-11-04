---
description: "Learn more about: EVALUATEANDLOG"
title: "EVALUATEANDLOG function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 10/26/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# EVALUATEANDLOG

Returns the value of the first argument and logs it in Trace event, DAX Evaluation Log. This function applies to Power BI Desktop only.
  
## Syntax  
  
```dax
EVALUATEANDLOG(<Value>, [Label], [MaxRows])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Value|Any scalar value or table expression to be logged. The value of the expression is returned, as well as entered in JSON format to the DAX Evaluation Log event.|  
|Label|(Optional) A constant string included in the event return. Labels help identify and differentiate between multiple EVALUATEANDLOG expressions in the same query.|  
|MaxRows|(Optional) The maximum number of rows output when the first argument is a table expression. Default is 10. If the value is a scalar, this parameter is ignored. |
  
## Return value

Result of the expression.

## Remarks

- Trace events can be captured by using [SQL Server Profiler](/analysis-services/instances/use-sql-server-profiler-to-monitor-analysis-services) and the open-source [DAX Debug Output](https://github.com/pbidax/DAXDebugOutput/releases/) tool.
- This function does not change the result of the Value expression.

- Value is logged together with its arguments for every set of arguments.

- If the argument for Value is a table, only the top MaxRows rows are shown.

- In some cases, this function is not executed due to optimizations.

- If the DAX Evaluation Log event is greater than one million characters, it's truncated to preserve correct json structure.
  
## Example 1

The following DAX query:

```dax
evaluate
SUMMARIZE(
    EVALUATEANDLOG(FILTER(FactInternetSales, [ProductKey] = 528)),
    FactInternetSales[SalesTerritoryKey],
    "sum",
    sum(FactInternetSales[SalesAmount])
)
```

Returns the following log:

```json
{
    "expression": "SELECTCOLUMNS(FILTER(FactInternetSales, [ProductKey] = 528), \n\t\t[SalesTerritoryKey], \n\t\t[ProductKey], \n\t\t[SalesAmount],\n\t\t[OrderDate]\n\t\t)",
    "inputs": [],
    "outputs": ["'FactInternetSales'[SalesTerritoryKey]", "'FactInternetSales'[ProductKey]", "'FactInternetSales'[SalesAmount]", "'FactInternetSales'[OrderDate]"],
    "data": [
        {
            "input": [],
            "rowCount": 3095,
            "output": [
                [4, 528, 4.99, "2013-02-04T00:00:00"],
                [4, 528, 4.99, "2013-02-04T00:00:00"],
                [4, 528, 4.99, "2013-02-04T00:00:00"],
                [4, 528, 4.99, "2013-02-03T00:00:00"],
                [4, 528, 4.99, "2013-02-03T00:00:00"],
                [4, 528, 4.99, "2013-02-01T00:00:00"],
                [4, 528, 4.99, "2013-01-31T00:00:00"],
                [4, 528, 4.99, "2013-01-31T00:00:00"],
                [4, 528, 4.99, "2013-01-29T00:00:00"],
                [4, 528, 4.99, "2013-01-28T00:00:00"]
            ]
        }
    ]
}
```

The JSON log structure for this example includes:

- “expression” as a text version of logged expression.
- “inputs” as names of varying attributes. In this example, the expression has no varying attributes.
- “outputs” as names of columns of logged expressions.
- “data” contains expression values for every varying attribute as well as values of attributes.
- “RowCount” is the number of rows for a table specified as Value.

## Example 2

The following DAX query with a scalar argument and varying attributes:

```dax
evaluate
SELECTCOLUMNS(
    TOPN(5, DimCustomer),
    [FirstName],
    [LastName],
    "FullName",
    EVALUATEANDLOG([FirstName] & " " & [LastName], "myLog")
)

```

Returns the following log:

```json
{
    "expression": "[FirstName] & \" \" & [LastName]",
    "label": "myLog",
    "inputs": ["'DimCustomer'[FirstName]", "'DimCustomer'[LastName]"],
    "data": [
        {
            "input": ["Larry", "Gill"],
            "output": "Larry Gill"
        },
        {
            "input": ["Geoffrey", "Gonzalez"],
            "output": "Geoffrey Gonzalez"
        },
        {
            "input": ["Blake", "Collins"],
            "output": "Blake Collins"
        },
        {
            "input": ["Alexa", "Watson"],
            "output": "Alexa Watson"
        },
        {
            "input": ["Jacquelyn", "Dominguez"],
            "output": "Jacquelyn Dominguez"
        }
    ]
}

```

The JSON log structure for this example includes:

- “expression” as a text version of logged expression.
- “Label” is the Label parameter specified in the expression.
- “inputs” as names of varying attributes. In this example, the expression has no varying attributes.
- “outputs” as names of columns of logged expressions.
- “data” contains expression values for every varying attribute as well as values of attributes.
- “RowCount” is the number of rows for a table specified as Value.

## See also

[TOCSV](tocsv-function-dax.md)  
[TOJSON](tojson-function-dax.md)  
