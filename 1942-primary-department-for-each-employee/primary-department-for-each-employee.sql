# Write your MySQL query statement below
select employee_id , department_id
from Employee
where primary_flag='Y'
group by employee_id
UNION
select employee_id , department_id
from Employee
group by employee_id
HAVING count(employee_id)=1