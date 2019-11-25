---
title: "Date.ToRecord | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.ToRecord

## Syntax

<pre>
Date.ToRecord(<b>date</b> as date) as record
</pre>
  
## About  
Returns a record containing the parts of the given date value, `date`. <ul> <li><code>date</code>: A <code>date</code> value for from which the record of its parts is to be calculated.</li> </ul>

## Example 1
Convert the `#date(2011, 12, 31)` value into a record containing parts from the date value.

```powerquery-m
Date.ToRecord(#date(2011, 12, 31))
```

<table> <tr> <th>Year</th> <td>2011</td> </tr> <tr> <th>Month</th> <td>12</td> </tr> <tr> <th>Day</th> <td>31</td> </tr> </table>
