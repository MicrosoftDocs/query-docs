---
description: "Learn more about: DateTime.ToRecord"
title: "DateTime.ToRecord | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.ToRecord

## Syntax

<pre>
DateTime.ToRecord(<b>dateTime</b> as datetime) as record
</pre>
  
## About  
Returns a record containing the parts of the given datetime value, `dateTime`. <ul> <li><code>dateTime</code>: A <code>datetime</code> value for from which the record of its parts is to be calculated.</li> </ul>

## Example 1
Convert the `#datetime(2011, 12, 31, 11, 56, 2)` value into a record containing Date and Time values.

```powerquery-m
DateTime.ToRecord(#datetime(2011, 12, 31, 11, 56, 2))
```

<table> <tr> <th>Year</th> <td>2011</td> </tr> <tr> <th>Month</th> <td>12</td> </tr> <tr> <th>Day</th> <td>31</td> </tr> <tr> <th>Hour</th> <td>11</td> </tr> <tr> <th>Minute</th> <td>56</td> </tr> <tr> <th>Second</th> <td>2</td> </tr> </table>
