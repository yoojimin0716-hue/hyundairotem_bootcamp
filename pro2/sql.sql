-- 주석 
-- C(insert), R(select), U(update), D(delete) 잠깐 연습
CREATE TABLE good(NO INT PRIMARY key,NAME VARCHAR(10) NOT NULL,tel VARCHAR(10),
inwon INT, addr TEXT);
DESC good;
-- 자료 추가 
-- 형식 : insert into 테이블명(칼럼명 타입, ...) values(자료,...)
INSERT INTO good(NO, NAME, tel, inwon, addr) VALUES(1,'인사과', '123-1234',5,'삼성1동');
INSERT INTO good VALUES(2,'영업과', '123-1222',12,'역삼 1동');
INSERT INTO good(NO, NAME, inwon) VALUES('3','자재과','8');
INSERT INTO good(addr, NO, NAME, inwon) VALUES('역삼 3동','4','영업과과','7');
SELECT * FROM good;
--오류인경우 
-- 입력자료와 칼럼의 순서가 불일치할때 
-- 중복에러
-- name = Not NULL ,공백으로 두면 오류
-- 입력 자료의 타입 불일치 
-- 데이터가 너무 길때 
-- 자료 수정 
-- 형식 : update 테이블명 set 칼럼명 = 수정값, ...where 조건
UPDATE good SET inwon = 100 WHERE NO = 1;
UPDATE good SET inwon = 70,tel = '777-7777' WHERE NO = 2;
UPDATE good SET inwon = 2,tel = null WHERE NO = 2;
SELECT * FROM good;
-- 오류인 경우 
UPDATE good SET NAME = NULL WHERE NO =2;
UPDATE good SET NO = 2 WHERE NO=1;
-- 형식 2 
TRUNCATE TABLE good;
SELECT * FROM good;
DROP TABLE good;
SHOW TABLES;
-- -------------------------------
-- 데이터 베이스 무결성은 저장된 데이터가 정확학 일관되며,
-- 손상되지 않고 신뢰할 수 있는 상태를 유지하는것을 뜻합니다. 
-- 데이터의 품질을 지키고 오류를 막기 위해 데이터 베이스 관리 시스템이 지키는 핵심 규치 ㄱ
-- 주요 무결성 제약 조건 
-- 개체 무결성 : 모든 테이블은 기본 키를 가져야함 
-- 기본키는 빈값이나 중복값을 가질수 없습니다. 
-- 도메인 무결성 : 필드에 들어가는 값이 지정된 자료형, 범위 , 조건
-- 사용자 정의 무결성 
-- 참조 무결성 : 테이블 간의 관계를 뜻한다. 
-- 무결성이 중요한 이유 : 중복 데이터나 잘못된 데이터 값을 막는다 신뢰도를 높인다.
-- Primary key (기본키) : 제약 조건 - Entity Integrity
-- 기본 키는 빈 값이나 중복 값을 가질 수 없다. 자동으로 인덱스 생성됨

-- 참고 : 체이블 작성시 칼럼의 이름, 타입은 중요, 순서는 마음대로 계산에 의해 처리될수 있는 값은 칼럼으로 작성 안됨
-- 방법 1) 칼럼 레벨  
CREATE TABLE a(bun INT PRIMARY KEY, irum CHAR(10));
DESC a;
INSERT INTO a VALUES(1,'tom');
INSERT INTO a VALUES(2,'tom');
-- INSERT INTO a VALUES(1,'tom'); -- 중복 불가 pk err
INSERT INTO a(irum) VALUES('tom'); -- pk err : not Null, 
SELECT * FROM a; 
-- 제약조건 확인 
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME = 'aa';
DROP TABLE a;
-- 방법 2) 테이블 레벨 
CREATE TABLE aa(bun INT, irum CHAR(10),CONSTRAINT aa_bun__pk PRIMARY KEY(bun));
DESC aa;
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME = 'aa';
ALTER TABLE aa DROP CONSTRAINT aa_bun__pk; --pk 제약조건 삭제.oracle 에서 유효 
ALTER TABLE aa DROP PRIMARY KEY;
DROP TABLE aa;
 
-- check 제약조건 : 도메인 무결성에 해당됨 (Domain integrity) : 입력값 조건 부여 
CREATE TABLE aa(bun INT, irum CHAR(10),nai INT CHECK(nai >= 20));
SELECT * FROM information_schema.table_constraints WHERE TABLE_NAME = 'aa';
INSERT INTO aa VALUES(1,'tom',25);
INSERT INTO aa VALUES(1,'tom',15); --chk err : 조건 불만족 

ALTER TABLE aa ADD CONSTRAINT ck_name CHECK(irum IN('tom','john')); 
INSERT INTO aa VALUES(2,'john',25);
INSERT INTO aa VALUES(1,'james',25);  --chk err : irum 조건 불만족 
SELECT * FROM aa; 

-- unique 제약 조건 - Domain Integrity : 동일 값 입력 불허 
CREATE TABLE aa(bun INT, irum CHAR(10) UNIQUE);
CREATE TABLE aa(bun INT, irum CHAR(10), CONSTRAINT aa_irum_uk  UNIQUE(irum)); --얘도 가능 
INSERT INTO aa VALUES(1,'john');
INSERT INTO aa VALUES(2,'tom');
INSERT INTO aa VALUES(3,'tom');  -- unique err : 중복 불가 

