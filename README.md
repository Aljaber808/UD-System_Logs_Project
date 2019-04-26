


@author: abdulazizaljaber.

Project Name:  Logs Analysis Project.

V.2.1



About: database contains newspaper articles, as well as the web server
       log for the site. The log has a database row for each time a reader
       loaded a web page. Using that information, the code bewlo will answer the
       three questions as shows below questions # 0,1,2 and 3.



Technologies uesd in this project:

1- Python with API-DB
2- PSQL
3- VM


Project Requirements:

Is to create a project that collect imformation about the logs for thre htree questions:

What are the most popular three articles of all time?
Who are the most popular article authors of all time?
On which days did more than 1% of requests lead to errors?

______________________
Tips
You need to check the Database and understane the relationship for each table in the DB before stating this project.
______________________

Software Requerments:

1- python 3.7
2- PSQL
3- VM Box
4- Download Vagrant and install.

______________________

How To run it.
clone this repository
Install Python3
Download Vagrant
Download  VirtualBox
let  the system_log.py under the /vagrant directory
Download the database
Go to the /vagrant directory:
Type Vagrant up
You will se something like this:
 Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'base' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Box file was not detected as metadata. Adding it directly...
==> default: Adding box 'base' (v0) for provider: virtualbox
    default: Downloading: base

Type vagrant ssh

and you should be logged in to the VM.

Now, cd to /vagrant

do ls to go around the dir. 

To run the DB.

Type: psql news


Create Your views into the DB 

-- total visiting
create view totalvisit as
select
  time :: date as dates,
  count(status) as visits
from
  log
group by
  dates
order by
  dates

  -- total errors 404 NOT FOUND
  create view totalerrors as
select
  time :: date as dates,
  count(status) as errorPerDay
from
  log
where
  status = '404 NOT FOUND'
group by
  dates
order by
  dates


  -- get errors > 1  order by desc

SELECT totalerrors
  FROM TotalErrors
 WHERE errorperday > 1
 ORDER BY errorperday DESC limit 1;


  -- total 200 OK
  create view TotalOK as
select
  time :: date as date,
  count(status) as visit
from
  log
  where log.status = '200 OK'
group by
  date
order by
  date;

  -- Showing persntage of the error
  create view error_Persntage as
select
  totalvisit.dates,
  round(100.00 * errorPerDay / visits, 3) as Persentage
from
  totalvisit,
  totalerrors
where
  totalvisit.dates = totalerrors.dates

  -- showing results by error > 1
select
  *
from
  error_Persntage
where
  persentage > 1
limit
  2;


  -- puting two in one

SELECT *
  FROM TotalErrors, error_Persntage
 WHERE errorperday > 1 and  persentage > 1
 ORDER BY errorperday DESC limit 1;



