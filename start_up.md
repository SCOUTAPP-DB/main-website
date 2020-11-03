these are the mysql commands to get the development variant of the database started up

```
create user dev identified with mysql_native_password by '$3cureUS';
create database cdp character set utf8;
grant all on cdp.* to dev;
```

after you push in the data 

```
alter table models_civil_case add column filed_date2 DATE;
update models_civil_case set filed_date2 = str_to_date(filed_date, '%m/%d/%Y');
alter table models_crim_case add column filed_date2 DATE;
update models_crim_case set filed_date2 = str_to_date(filed_date, '%m/%d/%Y');
```