-- Referential Integrity(참조키, foreign key, fk, 외래키) 제약조건 
-- 다른 테이블의 칼럼값을 참조 (fk의 대상은 다른 테이블의 pk 또는 unique 가능)
-- 직원 테이블 

CREATE TABLE jikwon(bun INT PRIMARY KEY, irum VARCHAR(10) NOT NULL, buser CHAR(10));
INSERT INTO jikwon VALUES(1, '한송이','인사과');
INSERT INTO jikwon VALUES(2, '박치기이','인사과');
INSERT INTO jikwon VALUES(3, '한송이','총무과과');
SELECT * FROM jikwon;
-- 가족 테이블 
CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10),birth DATETIME, jikwon_bun INT,
FOREIGN KEY(jikwon_bun) REFERENCES jikwon(bun));

CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10),birth DATETIME, jikwon_bun INT,
FOREIGN KEY(jikwon_bun) REFERENCES jikwon(bun)); -- 위와 동일
-- 부모 데이터를 자식이 참조하고 있으면 부모의 삭제나 키의 변경을 막는다 

CREATE TABLE gajok(CODE INT PRIMARY KEY, NAME VARCHAR(10),birth DATETIME, jikwon_bun INT,
FOREIGN KEY(jikwon_bun) REFERENCES jikwon(bun) ON DELETE CASCADE ON UPDATE SET NULL);
-- cascade : 부모 삭제시 자식도 삭제
-- set null : 부모 삭제시 자식의 fk 칼럼 값은 null이됨 
-- 대개의 경우 부모의 pk는 변경이 흔치 않으므로 set null은 자주 사용되지 않는다. 
DESC gajok;
INSERT INTO gajok VALUES(10,'가나다', NOW(),1);
INSERT INTO gajok VALUES(20,'이겨라'', '2005-07-16',2);
INSERT INTO gajok VALUES(30,'한국인', '2023-3-2',1');
SELECT * FROM gajok;
INSERT INTO gajok VALUES(40,'지구인', '2026-08-20',5); -fk err : 5번 직원은 없음 

-- 직원 자료 삭제 
delete from jikwon where bun = 3;
delete from jikwon where bun = 2;   -- err : 2번 직원의 가족이 있기 때뭄ㄴ

delete from gajok where code = 20;  -- 2번직원의 가족 삭제 
delete from jikwon where bun = 2; -- 성공 : 가족이 없기 때문 

SELECT * FROM jikwon;
Drop table jikwon; -- err 테이블 삭제 불가 - 참조 되고 있는 자식 테이블 때문 
Drop table gajok;
Drop table jikwon; -- 성공 
DROP TABLE aa;

show tables;

-- default : 특정 칼럼에 초기값 부여 - null 방지 목적 
create table aa(bun int auto_increment PRIMARY key, irum char(10),
juso varchar(50) DEFAULT '역삼동'); -- AuTo_increment : 번호 자동 증가 
-- Oracle 운 AUTO_INCREMENT X : sequance를 사용 
DESC aa; 

INSERT INTO aa(irum,juso) VALUES('길동','서초동');

INSERT INTO aa(irum,juso) VALUES('나라','익선동동');

INSERT INTO aa(irum) VALUES('국가'); -- juso 는 default 값으로 채움 

ALTER TABLE aa AUTO_INCREMENT = 100; -- AUTO_INCREMENT값 변경 
INSERT INTO aa(irum,juso) VALUES('국가','필동'); 
INSERT INTO aa(irum,juso) VALUES('국가','대치동'); 

SELECT * FROM aa;

-- 연습 문제 
create table professor(
pro_num int PRIMARY KEY, 
irum CHAR(10) NOT NULL, 
lab_num INT CHECK(lab_num BETWEEN 100 AND 500));

INSERT INTO professor VALUES(1, '이정수', 300);
INSERT INTO professor VALUES(2, '이경택', 150);
INSERT INTO professor VALUES(3, '정원종', 450);

SELECT * FROM professor;

create table SUBJECT(
sub_num int auto_increment PRIMARY KEY, 
subname VARCHAR(20) UNIQUE, 
book VARCHAR(20), dam_pro INT, 
FOREIGN KEY(dam_pro) REFERENCES professor(pro_num));

INSERT INTO subject(subname, book, dam_pro) VALUES('자바', '자바의정석', 1);
INSERT INTO subject(subname, book, dam_pro) VALUES('데이터베이스', 'SQL기초', 2);
INSERT INTO subject(subname, book, dam_pro) VALUES('네트워크', '네트워크개론', 3);

SELECT * FROM SUBJECT;

create table student(
std_num CHAR(4) PRIMARY KEY, 
irum CHAR(10) NOT NULL, sub INT, 
grade INT DEFAULT 1 CHECK(grade BETWEEN 1 AND 4), 
FOREIGN KEY(sub) REFERENCES subject(sub_num));

INSERT INTO student VALUES('S001', '홍길동', 1, 2);
INSERT INTO student(std_num, irum, sub) VALUES('S002', '김철수', 2);  
INSERT INTO student VALUES('S003', '이영희', 3, 4);

SELECT * FROM student;

Drop table professor;
Drop table subject;
Drop table student;

-- 인덱스 : 인덱스는 쉽게 말하며ㅏㄴ 책의 목차나 색인과 비슷하다. 검색 속도 향상이 목표 
-- 인덱스 없음 --> 처음부터 끝까지 데이터를 확인 
-- 인덱스 있음 --> 위치를 빠르게 찾아서 데이터 접근 (인덱스는 색인임)

CREATE TABLE aa(id INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(20), age INT, city VARCHAR(30));

INSERT INTO aa(NAME, age, city) VALUES 
('홍길동', 25, '서울'),
('김철수', 30, '부산'),
('이영희', 27, '서울'),
('박민수' ,35, '대전'),
('최영희' ,23, '인천'),
('강호동' ,40, '서울'),
('유재석' ,38, '부산'),
('신동엽' ,42, '서울'),
('홍길동' ,29, '수원'),
('김민지' ,31, '대구');

SELECT * FROM aa;

SELECT * FROM aa WHERE NAME = '강호동'; -- 인덱스가 없으므로 전체 테이블 검색 

-- 실행 계획 확인 
EXPLAIN SELECT* FROM aa WHERE NAME = '강호동'; -- type : ALL - FULL Table scan 

-- 검색을 자주하는 name에 인덱스 생성 - 인덱스 테이블 별도 생성 
CREATE INDEX idx_aa_name ON aa(NAME); -- 이미 테이블이 있는경우 
SHOW INDEX FROM aa; -- index_aa_name 과 pk(인덱스 자동생성) 인덱스 확인 가능 
SHOW keys FROM aa; -- 이것도 가능 

-- 테이블 생성시 인덱스를 부여할 수도 있다 
CREATE TABLE aa (id INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(20),
age INT, city VARCHAR(30), INDEX idx_aa_name (NAME)); 

-- 참고 : 인덱스가 여러개인 경우 '옵티마이저'가 적당한 인덱스를 선택해 실행에 참여 
DESC aa;

-- idc_aa_name 테이블 생성 
-- 강호동 -> 위치(pointer - pk 값) pk가 없으면 내부적으로 row id를 만든다 
-- 이영희 -> 위치 

-- index 삭제 
DROP INDEX idx_aa_name ON aa;
SHOW INDEX FROM aa; 

-- index는 특정 칼럼의 검색 속도 증진이 목적이나 단점도 있다. 
-- insert, update, delete 등이 빈번한 경우에는 인덱스 재설정 비용이 든다. 

-- 참고 : 내장함수 now(),sydate()의 차이 
SELECT NOW(),SLEEP(2),NOW();   -- 결과가 같다. 
SELECT NOW(),SLEEP(2),SYSDATE(); -- 결과가 다르다.
-- sysdate()는 동일 SQL 문장 내에서 호출되는 시점에 따라 결과값을 바로 반환 

-- 테이블 관련 명령 
-- create table 테이블명 ~ 생성
-- ALTER table 테이블명 ~ 구조를 수정 
-- drop table 테이블명 ~ 삭제 

CREATE TABLE aa(irum CHAR(10), juso VARCHAR(50));
alter TABLE aa RENAME kbs; -- 테이블 이름 변경 
SELECT * FROM aa; -- 오류 
SELECT * FROM kbs; -- o
ALTER TABLE kbs RENAME aa
-- 칼럼 관련 명령 
ALTER TABLE aa ADD (job_id INT DEFAULT 10); -- 칼럼 추가 
DESC aa;
INSERT INTO aa VALUES('tom','seoul',20);
INSERT INTO aa(irum, juso) VALUES('tom2','jeju');
SELECT * FROM aa;

ALTER TABLE aa CHANGE job_id job_number INT;
SELECT * FROM aa;

ALTER TABLE aa MODIFY job_number VARCHAR(10);
DESC aa; 

create table sangdata(
code int primary key,
sang varchar(20),
su int,
dan int);       

insert into sangdata values(1,'장갑',3,10000);
insert into sangdata values(2,'벙어리장갑',2,12000);
insert into sangdata values(3,'가죽장갑',10,50000);
insert into sangdata values(4,'가죽점퍼',5,650000);
select * from sangdata;

create table buser(
buserno int primary key, 
busername varchar(10) not null,
buserloc varchar(10),
busertel varchar(15));

insert into buser values(10,'총무부','서울','02-100-1111');
insert into buser values(20,'영업부','서울','02-100-2222');
insert into buser values(30,'전산부','서울','02-100-3333');
insert into buser values(40,'관리부','인천','032-200-4444');
select * from buser;

create table jikwon(
jikwonno int primary key,
jikwonname varchar(10) not null,
busernum int not null,
jikwonjik varchar(10) default '사원', 
jikwonpay int,
jikwonibsail date,
jikwongen varchar(4),
jikwonrating char(3),
CONSTRAINT ck_jikwongen check(jikwongen='남' or jikwongen='여'));

insert into jikwon values(1,'홍길동',10,'이사',9900,'2008-09-01','남','a');
insert into jikwon values(2,'한송이',20,'부장',8800,'2010-01-03','여','b');
insert into jikwon values(3,'이순신',20,'과장',7900,'2010-03-03','남','b');
insert into jikwon values(4,'이미라',30,'대리',4500,'2014-01-04','여','b');
insert into jikwon values(5,'이순라',20,'사원',3000,'2017-08-05','여','b');
insert into jikwon values(6,'김이화',20,'사원',2950,'2019-08-05','여','c');
insert into jikwon values(7,'김부만',40,'부장',8600,'2009-01-05','남','a');
insert into jikwon values(8,'김기만',20,'과장',7800,'2011-01-03','남','a');
insert into jikwon values(9,'채송화',30,'대리',5000,'2013-03-02','여','a');
insert into jikwon values(10,'박치기',10,'사원',3700,'2016-11-02','남','a');
insert into jikwon values(11,'김부해',30,'사원',3900,'2016-03-06','남','a');
insert into jikwon values(12,'박별나',40,'과장',7200,'2011-03-05','여','b');
insert into jikwon values(13,'박명화',10,'대리',4900,'2013-05-11','남','a');
insert into jikwon values(14,'박궁화',40,'사원',3400,'2016-01-15','여','b');
insert into jikwon values(15,'채미리',20,'사원',4000,'2016-11-03','여','a');
insert into jikwon values(16,'이유가',20,'사원',3000,'2016-02-01','여','c');
insert into jikwon values(17,'한국인',10,'부장',8000,'2006-01-13','남','c');
insert into jikwon values(18,'이순기',30,'과장',7800,'2011-11-03','남','a');
insert into jikwon values(19,'이유라',30,'대리',5500,'2014-03-04','여','a');
insert into jikwon values(20,'김유라',20,'사원',2900,'2019-12-05','여','b');
insert into jikwon values(21,'장비',20,'사원',2950,'2019-08-05','남','b');
insert into jikwon values(22,'김기욱',40,'대리',5850,'2013-02-05','남','a');
insert into jikwon values(23,'김기만',30,'과장',6600,'2015-01-09','남','a');
insert into jikwon values(24,'유비',20,'대리',4500,'2014-03-02','남','b');
insert into jikwon values(25,'박혁기',10,'사원',3800,'2016-11-02','남','a');
insert into jikwon values(26,'김나라',10,'사원',3500,'2016-06-06','남','b');
insert into jikwon values(27,'박하나',20,'과장',5900,'2012-06-05','여','c');
insert into jikwon values(28,'박명화',20,'대리',5200,'2013-06-01','여','a');
insert into jikwon values(29,'박가희',10,'사원',4100,'2016-08-05','여','a');
insert into jikwon values(30,'최미숙',30,'사원',4000,'2015-08-03','여','b');
select * from jikwon;

create table gogek(
gogekno int primary key,
gogekname varchar(10) not null,
gogektel varchar(20),
gogekjumin char(14),
gogekdamsano int,
CONSTRAINT FK_gogekdamsano foreign key(gogekdamsano) references jikwon(jikwonno));

insert into gogek values(1,'이나라','02-535-2580','850612-1156777',5);
insert into gogek values(2,'김혜순','02-375-6946','700101-1054777',3);
insert into gogek values(3,'최부자','02-692-8926','890305-1065777',3);
insert into gogek values(4,'김해자','032-393-6277','770412-2028777',13);
insert into gogek values(5,'차일호','02-294-2946','790509-1062777',2);
insert into gogek values(6,'박상운','032-631-1204','790623-1023777',6);
insert into gogek values(7,'이분','02-546-2372','880323-2558777',2);
insert into gogek values(8,'신영래','031-948-0283','790908-1063777',5);
insert into gogek values(9,'장도리','02-496-1204','870206-2063777',4);
insert into gogek values(10,'강나루','032-341-2867','780301-1070777',12);
insert into gogek values(11,'이영희','02-195-1764','810103-2070777',3);
insert into gogek values(12,'이소리','02-296-1066','810609-2046777',9);
insert into gogek values(13,'배용중','02-691-7692','820920-1052777',1);
insert into gogek values(14,'김현주','031-167-1884','800128-2062777',11);
insert into gogek values(15,'송운하','02-887-9344','830301-2013777',2);
select * from gogek;

SELECT * FROM sangdata;

DESC buser; 
DESC jikwon; 
DESC gogek; 

-- select 출발 : 9/7 고고링 

-- select 조회방법
-- 행 단위 조회: selection

-- 열 단위 조회: projection
DESC jikwon;
SELECT *FROM jikwon; -- 모든행 모든열 읽기 
SELECT jikwonno,jikwonname,jikwonpay FROM jikwon; -- 일부 칼럼만 읽기 
SELECT jikwonpay,jikwonno,jikwonname FROM jikwon; -- jikwonpay -> jikwonno -> jikwonname 순서대로 읽는다.(일부 칼럼 읽기)
SELECT jikwonno as 사번, jikwonname 직원명, jikwonpay '연봉' FROM jikwon; -- 컬럼에 별명 부여 * 이렇게 별명을 주면 칼럼명이 바뀐다. jikwonno가 아닌 사번으로 

SELECT 10, '안녕',12 / 3 AS result FROM DUAL; -- DUAL : 가상의 테이블 
SELECT 10. '안녕',12 / 3 AS result;

SELECT jikwonname AS 직원명, jikwonpay AS 연봉, jikwonpay * 0.02 AS 세금 FROM jikwon; -- 컬럼에 대해서 연산도 가능하다. 세금 처럼 
SELECT CONCAT(jikwonname, '님') AS 이름, jikwongen AS 성별 FROM jikwon; -- concat은 문자열 더하기, 홍길동 + 님 

SELECT test.jikwon.jikwonname FROM jikwon; -- db명.소유자명.테이블명.칼럼명 [AS 별명]...[INTO 테이블명]
SELECT myjik.jikwonname FROM jikwon AS myjik; --테이블에 별명을 주고 별명.컬럼명 가능

-- 정렬(sort) - 그룹별 작업이 가능해짐
SELECT *FROM jikwon ORDER BY jikwonpay ASC; -- jikwonpay 별 오름차순 정렬
SELECT *FROM jikwon ORDER BY jikwonpay;
SELECT jikwonno,jikwonname,jikwongen FROM jikwon ORDER BY jikwongen;
SELECT jikwonno,jikwonname,jikwongen FROM jikwon ORDER BY jikwongen DESC;

SELECT *FROM jikwon ORDER BY busernum ASC, jikwonjik DESC, jikwonpay ASC;
SELECT jikwonname, jikwonpay /100 *100 AS pay FROM jikwon ORDER BY pay DESC; --연산결과에 대한 정렬도 가능

SELECT DISTINCT jikwonjik FROM jikwon; --중복자료배제
SELECT DISTINCT jikwonjik, jikwonname FROM jikwon; -- 의미없음

-- 연산자 사용 : 우선순위 () > 산술 > 관계(비교) > is null, like, in > between, not > and > or

-- 행 단위 조회: selection
SELECT *FROM jikwon WHERE jikwonjik='대리'; -- 행(레코드) 제한 
SELECT *FROM jikwon WHERE jikwonno <= 5;
SELECT *FROM jikwon WHERE jikwonibsail='2010-01-03';
SELECT *FROM jikwon WHERE jikwonibsail>='17-01-03'; --날짜도 연산자가능하다. 2017년 이후 입사한 사람 찾기 
SELECT *FROM jikwon WHERE jikwonno=5 OR jikwonno=7;
SELECT *FROM jikwon WHERE jikwonno=5 AND jikwonno=7; -- 이건 안된다.
SELECT *FROM jikwon WHERE jikwonjik='사원' AND jikwongen='남' AND jikwonpay <= 4500;
SELECT *FROM jikwon WHERE jikwonjik='사원' AND jikwongen='여' AND jikwonibsail >= '2017-1-1';
SELECT *FROM jikwon WHERE jikwonjik='사원' AND (jikwongen='여' AND jikwonibsail >= '2017-1-1'); -- ()로 우선순위가 바뀐다.

SELECT *FROM jikwon WHERE jikwonno >=5 AND jikwonno <=10;
SELECT *FROM jikwon WHERE jikwonno BETWEEN 5 AND 10; -- 결과 위 코드와 동일
SELECT *FROM jikwon WHERE jikwonno < 5 OR jikwonno > 10;
SELECT *FROM jikwon WHERE jikwonno  not BETWEEN 5 AND 10; -- 결과 위 코드와 동일
-- 참고 : 조건은 긍정적 형태일 경우 속도가 빠름. 예를 들어 not between 보다는 between 그 자체를 써라.

SELECT *FROM jikwon WHERE jikwonibsail BETWEEN '2015-1-1'  AND '2016-12-31';

SELECT *FROM jikwon WHERE jikwonname='홍길동';
SELECT *FROM jikwon WHERE jikwonname >='박'; -- 사전 기준 '박'보다 이상
SELECT ASCII('a'),ASCII('A'),ASCII('가'),ASCII('나');
SELECT *FROM jikwon WHERE jikwonname >='김' AND jikwonname <='박';
SELECT *FROM jikwon WHERE jikwonname BETWEEN '김' AND '박'; -- 결과가 위 코드와 동일하다.

-- in 맴버 조건 연산 
SELECT *FROM jikwon WHERE jikwonjik ='대리' OR jikwonjik ='과장' OR jikwonjik ='부장';
SELECT *FROM jikwon WHERE jikwonjik IN ('대리','과장','부장'); -- 결과가 위 코드와 동일.
SELECT *FROM jikwon WHERE busernum IN (10,30) ORDER BY busernum ASC;

-- like 조건 연산: %(0개 이상의 문자열),_(한 개 문자)
SELECT *FROM jikwon WHERE jikwonname LIKE '이%'; -- 첫글자만 '이' %는 이 다음에 아무거나 나와도 된다.
SELECT *FROM jikwon WHERE jikwonname LIKE '%라'; -- 라로 끝나는 이름 출력
SELECT *FROM jikwon WHERE jikwonname LIKE '%순%'; -- 가운데 글자가 순인  이름 출력 
SELECT *FROM jikwon WHERE jikwonname LIKE '이%라'; -- 이로 시작 라로 끝나는 이름 출력 

SELECT *FROM jikwon WHERE jikwonname LIKE '이_라'; -- 가운데 한 글자만 아무거나(이름이 세 글자만)
SELECT *FROM jikwon WHERE jikwonname LIKE '__'; -- 이름이 두 글자 

SELECT *FROM gogek WHERE gogekname LIKE '__';
SELECT *FROM gogek WHERE gogekname LIKE '최%' OR gogekname LIKE '__라'; -- 최로 시작하거나 라로 끝나는 이름 

-- gogek 테이블에서 gogekjumin을 이용해 여성만 출력 
SELECT *FROM gogek WHERE gogekjumin LIKE '______-2%' OR gogekjumin LIKE '______-4%';
SELECT *FROM gogek WHERE gogekjumin LIKE '%-2%' OR gogekjumin LIKE '%-4%'; -- 위 코드와 결과값이 같다.

SELECT *FROM jikwon WHERE jikwonpay LIKE '5%';

SELECT *FROM jikwon WHERE jikwonpay LIMIT 5, 4;
SELECT *FROM jikwon WHERE jikwonpay LIKE '5%' LIMIT 3;

-- update, delete에도 조건 연산자 사용 가능
UPDATE jikwon SET jikwonpay=NULL WHERE jikwonno=5; -- 5번 직원 연봉에 null
SELECT *FROM jikwon;
SELECT *FROM jikwon WHERE jikwonpay=NULL; -- 오류 null은 값 자체가 아니라 값이 없음을 의미하기 때문.
SELECT *FROM jikwon WHERE jikwonpay IS NULL; -- null은 is랑 같이 쓰자 ! null만 쓰면 err 

-- 다양한 연산자 조합 
SELECT jikwonno AS 직원번호, jikwonname 직원명, jikwonjik, jikwonpay / 12 AS 보너스, mytab.jikwonibsail
FROM jikwon AS mytab 
WHERE jikwonjik IN('과장','사원') AND
jikwonpay >= 4000 AND 
jikwonibsail BETWEEN '2015-1-1' AND '2019-12-31'
ORDER BY jikwonjik ASC, jikwonpay DESC 
LIMIT 3;

-- json 형식(key:value)으로 출력 
SELECT JSON_OBJECT('jikwonno',jikwonno,'jikwonname',jikwonname) AS 'json data' FROM jikwon
WHERE jikwonjik='대리'

-- csv 형식으로 파일에 저장 
SELECT jikwonno,jikwonname,jikwonpay*10000 INTO OUTFILE 'c:/works/jikdata.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
FROM jikwon WHERE jikwonjik = '대리';
-- 출력 형태 예 
-- "4","이미라","45000000"
-- "9","채송화","50000000"
-- "13","박명화","49000000"
-- "19","이유라","55000000"
-- "22","김기욱","58500000"
-- "24","유비","45000000"
-- "28","박명화","52000000"

-- html 형식으로 파일에 저장

SELECT CONCAT(
'<table>',
'<tr>',
'<td>', jikwonno,'</td>','<td>',jikwonname,'</td>','<td>',jikwonpay * 10000, '</td>',
'</tr>',
'</table>'
) INTO OUTFILE 'c:/works/jikdata.html'
FROM jikwon WHERE jikwonjik='대리';

-- 내장함수호출 : 데이터 조작의 효율성 향상이 목적

-- 단일 행 함수 : 행 단위 처리
-- 문자 관련 함수 
SELECT LOWER('Hello Sql'),UPPER('Hello Sql') FROM DUAL; -- 대,소문자로 변환 
SELECT CONCAT('Hello' 'World');
SELECT SUBSTR('Hello World', 3),SUBSTR('Hello world', 3,3),SUBSTR('Hello world', -3,3); --문자열 일부 추출 
SELECT LENGTH('Hello World');
SELECT INSTR('Hello World', 'e'), INSTR('Hello World', 'k'); -- 특정 문자 위치를 반환 
SELECT TRIM(' aabb bbaa '),LTRIM(' aabb bbaa '),RTRIM(' aabb bbaa '); -- 앞 뒤,좌,우의 공백 제거 
SELECT REPLACE('011.1234.5678','.','-'), REPLACE('abc def abc','abc','ABC'); -- 문자열 치환 

SELECT jikwonname,jikwonjik,REPLACE(jikwonjik,'사원','평직원') FROM jikwon; -- 행단위로 사원 -> 평직원으로 치환 

SELECT *FROM jikwon;
-- jikwon 테이블에서 이름에 '이'가 포함된 직원이 있다면 '이'부터 두 글자 출력.
-- (마지막에 '이'가 있는 경우는 한 글자 출력), 문제입니다.
SELECT jikwonname,
SUBSTR(jikwonname, INSTR(jikwonname, '이'),2)
FROM jikwon 
WHERE jikwonname LIKE '%이%';

-- 숫자 관련 함수 일부 체험 
SELECT ROUND(12.3456), ROUND(12.5678,0), ROUND(12.3456,1), ROUND(12.3456,-1), ROUND(17.3456,-1); -- 반올림
SELECT CEIL(12.3456), FLOOR(12.5678); -- 무조건 올림/버림
SELECT jikwonname, jikwonpay,ROUND(jikwonpay * 0.025) AS tax FROM jikwon LIMIT 5;

SELECT TRUNCATE(45.678,0),TRUNCATE(45.678,1),TRUNCATE(45.678,-1); -- 자릿수 기준으로 정수 취하고 나머지 절삭 

SELECT MOD(15,2); -- 나누고 나머지 

SELECT GREATEST(15.5,12,32), LEAST(15.5,12,32), POW(2,3), SQRT(4); -- 제일 큰 값/ 제일 작은 값/ 2의 3승 

-- 날짜 함수 
SELECT CURDATE(), CURDATE() +0; -- 2026-09-07 20260907(1970년1월1일 기준(unix 시스템) 시간계산)
SELECT NOW(), NOW() +0; -- 날짜와 시간까지 
SELECT NOW(), SYSDATE(); -- 날짜함수 차이 정리하기 

-- 날짜 더하기 빼기
SELECT ADDDATE(DATE'2026-9-1',3), SUBDATE(DATE'2026-9-1',3);
SELECT DATE_ADD(NOW(),INTERVAL 1 MINUTE), DATE_ADD(NOW(),INTERVAL 5 DAY),DATE_ADD(NOW(),INTERVAL 1 MONTH);
SELECT DATE_SUB(NOW(),INTERVAL 2 YEAR), DATE_SUB(NOW(),INTERVAL -2 YEAR);

SELECT DATEDIFF('2026-9-1','2023-6-1'), DATEDIFF(NOW(), '2030-6-1'); -- 날짜 관련
SELECT TIMEDIFF('2026-9-1','2023-6-1'), DATEDIFF(NOW(), '2030-6-1'); -- 시간 관련 

-- 형 변환 함수 : date_format - 날짜를 문자열로 변환 
SELECT DATE_FORMAT(NOW(), '%Y%m%d'), DATE_FORMAT(NOW(),'%Y%m%d'), DATE_FORMAT(NOW(), '%Y년%m월%d일');
SELECT DATE_FORMAT(NOW(), '%Y-%m-%d %H:%h:%S'), DATE_FORMAT(NOW(), '%y-%M-%D %h:%i:%S');
-- DATE_FORMAT 서식 검색을 이용

SELECT STR_TO_DATE('2026-9-7','%Y-%m-%d');

SELECT FORMAT(1234.567,2), ROUND(1234.567,2); -- 타입이 문자열/ 타입이 숫자

-- 기타함수 
-- rank() : 순위 결정 - 동점 처리, dense_rank() : 동점 처리 안함 
SELECT jikwonno,jikwonname,jikwonpay,
rank() OVER(ORDER BY jikwonpay DESC),
dense_rank() OVER(ORDER BY jikwonpay)
FROM jikwon WHERE jikwonpay IS NOT NULL; -- 내림차순 

SELECT jikwonno,jikwonname,jikwonpay,
rank() OVER(ORDER BY jikwonpay),
dense_rank() OVER(ORDER BY jikwonpay)
FROM jikwon WHERE jikwonpay IS NOT NULL; -- 오름차순

SELECT jikwonno,jikwonname,jikwonibsail,
rank() OVER(ORDER BY jikwonibsail),
dense_rank() OVER(ORDER BY jikwonibsail)
FROM jikwon;                             -- 입사 년도별 

-- nvl(value1, value2) : value1이 null이면 value2를 취함
UPDATE jikwon SET jikwonjik=NULL WHERE jikwonno=5;
SELECT *FROM jikwon WHERE jikwonno=5;
SELECT jikwonname,nvl(jikwonjik,'임시직'),nvl(jikwonpay,0) FROM jikwon;

-- nvl2(value1, value2, value3) : value1이 null이면 value3을 취하고 NULL이 아니면 value2를 취함.
SELECT jikwonname,NVL2(jikwonjik, '정규직','임시직') AS jik,jikwongen,
NVL2(jikwonpay, jikwonpay,0) AS pay
FROM jikwon;

-- nullif(value1, value2): 두 개의 값이 일치하면 null을, 일치하지 않으면 value1을 취함.
SELECT NULLIF(LENGTH('abcd'), LENGTH('123')); -- 4
SELECT NULLIF(LENGTH('abc'), LENGTH('123')); -- null
SELECT jikwonname,jikwonjik, NULLIF(jikwonjik,'사원') FROM jikwon WHERE jikwonjik IS NOT NULL;

-- 조건 표현식 (conditional Expressions) ---------------------------- 이거 시험 무조건 나오겠다.
-- 형식 1) case 표현식 when 비교값1 then 결과값1 when 비교값2 then 결과값2 ... [else 결과값n] end as 별명 
SELECT case 10 / 5 when 5 then '안녕' when 2 then '수고' ELSE '잘가' END AS 결과 FROM DUAL; 
SELECT jikwonname,
case jikwonpay
when 3000 then '연봉 3000'
when 3500 then '연봉 3500'
ELSE '기타연봉'
END AS result
FROM jikwon;

SELECT jikwonname,jikwonpay,jikwonjik,
case jikwonjik
when '이사' then jikwonpay * 0.05
when '부장' then jikwonpay * 0.04
when '과장' then jikwonpay * 0.03
ELSE jikwonpay * 0.02
END AS donation
FROM jikwon;

-- 형식 2) case  when 조건1 then 결과값1 when 조건2 then 결과값2 ... [else 결과값n] end as 별명

