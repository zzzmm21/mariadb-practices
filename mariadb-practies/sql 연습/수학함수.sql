-- 함수: 수학

-- abs
select abs(1), abs(-1);

-- ceil 올림
select ceil(3.14), ceiling(3.14);
-- floor 내림
select floor (3.14);

--  mod 나누고 남은
select mod(11,3);

-- round(x) : x에 가장 근접한 정수
-- round(x, d): x 값중에 소수점 d자리에 가장 근접한 실수
select round(1.498), round(1.498,1);

-- power(x,y) , pow(x,y) : x의 y승
select power(2,10), pow(2,10);


-- sign(x) 양수 : 1, 음수 : -1  0:0
select sign(20), sign(-100), sign(0);

-- greatest(x, y, ...)  이중에 큰값  least(x,y,.....)  이중에 작은값
select greatest(10,40,20,50) , least(10,40, 20, 50);
select greatest('a','b','c','d') ,greatest('hello','helA','hell');
