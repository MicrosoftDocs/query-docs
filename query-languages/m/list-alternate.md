---
title: "List.Alternate | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.Alternate

## Syntax

<pre>
List.Alternate(<b>list</b> as list, <b>count</b> as number, optional <b>repeatInterval</b> as nullable number, optional <b>offset</b> as nullable number) as list 
</pre>
  
## About  
Returns a list comprised of all the odd numbered offset elements in a list. Alternates between taking and skipping values from the list `list` depending on the parameters. <ul> <li><code>count</code>: Specifies number of values that are skipped each time.</li> <li><code>repeatInterval</code>: An optional repeat interval to indicate how many values are added in between the skipped values.</li> <li><code>offset</code>: An option offset parameter to begin skipping the values at the initial offset.</li> </ul>

## Example 1
Create a list from {1..10} that skips the first number.

```powerquery-m
List.Alternate({1..10}, 1)
```

<table> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> <tr><td>6</td></tr> <tr><td>7</td></tr> <tr><td>8</td></tr> <tr><td>9</td></tr> <tr><td>10</td></tr> </table>

## Example 2
Create a list from {1..10} that skips the every other number.

```powerquery-m
List.Alternate({1..10}, 1, 1)
```

<table> <tr><td>2</td></tr> <tr><td>4</td></tr> <tr><td>6</td></tr> <tr><td>8</td></tr> <tr><td>10</td></tr> </table>

## Example 3
Create a list from {1..10} that starts at 1 and skips every other number.

```powerquery-m
List.Alternate({1..10}, 1, 1, 1)
```

<table> <tr><td>1</td></tr> <tr><td>3</td></tr> <tr><td>5</td></tr> <tr><td>7</td></tr> <tr><td>9</td></tr> </table>

## Example 4
Create a list from {1..10} that starts at 1, skips one value, keeps two values and so on.

```powerquery-m
List.Alternate({1..10}, 1, 2, 1)
```

<table> <tr><td>1</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>6</td></tr> <tr><td>7</td></tr> <tr><td>9</td></tr> <tr><td>10</td></tr> </table>