SELECT jikwonname,
case when jikwongen='남' then 'M' when jikwongen='여' then 'F' END AS jender 
FROM jikwon;

SELECT jikwonname,jikwonpay,
case when jikwonpay >= 7000 then '고액연봉'
when jikwonpay >= 5000 then '보통연봉'
ELSE '낮은연봉'
END AS result 
FROM jikwon WHERE jikwonjik IN ('대리','과장');

-- 조건표현식 (if(조건) 참값, 거짓값 as 별명)
SELECT jikwonname,jikwonpay,jikwonjik,
if(TRUNCATE(jikwonpay / 1000,0) >= 5, 'good', 'normal') AS 'result'
FROM jikwon;

-- --------------------------------------------------------------------------------------
-- 복수행 함수 (집계 함수) : 전체 자료를 그룹별로 구분해 통계결과를 얻기 위한 함수 
-- NULL 값 무시 (count(*)) 는 예외)

SELECT SUM(jikwonpay) AS 합, AVG(jikwonpay) AS 평균 FROM jikwon; 
SELECT max(jikwonpay) AS 최대값, min(jikwonpay) AS 최소값 FROM jikwon; 
SELECT * FROM jikwon;
SELECT AVG(jikwonpay), AVG(nvl(jikwonpay,0)) FROM jikwon; 
SELECT AVG(jikwonpay) / 29, SUM(jikwonpay)/30 FROM jikwon; 
SELECT COUNT(*), COUNT(jikwonno), COUNT(jikwonpay) FROM jikwon;
SELECT STDDEV(jikwonpay) AS 표준편차, VAR_SAMP(jikwonpay) AS 분산 FROM jikwon;

