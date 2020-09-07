

--************************************************************
--					һ�����������
--************************************************************
--�򵥸�ֵ 
declare @a int
set @a=5 
print @a 
  
--ʹ��select��丳ֵ 
declare @user1 nvarchar(50) 
select @user1='����'
print @user1 
declare @user2 nvarchar(50) 
select @user2 = Name from [User] where ID=1 
print @user2 
  
--ʹ��update��丳ֵ 
declare @user3 nvarchar(50) 
update [User] set @user3 = Name where ID=1 
print @user3


--************************************************************
--					��������ʱ�������
--************************************************************
--������ʱ��1 
create table #DU_User1 
( 
     [ID] [int]  NOT NULL, 
     [Oid] [int] NOT NULL, 
     [Login] [nvarchar](50) NOT NULL, 
     [Rtx] [nvarchar](4) NOT NULL, 
     [Name] [nvarchar](5) NOT NULL, 
     [Password] [nvarchar](max) NULL, 
     [State] [nvarchar](8) NOT NULL
); 
--����ʱ��1����һ����¼ 
insert into #DU_User1 (ID,Oid,[Login],Rtx,Name,[Password],State) values (100,2,'LS','0000','��ʱ','321','����'); 
  
--��ST_User��ѯ���ݣ�����������ɵ���ʱ�� 
select * into #DU_User2 from [User] where ID<8 
  
--��ѯ����������ʱ�� 
select * from #DU_User2 where ID<3 union select * from #DU_User1 
  
--ɾ������ʱ�� 
drop table #DU_User1 
drop table #DU_User2
 
--������ʱ�� 
CREATE TABLE #t 
( 
    [ID] [int] NOT NULL, 
    [Oid] [int] NOT NULL, 
    [Login] [nvarchar](50) NOT NULL, 
    [Rtx] [nvarchar](4) NOT NULL, 
    [Name] [nvarchar](5) NOT NULL, 
    [Password] [nvarchar](max) NULL, 
    [State] [nvarchar](8) NOT NULL, 
) 
  
--����ѯ��������������ݣ�������ʱ�� 
insert into #t select * from ST_User 
--������������ 
--select * into #t from dbo.ST_User 
  
--���һ�У�Ϊint���������Ӷ� 
alter table #t add [myid] int NOT NULL IDENTITY(1,1) 
--���һ�У�Ĭ�����ȫ��Ψһ��ʶ 
alter table #t add [myid1] uniqueidentifier NOT NULL default(newid()) 
  
select * from #t 
drop table #t
--����ѯ����������������� 
  
--������ʱ��
select IDENTITY(int,1,1)as ID, Name,[Login],[Password] into #t from ST_User 
select * from #t 
  
--������ʱ�� 
select (select SUM(1) from ST_User where ID<= a.ID) as myID,* from ST_User a order by myID


--�������� 
declare @t table
( 
    id int not null, 
    msg nvarchar(50) null
) 
insert into @t values(1,'1') 
insert into @t values(2,'2') 
select * from @t


--************************************************************
--					 ����ѭ��
--************************************************************
--whileѭ������1��100�ĺ� 
declare @a int
declare @sum int
set @a=1 
set @sum=0 
while @a<=100 
begin
    set @sum+=@a 
    set @a+=1 
end
print @sum

--************************************************************
--					�ġ��������
--************************************************************
--if,else������֧ 
if(1+1=2) 
begin
    print '��'
end
else
begin
    print '��'
end
  
--when then������֧ 
declare @today int
declare @week nvarchar(3) 
set @today=3 
set @week=case
    when @today=1 then '����һ'
    when @today=2 then '���ڶ�'
    when @today=3 then '������'
    when @today=4 then '������'
    when @today=5 then '������'
    when @today=6 then '������'
    when @today=7 then '������'
    else 'ֵ����'
end
print @week
 


--************************************************************
--					�塢�α�									**********				
--************************************************************
declare @ID int
declare @Oid int
declare @Login varchar(50) 
  
--����һ���α� 
declare user_cur cursor for select ID,Oid,[Login] from ST_User 
--���α� 
open user_cur 
while @@fetch_status=0 
begin
--��ȡ�α� 
    fetch next from user_cur into @ID,@Oid,@Login 
    print @ID 
    --print @Login 
end
close user_cur 
--�ݻ��α� 
deallocate user_cur



--************************************************************
--					����������									********			
--************************************************************
����--�������е���ʱ��
����--Inserted 
����--��Ž���insert��update ����������� 
����--Deleted 
����--��Ž���delete ��update����ǰ������

--���������� 
Create trigger User_OnUpdate  
    On ST_User  
    for Update 
As 
    declare @msg nvarchar(50) 
    --@msg��¼�޸���� 
    select @msg = N'�����ӡ�' + Deleted.Name + N'���޸�Ϊ��' + Inserted.Name + '��' from Inserted,Deleted 
    --������־�� 
    insert into [LOG](MSG)values(@msg) 
      
--ɾ�������� 
drop trigger User_OnUpdate



--************************************************************
--					�ߡ��洢����											
--************************************************************
--������output�����Ĵ洢���� 
if (exists (select * from sys.objects where name = 'PR_Sum')) drop proc PR_Sum 
CREATE PROCEDURE PR_Sum 
    @a int,
    @b int, 
    @sum int output
AS
BEGIN
    set @sum=@a+@b 
END

--����Return����ֵ�洢���� 
CREATE PROCEDURE PR_Sum2 
    @a int, 
    @b int
AS
BEGIN
    Return @a+@b 
END


