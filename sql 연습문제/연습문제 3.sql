--	테이블간 조인(JOIN) SQL 문제입니다.

-- 문제 1. -- 
-- 현재 급여가 많은 직원부터 직원의 사번, 이름, 그리고 연봉을 출력 하시오.
select a.emp_no , first_name, salary
from employees a , salaries b
where a.emp_no = b.emp_no
and b.to_date = '9999-01-01'
order by salary;
-- 문제2.
-- 전체 사원의 사번, 이름, 현재 직책을 이름 순서로 출력하세요.
select a.emp_no , first_name , b.title
from employees a , titles b
where a.emp_no = b.emp_no
order by a.first_name;

-- 문제3.
-- 전체 사원의 사번, 이름, 현재 부서를 이름 순서로 출력하세요..
select c.emp_no , c.first_name , a.dept_name
from departments a , dept_emp b, employees c 
where a.dept_no = b.dept_no
and b.emp_no = c.emp_no
order by c.first_name desc;

-- 문제4.
-- 전체 사원의 사번, 이름, 연봉, 직책, 부서를 모두 이름 순서로 출력합니다.
select e.emp_no , e.first_name, c.salary, d.title ,a.dept_name
from departments a ,dept_emp b  , salaries c , titles d ,employees e 
where a.dept_no = b.dept_no
	and b.emp_no = c.emp_no
	and c.emp_no = d.emp_no
    and d.emp_no = e.emp_no
order by e.first_name desc;


-- 문제5.
-- ‘Technique Leader’의 직책으로 과거에 근무한 적이 있는 모든 사원의 사번과 이름을 출력하세요. (현재 ‘Technique Leader’의 직책(으로 근무하는 사원은 고려하지 않습니다.) 
-- 이름은 first_name과 last_name을 합쳐 출력 합니다.
select a.emp_no, concat( a.first_name ,'' , a.last_name)as '이름'
from employees a , titles b
where a.emp_no = b.emp_no
and b.title = 'Technique Leader';


-- 문제6.
-- 직원 이름(last_name) 중에서 S(대문자)로 시작하는 직원들의 이름, 부서명, 직책을 조회하세요.
select concat( d.first_name ,'' , d.last_name )as '이름', a.dept_name, c.title 
from departments a ,dept_emp b  , titles c ,employees d 
where a.dept_no = b.dept_no
	and b.emp_no = c.emp_no
	and c.emp_no = d.emp_no
	and d.last_name like 'S%';



-- 문제7.
-- 현재, 직책이 Engineer인 사원 중에서 현재 급여가 40000 이상인 사원을 급여가 큰 순서대로 출력하세요.
select *
from titles a , salaries b
where a.emp_no = b.emp_no
and a.title = 'engineer'
and a.to_date = '9999-01-01'
and b.to_date = '9999-01-01'
having b.salary >= 40000
order by b.salary desc;

-- 문제8.
-- 현재 급여가 50000이 넘는 직책을 직책, 급여로 급여가 큰 순서대로 출력하시오
select a.title , b.salary
from titles a , salaries b
where a.emp_no = b.emp_no
and b.salary >= 50000
and b.to_date = '9999-01-01'
order by b.salary desc;
-- 문제9.
-- 현재, 부서별 평균 연봉을 연봉이 큰 부서 순서대로 출력하세요.
select a.dept_name, avg(c.salary)
from departments a , dept_emp b , salaries c
where a.dept_no = b.dept_no
and b.emp_no = c.emp_no
and b.to_date = '9999-01-01'
and c.to_date = '9999-01-01'
 group by a.dept_name
 order by avg(c.salary) desc;
 
-- 문제10.
-- 현재, 직책별 평균 연봉을 연봉이 큰 직책 순서대로 출력하세요.
select a.title , avg(salary)
from titles a , salaries b
where a.emp_no = b.emp_no
 and a.to_date = '9999-01-01'
  and b.to_date = '9999-01-01'
  group by a.title
  order by avg(b.salary) desc ;