-- 과장은 몇명? 
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonjik = '과장';

-- 2010년 이전에 입사한 남직원은 몇명?
SELECT COUNT(*) AS 인원수 FROM jikwon WHERE jikwonibsail < '2010-1-1' AND jikwongen ='남자'; 

-- 2015년 이후 입사한 여직원의 연봉합, 편균, 인원수 ? 
SELECT sum(jikwonpay) 연봉합, avg(jikwonpay) 연봉평균, COUNT(*) AS 인원수 
FROM jikwon WHERE jikwonibsail >= '2015-1-1' AND jikwongen ='여'; 

-- 그룹 함수 - group by : 소계 출력
-- 형식 : select 그룹 칼럼명, 계산함수 ... from 테이블명 where 조건
-- group by 그룹 칼럼명 having 출력 결과에 대한 조건 
-- group by에 order by 할 수 없다.(내장됨), 단 출력결과는 order by 가능함  

-- 성별 연봉의 평균, 인원수 출력
SELECT AVG(jikwonpay),COUNT(*) FROM jikwon GROUP BY jikwongen; 
SELECT AVG(jikwonpay),COUNT(jikwonpay) FROM jikwon GROUP BY jikwongen; -- NULL 제외 
SELECT AVG(nvl(jikwonpay,0)),COUNT(*) FROM jikwon GROUP BY jikwongen; -- NULL 처리 

