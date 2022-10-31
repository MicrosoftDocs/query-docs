---
description: "Learn more about: EvaluateAndLog"
title: "EvaluateAndLog function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 10/26/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# EvaluateAndLog

Returns the value of the first argument and logs it in a DAX evaluation log. This function applies to Power BI Desktop only.
  
## Syntax  
  
```dax
EvaluateAndLog(<Value>, [Label], [MaxRows])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Value|Any scalar value or table expression to be logged.|  
|Label|(Optional) A constant string.|  
|MaxRows|(Optional) The maximum number of rows output to the DAX evaluation log when the first argument is a table expression. If the value is a scalar, this parameter is ignored. Default is 10.|
  
## Return value

First argument.

## Remarks

- You can wrap this function around almost any expression in a DAX query and the whole query will still be valid.

- Value is logged together with its arguments for every set of arguments.

- If the argument is a table, then only the top MaxRows rows are shown.

- The label parameter is included in the event return. The string can make finding specific logs more convenient in cases where multiple EvaluateAndLog expressions are used in a single query.

- In some cases, this function is not executed due to optimizations.

- If the log is greater than one million symbols, it is truncated (preserving correct json structure).
  
## Example 1

The following DAX query:

```dax
evaluate
SUMMARIZE(
    EvaluateAndLog(FILTER(FactInternetSales, [ProductKey] = 528)),
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

## Example 2

The following DAX query with a scalar argument and varying attributes:

```dax
evaluate
SELECTCOLUMNS(
    TOPN(5, DimCustomer),
    [FirstName],
    [LastName],
    "FullName",
    EvaluateAndLog([FirstName] & " " & [LastName], "myLog")
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

“expression” as a text version of logged expression.

“inputs” as names of varying attributes. In this example, the expression has no varying attributes.

“outputs” as names of columns of logged expressions.

“data” contains expression values for every varying attribute as well as values of attributes.

“RowCount” is the number of rows for a table specified as Value.

“Label” is the Label parameter specified in the expression.

## See also

[ToCSV](tocsv-function-dax.md)  
[ToJSON](tojson-function-dax.md)  
