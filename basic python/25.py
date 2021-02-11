#select * from tablename where cit="chd" limit 1
#select distinct(city) from tablename
#select * from tablename where cit="chd" AND salary=10000
#select * from tablename where cit="chd" or salary=10000
#select * from tablename where not cit="chd"
#select * from tablename where cit in('chd','mzn')
#select * from tablename where salary between 1000 and 150000
#select * from tablename order by id desc limit 5
#select sum(salary) from tablename
#select min(salary) from tablename
#select max(salary) from tablename
#select count(id) from tablename
#select avg(salary) from tablename
#select sum(salary) from tablename group by city="chd"
#select sum(salary) from tablename group by city(having condition)
#select max(salary) from tablename where not (select max(Salary) from tablename)
#(select salary from tablename order by salary desc limit 2) as v
#select salary from v order by salary limit 1
#select * from tablename where city like 'c%'
#select * from tablename where city like '%c'
#select