-- 부서별 연봉합 
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum;

-- 부서별 연봉합 - 연봉합이 35000 이상 
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum HAVING SUM(jikwonpay) >= 35000;
SELECT busernum bun, SUM(jikwonpay) hap FROM jikwon GROUP BY busernum HAVING hap >= 35000; -- 별명 사용 

-- 부서별 연봉합 - 연봉합이 15000 이상인 여직원이 대상 
SELECT busernum,SUM(jikwonpay) FROM jikwon WHERE jikwongen = '여' 
GROUP BY busernum HAVING SUM(jikwonpay) >= 15000; 

SELECT busernum, SUM(jikwonpay) from jikwon ORDER BY busernum DESC GROUP BY busernum; -- 에러 
SELECT busernum, SUM(jikwonpay) from jikwon group BY busernum 
ORDER BY SUM(jikwonpay) DESC; -- group by 결과에 대한 정렬은 가능 
 

-- 문1) 직급별 급여의 평균 (NULL인 직급 제외)
show TABLES;
DESC jikwon;
SELECT jikwonjik, count(jikwonpay), avg(jikwonpay) FROM jikwon GROUP BY jikwonjik
ORDER BY avg(jikwonpay) DESC; 

-- 문2) 부장,과장에 대해 직급별 급여의 총합
SELECT jikwonjik, SUM(jikwonpay) FROM jikwon WHERE jikwonjik IN('부장', '과장') 
GROUP BY jikwonjik ORDER BY SUM(jikwonpay) DESC;

-- 문3) 2015년 이전에 입사한 자료 중 년도별 직원수 출력
show TABLES;
DESC jikwon;
SELECT COUNT(*) as 인원수 fron jikwon, where jikwonibsail <= '2015-1-1'
GROUP BY jikwonibsail DESC; 

문4) 직급별 성별 인원수, 급여합 출력 (NULL인 직급은 임시직으로 표현)

문5) 부서번호 10,20에 대한 부서별 급여 합 출력

문6) 급여의 총합이 7000 이상인 직급 출력(NULL인 직급은 임시직으로 표현)

문7) 직급별 인원수, 급여합계를 구하되 인원수가 3명 이상인 직급만 출력
        (NULL인 직급은 임시직으로 표현)


