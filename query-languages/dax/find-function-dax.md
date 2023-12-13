---
description: "Learn more about: FIND"
title: "FIND function (DAX) | Microsoft Docs"
---
# FIND

Returns the starting position of one text string within another text string. FIND is case-sensitive.  
  
## Syntax  
  
```dax
FIND(<find_text>, <within_text>[, [<start_num>][, <NotFoundValue>]])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|find_text|The text you want to find. Use double quotes (empty text) to match the first character in **within_text**. |
|within_text|The text containing the text you want to find.|  
|start_num|(optional) The character at which to start the search; if omitted, **start_num** = 1. The first character in **within_text** is character number 1.|  
|NotFoundValue|(optional, but strongly recommended) The value that should be returned when the operation does not find a matching substring, typically 0, -1, or BLANK(). If not specified, an error is returned.|  
  
## Return value

Number that shows the starting point of the text string you want to find.  
  
## Remarks

- Whereas Microsoft Excel has multiple versions of the FIND function to accommodate single-byte character set (SBCS) and double-byte character set (DBCS) languages, DAX uses Unicode and counts each character the same way; therefore, you do not need to use a different version depending on the character type.  
  
- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

- FIND does not support wildcards. To use wildcards, use [SEARCH](search-function-dax.md).
  
## Example

The following DAX query finds the position of the first letter of "Bike", in the string that contains the reseller name. If not found, Blank is returned.

Keep in mind, FIND is case-sensitive. In this example, if "bike" were used in the \<find_text> argument, no results would be returned. Use [SEARCH](search-function-dax.md) for case-insensitive.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]
  
```dax
EVALUATE
CALCULATETABLE (
    ADDCOLUMNS (
        TOPN ( 10, SUMMARIZE('Reseller', [Reseller], [Business Type])),
        "Position of Bike", FIND ( "Bike", 'Reseller'[Reseller], 1, BLANK () )
    ),
    'Reseller'[Business Type] IN { "Specialty Bike Shop", "Value Added Reseller", "Warehouse"}
)
```

Returns,  

|Reseller  |Business Type | Position of Bike |
|---------|---------|---------|
|Volume Bike Sellers    |Warehouse|     8    |
|Mass Market Bikes     |Value Added Reseller|    13     |
|Twin Cycles     |Value Added Reseller|         |
|Rich Department Store     |Warehouse|         |
|Rental Gallery     |Specialty Bike Shop|         |
|Budget Toy Store     |Warehouse|         |
|Global Sports Outlet     |Warehouse|         |
|Online Bike Catalog     |Warehouse|     8    |
|Helmets and Cycles     |Value Added Reseller|         |
|Jumbo Bikes     |Specialty Bike Shop|    7     |

## Related content

[SEARCH](search-function-dax.md)  
[Text functions](text-functions-dax.md)  