--ִ�д洢���̻�ȡoutput�ͷ���ֵ 
declare @mysum int
execute PR_Sum 1,2,@mysum output
print @mysum 
  
--ִ�д洢���̻�ȡReturn�ͷ���ֵ 
declare @mysum2 int
execute @mysum2= PR_Sum2 1,2 
print @mysum2
 
  
--************************************************************
--					�ˡ��Զ��庯��										
--************************************************************
����--�����ķ��ࣺ

����--����1������ֵ����

����--����2����ֵ����

����--������������a:������ֵ����

����--������������b:������ֵ����

����--����3��ϵͳ����

����

--�½�����ֵ���� 
create function FUNC_Sum1 
( 
    @a int, 
    @b int
) 
returns int
as
begin
    return @a+@b 
end
  
--�½�������ֵ���� 
create function FUNC_UserTab_1 
( 
    @myId int
) 
returns table
as
return (select * from ST_User where ID<@myId) 
  
--�½�������ֵ���� 
create function FUNC_UserTab_2 
( 
    @myId int
) 
returns @t table
( 
    [ID] [int] NOT NULL, 
    [Oid] [int] NOT NULL, 
    [Login] [nvarchar](50) NOT NULL, 
    [Rtx] [nvarchar](4) NOT NULL, 
    [Name] [nvarchar](5) NOT NULL, 
    [Password] [nvarchar](max) NULL, 
    [State] [nvarchar](8) NOT NULL
) 
as
begin
    insert into @t select * from ST_User where ID<@myId 
    return
end
  
--���ñ�ֵ���� 
select * from dbo.FUNC_UserTab_1(15) 
--���ñ���ֵ���� 
declare @s int
set @s=dbo.FUNC_Sum1(100,50) 
print @s 
  
--ɾ������ֵ���� 
drop function FUNC_Sum1
--̸̸�Զ��庯����洢���̵�����

--һ���Զ��庯����

--����1. ���Է��ر����

--����2. �����Ķ࣬����

--������������ʹ��output������

--����������������ʱ��

--�������������ڲ��Ĳ�������Ӱ�쵽�ⲿ������

--������������ͨ��select���ؽ������

--������������update��delete�����ݿ��

--����3. ����return һ������ֵ������

--�����Զ��庯��һ�����ڸ��öȸߣ����ܼ򵥵�һ��������ǿ�ĵط���

--�����洢����

--����1. ���ܷ��ر����

--����2. �����٣�����ִ�ж����ݿ��Ĳ��������Է������ݼ�

--����3. ����returnһ������ֵ��Ҳ����ʡ��return

--�������洢����һ������ʵ�ָ��ӵĹ��ܣ����ݲ��ݷ��档

--************************************************************
--					�洢����--��ѯ��
--EXEC GetUser 1;
--************************************************************
if (exists (select * from sys.objects where name = 'GetUser')) drop proc GetUser   --�жϴ洢�����Ƿ���ڣ�������ɾ��Ȼ���ؽ���
go
create proc GetUser  --�����洢���� GetUser
@Id int --����
as 
set nocount on;  --�����ؼ��������Ӧ�ó�������
begin --��ʼ
    select * from [dbo].[User] where Id=@Id  --ִ��sql���
end;--����


--************************************************************
--					�洢����--�޸ģ�		
--EXEC UpdateUser 1,'�Դ�1',2,222,'1994-07-16 11:36:27';
--************************************************************
if (exists (select * from sys.objects where name = 'UpdateUser')) drop proc UpdateUser   --�жϴ洢�����Ƿ���ڣ�������ɾ��Ȼ���ؽ���
go
create proc UpdateUser  --�����洢���� GetUser
@Id int, --����
@Name varchar(255),--����
@Sex int, --����
@Age int, --����
@Birthday date --����
as 
set nocount on;  --�����ؼ��������Ӧ�ó�������
begin --��ʼ     
    UPDATE [dbo].[User] SET [Name]=@Name,[Sex]=@Sex, [Age]=@Age,[Birthday]=@Birthday WHERE ([Id]=@Id) --ִ��sql���
end;--����




--************************************************************
--				�洢���̷�ҳ
--EXEC Page_UserInfo  '' ,0,2
--************************************************************
if (exists (select * from sys.objects where name = 'Page_UserInfo')) drop proc Page_UserInfo   --�жϴ洢�����Ƿ���ڣ�������ɾ��Ȼ���ؽ���
go
create proc Page_UserInfo  --�����洢���� 
    @name nvarchar(255),--�û���
    @pageindex int,--�ڼ�ҳ
    @pagesize int --һҳ������
as 
set nocount on;  --�����ؼ��������Ӧ�ó�������
begin --��ʼ
    declare @pagebefore int;--ĳҳ��ʼ
    declare @pagerear int;--ĳҳ��β
	declare @condition nvarchar(2000);  --����where����
    set @pagebefore=@pagesize*@pageindex; --��ʼҳ
    set @pagerear=@pagebefore+@pagesize;--����ҳ
    set @condition=' where 1=1 ';
    if(@name<>'')
    set @condition=@condition+' and name like ''%'+@name+'%''';
	print @condition
	print @pagebefore
	print @pagerear
  --����һ����������UserInfo������
  --��ȡ��ҳ����
  --��ȡ����
    exec('
    declare @table table(
    iid int identity,
    Id int,
    Name nvarchar(20),
    Sex int,
    Age int,
    Birthday datetime,
	data_insert datetime
    )
    insert into @table
    select * from [User]'+@condition+' order by id desc  
    select * from @table where iid>'+@pagebefore+' and iid<='+@pagerear+'
    select count(*) as rows from @table;');
end;--����

