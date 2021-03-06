
#

## python语言特性（15%）

### 面向对象的特征

## 数据结构与算法（30%）

## 计算机网络（20%）

## 数据库（15%）

### 关系型数据库（mysql）

#### mysql常用sql语句

DDL—数据定义语言(Create，Alter，Drop，DECLARE)
DML—数据操纵语言(Select，Delete，Update，Insert
DCL—数据控制语言(GRANT，REVOKE，COMMIT，ROLLBACK)

##### 用户 授权
```
创建用户 host：本地为localhost 任意为%
CREATE USER 'username'@'host' IDENTIFIED BY 'password'; 

删除用户
DROP USER 'username'@'host';

设置与更改用户密码
SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
如果是当前登录用户用：
SET PASSWORD = PASSWORD("newpassword");

授权 privileges：SELECT , INSERT , UPDATE，DELETE 等 全部为all
GRANT privileges ON databasename.tablename TO 'username'@'host';
注意：用以上命令授权的用户不能给其它用户授权，如果想让该用户可以授权，用以下命令：
GRANT privileges ON databasename.tablename TO 'username'@'host' WITH GRANT OPTION;

撤销用户权限
REVOKE privilege ON databasename.tablename FROM 'username'@'host';
注意: 假如你在给用户’username’@’%’授权的时候是这样的(或类似的)：GRANT SELECT ON testDB.user TO ‘username’@’%’, 则在使用REVOKE SELECT ON . FROM ‘username’@’%’;命令并不能撤销该用户对testDB数据库中user表的SELECT 操作。相反，如果授权使用的是GRANT SELECT ON . TO ‘username’@’%’;则REVOKE SELECT ON testDB.user FROM ‘username’@’%’;命令也不能撤销该用户对testDB数据库中user表的Select 权限。
具体信息可以用命令SHOW GRANTS FOR ‘username’@’%’; 查看。
```
##### 数据库 表 查询

1. 数据库    
    ```
    创建数据库 create databse mydb1; 
    创建数据库并设置编码格式为gbk。不指定的话默认为utf-8,这个在安装的时候设置了 create database mydb2 character set gbk; 
    设置校验规则 create database mydb3 character set gbk collate gbk_chinese_ci; 
    修改数据库名称 alter database 旧名称 modify name = 新名称
    查看当前数据库服务器中的所有数据库 show databases; 
    查看前面创建的mydb2数据库的定义信息 show create database mydb2
    删除前面创建的mydb3数据库 drop database mydb3; 
    把mydb2的字符集修改为utf8 alter database mydb2 set utf8; 
    查看当前使用的数据库 select database(); 
    切换数据库 use mydb2;
    注意：注释为敲完两个短线之后要敲一个空格 -- xxx
    ```
2. 表
   1. 字段类型
      ```
      int :整型，4个字节
      double:浮点型，例如double(5,2)表示最多5位，其中2位为小数，即最大值为999.99。
      varchar:可变长度字符串类型。varchar(10) ‘aaa’ 占3位
      datetime:日期时间类型。yyyy-MM-dd hh:mm:ss
      char:固定长度字符串类型。char(10) ‘aaa ’ 占10位
      text:大文本字符串类型
      blob:字节类型
      date：日期类型，格式为：yyyy-MM-dd
      time:时间类型，格式为：hh:mm:ss
      timestamp:时间戳类型 yyyy-MM-dd hh:mm:ss 会自动赋值
      空值：null
      字符串类型和日期类型都要用单引号括起来
      ```
    1. 建表
         - 创建新表
            ```
            CREATE TABLE IF NOT EXISTS runoob_tbl(
              runoob_id INT UNSIGNED AUTO_INCREMENT,
              runoob_title VARCHAR(100) NOT NULL,
              runoob_author VARCHAR(40) NOT NULL,
              submission_date DATE,
              PRIMARY KEY ( runoob_id )
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;

            CREATE TABLE IF NOT EXISTS t_user( 
              u_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL COMMENT '编号', 
              u_phone BIGINT NOT NULL COMMENT '账号-手机号', 
              u_passwd VARCHAR(100) NOT NULL COMMENT '密码，4-20字符，MD5加密', 
              u_regtime BIGINT UNSIGNED NOT NULL COMMENT '注册时间，时间戳', 
              u_check_uid BIGINT UNSIGNED COMMENT '用户类型审核人员ID', 
              PRIMARY KEY(u_id) COMMENT '主键', 
              UNIQUE KEY(u_phone) COMMENT '唯一键', FOREIGN KEY(u_check_uid) REFERENCES t_user(u_id) ON DELETE CASCADE, 
              KEY index_regtime(u_regtime) COMMENT '注册时间-索引' 
            )ENGINE=INNODB DEFAULT CHARSET=utf8
            COMMENT '用户表';
            ```
         - 通过复制表创建
            ```
            CREATE TABLE tab_new like tab_old
            ```
         - 通过查询语句创建
            ```
            CREATE TABLE tab_new as select col1,col2… from tab_old definition only #用户表 
            ```
    2. 单表约束
        主键约束：primary key,要求被修饰的字段：唯一和非空
        ```
        创建：ALTER TABLE tablename ADD PRIMARY KEY(col)
        删除：ALTER TABLE tablename DROP PRIMARY KEY(col)
        ```
        唯一约束：unique，要求被修饰的字段：唯一
        非空约束：not null，要求被修饰的字段：非空
    3. 查看表
        ```
        查看数据库中的所有表：show tables;
        查看表结构：desc/describe 表名;
        查看表的创建细节：show create table 表名;
        ```
    4. 删除表
        ```
        drop table 表名;
        ```
    5. 修改表
        ```
        alter table 表名 add 列名 类型（长度） [约束]; --添加列
        注意：列增加后将不能删除。DB2中列加上后数据类型也不能改变，唯一能改变的是增加varchar类型的长度
        alter table 表名 modify 列名 类型（长度） [约束]; --修改列类型长度及约束
        alter table 表名 change 旧列名 新列名 类型（长度） [约束];--修改表列名 
        alter table 表名 drop 列名; --删除列 
        alter table 表名 character set 字符集; --修改表的字符集 rename table 表名 to 新表名; --修改表名
        ```
    6. 对表内容的增删改
        ```
        插入数据：insert
        insert into 表(列名1，列名2，列名3..) values(值1，值2，值3..);--向表中插入某些列
        insert into 表 values(值1，值2，值3..); --向表中插入所有列
        列名与列值的类型，个数，顺序要一一对应。可以把列名当做Java中的形参，把列值当做实参。
        值不要超出列定义的长度。值如果是字符串或者日期需要加单引号。

        更新记录：update
        update 表名 set 字段名=值,字段名=值...; --这个会修改所有的数据，把一列的值都变了
        update 表名 set 字段名=值,字段名=值... where 条件;

        删除记录：delete
        delete from 表名; --删除表中所有记录
        delete from 表名 where 条件;
        truncate table 表名;
        delete删除表中的数据，是一条一条删除，不清空auto_increment记录数；删除后的数据如果在一个事务中还可以找回。
        truncate删除是把表直接drop掉，重新建表，auto_increment将置为零。删除的数据不能找回。执行速度比delete快。
        ```
3. 数据查询语言DQL
   1. 简单查询
      ```
      查询所有列
      select * from stu;
      查询指定列
      select sid,sname,age from stu;
      ```
   2. 别名查询
      ```
      as可以省略
      表别名
      select * from product as p;
      列别名
      select pname as pn from product;
      ```
   3. 去掉重复值
      ```
      用来去除重复数据，是对整个结果集(结果集就是查出来的那些数据)进行数据重复抑制的，而不是针对某一列。
      性能不好，实际多用group by去重。
      select distinct Department,SubCompany from Employee;
      ```
   4. 计算字段
      ```
      字段间计算 select age*salary,name from employee; 
      运算查询 select pname,price+10 from product; 
      comm列有很多记录的值为NULL，因为任何东西与NULL相加结果还是NULL，所以结算结果可能会出现NULL。下面使用了把NULL转换成数值0的函数
      IFNULL select *,sal+ifnull(comm,0) from emp;
      ```
   5. 条件查询
      ```
      where后的条件写法 = != <> < <= > >= between…and in(set) and or not is null
      like，_代表任意一个字符，%代表任意0-n个字符
      select * from stu where gender='female' and age<50; 
      select * from stu where sid='S_1001' and sname='lisi'; 
      select * from stu where sid in('S_1001','S_1002','S_1003');
      select * from stu where sid not in('S_1001','S_1002','S_1003')
      select * from stu where age is null; 
      select * from stu where age>=20 and age<=40; 
      -- between限制查询数据范围时包括了边界值，not between不包括
      select * from stu where age between 20 and 40; 
      select * from stu where stu where gender!='male'; 
      select * from stu where gender<>'male'; 
      select * from stu where not gender='male'; 
      select * from stu where not sname is null;
      select * from stu where sname like '_____'; -- 查询姓名由5个字母构成的学生记录 
      select * from stu where sname like '____i'; -- 查询姓名由5个字母构成，并且第5个字母为“i”的学生 
      select * from stu where sname like 'z%'; -- 查询姓名以“z”开头的学生记录 
      select * from stu where sname like '_i%';-- 查询姓名中第2个字母为“i”的学生记录 
      select * from stu where sname like '%a%';-- 查询姓名中包括“a”字母的学生记录
      ```
   6. 排序
      ```
      select * from stu order by age asc; -- 升序排序，也可以不加asc，默认为升序 
      select * from stu order by age desc; --降序 
      select * from emp order by sal desc,empno asc;
      -- 按月薪降序排序，如果月薪相同时，按编号升序排序。只有在前一个条件相同时，后一个条件才会起作用。
      ```
   7. 聚合函数
    聚合函数是用来做纵向运算的函数
       - count():统计指定列不为null的记录行数
       - max():计算指定列的最大值，如果指定列是字符串类型，那么使用字符串排序运算
       - min():计算指定列的最小值，如果指定列是字符串类型，那么使用字符串排序运算
       - sum():计算指定列的数值和，如果指定列类型不是数值类型，那么计算结果为0。求和的时候忽略null，如果都是null，则算出来的结果为null
       - avg():计算指定列的平均值，如果指定列类型不是数值类型，那么计算结果为0
      ```
      select count(*) as cnt from emp;-- 计算emp表中记录数 
      select count(comm) cnt from emp;-- 查询emp表中拥有佣金的人数，因为count()函数中给出的是comm列，那么只统计comm列非null的行数。 
      select count(*) from emp where sal>2500;-- 查询emp表中月薪大于2500的人数 
      select count(comm),count(mgr) from emp; -- 查询有佣金的人数，以及由领导的人数 
      select sum(sal) from emp; -- 查询所有雇员的佣金和 
      select sum(sal),sum(comm) from emp; -- 查询所有雇员月薪和，以及所有雇员佣金和 
      select sum(sal+ifnumm(comm,0)) from emp; -- 查询所有雇员月薪+佣金和 
      select avg(sal) from emp; select max(sal),min(sal) from emp;-- 查询最高工资和最低工资
      ```
   8. 分组查询
   当需要分组查询时需要使用group by子句，例如查询每个部分的工资和，就需要使用部门来分组。
   
   **注：凡是和聚合函数同时出现的列名，则一定要写在group by之后**
      ```
      select deptno,sum(sal) from emp group by deptno;-- 查询每个部门的编号和每个部门的工资和 
      select deptno,count(*) from emp group by deptno;-- 查询每个部门的部门编号以及每个部门的人数 
      select deptno,count(*) from emp where sal>1500 group by deptno;-- 查询每个部门的编号以及每个部门工资大于1500的人数 
      ```
   9. having子句
   where和having的区别：
      - 作用的对象不同。WHERE 子句作用于表和视图，HAVING 子句作用于组。having一般跟在group by之后，执行记录组选择的一部分来工作的。where则是执行所有数据来工作的。
      - WHERE 在分组和聚集计算之前选取输入行（因此，它控制哪些行进入聚集计算）， 而 HAVING 在分组和聚集之后选取分组的行。因此，WHERE 子句不能包含聚集函数；而having子句总是包含聚集函数
      ```
      select deptno,sum(sal) from emp group by deptno having sum(sal)>9000;
      ```
   1.  limit（方言，MySQL特有的）
   limit用来限制查询结果的起始行，以及总行数
        ```
        select * from emp limit 0,5; -- 查询5行记录，起始行从0开始。起始行从0开始，即从第一行开始
        select * from emp limit 5; -- 查询5行记录，起始行默认从0开始。起始行从0开始，即从第一行开始
        select * from emp limit 3,10;-- 查询10行记录，起始行从3开始。就是从第4行开始查
        ```
   11. 分页查询
   如果一页记录为10条，希望查看第3页应该怎么查呢？
        - 第一页记录起始行为0，一共查询10行
        - 第二页记录起始行为10，一共查询10行
        - 第三页记录起始行为20，一共查询10行
   12. 查询语句的执行顺序
       - 查询语句书写顺序：select-from-where-group by-having-order by-limit
       - 查询语句执行顺序：from-where-group by-having-select-order by-limit
       - from决定从哪儿获取数据，where，group by，having决定决定显示那几行，select决定显示的列，order by对列进行排序，limit觉得获取哪些数据。
4. 多表查询
   1. 合并结果集
      ```
      create table A(
          name varchar(10),
          score int
      ); create table B(
          name varchar(10),
          score int
      ); 
      insert into A values('a',10),('b',20),('c',30);-- 这种语法可以插入三条数据 
      insert into B values('a',10),('b',20),('d',40);
      ```
      union，合并两个或多个select语句的结果集。条件：每个结果集必须有相同的列数，相容的数据类型。
      union运算符合并了两个查询结果结果集，其中完全重复的数据被合并为了一条。如果要返回所有记录，在后边添加all。
      ```
      select * from A
      union
      select * from B;

      select * from A
      union all
      select * from B;
      ```
    2. 连接查询
   (inner) join
   Left/right/full (outer) join [where …]
        ```
        通过left join去重
        select test1.*,t2.kjxyh from test1 left join(
        Select * From
        (
        select a.*,row_number() over(partition by Name,sex order by id) r
        from test2 a
        ) where r = 1 ) t2
        on  test1.Name = t2.Name And  test1.sex = t2.sex
        ```
   1. 子查询
   SQL语句允许将一个查询语句做为一个结果集供其他SQL语句使用，就像使用普通的表一样，被当作结果集的查询语句被称为子查询。
      - 若结果集为单行单列（标量子查询），则可放在select或where语句中
      - 若结果集为多行单列，可放在where语句中，配合in使用
      - 若结果集中有多行多列（就相当于一个表，派生表），一般作为数据源进行再一次检索。
      ```
      -- 查询与SCOTT同一个部门的员工 
      select * from emp where deptno=(select deptno from emp where ename='SCOTT'); 
      -- 查询工作和工资与MARTIN完全相同的员工信息 
      select * from emp where (job,sal) in (select job,sal from emp where ename='MARTIN'); 
      -- 查询有2个以上直接下属的员工信息 
      select * from emp where empno in (select mgr from emp group by mgr having count(mgr)>=2); 
      -- 查询员工编号为7788的员工名称、员工工资、部门名称、部门地址 
      select e.ename,e.sal,d.dname,d.loc from emp e,(select dname,loc,deptno from dept) d where e.deptno=d.deptno and e.empno=7788;
      ```
#### mysql的InnoDB引擎和Myisam的区别

##### 区别

1. InnoDB支持事务，MyISAM不支持，对于InnoDB每一条SQL语言都默认封装成事务，自动提交，这样会影响速度，所以最好把多条SQL语言放在begin和commit之间，组成一个事务；  
2. InnoDB支持外键，而MyISAM不支持。对一个包含外键的InnoDB表转为MYISAM会失败；  
3. InnoDB是聚集索引，数据文件是和索引绑在一起的，必须要有主键，通过主键索引效率很高。但是辅助索引需要两次查询，先查询到主键，然后再通过主键查询到数据。因此，主键不应该过大，因为主键太大，其他索引也都会很大。而MyISAM是非聚集索引，数据文件是分离的，索引保存的是数据文件的指针。主键索引和辅助索引是独立的。
4. InnoDB不保存表的具体行数，执行`select count(*) from table`时需要全表扫描。而MyISAM用一个变量保存了整个表的行数，执行上述语句时只需要读出该变量即可，速度很快；
5. Innodb不支持全文索引，而MyISAM支持全文索引，查询效率上MyISAM要高；
6. InnoDB支持行锁和表锁，Myisam只支持表锁。

##### 如何选择

1. 是否要支持事务，如果要请选择innodb，如果不需要可以考虑MyISAM；
2. 如果表中绝大多数都只是读查询，可以考虑MyISAM，如果既有读写也挺频繁，请使用InnoDB；
3. 系统奔溃后，MyISAM恢复起来更困难，能否接受；
4. 如果并发要求高，使用InnoDB；
5. MySQL5.5版本开始Innodb已经成为Mysql的默认引擎(之前是MyISAM)，说明其优势是有目共睹的，如果你不知道用什么，那就用InnoDB，至少不会差。

##### 简言之

1. myisam支持全文索引，查询效率更高。innodb不支持全文索引，查询效率差myisam6-7倍；

2. innodb支持事务，行锁，外键。myisam不支持。如果数据表涉及的存储数据多、查询多，用myisam，如文章表。如果数据表涉及业务逻辑多，增删改操作多，就用innodb，如订单表。

3. innodb支持行锁和表锁，myisam只支持表锁。由于行锁颗粒度很小，所以发生锁定资源争用的概率也最小，具有更大的并发处理能力。

#### mysql的四种事务隔离级别

|           隔离级别           | 脏读  | 不可重复读 | 幻读  |
| :--------------------------: | :---: | :--------: | :---: |
| 读已提交（read-uncommitted） |   √   |     √      |   √   |
|  读未提交（read-committed）  |   ×   |     √      |   √   |
| 可重复读（repeatable-read）  |   ×   |     ×      |   √   |
|   可串行化（serializable）   |   ×   |     ×      |   ×   |

##### 事务的并发问题

1. 脏读：是指在一个事务处理过程里读取了另一个未提交的事务中的数据。事务A读取了事务B更新的数据，然后B回滚操作，那么A读取到的数据是脏数据。
2. 不可重复读（在一个事务的两次查询之中数据值不一致）：是指在对于数据库中的某个数据，一个事务范围内多次查询却返回了不同的数据值，这是由于在查询间隔，被另一个事务修改(update/delete)并提交了。
3. 幻读（在一个事务的两次查询中数据笔数不一致）：幻读是事务非独立执行时发生的一种现象。例如事务T1对一个表中所有的行的某个数据项做了从“1”修改为“2”的操作，这时事务T2又对这个表中插入(inert)了一行数据项，而这个数据项的数值还是为“1”并且提交给数据库。而操作事务T1的用户如果再查看刚刚修改的数据，会发现还有一行没有修改，其实这行是从事务T2中添加的，就好像产生幻觉一样，这就是发生了幻读。

- 小结：不可重复读的和幻读很容易混淆，不可重复读侧重于修改，幻读侧重于新增或删除。解决不可重复读的问题只需锁住满足条件的行，解决幻读需要锁表

##### 四种隔离级别

在MySQL的众多存储引擎中，只有InnoDB支持事务，所有这里说的事务隔离级别指的是InnoDB下的事务隔离级别。

1. Read Uncommitted（读未提交）：一个事务可以读取到另一个事务未提交的修改。这会带来脏读、幻读、不可重复读问题。（基本没用）。
2. Read Committed（读已提交）：一个事务只能读取另一个事务已经提交的修改。其避免了脏读，但仍然存在不可重复读和幻读问题。（oracle等数据库的默认级别）
3. Repeatable Read（可重复读）： 同一个事务中多次读取相同的数据返回的结果是一样的。其避免了脏读和不可重复读问题，但幻读依然存在。是Innodb默认隔离级别，通过MVCC（多版本并发控制）解决了幻读。
4. Serializable（可串行化）：事务串行执行。避免了以上所有问题。这是最高的隔离级别，它通过强制事务排序，使之不可能相互冲突，从而解决幻读问题。简言之，它是在每个读的数据行上加上共享锁。在这个级别，可能导致大量的超时现象和锁竞争。
   
##### 

1. Read Uncommitted（读未提交）：
2. Read Committed（读已提交）：
3. Repeatable Read（可重复读）：
4. Serializable（可串行化）：


##### RR模式中InnoDB引擎的MVCC解决幻读

1. 说明
   网上看到大量的文章讲到MVCC都是说给没一行增加两个隐藏的字段分别表示行的创建时间以及过期时间，它们存储的并不是时间，而是事务版本号。

   事实上，这种说法并不准确，严格的来讲，InnoDB会给数据库中的每一行增加三个字段，它们分别是DB_TRX_ID、DB_ROLL_PTR、DB_ROW_ID。

   但是，为了理解的方便，我们可以这样去理解，索引接下来的讲解中也还是用这两个字段的方式去理解。

2. 增删查改
   在InnoDB中，给每行增加两个隐藏字段来实现MVCC，一个用来记录数据行的创建时间，另一个用来记录行的过期时间（删除时间）。在实际操作中，存储的并不是时间，而是事务的版本号，每开启一个新事务，事务的版本号就会递增。

   于是乎，默认的隔离级别（REPEATABLE READ）下，增删查改变成了这样：
      - SELECT
        读取创建版本小于或等于当前事务版本号，并且删除版本为空或大于当前事务版本号的记录。这样可以保证在读取之前记录是存在的。
      - INSERT
        将当前事务的版本号保存至行的创建版本号
      - UPDATE
        新插入一行，并以当前事务的版本号作为新行的创建版本号，同时将原记录行的删除版本号设置为当前事务版本号
      - DELETE
        将当前事务的版本号保存至行的删除版本号
3. 快照读和当前读
   - 快照读：读取的是快照版本，也就是历史版本
   - 当前读：读取的是最新版本
   - 普通的SELECT就是快照读，而UPDATE、DELETE、INSERT、SELECT ...  LOCK IN SHARE MODE、SELECT ... FOR UPDATE是当前读。

4. 一致性非锁定读和锁定读
   - 锁定读
   在一个事务中，标准的SELECT语句是不会加锁，但是有两种情况例外。

        ``` mysql
        SELECT ... LOCK IN SHARE MODE
        ```

     给记录假设共享锁，这样一来的话，其它事务只能读不能修改，直到当前事务提交

        ``` mysql
        SELECT ... FOR UPDATE
        ```

     给索引记录加锁，这种情况下跟UPDATE的加锁情况是一样的

   - 一致性非锁定读
   consistent read （一致性读），InnoDB用多版本来提供查询数据库在某个时间点的快照。如果隔离级别是REPEATABLE READ，那么在同一个事务中的所有一致性读都读的是事务中第一个这样的读读到的快照；如果是READ COMMITTED，那么一个事务中的每一个一致性读都会读到它自己刷新的快照版本。Consistent read（一致性读）是READ COMMITTED和REPEATABLE READ隔离级别下普通SELECT语句默认的模式。一致性读不会给它所访问的表加任何形式的锁，因此其它事务可以同时并发的修改它们。

   - 悲观锁和乐观锁
     悲观锁，正如它的名字那样，数据库总是认为别人会去修改它所要操作的数据，因此在数据库处理过程中将数据加锁。其实现依靠数据库底层。
     
     乐观锁，如它的名字那样，总是认为别人不会去修改，只有在提交更新的时候去检查数据的状态。通常是给数据增加一个字段来标识数据的版本。
   - 锁
  
     有这样三种锁我们需要了解
     - Record Locks（记录锁）：在索引记录上加锁。
     - Gap Locks（间隙锁）：在索引记录之间加锁，或者在第一个索引记录之前加锁，或者在最后一个索引记录之后加锁。
     - Next-Key Locks：在索引记录上加锁，并且在索引记录之前的间隙加锁。它相当于是Record Locks与Gap Locks的一个结合。
     
     假设一个索引包含以下几个值：10,11,13,20。那么这个索引的next-key锁将会覆盖以下区间：
      ```
      (negative infinity, 10]
      (10, 11]
      (11, 13]
      (13, 20]
      (20, positive infinity)
      ```
      了解了以上概念之后，接下来具体就简单分析下REPEATABLE READ隔离级别是如何实现的

5. 理论分析
   
   在默认的隔离级别中，普通的SELECT用的是一致性读不加锁。而对于锁定读、UPDATE和DELETE，则需要加锁，至于加什么锁视情况而定。如果你对一个唯一索引使用了唯一的检索条件，那么只需锁定索引记录即可；如果你没有使用唯一索引作为检索条件，或者用到了索引范围扫描，那么将会使用间隙锁或者next-key锁以此来阻塞其它会话向这个范围内的间隙插入数据。

   作者曾经有一个误区，认为按照前面说MVCC下的增删查改的行为就不会出现任何问题，也不会出现不可重复读和幻读。但其实是大错特错。

   举个很简单的例子，假设事务A更新表中id=1的记录，而事务B也更新这条记录，并且B先提交，如果按照前面MVVC说的，事务A读取id=1的快照版本，那么它看不到B所提交的修改，此时如果直接更新的话就会覆盖B之前的修改，这就不对了，可能B和A修改的不是一个字段，但是这样一来，B的修改就丢失了，这是不允许的。

   所以，在修改的时候一定不是快照读，而是当前读。

   而且，前面也讲过只有普通的SELECT才是快照读，其它诸如UPDATE、删除都是当前读。修改的时候加锁这是必然的，同时为了防止幻读的出现还需要加间隙锁。

   一致性读保证了可用重复读
   间隙锁防止了幻读

   回想一下

   1. 利用MVCC实现一致性非锁定读，这就有保证在同一个事务中多次读取相同的数据返回的结果是一样的，解决了不可重复读的问题

   2. 利用Gap Locks和Next-Key可以阻止其它事务在锁定区间内插入数据，因此解决了幻读问题

   综上所述，默认隔离级别的实现依赖于MVCC和锁，再具体一点是一致性读和锁。

#### mysql的锁机制及引擎锁级优化

##### 表级锁和行级锁和页级锁的特点

1. 表级锁定（table-level）

   表级别的锁定是MySQL各存储引擎中最大颗粒度的锁定机制。该锁定机制最大的特点是实现逻辑非常简单，带来的系统负面影响最小。所以获取锁和释放锁的速度很快。由于表级锁一次会将整个表锁定，所以可以很好的避免困扰我们的死锁问题。

   当然，锁定颗粒度大所带来最大的负面影响就是出现锁定资源争用的概率也会最高，致使并大度大打折扣。

   使用表级锁定的主要是MyISAM，MEMORY，CSV等一些非事务性存储引擎。
2. 行级锁定（row-level）

   行级锁定最大的特点就是锁定对象的颗粒度很小，也是目前各大数据库管理软件所实现的锁定颗粒度最小的。由于锁定颗粒度很小，所以发生锁定资源争用的概率也最小，能够给予应用程序尽可能大的并发处理能力而提高一些需要高并发应用系统的整体性能。
  
   虽然能够在并发处理能力上面有较大的优势，但是行级锁定也因此带来了不少弊端。由于锁定资源的颗粒度很小，所以每次获取锁和释放锁需要做的事情也更多，带来的消耗自然也就更大了。此外，行级锁定也最容易发生死锁。

   使用行级锁定的主要是InnoDB存储引擎。
3. 页级锁定（page-level）

   页级锁定是MySQL中比较独特的一种锁定级别，在其他数据库管理软件中也并不是太常见。页级锁定的特点是锁定颗粒度介于行级锁定与表级锁之间，所以获取锁定所需要的资源开销，以及所能提供的并发处理能力也同样是介于上面二者之间。另外，页级锁定和行级锁定一样，会发生死锁。

   在数据库实现资源锁定的过程中，随着锁定资源颗粒度的减小，锁定相同数据量的数据所需要消耗的内存数量是越来越多的，实现算法也会越来越复杂。不过，随着锁定资源颗粒度的减小，应用程序的访问请求遇到锁等待的可能性也会随之降低，系统整体并发度也随之提升。

   使用页级锁定的主要是BerkeleyDB存储引擎。

- 总的来说，MySQL这3种锁的特性可大致归纳如下：
  
   表级锁：开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高，并发度最低；MyISAM，MEMORY，CSV等非事务性存储引擎。
  
   行级锁：开销大，加锁慢；会出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度也最高；InnoDB存储引擎。    
  
   页面锁：开销和加锁时间界于表锁和行锁之间；会出现死锁；锁定粒度界于表锁和行锁之间，并发度一般；BerkeleyDB存储引擎。

   适用：从锁的角度来说，表级锁更适合于以查询为主，只有少量按索引条件更新数据的应用，如Web应用；而行级锁则更适合于有大量按索引条件并发更新少量不同数据，同时又有并发查询的应用，如一些在线事务处理（OLTP）系统。

    |                     锁级别                     | 颗粒度 | 加锁时间 | 加锁和释放锁的开销 | 是否会发生死锁 | 并发度 |           存储引擎            |         适用          |
    | :--------------------------------------------: | :----: | :------: | :----------------: | :------------: | :----: | :---------------------------: | :-------------------: |
    |                     表级锁                     |  最大  |   最快   |        最小        |      不会      |  最低  | MyISAM，MEMORY，CSV等非事务性 | 少量索引条件 web应用  |
    | 行级锁（只有并发度占优势，并且都和表级锁相反） |  最小  |   最慢   |        最大        |       会       |  最高  |            InnoDB             | 大量索引条件 并发查询 |
    |            页级锁（都介于两者之间）            |  之间  |   一般   |        之间        |       会       |  之间  |          BerkeleyDB           |         ——          |

##### 表级锁

- 对于MyISAM存储引擎，虽然使用表级锁定在锁定实现的过程中比实现行级锁定或者页级锁所带来的附加成本都要小，锁定本身所消耗的资源也是最少。但是由于锁定的颗粒度比较到，所以造成锁定资源的争用情况也会比其他的锁定级别都要多，从而在较大程度上会降低并发处理能力。所以，在优化MyISAM存储引擎锁定问题的时候，最关键的就是如何让其提高并发度。由于锁定级别是不可能改变的了，所以我们首先需要尽可能让锁定的时间变短，然后就是让可能并发进行的操作尽可能的并发。

1. 查询表级锁争用情况
  MySQL内部有两组专门的状态变量记录系统内部锁资源争用情况：

    ``` mysql
      mysql> show status like 'table%';
      +----------------------------+---------+
      | Variable_name              | Value   |
      +----------------------------+---------+
      | Table_locks_immediate      | 100     |
      | Table_locks_waited         | 11      |
      +----------------------------+---------+
    ```

      这里有两个状态变量记录MySQL内部表级锁定的情况，两个变量说明如下：

      Table_locks_immediate：产生表级锁定的次数；

      Table_locks_waited：出现表级锁定争用而发生等待的次数；

      两个状态值都是从系统启动后开始记录，出现一次对应的事件则数量加1。如果这里的Table_locks_waited状态值比较高，那么说明系统中表级锁定争用现象比较严重，就需要进一步分析为什么会有较多的锁定资源争用了。

2. 缩短锁定时间
  
   如何让锁定时间尽可能的短呢？唯一的办法就是让我们的Query执行时间尽可能的短。
    1. 尽两减少大的复杂Query，将复杂Query分拆成几个小的Query分布进行；
    2. 尽可能的建立足够高效的索引，让数据检索更迅速；
    3. 尽量让MyISAM存储引擎的表只存放必要的信息，控制字段类型；
    4. 利用合适的机会优化MyISAM表数据文件。

3. 分离能并行的操作

   说到MyISAM的表锁，而且是读写互相阻塞的表锁，可能有些人会认为在MyISAM存储引擎的表上就只能是完全的串行化，没办法再并行了。大家不要忘记了，MyISAM的存储引擎还有一个非常有用的特性，那就是ConcurrentInsert（并发插入）的特性。

   MyISAM存储引擎有一个控制是否打开Concurrent Insert功能的参数选项：concurrent_insert，可以设置为0，1或者2。三个值的具体说明如下：

   concurrent_insert=2，无论MyISAM表中有没有空洞，都允许在表尾并发插入记录；

   concurrent_insert=1，如果MyISAM表中没有空洞（即表的中间没有被删除的行），MyISAM允许在一个进程读表的同时，另一个进程从表尾插入记录。这也是MySQL的默认设置；

   concurrent_insert=0，不允许并发插入。

   可以利用MyISAM存储引擎的并发插入特性，来解决应用中对同一表查询和插入的锁争用。例如，将concurrent_insert系统变量设为2，总是允许并发插入；同时，通过定期在系统空闲时段执行OPTIMIZE TABLE语句来整理空间碎片，收回因删除记录而产生的中间空洞。

4. 合理利用读写优先级
  
   MyISAM存储引擎的是读写互相阻塞的，那么，一个进程请求某个MyISAM表的读锁，同时另一个进程也请求同一表的写锁，MySQL如何处理呢？
  
   答案是写进程先获得锁。不仅如此，即使读请求先到锁等待队列，写请求后到，写锁也会插到读锁请求之前。

   这是因为MySQL的表级锁定对于读和写是有不同优先级设定的，默认情况下是写优先级要大于读优先级。

   所以，如果我们可以根据各自系统环境的差异决定读与写的优先级：

   通过执行命令SET LOW_PRIORITY_UPDATES=1，使该连接读比写的优先级高。如果我们的系统是一个以读为主，可以设置此参数，如果以写为主，则不用设置；
  
   通过指定INSERT、UPDATE、DELETE语句的LOW_PRIORITY属性，降低该语句的优先级。

   虽然上面方法都是要么更新优先，要么查询优先的方法，但还是可以用其来解决查询相对重要的应用（如用户登录系统）中，读锁等待严重的问题。

   另外，MySQL也提供了一种折中的办法来调节读写冲突，即给系统参数max_write_lock_count设置一个合适的值，当一个表的读锁达到这个值后，MySQL就暂时将写请求的优先级降低，给读进程一定获得锁的机会。

   这里还要强调一点：一些需要长时间运行的查询操作，也会使写进程“饿死”，因此，应用中应尽量避免出现长时间运行的查询操作，不要总想用一条SELECT语句来解决问题，因为这种看似巧妙的SQL语句，往往比较复杂，执行时间较长，在可能的情况下可以通过使用中间表等措施对SQL语句做一定的“分解”，使每一步查询都能在较短时间完成，从而减少锁冲突。如果复杂查询不可避免，应尽量安排在数据库空闲时段执行，比如一些定期统计可以安排在夜间执行。

##### 行级锁

- 行级锁定不是MySQL自己实现的锁定方式，而是由其他存储引擎自己所实现的，如广为大家所知的InnoDB存储引擎，以及MySQL的分布式存储引擎NDBCluster等都是实现了行级锁定。考虑到行级锁定君由各个存储引擎自行实现，而且具体实现也各有差别，而InnoDB是目前事务型存储引擎中使用最为广泛的存储引擎，所以这里我们就主要分析一下InnoDB的锁定特性。

1. InnoDB锁定模式及实现机制

   考虑到行级锁定君由各个存储引擎自行实现，而且具体实现也各有差别，而InnoDB是目前事务型存储引擎中使用最为广泛的存储引擎，所以这里我们就主要分析一下InnoDB的锁定特性。
  
   总的来说，InnoDB的锁定机制和Oracle数据库有不少相似之处。InnoDB的行级锁定同样分为两种类型，共享锁和排他锁，而在锁定机制的实现过程中为了让行级锁定和表级锁定共存，InnoDB也同样使用了意向锁（表级锁定）的概念，也就有了意向共享锁和意向排他锁这两种。
  
   当一个事务需要给自己需要的某个资源加锁的时候，如果遇到一个共享锁正锁定着自己需要的资源的时候，自己可以再加一个共享锁，不过不能加排他锁。但是，如果遇到自己需要锁定的资源已经被一个排他锁占有之后，则只能等待该锁定释放资源之后自己才能获取锁定资源并添加自己的锁定。而意向锁的作用就是当一个事务在需要获取资源锁定的时候，如果遇到自己需要的资源已经被排他锁占用的时候，该事务可以需要锁定行的表上面添加一个合适的意向锁。如果自己需要一个共享锁，那么就在表上面添加一个意向共享锁。而如果自己需要的是某行（或者某些行）上面添加一个排他锁的话，则先在表上面添加一个意向排他锁。意向共享锁可以同时并存多个，但是意向排他锁同时只能有一个存在。所以，可以说InnoDB的锁定模式实际上可以分为四种：共享锁（S），排他锁（X），意向共享锁（IS）和意向排他锁（IX），我们可以通过以下表格来总结上面这四种所的共存逻辑关系：

   如果一个事务请求的锁模式与当前的锁兼容，InnoDB就将请求的锁授予该事务；反之，如果两者不兼容，该事务就要等待锁释放。

    |       ——       | 共享锁（S） | 排它锁（X） | 意向共享锁（IS） | 意向排它锁（IX） |
    | :--------------: | :---------: | :---------: | :--------------: | :--------------: |
    |   共享锁（S）    |    兼容     |    冲突     |       兼容       |       冲突       |
    |   排它锁（X）    |    冲突     |    冲突     |       冲突       |       冲突       |
    | 意向共享锁（IS） |    兼容     |    冲突     |       兼容       |       兼容       |
    | 意向排它锁（IX） |    冲突     |    冲突     |       兼容       |       兼容       |

   意向锁是InnoDB自动加的，不需用户干预。对于UPDATE、DELETE和INSERT语句，InnoDB会自动给涉及数据集加排他锁（X)；对于普通SELECT语句，InnoDB不会加任何锁；事务可以通过以下语句显示给记录集加共享锁或排他锁。

      ``` mysql
      共享锁 (S) : SELECT * FROM table_name WHERE ... LOCK IN SHARE MODE
      排他锁 (X) : SELECT * FROM table_name WHERE ... FOR UPDATE
      ```

