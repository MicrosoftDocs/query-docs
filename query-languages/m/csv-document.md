---
title: "Csv.Document | Microsoft Docs"
ms.date: 4/17/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Csv.Document
<code>Csv.Document(<b>source</b> as any, optional <b>columns</b> as any, optional <b>delimiter</b> as any, optional <b>extraValues</b> as nullable number, optional <b>encoding</b> as nullable number) as table</code>

## About
Returns the contents of the CSV document as a table. <ul> <li> <code>columns</code> can be null, the number of columns, a list of column names, a table type, or an options record. (See below for more details on the options record.)</li> <li> <code>delimiter</code> can be a single character, or a list of characters. Default: <code>","</code>.</li> <li> Please refer to <code>ExtraValues.Type</code> for the supported values of <code>extraValues</code>.</li> <li> <code>encoding</code> specifies the text encoding type.</li> </ul> If a record is specified for <code>columns</code> (and <code>delimiter</code>, <code>extraValues</code>, and <code>encoding</code> are null), the following record fields may be provided: <ul> <li> <code>Delimiter</code>: The column delimiter. Default: <code>","</code>.</li> <li> <code>Columns</code>: Can be null, the number of columns, a list of column names, or a table type. If the number of columns is lower than the number found in the input, the additional columns will be ignored. If the number of columns is higher than the number found in the input, the additional columns will be null. When not specified, the number of columns will be determined by what is found in the input.</li> <li> <code>Encoding</code>: The text encoding of the file. Default: 65001 (UTF-8).</li> <li> <code>CsvStyle</code>: Specifies the significance of quotes. <code>CsvStyle.QuoteAlways</code> (default): Quotes in a field are always significant, regardless of where they appear. <code>CsvStyle.QuoteAfterDelimiter</code>: Quotes in a field are only significant immediately following the delimiter.</li> <li> <code>QuoteStyle</code>: Specifies the quote style / field qualifier to use when values contain delimiters. <code>QuoteStyle.None</code> (default): Field qualifiers are not used. <code>QuoteStyle.Csv</code>: Quoting follows the format specified in RFC 4180. A double quote character is used to demarcate such regions, and a pair of double quote characters is used to indicate a single double quote character within such a region.</li> </ul> 

## Example 1
Process CSV text with column headers

```
Table.PromoteHeaders(Csv.Document("OrderID,Item 1,Fishing rod 2,1 lb. worms"))
```

|OrderID  |Item  |
|---------|---------|
|1     |   Fishing rod      |
|2     |   1 lb. worms      |

