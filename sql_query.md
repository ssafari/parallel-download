# USEFUL SQL QUERIES

## PROBLEM 1:

Having 2 tables companies and categories, find a sql query to create another table
where the name of company start by '## promoted' if the promoted is equal 1 with a
rating column value 'NULL' and if promoted is 0 the add the average review with numbers
of rating into rating column.

### comanies table:

```
"id"	"name"	  "phone"	   "promoted"
 3	 "amazon"	 "3434343"	    0
 2	 "google"	 "3414342"	    1
 1	 "cisco"	 "3328391"	    1
```

### categories table:

```
"company_id"	"review_rating"	  "name"	"id"
    1	          2.5	          "cisco"	  1
    1	          3.5	          "cisco"	  2
    1	          4.5	          "cisco"	  3
    2	          4.5	          "google"	  4
    2	          1.5	          "google"	  5
    2	          1.5	          "google"	  6
    3	          0.5	          "amazon"	  7
    3	          1.5	          "amazon"	  8
    3	          0	              "amazon"	  9
```

### solution sql query:

```
SELECT 
case
	when co.promoted = 1 then concat('## promoted ', co.name) 
	else co.name 
end as company_name,
co.phone, 
case 
	when co.promoted = 0 then concat('** Num rating ', COUNT(ca.review_rating), ' average: ', ROUND(AVG(ca.review_rating)::numeric, 2))
	else 'NULL'
end as rating
from companies as co join categories as ca on ca.company_id = co.id
GROUP BY co.id;
```

### Resulting table:

```
    "company_name"	      "phone"	    "rating"
"## promoted google"	   "3414342"	  "NULL"
"## promoted cisco"	       "3328391"	  "NULL"
"amazon"	               "3434343"	  "** Num rating 3 average: 0.67"
```
