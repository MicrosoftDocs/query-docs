---
title: "List.InsertRange | Microsoft Docs"
ms.date: 7/26/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# List.InsertRange

## Syntax
<pre>
List.InsertRange(<b>list</b> as list, <b>index</b> as number, <b>values</b> as list) as list 
</pre>

## About  

Returns a new list produced by inserting the values in <code>values</code> into <code>list</code> at <code>index</code>. The first position in the list is at index 0. <ul> <li><code>list</code>: The target list where values are to be inserted.</li> <li><code>index</code>: The index of the target list(<code>list</code>) where the values are to be inserted. The first position in the list is at index 0.</li> <li><code>values</code>: The list of values which are to be inserted into <code>list</code>.</li> </ul>  

## Example 1
Insert the list ({3, 4}) into the target list ({1, 2, 5}) at index 2.

```powerquery-m
List.InsertRange({1, 2, 5}, 2, {3, 4})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>


## Example 2
Insert a list with a nested list ({1, {1.1, 1.2}}) into a target list ({2, 3, 4}) at index 0.

```powerquery-m
List.InsertRange({2, 3, 4}, 0, {1, {1.1, 1.2}})
```

<table> <tr><td>1</td></tr> <tr><td>[List]</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> </table>




