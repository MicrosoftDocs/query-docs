---
description: "Learn more about: Types in the Power Query M formula language"
title: "Power Query M type system"
ms.date: 4/16/2018
---

# Types in the Power Query M formula language

The Power Query M Formula Language is a useful and expressive data mashup language. But it does have some limitations. For example, there is no strong enforcement of the type system. In some cases, a more rigorous validation is needed. Fortunately, M provides a built-in library with support for types to make stronger validation feasible.

Developers should have a thorough understanding of the type system in-order to do this with any generality. And, while the Power Query M language specification explains the type system well, it does leave a few surprises. For example, validation of function instances requires a way to compare types for compatibility.

By exploring the M type system more carefully, many of these issues can be clarified, and developers will be empowered to craft the solutions they need.

Knowledge of predicate calculus and na&#239;ve set theory should be adequate to understand the notation used.
 
## PRELIMINARIES

(1) *B*  := { _true_; _false_ }<br/>
_B is the typical set of Boolean values_

(2) *N*  := { valid M identifiers }<br/>
_N is the set of all valid names in M. This is defined elsewhere._

(3) *P*  := &#10216;*B*, *T*&#10217;<br/>
_P is the set of function parameters. Each one is possibly optional, and has a type. Parameter names are irrelevant._

(4) *P<sup>n</sup>*  := &#8899;<sub>*0&#8804;i&#8804;n*</sub>  &#10216;_i_, *P*<sup>*i*</sup>&#10217;<br/>
_P<sup>n</sup> is the set of all ordered sequences of n function parameters._

(5) *P*<sup>\*</sup> := &#8899;<sub>*0&#8804;i&#8804;&#8734;*</sub>  *P<sup>i</sup>*<br/>
_P<sup>\*</sup> is the set of all possible sequences of function parameters, from length 0 on up._

(6) *F*  := &#10216;*B*, *N*, *T*&#10217;<br/>
_F is the set of all record fields. Each field is possibly optional, has a name, and a type._

(7) *F*<sup>*n*</sup>  := &#8719;<sub>_0&#8804;i&#8804;n_</sub> *F*<br/>
_F<sup>n</sup> is the set of all sets of n record fields._