2. InnoDB行锁实现方式

   InnoDB行锁是通过给索引上的索引项加锁来实现的，只有通过索引条件检索数据，InnoDB才使用行级锁，否则，InnoDB将使用表锁
  
   在实际应用中，要特别注意InnoDB行锁的这一特性，不然的话，可能导致大量的锁冲突，从而影响并发性能。下面通过一些实际例子来加以说明。
    1. 在不通过索引条件查询的时候，InnoDB确实使用的是表锁，而不是行锁。
    2. 由于MySQL的行锁是针对索引加的锁，不是针对记录加的锁，所以虽然是访问不同行的记录，但是如果是使用相同的索引键，是会出现锁冲突的。
    3. 当表有多个索引的时候，不同的事务可以使用不同的索引锁定不同的行，另外，不论是使用主键索引、唯一索引或普通索引，InnoDB都会使用行锁来对数据加锁。
    4. 即便在条件中使用了索引字段，但是否使用索引来检索数据是由MySQL通过判断不同执行计划的代价来决定的，如果MySQL认为全表扫描效率更高，比如对一些很小的表，它就不会使用索引，这种情况下InnoDB将使用表锁，而不是行锁。因此，在分析锁冲突时，别忘了检查SQL的执行计划，以确认是否真正使用了索引。

