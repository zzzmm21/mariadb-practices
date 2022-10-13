-- 함수 : 날짜 함수

-- curdate(), current_date 날짜만
select curdate(), current_date;

-- curtime(), current_time 시간만
select curtime(), current_time;

-- now() 둘다 vs sysdate()
select now() , sysdate();
select now(), sleep(2), now();
select now(), sleep(2), sysdate();


-- date_format()
-- 2022년 10월 13일 10:12:55

select date_format(now(),"%Y년 %m월 %d일 %h시 %i분 %s초");
select date_format(now(),"%y년 %m월 %d일 %h시 %i분 %s초");

-- period_diff
-- 포멧팅 YYMM YYYYMM
-- 예) 근무 개월 수 
select first_name, period_diff(date_format(curdate(),'%y %m'),
date_format(hire_date,'%y%m')) as month 
from employees
order by month desc;

-- date_add(=adddate), date_sub(=subdate)
-- 예제 각 사원들의 근속년 수가 5년이 되는 날은 언제 일까여?
-- 날짜를 date에 type(year , month,day)의 표현식을 더하거나 뺸다.
select  first_name,
		hire_date,
        date_add(hire_date, interval 5 year)
        from employees;
        
-- cast
select '12345'+ 10 , cast('12345' as int) +10;
select date_format(cast('2022-10-10' as  date),'%Y년 %m월 %d일');
select cast(cast(1-2 as unsigned) as int);
 

-- type
-- 문자 : varchar,char,text, CLOB(Character Large Object)
-- 정수 : signed(unsigned), int(integer) , medium int, big int
-- 실수 : float , double
-- 시간 : date , datetime
-- LOB: CLOB, BLOB(binary Large OBject)