(8) *F*<sup>\*</sup>  := ( &#8899;<sub>*0&#8804;i&#8804;&#8734;*</sub> *F*<sup>*i*</sup> ) &#8726; { _F_ | &#10216;_b<sub>1</sub>_, _n<sub>1</sub>_, _t<sub>1</sub>_&#10217;, &#10216;_b<sub>2</sub>_, _n<sub>2</sub>_, _t<sub>2</sub>_&#10217; &#8712; _F_ &#8896; _n<sub>1</sub>_ = _n<sub>2</sub>_ }<br/>
_F<sup>\*</sup> is the set of all sets (of any length) of record fields, except for the sets where more than one field has the same name._
 
(9) *C*  := &#10216;*N*,*T*&#10217;<br/>
_C is the set of column types, for tables. Each column has a name and a type._

(10) *C*<sup>*n*</sup>  &#8834; &#8899;<sub>_0&#8804;i&#8804;n_</sub> &#10216;*i*, *C*&#10217;<br/>
_C<sup>n</sup> is the set of all ordered sequences of n column types._
 
(11) _C_<sup>\*</sup>  := ( &#8899;<sub>_0&#8804;i&#8804;&#8734;_</sub> *C*<sup>*i*</sup> ) &#8726; { *C*<sup>*m*</sup> | &#10216;*a*, &#10216;*n<sub>1</sub>*, *t<sub>1</sub>*&#10217;&#10217;, &#10216;*b*, &#10216;*n<sub>2</sub>*, *t<sub>2</sub>*&#10217;&#10217; &#8712; _C<sup>m</sup>_ &#8896; *n<sub>1</sub>* = *n<sub>2</sub>* }<br/>
_C<sup>\*</sup> is the set of all combinations (of any length) of column types, except for those where more than one column has the same name._

## M TYPES

(12) *T*<sub>*F*</sub>  := &#10216;*P*, *P*<sup>\*</sup>&#10217;<br/>
_A Function Type consists of a return type, and an ordered list of zero-or-more function parameters._

(13) *T*<sub>*L*</sub>  :=&#12310;*T*&#12311;<br/>
_A List type is indicated by a given type (called the "item type") wrapped in curly braces.
Since curly braces are used in the metalanguage,_ &#12310; &#12311; _brackets are used in this document._

(14) *T*<sub>*R*</sub>  := &#10216;*B*, *F*<sup>\*</sup>&#10217;<br/>
_A Record Type has a flag indicating whether it's "open", and zero-or-more unordered record fields._

(15) *T*<sub>*R*</sub><sup>o</sup>  := &#10216;*true*, *F*&#10217;<br/>  

(16) *T*<sub>*R*</sub><sup>&#x2022;</sup>  := &#10216;*false*, *F*&#10217;<br/> 
_T<sub>R</sub><sup>o</sup> and T<sub>R</sub><sup>&#x2022;</sup> are notational shortcuts for open and closed record types, respectively._

(17) *T*<sub>*T*</sub>  := *C*<sup>\*</sup><br/>
_A Table Type is an ordered sequence of zero-or-more column types, where there are no name collisions._

(18) *T*<sub>*P*</sub>  := { any; none; null; logical; number; time; date; datetime; datetimezone;  duration; text; binary; type; list; record; table; function; anynonnull }<br/>
_A Primitive Type is one from this list of M keywords._

(19) *T*<sub>*N*</sub>  := { *t<sub>n</sub>*, u &#8712; *T* | *t<sub>n</sub>* = u+null } = nullable *t*<br/>
_Any type can additionally be marked as being nullable, by using the_ "nullable" _keyword._
 
(20) *T*  := _T<sub>F</sub>_ &#8746; _T<sub>L</sub>_ &#8746; _T<sub>R</sub>_ &#8746; _T<sub>T</sub>_ &#8746; _T<sub>P</sub>_ &#8746; _T<sub>N</sub>_<br/>
_The set of all M types is the union of these six sets of types:  
Function Types, List Types, Record Types, Table Types, Primitive Types, and Nullable Types._

## FUNCTIONS

One function needs to be defined: *NonNullable* : *T* &#8592; *T*<br/>
This function takes a type, and returns a type that is equivalent except it does not conform with the null value.

## IDENTITIES

Some identities are needed to define some special cases, and may also help elucidate the above.

(21) nullable any = any<br/>
(22) nullable anynonnull = any<br/>
(23) nullable null = null<br/>
(24) nullable none = null<br/>
(25) nullable nullable *t* &#8712; *T* = nullable *t*<br/>
(26) *NonNullable*(nullable *t* &#8712; *T*) = *NonNullable*(*t*)</br>
(27) *NonNullable*(any) = anynonnull<br/>
 
## TYPE COMPATIBILITY

As defined elsewhere, an M type is compatable with another M type if and only if all values that conform to the first type also conform to the second type.

Here is defined a compatability relation that does not depend on conforming values, and is based on the properties of the types themselves. It is anticiplated that this relation, as defined in this document, is completely equivalent to the original semantic definition.

The "is compatible with" relation : &#8804; : *B* &#8592; *T* &#215; *T*<br/> 
In the below section, a lowercase *t* will always represent an M Type, an element of *T*. 

A *&#934;* will represent a subset of *F*<sup>\*</sup>, or of *C*<sup>\*</sup>.

(28) *t* &#8804; *t*<br/>
_This relation is reflexive._

(29) _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_ &#8743; _t<sub>b</sub>_ &#8804; _t<sub>c</sub>_ &#8594; _t<sub>a</sub>_ &#8804; _t<sub>c</sub>_<br/>
_This relation is transitive._

(30) none &#8804; *t* &#8804; any<br/>
_M types form a lattice over this relation;_ none _is the bottom, and_ any _is the top._

(31) _t<sub>a</sub>_, _t<sub>b</sub>_ &#8712; _T<sub>N</sub>_ &#8743; _t<sub>a</sub>_ &#8804; _t<sub>a</sub>_ &#8594; _NonNullable_(_t<sub>a</sub>_) &#8804; _NonNullable_(_t<sub>b</sub>_)<br/>
_If two types are compatible, then the NonNullable equivalents are also compatible._

(32) null &#8804; _t_ &#8712; _T<sub>N</sub>_<br/>
_The primitive type_ null _is compatible with all nullable types._

(33) _t_ &#8713; _T<sub>N</sub>_ &#8804; anynonnull<br/>
_All nonnullable types are compatible with_ anynonnull.

(34) _NonNullable_(_t_) &#8804; _t_<br/>
_A NonNullible type is compatible with the nullable equivalent._

(35) _t_ &#8712; _T<sub>F</sub>_ &#8594; _t_ &#8804; function<br/>
_All function types are compatible with_ function.

(36) _t_ &#8712; _T<sub>L</sub>_ &#8594; _t_ &#8804; list<br/>
_All list types are compatible with_ list.

(37) _t_ &#8712; _T<sub>R</sub>_ &#8594; _t_ &#8804; record<br/>
_All record types are compatible with_ record.

(38) _t_ &#8712; _T<sub>T</sub>_ &#8594; _t_ &#8804; table<br/>
_All table types are compatible with_ table.

(39) _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_ &#8596; &#12310;_t<sub>a</sub>_&#12311;&#8804;&#12310;_t<sub>b</sub>_&#12311;<br/>
_A list type is compaible with another list type if the item types are compatible, and vice-versa._

(40) _t<sub>a</sub>_ &#8712; _T<sub>F</sub>_ = &#10216; _p<sub>a</sub>_, <em>p<sup>\*</sup></em> &#10217;, _t<sub>b</sub>_ &#8712; <em>T<sub>F</sub></em> = &#10216; _p<sub>b</sub>_, <em>p<sup>\*</sup></em> &#10217; &#8743; _p<sub>a</sub>_ &#8804; _p<sub>b</sub>_ &#8594; _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_<br/>
_A function type is compatible with another function type if the return types are compatible, and the parameter lists are identical._

(41) _t<sub>a</sub>_ &#8712; *T*<sub>*R*</sub><sup>o</sup>, _t<sub>b</sub>_ &#8712; *T*<sub>*R*</sub><sup>&#x2022;</sup> &#8594; _t<sub>a</sub>_ &#8816; _t<sub>b</sub>_<br/>
_An open record type is never compatible with a closed record type._

(42) _t<sub>a</sub>_ &#8712; *T*<sub>*R*</sub><sup>&#x2022;</sup> = &#10216;_false_, _&#934;_&#10217;, _t<sub>b</sub>_ &#8712; *T*<sub>*R*</sub><sup>o</sup> = &#10216;<em>true</em>, _&#934;_&#10217; &#8594; _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_<br/>
_A closed record type is compatible with an otherwise identical open record type._

(43) _t<sub>a</sub>_ &#8712; *T*<sub>*R*</sub><sup>o</sup> = &#10216;<em>true</em>, (_&#934;_, &#10216;<em>true</em>, <em>n</em>, any&#10217;)&#10217;, _t<sub>b</sub>_ &#8712; *T*<sub>*R*</sub><sup>o</sup> = &#10216;<em>true</em>, _&#934;_&#10217;  &#8594; _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_ &#8743; _t<sub>b</sub>_ &#8804; _t<sub>a</sub>_<br/>
_An optional field with the type_ any _may be ignored when comparing two open record types._

(44) _t<sub>a</sub>_ &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, (&#934;, &#10216;<em>&#946;</em>, <em>n</em>, <em>u<sub>a</sub></em>&#10217;)&#10217;, _t<sub>b</sub>_ &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, (&#934;, &#10216;<em>&#946;</em>, <em>n</em>, <em>u<sub>b</sub></em>&#10217;)&#10217; &#8743; _u<sub>a</sub>_ &#8804; _u<sub>b</sub>_ &#8594; _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_<br/>
_Two record types that differ only by one field are compatible if the name and optionality of the field are identical, and the types of said field are compatible._

(45) _t<sub>a</sub>_ &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, (&#934;, &#10216;<em>false</em>, <em>n</em>, <em>u</em>&#10217;)&#10217;, _t<sub>b</sub>_ &#8712; <em>T<sub>R</sub></em> = &#10216;<em>b</em>, (&#934;, &#10216;<em>true</em>, <em>n</em>, <em>u</em>&#10217;)&#10217; &#8594; _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_<br/>
_A record type with a non-optional field is compatible with a record type identical but for that field being optional._

(46)  _t<sub>a</sub>_ &#8712; *T*<sub>*R*</sub><sup>o</sup> = &#10216;<em>true</em>, (_&#934;_, &#10216;<em>b</em>, <em>n</em>, <em>u</em>&#10217;)&#10217;,  _t<sub>b</sub>_ &#8712; *T*<sub>*R*</sub><sup>o</sup> = &#10216;<em>true</em>, _&#934;_&#10217;  &#8594;  _t<sub>a</sub>_ &#8804;  _t<sub>b</sub>_<br/>
_An open record type is compatible with another open record type with one fewer field._
 
(47) _t<sub>a</sub>_ &#8712; _T<sub>T</sub>_ = (_&#934;_, &#10216;<em>i</em>, &#10216;<em>n</em>, _u<sub>a</sub>_&#10217;&#10217;), _t<sub>b</sub>_ &#8712;  _T<sub>T</sub>_ = (_&#934;_, &#10216;<em>i</em>, &#10216;<em>n</em>, _u<sub>b</sub>_&#10217;&#10217;) &#8743; _u<sub>a</sub>_ &#8804; _u<sub>b</sub>_ &#8594; _t<sub>a</sub>_ &#8804; _t<sub>b</sub>_<br/>
_A table type is compatible with a second table type, which is identical but for one column having a differing type, when the types for that column are compatible._

## REFERENCES

Microsoft Corporation (2015 August)<br/>
Microsoft Power Query for Excel Formula Language Specification [PDF]<br/>
Retrieved from https://msdn.microsoft.com/library/mt807488.aspx

Microsoft Corporation (n.d.)<br/>
Power Query M function reference [web page]<br/>
Retrieved from https://msdn.microsoft.com/library/mt779182.aspx