3. 间隙锁（Next-Key锁）

   当我们用范围条件而不是相等条件检索数据，并请求共享或排他锁时，InnoDB会给符合条件的已有数据记录的索引项加锁；
  
   对于键值在条件范围内但并不存在的记录，叫做“间隙（GAP)”，InnoDB也会对这个“间隙”加锁，这种锁机制就是所谓的间隙锁（Next-Key锁）。
  例：
  
   假如emp表中只有101条记录，其empid的值分别是 1,2,...,100,101，下面的SQL：

     ``` mysql
     mysql> select * from emp where empid > 100 for update;
     ```

   是一个范围条件的检索，InnoDB不仅会对符合条件的empid值为101的记录加锁，也会对empid大于101（这些记录并不存在）的“间隙”加锁。

   InnoDB使用间隙锁的目的：

    1. 防止幻读，以满足相关隔离级别的要求。对于上面的例子，要是不使用间隙锁，如果其他事务插入了empid大于100的任何记录，那么本事务如果再次执行上述语句，就会发生幻读；
    2. 为了满足其恢复和复制的需要。很显然，在使用范围条件检索并锁定记录时，即使某些不存在的键值也会被无辜的锁定，而造成在锁定的时候无法插入锁定键值范围内的任何数据。在某些场景下这可能会对性能造成很大的危害。

   除了间隙锁给InnoDB带来性能的负面影响之外，通过索引实现锁定的方式还存在其他几个较大的性能隐患：
    1. 当Query无法利用索引的时候，InnoDB会放弃使用行级别锁定而改用表级别的锁定，造成并发性能的降低；
    2. 当Query使用的索引并不包含所有过滤条件的时候，数据检索使用到的索引键所只想的数据可能有部分并不属于该Query的结果集的行列，但是也会被锁定，因为间隙锁锁定的是一个范围，而不是具体的索引键；
    3. 当Query在使用索引定位数据的时候，如果使用的索引键一样但访问的数据行不同的时候（索引只是过滤条件的一部分），一样会被锁定。

   因此，在实际应用开发中，尤其是并发插入比较多的应用，我们要尽量优化业务逻辑，尽量使用相等条件来访问更新数据，避免使用范围条件。
  
   还要特别说明的是，InnoDB除了通过范围条件加锁时使用间隙锁外，如果使用相等条件请求给一个不存在的记录加锁，InnoDB也会使用间隙锁。

4. 死锁

   其他上文讲过，MyISAM表锁是deadlock free的，这是因为MyISAM总是一次获得所需的全部锁，要么全部满足，要么等待，因此不会出现死锁。但在InnoDB中，除单个SQL组成的事务外，锁是逐步获得的，当两个事务都需要获得对方持有的排他锁才能继续完成事务，这种循环锁等待就是典型的死锁。
  
   在InnoDB的事务管理和锁定机制中，有专门检测死锁的机制，会在系统中产生死锁之后的很短时间内就检测到该死锁的存在。当InnoDB检测到系统中产生了死锁之后，InnoDB会通过相应的判断来选这产生死锁的两个事务中较小的事务来回滚，而让另外一个较大的事务成功完成。
  
   那InnoDB是以什么来为标准判定事务的大小的呢？MySQL官方手册中也提到了这个问题，实际上在InnoDB发现死锁之后，会计算出两个事务各自插入、更新或者删除的数据量来判定两个事务的大小。也就是说哪个事务所改变的记录条数越多，在死锁中就越不会被回滚掉。
  
   但是有一点需要注意的就是，当产生死锁的场景中涉及到不止InnoDB存储引擎的时候，InnoDB是没办法检测到该死锁的，这时候就只能通过锁定超时限制参数InnoDB_lock_wait_timeout来解决。
  
   需要说明的是，这个参数并不是只用来解决死锁问题，在并发访问比较高的情况下，如果大量事务因无法立即获得所需的锁而挂起，会占用大量计算机资源，造成严重性能问题，甚至拖跨数据库。我们通过设置合适的锁等待超时阈值，可以避免这种情况发生。

   通常来说，死锁都是应用设计的问题，通过调整业务流程、数据库对象设计、事务大小，以及访问数据库的SQL语句，绝大部分死锁都可以避免。下面就通过实例来介绍几种避免死锁的常用方法：
    1. 在应用中，如果不同的程序会并发存取多个表，应尽量约定以相同的顺序来访问表，这样可以大大降低产生死锁的机会。
    2. 在程序以批量方式处理数据的时候，如果事先对数据排序，保证每个线程按固定的顺序来处理记录，也可以大大降低出现死锁的可能。
    3. 在事务中，如果要更新记录，应该直接申请足够级别的锁，即排他锁，而不应先申请共享锁，更新时再申请排他锁，因为当用户申请排他锁时，其他事务可能又已经获得了相同记录的共享锁，从而造成锁冲突，甚至死锁。
    4. 在REPEATABLE-READ隔离级别下，如果两个线程同时对相同条件记录用SELECT...FOR UPDATE加排他锁，在没有符合该条件记录情况下，两个线程都会加锁成功。程序发现记录尚不存在，就试图插入一条新记录，如果两个线程都这么做，就会出现死锁。这种情况下，将隔离级别改成READ COMMITTED，就可避免问题。
    5. 当隔离级别为READ COMMITTED时，如果两个线程都先执行SELECT...FOR UPDATE，判断是否存在符合条件的记录，如果没有，就插入记录。此时，只有一个线程能插入成功，另一个线程会出现锁等待，当第1个线程提交后，第2个线程会因主键重出错，但虽然这个线程出错了，却会获得一个排他锁。这时如果有第3个线程又来申请排他锁，也会出现死锁。对于这种情况，可以直接做插入操作，然后再捕获主键重异常，或者在遇到主键重错误时，总是执行ROLLBACK释放获得的排他锁。

