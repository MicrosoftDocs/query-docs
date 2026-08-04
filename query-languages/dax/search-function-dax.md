---
description: "Learn more about: SEARCH"
title: "SEARCH function (DAX)"
ms.topic: reference
ms.date: 06/29/2026
ms.custom: ExampleTypeAW2020
---
# SEARCH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the number of the character at which a specific character or text string is first found, reading left to right. Search is case-insensitive, kanatype-insensitive, width-insensitive, and accent sensitive.

## Syntax

```dax
SEARCH(<find_text>, <within_text>[, [<start_num>][, <NotFoundValue>]])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`find_text`|The text that you want to find.<br /><br />You can use wildcard characters — the question mark (?) and asterisk (\*) — in `find_text`. A question mark matches any single character; an asterisk matches any sequence of characters. If you want to find an actual question mark or asterisk, type a tilde (~) before the character.|
|`within_text`|The text in which you want to search for `find_text`, or a column containing text.|
|`start_num`|(optional) The character position in `within_text` at which you want to start searching. If omitted, 1.|
|`NotFoundValue`|(optional, but strongly recommended) The value to return when the operation doesn't find a matching substring, typically 0, -1, or BLANK(). If you don't specify it, the function returns an error.|

## Return value

The number of the starting position of the first text string from the first character of the second text string.

## Remarks

- The search function is case insensitive. Searching for "N" finds the first occurrence of 'N' or 'n'.

- The search function is kanatype-insensitive, width-insensitive. Searching for "か" finds the first occurrence of 「か」 (hiragana), 「カ」 (katakana), or 「ｶ」 (half-width katakana).

- The search function is accent sensitive. Searching for "á" finds the first occurrence of 'á' but no occurrences of 'a', 'à', or the capitalized versions 'A', 'Á'.

- You can use the SEARCH function to determine the location of a character or text string within another text string, and then use the MID function to return the text, or use the REPLACE function to change the text.

- If the `find_text` can't be found in `within_text`, the formula returns an error. This behavior is like Excel, which returns #VALUE if the substring isn't found. Nulls in `within_text` are interpreted as an empty string in this context.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query finds the position of the first letter of "cycle", in the string that contains the reseller name. If not found, SEARCH returns Blank.

SEARCH is case-insensitive. In this example, if you use "cycle" or "Cycle" in the `find_text` argument, the query returns results for either case. Use [FIND](FIND-function-dax.md) for case-sensitive.

[!INCLUDE [power-bi-dax-sample-model](includes/power-bi-dax-sample-model.md)]

```dax
EVALUATE
CALCULATETABLE (
    ADDCOLUMNS (
        TOPN ( 10, SUMMARIZE ( 'Reseller', [Reseller], [Business Type] ) ),
        "Position of cycle", SEARCH ( "cycle", 'Reseller'[Reseller], 1, BLANK () )
    ),
    'Reseller'[Business Type]
        IN { "Specialty Bike Shop", "Value Added Reseller", "Warehouse" }
)
```

Returns,

|Reseller  |Business Type | Position of cycle |
|---------|---------|---------|
|Volume Bike Sellers    |Warehouse|        |
|Mass Market Bikes     |Value Added Reseller|         |
|Twin Cycles     |Value Added Reseller|     6    |
|Rich Department Store     |Warehouse|         |
|Rental Gallery     |Specialty Bike Shop|         |
|Budget Toy Store     |Warehouse|         |
|Global Sports Outlet     |Warehouse|         |
|Online Bike Catalog     |Warehouse|         |
|Helmets and Cycles     |Value Added Reseller|    13     |
|Jumbo Bikes     |Specialty Bike Shop|         |

## Related content

- [FIND](find-function-dax.md)
- [REPLACE](replace-function-dax.md)
- [Text functions](text-functions-dax.md)
