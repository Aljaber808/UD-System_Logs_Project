#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 21:35:42 2019

@author: abdulazizaljaber

Project Name:  System Log Project.

V.2.00

About: database contains newspaper articles, as well as the web server 
       log for the site. The log has a database row for each time a reader
       loaded a web page. Using that information, the code below will answer the
       three questions as shows below questions # 0,1,2 and 3.

"""
# getting the psql to python 
import psycopg2

# to call the DB 
DBNAME = "news"

# To Connect to The DB 
"""
DataBase = psycopg2.connect("dbname=news")
"""
# def to send query to be execute.
def get_conn(send_query):
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    c.execute(send_query)
    sent = c.fetchall()
    db.close()
    return sent



# (1) To do The first queiry. 
    
# queiry (1)

queiry1 = """ 
        select
  title,
  count(*) as NumberOfViews
from
  log,
  articles
where
  log.path =  '/article/' || articles.slug
group by
  articles.title
order by
  NumberOfViews desc 
limit
  3;
  """
  # Results for queiry 1
Send_Queiry1 = get_conn(queiry1) 

# queiry (2)

queiry2 = """
select
  name,
  count(*) as NumberOfViews
from
  articles,
  authors,
  log
where
  articles.author = authors.id
  and log.path  =  '/article/' || articles.slug
group by
  name
order by
  NumberOfViews desc
limit 
  3;

      """
      
Send_Queiry2  = get_conn(queiry2)



# queiry  get total errors where it was higher than others (3)

queiry3 =               """ 
                            SELECT *
                FROM TotalErrors, error_Persntage
                WHERE errorperday > 1 and  persentage > 1
                ORDER BY errorperday DESC limit 1; 
                        """
Send_Queiry3 = get_conn(queiry3)



queiry4 = """     
select
  *
from
  error_Persntage
where
  persentage > 1
  
limit
  2; 
 """

Send_Queiry4 = get_conn(queiry4)


print('---------------(1)-----------------')

# looping in the queiry to print
def print_queiry1(p_queiry):
    for show_results in range(len(p_queiry)):
        name = p_queiry[show_results][0]
        res = p_queiry[show_results][1]
        print( str(name) + " | " + str(res) + " viewes")
        print("\n")
print("\n")
print('Who are the most popular article authors of all time?')
print("\n")


print_queiry1(Send_Queiry1) 


print('--------------(2)------------------')

def print_queiry2(p_queiry):
    for show_results in range(len(p_queiry)):
        name= p_queiry[show_results][0]
        res = p_queiry[show_results][1]
        print( str(name) + " | " + str(res) + " viewes")
        print("\n")
        
print("Who are the most popular article authors of all time?")
print("\n")
print_queiry2(Send_Queiry2) 


def print_queiry3(p_queiry):
    for show_results in range(len(p_queiry)):
        date = p_queiry[show_results][0]
        total = p_queiry[show_results][1]
        print( "Date: " + str(date) + " | " + str(total) + " errors")
        print("\n")
        
print('---------------(3)-----------------')
print("On Which day was having lots of errros ?")
   
print_queiry3(Send_Queiry3) 

print('-------------(4)-------------------')

def print_queiry4(p_queiry):
    for show_results in range(len(p_queiry)):
        date= p_queiry[show_results][0]
        rate = p_queiry[show_results][1]
        print( "Date: " + str(date) + " | " + str(rate) + " % ")
        print("\n")

print("Rate Of The Error in Persntage.")
print_queiry4(Send_Queiry4)