5. 什么时候使用表锁

   对于InnoDB表，在绝大部分情况下都应该使用行级锁，因为事务和行锁往往是我们之所以选择InnoDB表的理由。但在个别特殊事务中，也可以考虑使用表级锁：

    1. 事务需要更新大部分或全部数据，表又比较大，如果使用默认的行锁，不仅这个事务执行效率低，而且可能造成其他事务长时间锁等待和锁冲突，这种情况下可以考虑使用表锁来提高该事务的执行速度。

    2. 事务涉及多个表，比较复杂，很可能引起死锁，造成大量事务回滚。这种情况也可以考虑一次性锁定事务涉及的表，从而避免死锁、减少数据库因事务回滚带来的开销。
      当然，应用中这两种事务不能太多，否则，就应该考虑使用MyISAM表了。

    在InnoDB下，使用表锁要注意以下两点：

    1. 使用LOCK TABLES虽然可以给InnoDB加表级锁，但必须说明的是，表锁不是由InnoDB存储引擎层管理的，而是由其上一层──MySQL Server负责的，仅当autocommit=0、InnoDB_table_locks=1（默认设置）时，InnoDB层才能知道MySQL加的表锁，MySQL Server也才能感知InnoDB加的行锁，这种情况下，InnoDB才能自动识别涉及表级锁的死锁，否则，InnoDB将无法自动检测并处理这种死锁。

    2. 在用 LOCK TABLES对InnoDB表加锁时要注意，要将AUTOCOMMIT设为0，否则MySQL不会给表加锁；事务结束前，不要用UNLOCK TABLES释放表锁，因为UNLOCK TABLES会隐含地提交事务；COMMIT或ROLLBACK并不能释放用LOCK TABLES加的表级锁，必须用UNLOCK TABLES释放表锁。正确的方式见如下语句：
      例如，如果需要写表t1并从表t读，可以按如下做：

          ``` mysql
          SET AUTOCOMMIT=0;
          LOCK TABLES t1 WRITE, t2 READ, ...;
          [do something with tables t1 and t2 here];
          COMMIT;
          UNLOCK TABLES;
          ```

6. InnoDB行锁优化建议

   InnoDB存储引擎由于实现了行级锁定，虽然在锁定机制的实现方面所带来的性能损耗可能比表级锁定会要更高一些，但是在整体并发处理能力方面要远远优于MyISAM的表级锁定的。当系统并发量较高的时候，InnoDB的整体性能和MyISAM相比就会有比较明显的优势了。但是，InnoDB的行级锁定同样也有其脆弱的一面，当我们使用不当的时候，可能会让InnoDB的整体性能表现不仅不能比MyISAM高，甚至可能会更差。

    1. 要想合理利用InnoDB的行级锁定，做到扬长避短，我们必须做好以下工作：
        1. 尽可能让所有的数据检索都通过索引来完成，从而避免InnoDB因为无法通过索引键加锁而升级为表级锁定；
        2. 合理设计索引，让InnoDB在索引键上面加锁的时候尽可能准确，尽可能的缩小锁定范围，避免造成不必要的锁定而影响其他Query的执行；
        3. 尽可能减少基于范围的数据检索过滤条件，避免因为间隙锁带来的负面影响而锁定了不该锁定的记录；
        4. 尽量控制事务的大小，减少锁定的资源量和锁定时间长度；
        5. 在业务环境允许的情况下，尽量使用较低级别的事务隔离，以减少MySQL因为实现事务隔离级别所带来的附加成本。

    2. 由于InnoDB的行级锁定和事务性，所以肯定会产生死锁，下面是一些比较常用的减少死锁产生概率的小建议：
        1. 类似业务模块中，尽可能按照相同的访问顺序来访问，防止产生死锁；
        2. 在同一个事务中，尽可能做到一次锁定所需要的所有资源，减少死锁产生概率；
        3. 对于非常容易产生死锁的业务部分，可以尝试使用升级锁定颗粒度，通过表级锁定来减少死锁产生的概率。

    3. 可以通过检查InnoDB_row_lock状态变量来分析系统上的行锁的争夺情况：

        ``` mysql
        mysql> show status like 'InnoDB_row_lock%';
        +-------------------------------+-------+
        | Variable_name                 | Value |
        +-------------------------------+-------+
        | InnoDB_row_lock_current_waits | 0     |
        | InnoDB_row_lock_time          | 0     |
        | InnoDB_row_lock_time_avg      | 0     |
        | InnoDB_row_lock_time_max      | 0     |
        | InnoDB_row_lock_waits         | 0     |
        +-------------------------------+-------+
        ```

        InnoDB 的行级锁定状态变量不仅记录了锁定等待次数，还记录了锁定总时长，每次平均时长，以及最大时长，此外还有一个非累积状态量显示了当前正在等待锁定的等待数量。对各个状态量的说明如下：

        InnoDB_row_lock_current_waits：当前正在等待锁定的数量；

        InnoDB_row_lock_time：从系统启动到现在锁定总时间长度；

        InnoDB_row_lock_time_avg：每次等待所花平均时间；

        InnoDB_row_lock_time_max：从系统启动到现在等待最常的一次所花的时间；

        InnoDB_row_lock_waits：系统启动后到现在总共等待的次数；

        对于这5个状态变量，比较重要的主要是InnoDB_row_lock_time_avg（等待平均时长），InnoDB_row_lock_waits（等待总次数）以及InnoDB_row_lock_time（等待总时长）这三项。尤其是当等待次数很高，而且每次等待时长也不小的时候，我们就需要分析系统中为什么会有如此多的等待，然后根据分析结果着手指定优化计划。

        如果发现锁争用比较严重，如InnoDB_row_lock_waits和InnoDB_row_lock_time_avg的值比较高，还可以通过设置InnoDB Monitors 来进一步观察发生锁冲突的表、数据行等，并分析锁争用的原因。

        具体方法如下：

            mysql> create table InnoDB_monitor(a INT) engine=InnoDB;

        然后就可以用下面的语句来进行查看：

            mysql> show engine InnoDB status;

        监视器可以通过发出下列语句来停止查看：

            mysql> drop table InnoDB_monitor;

        设置监视器后，会有详细的当前锁等待的信息，包括表名、锁类型、锁定记录的情况等，便于进行进一步的分析和问题的确定。可能会有读者朋友问为什么要先创建一个叫InnoDB_monitor的表呢？因为创建该表实际上就是告诉InnoDB我们开始要监控他的细节状态了，然后InnoDB就会将比较详细的事务以及锁定信息记录进入MySQL的errorlog中，以便我们后面做进一步分析使用。打开监视器以后，默认情况下每15秒会向日志中记录监控的内容，如果长时间打开会导致.err文件变得非常的巨大，所以用户在确认问题原因之后，要记得删除监控表以关闭监视器，或者通过使用“--console”选项来启动服务器以关闭写日志文件。
#### mysql索引机制


### 非关系型数据库（redis）

## 操作系统（15%）
### 常用命令

## Web框架（5%）